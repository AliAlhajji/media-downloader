from pytube import YouTube
from sclib import SoundcloudAPI, Track
from os import path, rename, mkdir

## Folders names
soundcloud_folder = 'SoundCloud'
youtube_folder = 'YouTube'

#Download files from YouTube
def youtube_download():
    link = ""
    while link == "":
        link = input(">> Type in the link: ")
    
    file_type = ""
    while file_type.lower() not in ["mp3", "mp4"]:
        file_type = input(">> [MP3] or [MP4]? ")
    
    yt = YouTube(link)
    streams = yt.streams

    if file_type.lower() == "mp3":
        audio_file = streams.get_audio_only().download(youtube_folder)
        base, ext = path.splitext(audio_file)
        rename(audio_file, '{}.mp3'.format(base))
    else:
        video = streams.filter(mime_type='video/mp4').first()
        video.download(youtube_folder)

#Download files from SoundCloud
def soundcloud_download():
    link = ""
    while link == "":
        link = input(">> Type in the link: ")
    
    api = SoundcloudAPI()
    track = api.resolve(link)
    file_name = ''.join([char for char in track.title if char not in '<>:"/\|?*'])
    file_name = '{}.mp3'.format(file_name)
    with open('./{}/{}'.format(soundcloud_folder, file_name), 'wb+') as file:
        track.write_mp3_to(file)

#Create the folders if they dont already exist
if not path.exists(youtube_folder):
    mkdir(youtube_folder)
if not path.exists(soundcloud_folder):
    mkdir(soundcloud_folder)

#Select the website and run the proper downloader function
website = ''
while website not in ['1', '2']:
    website = input('> Type 1 for YouTube, 2 for SoundCloud: ')

if website == '1':
    youtube_download()
elif website == '2':
    soundcloud_download()