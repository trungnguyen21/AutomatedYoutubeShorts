# AutomatedYoutubeShorts

This project produces videos for YoutubeShorts fully-automatic!

## Features ✨
No video compilation or editiing skills are needed. Everything is automatically generated. 

- Automatically fetch video from Pexels
- Generate voice-over, subtitle using AI, auto compile to one video using `moviepy`

## Files 💾

- `main.py` The main script
- `scripts/text_to-speech.py` Generate voiceover based on your content using ElevenLabs
- `scripts/video-downloader.py` Fetch videos from Pexels as background videos
- `scripts/generate_subtitle.py` Generate transcript and subtitle for the audio using AssemblyAI
- `scripts/edit_video.py` Edit the videos using moviepy 

## Dependencies 👨‍💻

- `requirements.txt` Essential Python packages
- An ElevenLabs API key
- AssemblyAI API key
- ['ImageMagick'](https://imagemagick.org/script/download.php) and ['ffmpeg'](https://www.ffmpeg.org/download.html)

## Installation 💻
1. Clone this project!

2. Setup .csv file: 
The file should include a 'title' and 'body' data for the script to work

3. Fill in `config.py`:
Include API keys in `config.py`

4. Installing dependencies:
*Window users*:
- `pip install -r requirements.txt`
- Install ['ImageMagik'](https://imagemagick.org/script/download.php) and ['ffmpeg'](https://www.ffmpeg.org/download.html)  
*For `ffmpeg` refer to this [guide](https://phoenixnap.com/kb/ffmpeg-windows)*
*Mac users*:
- Install HomeBrew
- Run these 2 commands in the terminal:
`brew intsall ffmpeg`
`brew intsall imagemagick`

5. Execute script: 
Run `main.py` and wait until the program finishes ✅

## Demo 🎞

https://user-images.githubusercontent.com/37546053/232180344-6758b9ae-7773-45d9-a707-61e93f3648b3.mp4


Exported files are included in `results` folder of this project


# Change logs:
* March 26, 2024: 
- Re-factor codes
- Re-organize files
- Migrate to ElevenLabs for TTS
- Add custom-built library for getting portrait videos from Pexels
- Add instructions for Mac users

* May 9, 2023: Add the `config.py` file

* April 14, 2023: Initial release
