from sentence_transformers import CrossEncoder
from backend.songs_data import song_to_passage

reranker_model = None


def score_with_cross_encoder(query, documents):
    global reranker_model

    if reranker_model is None:
        reranker_model = CrossEncoder("BAAI/bge-reranker-v2-m3")

    pairs = [[query, document] for document in documents]
    scores = reranker_model.predict(pairs)
    return scores.tolist()


def rerank_songs(query, rows):
    documents = [(song_to_passage(row)) for row in rows]
    scores = score_with_cross_encoder(query, documents)

    ranked_rows = list(zip(rows, scores))
    return sorted(ranked_rows, key=lambda item: item[1], reverse=True)
