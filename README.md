# AutomatedYoutubeShorts

This project produces videos for YoutubeShorts using AI, fully-automatic!

## Features ✨
No video compilation or editiing skills are needed. Everything is automatically generated. 

- Automatically fetch video from Pexels
- Generate voice-over, subtitle using AI, auto compile to one video using `moviepy`

## Files 💾

- `main.py` The main script
- `voice.py` Generate AI voices based on your content using Google Cloud Text to Speech
- `video-downloader.py` Fetch videos from Pexels as background videos
- `sub.py` Generate transcript and subtitle for the audio using AssemblyAI
- `final_video.py` Edit the videos using moviepy 

## Dependencies 👨‍💻

- `requirements.txt` Essential Python packages
- A Google Cloud account
- AssemblyAI API key
- ['ImageMagik'](https://imagemagick.org/script/download.php) and ['ffmpeg'](https://www.ffmpeg.org/download.html)

## Installation 💻
1. Clone this project!

2. Setup .csv file: 
The file should include a 'title' and 'body' data for the script to work

3. Fill in `config.py`:
Include API keys in `config.py`

4. Installing dependencies:
- `pip install -r requirements.txt`
- Install ['ImageMagik'](https://imagemagick.org/script/download.php) and ['ffmpeg'](https://www.ffmpeg.org/download.html)  
*For `ffmpeg` refer to this [guide](https://phoenixnap.com/kb/ffmpeg-windows)*

5. Execute script: 
Run `main.py` and wait until the program finishes ✅

## Demo 🎞

https://user-images.githubusercontent.com/37546053/232180344-6758b9ae-7773-45d9-a707-61e93f3648b3.mp4


Exported files are included in `media` folder of this project
