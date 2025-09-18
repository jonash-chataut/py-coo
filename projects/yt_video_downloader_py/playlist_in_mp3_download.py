import os
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress_bar  # progress bar

# Ask for playlist link
playlist_link = input("Enter the playlist link: ")

# Load playlist
p = Playlist(playlist_link)

# Make downloads folder
download_path = "playlist_mp3_downloads"
os.makedirs(download_path, exist_ok=True)

print(f"\nDownloading playlist: {p.title}")
print(f"Total videos: {len(p.video_urls)}\n")

# Download each video as MP3
for url in p.video_urls:
    try:
        yt = YouTube(url, on_progress_callback=on_progress_bar)
        print(f"\nDownloading audio: {yt.title}...")
        
        # Get best audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download
        out_file = audio_stream.download(output_path=download_path)
        
        # Convert to .mp3 (just renaming, not re-encoding)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        
        print(f"Saved as: {new_file}\n")
    except Exception as e:
        print(f"Failed to download {url}: {e}\n")

print("All audios processed!")
