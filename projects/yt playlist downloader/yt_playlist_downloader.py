# Playlist downloader with Pytube
from pytube import Playlist, YouTube
import os

# Ask for playlist link
playlist_link = input("Enter the playlist link: ")

# Load playlist
p = Playlist(playlist_link)

# Make downloads folder
download_path = "downloads"
os.makedirs(download_path, exist_ok=True)

print(f"\nDownloading playlist: {p.title}")
print(f"Total videos: {len(p.videos)}\n")

# Download videos
for video in p.videos:
    try:
        yt = YouTube(video.watch_url)
        print(f"Downloading: {yt.title}...")
        yt.streams.get_highest_resolution().download(output_path=download_path)
        print(f"Download completed! {video.title} \n")
    except Exception as e:
        print(f"Failed to download {video.title}: {e}\n")

print("All videos processed!")
