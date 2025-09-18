import os
from pytubefix import YouTube
from pytubefix.cli import on_progress  # progress callback with progress bar

url = input("Enter the URL of the video: ")

yt = YouTube(url, on_progress_callback=on_progress)
print("Title:", yt.title)

# Path for downloads
download_path = "mp3_downloads"
os.makedirs(download_path, exist_ok=True)

# Get the audio stream (best available)
audio_stream = yt.streams.filter(only_audio=True).first()

# Download as .mp4 audio
out_file = audio_stream.download(output_path=download_path)

# Rename to .mp3
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

print("Download completed! Saved as:", new_file)
