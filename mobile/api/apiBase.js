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
}
  , async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = await SecureStore.getItemAsync('refresh_token');
      if (refreshToken) {
        try {
          const res = await api.post('/refresh-token', { token: refreshToken });
          
          SecureStore.setItemAsync('access_token', res.access_token);
          SecureStore.setItemAsync('refresh_token', res.data.refresh_token);
          
          return api(originalRequest);
        } catch (error) {
          console.error('Refresh error:', error.response?.data || error.message);
        }
      }
    }
    return Promise.reject(error);
  });