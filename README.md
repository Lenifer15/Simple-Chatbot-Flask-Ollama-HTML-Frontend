# Simple Chatbot — Flask + Ollama + HTML Frontend

## 📌 Project Overview

A lightweight local chatbot application powered by **Ollama** (running `qwen3:1.7b`) with a **Flask** backend API and a clean **HTML/JavaScript** frontend. Users can type messages in the browser and receive AI-generated responses rendered with Markdown support.

---

## 🚀 Features

- Conversational chat interface served via a simple HTML page
- Flask REST API backend that communicates with a local Ollama instance
- Markdown rendering of bot responses using `marked.js`
- CORS-enabled API for seamless frontend-backend communication
- Minimal, dependency-light setup — runs entirely on your local machine

---

## 🧠 Technologies Used

- **Python 3** — Backend runtime
- **Flask** — Lightweight web framework for the chat API
- **Flask-CORS** — Cross-Origin Resource Sharing support
- **Ollama** — Local LLM runner (model: `qwen3:1.7b`)
- **HTML5 / CSS3 / JavaScript** — Frontend chat UI
- **marked.js (v9.1.6)** — Client-side Markdown parser for bot responses

---

## ⚙️ How It Works

1. The user types a message in the browser and clicks **Send**.
2. The frontend sends a `POST` request to `http://localhost:5000/chat` with the message payload.
3. The Flask backend receives the message and forwards it to the locally running Ollama API at `http://localhost:11434/api/generate`.
4. Ollama generates a response using the `qwen3:1.7b` model and returns it to Flask.
5. Flask sends the response back to the frontend as JSON.
6. The frontend renders the bot's reply using `marked.js` for proper Markdown display.

---

## 🛠️ Installation

**Prerequisites:**
- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- `qwen3:1.7b` model pulled in Ollama

```bash
# 1. Clone the repository
git clone https://github.com/your-username/simple-chatbot.git
cd simple-chatbot

# 2. Install Python dependencies
pip install flask flask-cors requests

# 3. Pull the Ollama model (if not already done)
ollama pull qwen3:1.7b

# 4. Start the Ollama server (if not already running)
ollama serve

# 5. Run the Flask backend
python app.py
```

---

## ▶️ Usage

```bash
python app.py
```

Then open `index.html` directly in your browser (or serve it via any static file server).

---

## 💡 Example

**Input:** What is the capital of France?

**Output:** The capital of France is **Paris**. It is the country's largest city and serves as its political, cultural, and economic center.

---

## 📁 Folder Structure

```
simple-chatbot/
├── app.py          # Flask backend — handles /chat POST endpoint
├── index.html      # Frontend — chat UI with Markdown rendering
└── README.md       # Project documentation
```

---

## 🤝 Contributing

- Fork the repository and create a new branch for your feature or fix
- Keep changes focused and well-documented
- Test locally before submitting a pull request
- Open an issue first for major changes or feature proposals
- Follow existing code style and naming conventions

---

## 📄 License

MIT

---

## Author

**Jessica Lenifer R.**
