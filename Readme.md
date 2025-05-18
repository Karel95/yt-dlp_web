# 📥 yt-dlp_web

Una interfaz web ligera para descargar videos de YouTube usando `yt-dlp`, empaquetada completamente con Docker y Docker Compose.

---

## 🧩 Características

- ✅ Pega una URL de YouTube desde la web y descárgala en segundos.
- 🌐 UI limpia y moderna usando HTML + CSS.
- 🐳 Completamente containerizado con Docker Compose.
- 🗂️ Todos los videos descargados se almacenan en el directorio `/downloads`.
- 🔗 Descargas disponibles como enlaces clicables desde la misma interfaz.

---

## 🚀 Cómo usar

### 1. Clona el repositorio

```bash
git clone https://github.com/Karel95/yt-dlp_web.git

cd yt-dlp_web
```

### 2. Ejecuta el contenedor con Docker Compose

```bash
docker-compose up --build
```

### 3. Accede a la interfaz web

Abre tu navegador en:
<http://localhost:5000>
Pega un link de YouTube, dale a “Descargar” y el video se guardará en la carpeta downloads/. Luego aparecerá un enlace para bajarlo.
