import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './HomeScreen';
import RegisterScreen from './RegisterScreen';
import { RootStackParamList } from './types'; // Importe os tipos

const Stack = createStackNavigator<RootStackParamList>();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: 'Facial Payment App' }} />
        <Stack.Screen name="Register" component={RegisterScreen} options={{ title: 'Register User' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}