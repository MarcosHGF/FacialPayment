// types.ts
import { StackNavigationProp } from '@react-navigation/stack';

export type RootStackParamList = {
  Home: undefined; // A rota "Home" não recebe parâmetros
  Register: undefined; // A rota "Register" também não recebe parâmetros
};

export type NavigationProps = StackNavigationProp<RootStackParamList>;