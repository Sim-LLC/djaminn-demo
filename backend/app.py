from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.db import init_db, index_songs, search_songs
from backend.rerankers import rerank_songs

app = FastAPI(title="Song Semantic Search API")
db = init_db()
index_songs(db)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SongResult(BaseModel):
    id: int
    title: str
    artist: str
    genre: str
    distance: float
    similarity_score: float

class SearchResponse(BaseModel):
    query: str
    total: int
    results: list[SongResult]

@app.get("/search", response_model=SearchResponse)
def api_search(q: str = Query(...), limit: int = 3):
    rows = search_songs(db, query_text=q, top_k=limit)
    results = [
        SongResult(
            id=r[0], title=r[1], artist=r[2], genre=r[3],
            distance=round(r[4], 4),
            similarity_score=round((1 - r[4]) * 100, 2),
        )
        for r in rows
    ]
    return SearchResponse(query=q, total=len(results), results=results)


def _reranked_search(
    q: str,
    limit: int,
) -> SearchResponse:
    rows = search_songs(db, query_text=q, top_k=20)
    ranked_rows = rerank_songs(q, rows)[:limit]
    results = [
        SongResult(
            id=row[0],
            title=row[1],
            artist=row[2],
            genre=row[3],
            distance=round(row[4], 4),
            similarity_score=round(score * 100, 2),
        )
        for row, score in ranked_rows
    ]
    return SearchResponse(
        query=q,
        total=len(results),
        results=results,
    )


@app.get("/search/bge", response_model=SearchResponse)
def api_search_bge(q: str = Query(...), limit: int = 3):
    return _reranked_search(q, limit)


# @app.get("/search/qwen", response_model=SearchResponse)
# def api_search_qwen(q: str = Query(...), limit: int = 3):
#     return _reranked_search(q, limit, "qwen")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


