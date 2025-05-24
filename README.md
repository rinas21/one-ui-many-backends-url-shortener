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

### 🐍 Running the Python Backend (Flask)

1. **Install Flask** (if not already installed):

    ```bash
    pip3 install flask
    ```

2. **Run the Flask server:**

    From the project root directory, run:

    ```bash
    python3 python/server.py
    ```

3. **Access the app:**

    Open your browser and go to:

    ```
    http://127.0.0.1:5000/
    ```

    This will serve the frontend `index.html` through the Flask backend.