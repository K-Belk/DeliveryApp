import { createContext, useContext, useState, useEffect } from 'react';
import { getCurrentUser } from '../api/authRoutes';
import { get } from 'react-native/Libraries/TurboModule/TurboModuleRegistry';

const GlobalContext = createContext();

export const useGlobalContext = () => {
  return useContext(GlobalContext);
}

export const GlobalProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [user, setUser] = useState({
    username: '',
    email: '',
    id: '',
    firstName: '',
    lastName: '',
  });
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    setIsLoading(true);
    getCurrentUser()
    .then(response => {
      console.log('Get user response:', response);
      if (response) {
        setIsLoggedIn(true);
        setUser({
          username: response.username,
          email: response.email,
          id: response.id,
          firstName: response.first_name,
          lastName: response.last_name,
        });
      } else {
        setIsLoggedIn(false);
        setUser({
          username: '',
          email: '',
          id: '',
          firstName: '',
          lastName: '',
        });
      }
      
    })
    .catch(error => {
      // console.error('Get user error:', error);
      console.log('Get user failed:', error.response?.data || error.message);
        setIsLoggedIn(false);
        setUser({
          username: '',
          email: '',
          id: '',
          firstName: '',
          lastName: '',
        });
    })
    .finally(() => {
      setIsLoading(false);
      // console.log('User:', user);
      // console.log('IsLoggedIn:', isLoggedIn);
    });
  }, [])
  

  return (
    <GlobalContext.Provider value={{
      isLoggedIn, 
      setIsLoggedIn, 
      user, 
      setUser,
      isLoading,
      setIsLoading,
    }}
    >
      {children}
    </GlobalContext.Provider>
  )



  }