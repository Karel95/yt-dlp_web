# 📥 yt-dlp_web

A lightweight web interface to download YouTube videos using yt-dlp, fully packaged with Docker and Docker Compose.

---

## 🧩 Features

-✅ Paste a YouTube URL from the web and download it in seconds.
-🌐 Clean, modern UI using HTML + CSS.
-🐳 Fully containerized with Docker Compose.
-🗂️ All downloaded videos are saved in the /downloads directory.
-🔗 Downloads available as clickable links from the same interface.

---

## 🚀 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/Karel95/yt-dlp_web.git

cd yt-dlp_web
```

### 2. Run the container with Docker Compose

```bash
docker-compose up --build
```

### 3. Access the Web Interface

Open your browser at:
<http://localhost:5000>
Paste a YouTube link, click “Download,” and the video will be saved to the downloads/ folder. A link will appear to download it.
