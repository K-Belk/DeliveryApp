import { StatusBar } from 'expo-status-bar';
import { ScrollView, Text, View, Image } from 'react-native';
import { router, Redirect } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
// import {logo} from '../constants/images';
import logo from '../assets/images/logo.png';
import CustomButton from '../components/CustomButton';


export default function App() {
  return (
    <>
      <SafeAreaView className="bg-primary h-full">
        <ScrollView contentContainerStyle={{ height: '100%' }}> 
          <View className="w-full justify-center items-center min-h-[85vh] px-4">
            <Image 
            source={logo}
            className="w-[300px] h-[200] "
            resizeMode="contain"
            tintColor={'white'}
            />

            <CustomButton 
            title='Login'
            handlePress={() => router.push('/login')}
            containerStyles='w-full mt-7 '
            />

            <CustomButton 
            title='Create Account'
            handlePress={() => router.push('/register')}
            containerStyles='w-full mt-7 '
            />
          </View>
        </ScrollView>
        </SafeAreaView>
        <StatusBar style="light" />
        </>
  );
}


