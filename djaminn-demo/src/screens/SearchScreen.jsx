import { useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

import ButtonComponent from "../components/ButtonComponent";
import TextInputComponent from "../components/TextInputComponent";
import ItemComponent from "../components/ItemComponent";
import ApiService from "../api/api";

export default function SearchScreen() {
  const api = ApiService();
  const [searchValue, setSearchValue] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  async function handleSearch() {
    const result = await api.get(searchValue);
    setSearchResults(result.results || []);
  }

  return (
    <div>
      <div className="search">
        <TextInputComponent
          controlledValue={searchValue}
          onChange={(e) => setSearchValue(e.target.value)}
          onEnter={handleSearch}
        />
        <ButtonComponent buttonText="Search" onClick={handleSearch} />
      </div>

      <Container>
        <Row>
          <Col className="bg-primary text-white">
            <h2>Name</h2>
          </Col>
          <Col className="bg-primary text-white">
            <h2>Artist</h2>
          </Col>
          <Col className="bg-primary text-white">
            <h2>Score</h2>
          </Col>
        </Row>
      </Container>

      {searchResults.map((item) => (
        <div key={item.id}>
          <ItemComponent
            item={{ name: item.title, artist: item.artist, score: item.similarity_score }}
          />
        </div>
      ))}
    </div>
  );
}
