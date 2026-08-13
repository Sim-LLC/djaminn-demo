# Song Semantic Search Backend

Hệ thống Backend hỗ trợ **Tìm kiếm ngữ nghĩa (Semantic Search)** cho danh sách bài hát, sử dụng **FastAPI**, **Sentence-Transformers** và **SQLite-vec**.

Hệ thống có khả năng hiểu ý nghĩa của câu truy vấn (tiếng Việt và tiếng Anh) và tìm ra những bài hát phù hợp nhất về nội dung, chủ đề, cảm xúc thay vì chỉ khớp từ khóa chính xác (keyword matching).

---

## 🚀 Tính năng chính

- **Tìm kiếm ngữ nghĩa (Semantic Search)**: Hiểu ngữ cảnh truy vấn (VD: *"bài hát về tình bạn"*, *"sad love song"*, *"nhạc sôi động"*) và trả về bài hát có ý nghĩa tương đồng.
- **Vector Embedding**: Sử dụng mô hình đa ngôn ngữ `intfloat/multilingual-e5-small` tạo vector nhúng 384 chiều với độ chính xác cao.
- **SQLite Vector Database**: Tích hợp extension `sqlite-vec` để lưu trữ và truy vấn khoảng cách Cosine (`cosine distance`) trực tiếp trên CSDL SQLite nhẹ và nhanh chóng.
- **RESTful API**: Cung cấp API tìm kiếm linh hoạt với FastAPI, tự động sinh tài liệu Swagger UI.
- **Tự động Indexing**: Tự động tạo bảng, trích xuất embedding và đánh chỉ số vector cho bài hát khi server khởi chạy.

---

## 📁 Cấu trúc thư mục

```text
backend/
├── app.py           # FastAPI Web Application & các API Endpoints
├── db.py            # Khởi tạo SQLite DB, lưu trữ và truy vấn vector (sqlite-vec)
├── embedder.py      # Xử lý vector embedding sử dụng SentenceTransformer (e5-small)
├── songs_data.py    # Dữ liệu bài hát mẫu và hàm chuẩn hóa định dạng văn bản
├── requirements.txt # Thư viện phụ thuộc của dự án
└── README.md        # Tài liệu hướng dẫn sử dụng Backend
```

---

## 🛠️ Yêu cầu hệ thống & Cài đặt

### Yêu cầu
- **Python**: version >= 3.10

### 1. Khởi tạo môi trường ảo (Virtual Environment)

**Trên Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Trên Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Cài đặt các gói phụ thuộc (Dependencies)

```bash
pip install -r backend/requirements.txt
```

Các thư viện chính trong `requirements.txt`:
- `sentence-transformers`: Tạo nhúng vector từ câu văn.
- `sqlite-vec`: Extension tìm kiếm vector cho SQLite.
- `fastapi`: Framework web API hiệu năng cao.
- `uvicorn`: ASGI Web Server.
- `numpy`: Xử lý mảng số học vector.

---

## 🏃‍♂️ Khởi chạy Backend Server

Từ thư mục gốc dự án (`semantic-search`), chạy lệnh:

```bash
python -m uvicorn backend.app:app --reload --port 8000
```
Hoặc chạy trực tiếp file `app.py`:
```bash
python backend/app.py
```

Server sẽ khởi chạy tại: `http://localhost:8000`

---

## 📖 Chi tiết API Endpoint

### 1. Tìm kiếm bài hát (`GET /search`)

Tìm kiếm các bài hát liên quan nhất theo câu truy vấn ngữ nghĩa.

#### **Query Parameters:**
| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `q` | `string` | **Có** | - | Nội dung cần tìm kiếm (VD: *"bài hát về tình học trò"*) |
| `limit` | `integer` | Không | `3` | Số lượng kết quả tối đa trả về |

#### **Ví dụ Request:**
```http
GET http://localhost:8000/search?q=b%C3%A0i%20h%C3%A1t%20v%E1%BB%81%20t%C3%ACnh%20b%E1%BA%A1n&limit=2
```

#### **Ví dụ Response (JSON):**
```json
{
  "query": "bài hát về tình bạn",
  "total": 2,
  "results": [
    {
      "id": 1,
      "title": "See You Again",
      "artist": "Wiz Khalifa ft. Charlie Puth",
      "genre": "hip-hop",
      "distance": 0.1752,
      "similarity_score": 82.48
    },
    {
      "id": 8,
      "title": "Fix You",
      "artist": "Coldplay",
      "genre": "alternative",
      "distance": 0.2814,
      "similarity_score": 71.86
    }
  ]
}
```

- `distance`: Khoảng cách Cosine giữa vector truy vấn và vector bài hát (giá trị càng nhỏ càng giống nhau).
- `similarity_score`: Điểm tương đồng quy đổi theo phần trăm (`(1 - distance) * 100`).

---

## 📑 Tài liệu API Tự động (Swagger UI)

Khi server đang chạy, truy cập đường dẫn sau trên trình duyệt để xem tài liệu API tương tác:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 💡 Cơ chế hoạt động (How It Works)

1. **Chuẩn hóa thông tin bài hát**:
   Mỗi bài hát được định dạng thành văn bản theo mẫu:
   `Bài hát: {title}. Nghệ sĩ: {artist}. Thể loại: {genre}. {description}`

2. **Tạo Vector Embedding**:
   - Sử dụng model `intfloat/multilingual-e5-small`.
   - Bài hát khi lưu trữ được thêm tiền tố: `passage: <nội dung bài hát>`
   - Câu truy vấn tìm kiếm được thêm tiền tố: `query: <nội dung truy vấn>`

3. **Lưu trữ & Truy vấn Vector**:
   - Lưu trữ vector 384 chiều vào bảng ảo `song_vec` trong SQLite với chỉ số mét `distance_metric=cosine`.
   - Khi tìm kiếm, `sqlite-vec` tính toán khoảng cách cosine giữa vector truy vấn và các vector bài hát, sắp xếp lấy `top_k` kết quả gần nhất.

