# Greyson Rowland (2023)

from pytube import YouTube, Playlist
import os
import requests

print("YouTube Video Downloader by Greyson Rowland 2023")

def Download(link, path=None):
    youtubeObject = YouTube(link)
    title = youtubeObject.title
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print(f"Downloading {title}...")
        youtubeObject.download(path)
        print("Download has completed successfully")
    except:
        print("An error has occurred")

choice = int(input("[0] Download Video\n[1] Download Playlist\n[2] Get Video Data\n[3] Download Thumbnail\n"))
playlistFolder = os.getcwd() + "/playlist"

if choice == 0:
    link = input("Enter the YouTube video URL: ")
    Download(link)
if choice == 1:
    link = input("Enter the YouTube Playlist URL: ")
    list = Playlist(link).video_urls
    for i in list:
        yt = YouTube(i)
        title = None
        while title == None:
            try:
                title = yt.title
            except:
                title = None
        if not title.replace('"', "").replace("|", "").replace(".", "") in [x[:-4] for x in os.listdir(playlistFolder)]:
            print(f"Downloading {title}...")
            try:
                Download(i, playlistFolder)
            except:
                Download(i, playlistFolder)
            print("Done!")
        else:
            print(f"already downloaded {yt.title}")
if choice == 2:
    link = input("Enter the YouTube video URL: ")
    video = YouTube(link)
    log = input("Log to .txt file? (Y/N)\n")
    data = f"Author: {video.author}\nTitle: {video.title}\nLink: {link}\nLength: {video.length}\nViews: {video.views}"
    print(data)
    if log.lower() in ["y", "yes"]:
        f = open(f"{video.title}.txt", "w")
        f.truncate(0)
        f.write(data)
        f.close()
if choice == 3:
    link = input("Enter YouTube video URL: ")
    y = YouTube(link)
    u = y.thumbnail_url
    f = open(f"{y.title}.jpg", "wb")
    i = requests.get(u).content
    f.write(i)
