SONGS = [
    {
        "id": 1,
        "title": "See You Again",
        "artist": "Wiz Khalifa ft. Charlie Puth",
        "genre": "hip-hop",
        "description": "Bài hát về tình bạn, chia tay và kỷ niệm với người đã ra đi.",
    },
    {
        "id": 2,
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "genre": "pop",
        "description": "Bài pop sôi động về tình yêu và sự hấp dẫn thể chất.",
    },
    {
        "id": 3,
        "title": "Someone Like You",
        "artist": "Adele",
        "genre": "ballad",
        "description": "Ballad buồn về tình yêu đã mất. Người hát gặp lại người yêu cũ.",
    },
    {
        "id": 4,
        "title": "Nơi Này Có Anh",
        "artist": "Sơn Tùng M-TP",
        "genre": "v-pop",
        "description": "Bài hát tình yêu ngọt ngào tiếng Việt. Kể về việc mang người yêu về quê.",
    },
    {
        "id": 5,
        "title": "Em Của Ngày Hôm Qua",
        "artist": "Sơn Tùng M-TP",
        "genre": "v-pop",
        "description": "Bài hát về nỗi nhớ người yêu cũ và cảm giác hối tiếc.",
    },
    {
        "id": 6,
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "genre": "rock",
        "description": "Bản rock opera huyền thoại kể câu chuyện về một người đã phạm tội.",
    },
    {
        "id": 7,
        "title": "Happy",
        "artist": "Pharrell Williams",
        "genre": "pop",
        "description": "Bài hát vui vẻ, lạc quan khuyến khích mọi người vui lên.",
    },
    {
        "id": 8,
        "title": "Fix You",
        "artist": "Coldplay",
        "genre": "alternative",
        "description": "Bài hát an ủi về việc chữa lành nỗi đau.",
    },
    {
        "id": 9,
        "title": "Despacito",
        "artist": "Luis Fonsi ft. Daddy Yankee",
        "genre": "reggaeton",
        "description": "Bài hát Latin sôi động về tình yêu và sự quyến rũ.",
    },
    {
        "id": 10,
        "title": "Hạ Còn Vương Nắng",
        "artist": "DatKaa",
        "genre": "v-pop",
        "description": "Ballad Việt về nỗi nhớ mùa hạ và tình yêu dang dở.",
    },
    {
        "id": 11,
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "genre": "synth-pop",
        "description": "Bài synth-pop về việc cảm thấy cô đơn trong thành phố về đêm.",
    },
    {
        "id": 12,
        "title": "Có Chàng Trai Viết Lên Cây",
        "artist": "Phan Mạnh Quỳnh",
        "genre": "v-pop",
        "description": "Bài ballad Việt về tình yêu thầm lặng thời học sinh.",
    },
]

def song_to_passage(song: dict) -> str:
    return f"Bài hát: {song['title']}. Nghệ sĩ: {song['artist']}. Thể loại: {song['genre']}. {song['description']}"
