import { useState } from "react";
import { FlatList, StyleSheet, Text, TextInput, View } from "react-native";

import ButtonApp from "../button-app";

// const baseURL = "https://musicbrainz.org/ws/2/artist";
const baseURL = "http://localhost:8000";

export default function SearchApp() {
  const [search, setSearch] = useState("");
  const [results, setResults] = useState<
    { id: string; title: string; artist: string }[]
  >([]);

  const handleSearch = () => {
    // Implement your search logic here
    return fetch(`${baseURL}/search?q=${encodeURIComponent(search)}&limit=10`)
      .then((response) => response.json())
      .then((json) => {
        const items = json.results.map((item: any) => ({
          id: item.id,
          title: item.title,
          artist: item.artist,
        }));
        setResults(items);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  return (
    <View>
      <View
        style={{
          flexDirection: "row",
        }}
      >
        <TextInput
          placeholder="Search..."
          value={search}
          onChangeText={setSearch}
          style={{
            borderWidth: 1,
            borderColor: "gray",
            borderRadius: 10,
            padding: 10,
            width: 250,
          }}
        />
        <ButtonApp title="Search" onPress={handleSearch} />
      </View>

      <FlatList
        data={results}
        renderItem={({ item }) => (
          <View style={styles.viewContainer}>
            <View style={{ flex: 2 }}>
              <Text>{item.title}</Text>
            </View>
            <View style={styles.viewCountry}>
              <Text>{item.artist}</Text>
            </View>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  viewContainer: {
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: "gray",
    flexDirection: "row",
  },
  viewCountry: { flex: 1 },
});
