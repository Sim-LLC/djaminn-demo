from fastapi import FastAPI, Query
from pydantic import BaseModel
from backend.db import init_db, index_songs, search_songs

app = FastAPI(title="Song Semantic Search API")
db = init_db()
index_songs(db)

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
            similarity_score=round((1 - r[4]) * 100, 2)
        )
        for r in rows
    ]
    return SearchResponse(query=q, total=len(results), results=results)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


