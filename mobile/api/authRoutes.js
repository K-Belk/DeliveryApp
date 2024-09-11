import {api} from './apiBase';
import * as SecureStore from 'expo-secure-store';


export const loginPost = async (data) => {
  try {
    const formData = new URLSearchParams();
    formData.append('username', data.username);
    formData.append('password', data.password);

    const res = await api.post('/token', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    SecureStore.setItemAsync('access_token', res.data.token.access_token);
    SecureStore.setItemAsync('refresh_token', res.data.token.refresh_token);
    // console.log(res.data)
    return res.data
    } catch (error) {
    console.error(error);
  }
}

export const register = async (data) => {
  try {
    const res = await api.post('/auth/register', data);
    return res.data;
    // Handle success (store token in local storage, reidrect to home page)
  } catch (error) {
    console.error('Login error:', error.response?.data || error.message);
    // Handle error (show error message)
  }

}

export const logout = async () => {
  try {
    await SecureStore.deleteItemAsync('access_token');
    await SecureStore.deleteItemAsync('refresh_token');
    return true;
  } catch (error) {
    console.error('Logout error:', error.response?.data || error.message);
    return false;
  }
}

export const getCurrentUser = async () => {
  try {
    const res = await api.get('/users/me');
    return res.data;
  } catch (error) {
    console.error('Get user error:', error.response?.data || error.message);
    throw error;
  }
}