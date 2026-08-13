import { Container, Row, Col } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

export default function ItemComponent({ item }) {
  console.log(item);
  return (
    <Container className="item">
      <Row>
        <Col className="bg-primary text-white">
          <h4>{item.name}</h4>
        </Col>
        <Col className="bg-secondary text-white">
          <p>{item.artist}</p>
        </Col>
        <Col className="bg-secondary text-white">
          <p>{item.score}</p>
        </Col>
      </Row>
    </Container>
  );
}
