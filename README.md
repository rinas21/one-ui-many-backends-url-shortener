# 🔗 One UI, Many Backends - URL Shortener

A simple and elegant URL shortener with a unified front-end and multiple interchangeable backends written in different programming languages.

---

## 🖼️ Frontend

- Single HTML/CSS/JavaScript page
- Clean, minimal design
- Interacts with backend through API:
  - `POST /shorten` → `{ short: "abc123" }`
  - `GET /abc123` → Redirects to long URL

---

## 🖥️ Available Backends

| Language | Framework    | File          | Status |
|----------|--------------|---------------|--------|
| Python   | Flask        | `python/server.py` | ✅ |
| Node.js  | Express      | `node/server.js`   | 🛠️ |
| Go       | net/http     | `go/main.go`       | 🛠️ |
| Java     | Spring Boot  | `java/`            | 🔜 |
| PHP      | Native       | `php/index.php`    | 🔜 |
| Ruby     | Sinatra      | `ruby/app.rb`      | 🔜 |

✅ = Done | 🛠️ = In progress | 🔜 = Planned

---

## 🚀 Running the Project

### Frontend

No build required. Open `frontend/index.html` in your browser or serve it using any static file server.

### Backend (Example: Python)

```bash
cd python
pip install flask
python server.py
