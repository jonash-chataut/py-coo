import os
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress_bar  # for progress bar

# Ask for playlist link
playlist_link = input("Enter the playlist link: ")

# Load playlist
p = Playlist(playlist_link)

# Make downloads folder
download_path = "playlist_downloads"
os.makedirs(download_path, exist_ok=True)

print(f"\nDownloading playlist: {p.title}")
print(f"Total videos: {len(p.video_urls)}\n")

# Download videos one by one
for url in p.video_urls:
    try:
        yt = YouTube(url, on_progress_callback=on_progress_bar)
        print(f"\nDownloading: {yt.title}...")
        yt.streams.get_highest_resolution().download(output_path=download_path)
        print(f"Download completed: {yt.title}\n")
    except Exception as e:
        print(f"Failed to download {url}: {e}\n")

print("All videos processed!")
