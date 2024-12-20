import os
import random
from flask import Flask, render_template, send_from_directory, redirect, url_for

print("Starting the app...")

app = Flask(__name__)

# Static configuration
VIDEO_FOLDER = "static/videos"
IMAGE_FOLDER = "static/images"

# Store the last played video to avoid repeats
last_video = None

@app.route("/")
def opening_screen():
    return render_template("index.html")

@app.route("/play")
def play_random_video():
    global last_video
    videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]

    if len(videos) > 1:
        next_video = random.choice([v for v in videos if v != last_video])
    else:
        next_video = videos[0]

    last_video = next_video
    return render_template("video.html", video_url=f"/static/videos/{next_video}")

@app.route("/thankyou")
def thank_you_screen():
    return render_template("thankyou.html")

@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    # Just run Flask directly. The debug flag is optional.
    app.run(host="0.0.0.0", port=8080)
