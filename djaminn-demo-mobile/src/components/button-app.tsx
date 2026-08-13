import { Button } from "react-native";

export default function ButtonApp({
  title,
  onPress,
}: {
  title: string;
  onPress: () => void;
}) {
  return <Button title={title} onPress={onPress} />;
}
