import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';
import { StackScreenProps } from '@react-navigation/stack';

// Define the parameter list for the stack navigator
type RootStackParamList = {
  Register: undefined;
  Login: undefined;
  Main: { user: { id: number; username: string; email: string } };
};

// Use StackScreenProps to define the props for MainScreen
type MainScreenProps = StackScreenProps<RootStackParamList, 'Main'>;

const MainScreen: React.FC<MainScreenProps> = ({ route, navigation }) => {
  const { user } = route.params;

  const handleLogout = () => {
    navigation.goBack(); // Navigate back to the login screen
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome, {user.username}!</Text>
      <Text>Email: {user.email}</Text>

      <Button title="Logout" onPress={handleLogout} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
});

export default MainScreen;