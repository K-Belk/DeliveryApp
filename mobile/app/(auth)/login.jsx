import { View, Text, ScrollView, Image } from 'react-native'
import React from 'react'
import { SafeAreaView } from 'react-native-safe-area-context'
import logo from '../../assets/images/logo.png';
import FormField from '../../components/FormField';
import { useState } from 'react';
import CustomButton from '../../components/CustomButton';
import {Link} from 'expo-router';
import { loginPost }  from '../../api/authRoutes.js';

const Login = () => {

  const [form, setForm] = useState({
    username: '',
    password: ''
  })

  const handleLogin = () => {
    // console.log(form)
    loginPost(form)
  }

  const [isSubmitting, setIsSubmitting ] = useState(false)

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
          isLoading={isSubmitting}
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