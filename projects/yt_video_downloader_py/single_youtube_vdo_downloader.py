import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Enter the url of the video: ")

yt = YouTube(url, on_progress_callback=on_progress)
print("Title: ", yt.title)

#here the path is in the same folder in which the code is so i gave directly if you want you can give the custom path of your own choice
download_path = "downloads" 
os.makedirs(download_path, exist_ok=True)

ys = yt.streams.get_highest_resolution()
ys.download(output_path=download_path)

print("Download completed!")

