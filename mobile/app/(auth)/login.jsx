import { View, Text, ScrollView, Image, Alert } from 'react-native'
import React from 'react'
import { SafeAreaView } from 'react-native-safe-area-context'
import logo from '../../assets/images/logo.png';
import FormField from '../../components/FormField';
import { useState } from 'react';
import CustomButton from '../../components/CustomButton';
import {Link, router} from 'expo-router';
import { loginPost }  from '../../api/authRoutes.js';
import { useGlobalContext } from '../../context/GlobalProvider';

const Login = () => {

  const {setIsLoggedIn, isLoggedIn, setUser, user, isLoading, setIsLoading} = useGlobalContext();

  const [form, setForm] = useState({
    username: '',
    password: ''
  })

  const handleLogin = () => {
    setIsLoading(true);
    loginPost(form)
    .then(response => {
      if(response) {
        setIsLoggedIn(true);
        setUser({
        username: response.user.username,
        email: response.user.email,
        id: response.user.id,
        firstName: response.user.first_name,
        lastName: response.user.last_name,
        
      });

      } else {
        console.log('Login failed:', response);
        setIsLoggedIn(false);
        setUser({
          username: '',
          email: '',
          id: '',
          firstName: '',
          lastName: '',
        });
      Alert.alert('Login failed', "Invalid username or password");
      }
    })
    .catch(error => {
      console.error('Login error:', error);
      console.log('Login failed:', error.response?.data || error.message);
      setIsLoggedIn(false);
    })
    .finally(() => {
      setIsLoading(false);
      console.log('User:', user);
      console.log('IsLoggedIn:', isLoggedIn);
      // redirect to home page
      router.push('/home');
    });
  }


  return (
    <SafeAreaView className="bg-primary h-full">
      <ScrollView>
        <View className="w-full justify-center min-h-[85vh] px-6">
          <Image 
          source={logo}
          resizeMode='contain'
          className="w-[115px] h-[200] "
          tintColor={'white'}
          />
          <Text className="text-white text-2xl font-bold">Login with Username</Text>
          <FormField 
          title='Username'
          placeholder='Enter your username'
          value={form.username}
          handleChangeText={(e) => setForm({...form, username: e})}
          otherStyles='mt-7'
          keyboardType='username'
          />
          <FormField 
          title='Password'
          placeholder='Enter your password'
          value={form.password}
          handleChangeText={(e) => setForm({...form, password: e})}
          otherStyles='mt-7'
          keyboardType='password'
          />
          <CustomButton 
          title = 'Login'
          handlePress={handleLogin}
          containerStyles='mt-7'
          isLoading={isLoading}
          />
        </View>
        <View className="flex justify-center pt-5 flex-row gap-2">
          <Text className="text-gray-400 text-lg">Don't have an account?</Text>
          <Link href='/register' className="text-lg text-white">Register</Link>
        </View>
      </ScrollView>
    </SafeAreaView>
  )
}

export default Login