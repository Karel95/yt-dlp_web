from flask import Flask, render_template, request, send_from_directory
import subprocess
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'downloads')
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    video_url = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            subprocess.run([
                'yt-dlp',
                url,
                '-P', DOWNLOAD_FOLDER
            ])
            video_url = url
    files = os.listdir(DOWNLOAD_FOLDER)
    return render_template("index.html", files=files, video_url=video_url)

@app.route("/downloads/<filename>")
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
