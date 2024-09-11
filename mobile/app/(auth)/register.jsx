import { View, Text, ScrollView, Image } from 'react-native'
import React from 'react'
import { SafeAreaView } from 'react-native-safe-area-context'
import logo from '../../assets/images/logo.png';
import FormField from '../../components/FormField';
import { useState } from 'react';
import CustomButton from '../../components/CustomButton';
import {Link} from 'expo-router';

const Register = () => {

  const [from, setFrom] = useState({
    username: '',
    email: '',
    firstName: '',
    lastName: '',
    password: '',
    rePassword: ''
  })

  const handleLogin = () => {
    console.log(from)
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
          <Text className="text-white text-2xl font-bold">Create an Account</Text>
          <FormField 
          title='Username'
          placeholder='Enter your username'
          value={from.username}
          handleChangeText={(e) => setFrom({...from, username: e})}
          otherStyles='mt-7'
          keyboardType='username'
          />
          <FormField 
          title='Email'
          placeholder='Enter your Email'
          value={from.username}
          handleChangeText={(e) => setFrom({...from, email: e})}
          otherStyles='mt-7'
          keyboardType='email'
          />
          <FormField 
          title='First Name'
          placeholder='Enter your First Name'
          value={from.username}
          handleChangeText={(e) => setFrom({...from, FirstName: e})}
          otherStyles='mt-7'
          keyboardType='name'
          />
          <FormField 
          title='Last Name'
          placeholder='Enter your Last Name'
          value={from.username}
          handleChangeText={(e) => setFrom({...from, lastName: e})}
          otherStyles='mt-7'
          keyboardType='name'
          />
          <FormField 
          title='Password'
          placeholder='Enter your password'
          value={from.password}
          handleChangeText={(e) => setFrom({...from, password: e})}
          otherStyles='mt-7'
          keyboardType='password'
          />
          <FormField 
          title='Re-enter Password'
          placeholder='Re-Enter your password'
          value={from.password}
          handleChangeText={(e) => setFrom({...from, rePassword: e})}
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
          <Text className="text-gray-400 text-lg">Already have an account?</Text>
          <Link href='/login' className="text-lg text-white">Login</Link>
        </View>
      </ScrollView>
    </SafeAreaView>
  )
}

export default Register