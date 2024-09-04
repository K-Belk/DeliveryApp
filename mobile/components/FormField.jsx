import { View, Text, TextInput, TouchableOpacity, Image } from 'react-native'
import React from 'react'
import { useState } from 'react'
import { visibility, visibilityOff} from '../constants/icons'

const FormField = ({ 
  title, 
  placeholder, 
  value, 
  handleChangeText, 
  otherStyles, 
  keyboardType,
  ...props
}) => {

  const [showPassword, setShowPassword] = useState(false)

  return (
    <View className={`space-y-2 ${otherStyles}`}>
      <Text className="text-base text-gray-100">{title}</Text>
      <View className="w-full h-16 px-4 bg-black-100 rounded-2xl items-center focus:border-gray-400 flex-row">  
        <TextInput 
        className="flex-1 text-white text-base"
        value={value}
        placeholder={placeholder}
        placeholderTextColor={'#9CA3AF'}
        onChange={handleChangeText}
        secureTextEntry={keyboardType === 'password' ? !showPassword : false}
        />

        {keyboardType === 'password' && (
          <TouchableOpacity onPress={() => setShowPassword(!showPassword)}>
            <Image source={showPassword ? visibility : visibilityOff} className="w-6 h-6" resizeMode='contain' />
          </TouchableOpacity>
        )}
      </View>
    </View>
  )
}

export default FormField