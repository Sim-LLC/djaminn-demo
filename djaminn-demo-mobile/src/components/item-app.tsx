import { Text, View } from "react-native";

const ItemApp = ({ item }: { item: string }) => {
  return (
    <View>
      <Text>{item}</Text>
    </View>
  );
};

export default ItemApp;
