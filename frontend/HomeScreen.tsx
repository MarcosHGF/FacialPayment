import React, { useState } from 'react';
import { View, Text, Button, Image, StyleSheet } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';
import { NavigationProps } from './types'; // Importe os tipos

const API_URL = 'https://8061-2804-14d-e642-8452-58e7-6115-e99c-15a5.ngrok-free.app/api'; // Substitua pelo seu ngrok URL

const HomeScreen: React.FC = () => {
  const [image, setImage] = useState<string | null>(null);
  const [result, setResult] = useState<string>('');
  const [userId, setUserId] = useState<number | null>(null);

  const navigation = useNavigation<NavigationProps>();

  // Função para selecionar uma imagem
  const pickImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images, // Use MediaTypeOptions.Images
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.canceled && userId) {
      setImage(result.assets[0].uri);
      uploadFace(userId, result.assets[0].uri);
    } else {
      setResult('Image selection canceled or user not registered.');
    }
  };

  // Função para enviar a imagem ao backend
  const uploadFace = async (user_id: number, uri: string) => {
    const formData = new FormData();
    formData.append('file', {
      uri,
      name: 'face.jpg',
      type: 'image/jpeg',
    } as any);

    try {
      const response = await axios.post(`${API_URL}/upload-face/${user_id}`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setResult(response.data.message);
    } catch (error) {
      console.error(error);
      setResult('Error uploading face.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Facial Payment App</Text>

      {/* Botão para navegar para a tela de registro */}
      <Button title="Register User" onPress={() => navigation.navigate('Register')} />

      {/* Selecionar Imagem */}
      <Button title="Pick an Image" onPress={pickImage} />
      {image && <Image source={{ uri: image }} style={styles.image} />}

      {/* Resultado */}
      <Text>{result}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  title: { fontSize: 24, marginBottom: 20 },
  image: { width: 200, height: 200, marginVertical: 20 },
});

export default HomeScreen;