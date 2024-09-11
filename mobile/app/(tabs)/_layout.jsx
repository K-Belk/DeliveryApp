import { View, Text, Image } from 'react-native'
import React from 'react'
import { Tabs, Redirect } from 'expo-router'
// import all of the icons from the constants folder
import { home, delivery, location, products } from '../../constants/icons'


const TabIcon = ({ icon, color, name, focused }) => {
  return (
    <View className="items-center justify-center gap-2">
      <Image
      source={icon}
      resizeMode="contain"
      tintColor={color}
      className="w-6 h-6"
      />
      <Text className={
        `text-xs ${focused ? 'text-white' : 'text-gray-500'}`
      }>
      {name}
      </Text>
    </View>
  )
}

const TabsLayout = () => {
  return (
    <>
      <Tabs
      screenOptions={{
        tabBarShowLabel: false,
        tabBarStyle: {
          backgroundColor: 'black',
          height: 84,
          },
        }
      }
      >
        <Tabs.Screen 
        name="home" 
        options={{ 
          title: 'home',
          headerShown: false,
          tabBarIcon: ({ color, focused }) => ( 
            <TabIcon icon={home} 
            color={color} 
            focused={focused} 
            name="Home" 
            />
          )
        }}

        />
        <Tabs.Screen
        name="deliveries"
        options={{ 
          title: 'deliveries',
          headerShown: false,
          tabBarIcon: ({ color, focused }) => ( 
            <TabIcon icon={delivery} 
            color={color} 
            focused={focused} 
            name="Deliveries" 
            />
          )
        }}
        />
        <Tabs.Screen
        name="locations"
        options={{ 
          title: 'locations',
          headerShown: false,
          tabBarIcon: ({ color, focused }) => ( 
            <TabIcon icon={location} 
            color={color} 
            focused={focused} 
            name="Locations" 
            />
          )
        }}
        /> 
        <Tabs.Screen
        name="products"
        options={{ 
          title: 'products',
          headerShown: false,
          tabBarIcon: ({ color, focused }) => ( 
            <TabIcon icon={products} 
            color={color} 
            focused={focused} 
            name="Products" 
            />
          )
        }}
        /> 
      </Tabs>
    </>
  )
}

export default TabsLayout