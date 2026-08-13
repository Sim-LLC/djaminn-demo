import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/multilingual-e5-small")

def embed_song(text: str) -> np.ndarray:
    return np.array(model.encode("passage: " + text, normalize_embeddings=True), dtype=np.float32)

def embed_search(text: str) -> np.ndarray:
    return np.array(model.encode("query: " + text, normalize_embeddings=True), dtype=np.float32)

