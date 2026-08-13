import sqlite3
import sqlite_vec
from sqlite_vec import serialize_float32
from backend.songs_data import SONGS, song_to_passage
from backend.embedder import embed_song, embed_search

def init_db(db_path="backend/songs.db"):
    db = sqlite3.connect(db_path, check_same_thread=False)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)
    
    db.execute("CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, genre TEXT, description TEXT)")
    db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS song_vec USING vec0(song_id INTEGER PRIMARY KEY, embedding float[384] distance_metric=cosine)")
    db.commit()
    return db

def index_songs(db):
    for song in SONGS:
        text = song_to_passage(song)
        vec = embed_song(text)
        db.execute("INSERT OR REPLACE INTO songs VALUES (?, ?, ?, ?, ?)", (song["id"], song["title"], song["artist"], song["genre"], song["description"]))
        db.execute("DELETE FROM song_vec WHERE song_id = ?", (song["id"],))
        db.execute("INSERT INTO song_vec VALUES (?, ?)", (song["id"], serialize_float32(vec)))
    db.commit()

def search_songs(db, query_text: str, top_k: int = 3):
    query_vec = embed_search(query_text)
    sql = """
        SELECT s.id, s.title, s.artist, s.genre, v.distance
        FROM song_vec v
        JOIN songs s ON s.id = v.song_id
        WHERE v.embedding MATCH ? AND k = ?
        ORDER BY v.distance ASC
    """
    return db.execute(sql, (serialize_float32(query_vec), top_k)).fetchall()

