import {api} from './apiBase';

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
    
    SecureStore.setItemAsync('access_token', res.access_token);
    SecureStore.setItemAsync('refresh_token', res.data.refresh_token);
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