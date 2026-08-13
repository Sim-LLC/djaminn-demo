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
    setSearchResults(result.artists || []);
  }

  return (
    <div>
      <div className="search">
        <TextInputComponent
          controlledValue={searchValue}
          onChange={(e) => setSearchValue(e.target.value)}
        />
        <ButtonComponent buttonText="Search" onClick={handleSearch} />
      </div>

      <Container>
        <Row>
          <Col className="bg-primary text-white">
            <h2>name</h2>
          </Col>
          <Col className="bg-secondary text-white">
            <h2>country</h2>
          </Col>
        </Row>
      </Container>

      {searchResults.map((artist) => (
        <div key={artist.id}>
          <ItemComponent
            item={{ name: artist.name, country: artist.country }}
          />
        </div>
      ))}
    </div>
  );
}
