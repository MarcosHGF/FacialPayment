import { View, Text, Button, Image, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { NavigationProps } from './types'; // Importe os tipos
import getAPI from './Api'

const API_URL = getAPI();

const HomeScreen: React.FC = () => {

  const navigation = useNavigation<NavigationProps>();

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Facial Payment App</Text>

      {/* Botão para navegar para a tela de registro */}
      <Button title="Register User" onPress={() => navigation.navigate('Register')} />

      <Button title="Login" onPress={() => navigation.navigate('Login')} />

    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  title: { fontSize: 24, marginBottom: 20 },
  image: { width: 200, height: 200, marginVertical: 20 },
});

export default HomeScreen;