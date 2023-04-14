# AutomatedYoutubeShorts

This project produces videos for YoutubeShorts using AI, fully-automatic!


# Scripts

- `main.py` The main script
- `voice.py` Generate AI voices based on your content using Google Cloud Text to Speech
- `video-downloader.py` Fetch videos from Pexels as background videos
- `sub.py` Generate transcript and subtitle for the audio using AssemblyAI
- `final_video.py` Edit the videos using moviepy 

# Dependencies

- `requirements.txt` Essential Python packages
- A Google Cloud account
- AssemblyAI API key
- ['ImageMagik'](https://imagemagick.org/script/download.php) and ['ffmpeg'](https://www.ffmpeg.org/download.html)

# Setup
## Setup .csv file
The file should include a 'title' and 'body' data for the script to work

## Create directories
Create audio and video directory (optional)

## Create `config.py`
Include 
`assemblyai  =  'INSERT YOUR API KEY HERE'`
`pexelKey  =  'INSERT YOUR API KEY HERE'`

## Download background videos

Run `video-downloader.py` to fetch background videos for working material (recommended 10)

## Execute script
Run `main.py` and wait until the program finishes

# Demo
[Product Video](https://github.com/trungnguyen21/AutomatedYoutubeShorts/blob/main/media/9-with-subtitle.mp4)
Exported files are included in `media` folder of this project
