import axios from 'axios';
import * as SecureStore from 'expo-secure-store';
import { BACKEND_URL } from '@env';

export const api = axios.create({
  baseURL: BACKEND_URL,
});

api.interceptors.request.use(async (config) => {
  const accessToken = await SecureStore.getItemAsync('access_token');
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
},
  (error) => {
    return Promise.reject(error);
  });

api.interceptors.response.use((response) => {
  return response;
},
async (error) => {
  const originalRequest = error.config;
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;
    
    const refreshToken = await SecureStore.getItemAsync('refresh_token');

    if (refreshToken) {
      try {
        const res = await api.post('/token/refresh', {
          refresh_token: refreshToken,
        });
         if (res.data && res.data.access_token) {
          await SecureStore.setItemAsync('access_token', res.data.access_token);
          await SecureStore.setItemAsync('refresh_token', res.data.refresh_token);

          originalRequest.headers['Authorization'] = `Bearer ${res.data.access_token}`;

          return api(originalRequest);
      } else {
        console.log('Refresh token failed:', res.data);
      }
    } catch (refreshError) {
      console.error('Refresh token error:', refreshError.response?.data || refreshError.message);

      await SecureStore.deleteItemAsync('access_token');
      await SecureStore.deleteItemAsync('refresh_token');
    }
  } else {
    await SecureStore.deleteItemAsync('access_token');
    await SecureStore.deleteItemAsync('refresh_token');
    console.log('Refresh token not found, logging out');
  }
}
return Promise.reject(error);
}
);

