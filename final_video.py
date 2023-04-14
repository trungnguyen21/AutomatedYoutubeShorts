from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, TextClip
from moviepy.video.tools.subtitles import SubtitlesClip
import random, os
import mutagen.mp3 as MP3
from sub import *

def createBackground(audio_path, videoPath): #the path to the mp3 file, the path to the video FILES (folder)
    print("Creating background for the video...Gathering Audio and Video files")
    audio = MP3.MP3(audio_path)
    voice = AudioFileClip(audio_path)
    print("Done gathering files")
    
    durationAudio = audio.info.length
    video = VideoFileClip("{}/{}".format(videoPath,random.choice(os.listdir(f'{videoPath}'))), audio=False)
    durationVideo = video.duration
    print("Editing the videos...")

    if durationVideo >= durationAudio:
        # get the duration of the video clip
        final_clip = video.subclip(0, durationAudio)
        exportClip = final_clip.set_audio(voice)
        return exportClip #return VideoClip instance
    elif durationAudio > durationVideo:
        # search through ./videos, get a random video and concatenate it with the first video, 
        # repeat until the video length is greater than the audio length

        while durationVideo < durationAudio:
            video2 = VideoFileClip("{}/{}".format(videoPath,random.choice(os.listdir(f'{videoPath}'))), audio=False)
            video = concatenate_videoclips([video, video2])
            durationVideo += video2.duration


        # video2 = VideoFileClip("./videos/{}".format(random.choice(os.listdir('./videos'))), audio=False)
        # final_clip = concatenate_videoclips([video, video2])
        final_clip = video.subclip(0, durationAudio)
        exportClip = final_clip.set_audio(voice)
        return exportClip #return VideoClip instance
    else:
        #return error if any
        return 1
        
def finalize(videoPath, audio_path, title, exportPath='./'): #the path to video FILES, the path to the mp3 file, the title of the video, export path
    final_clip = createBackground(audio_path, videoPath)
    #get the transcript
    transcript = save_transcript(audio_path, title, exportPath)

    #set the subtitle for the video from the srt file
    generator = lambda text: TextClip(text, font='Helvetica Neue', fontsize=50, color='white', 
                                      stroke_color='black', stroke_width=1, bg_color='black',
                                      method='caption', size=(final_clip.w*0.8, None))
    sub = SubtitlesClip(transcript, generator)
    subtitle = SubtitlesClip(sub, generator)
    subtitle = subtitle.set_pos('center').set_duration(final_clip.duration)
    final_clip = CompositeVideoClip([final_clip, subtitle])
    final_clip.write_videofile(f"{exportPath}/{title}-with-subtitle.mp4")
    print("Successfully saved the video {} with subtitle".format(str(title)+"-with-subtitle.mp4"))


# finalize('./result/7.mp3', '7', './final-videos/')



