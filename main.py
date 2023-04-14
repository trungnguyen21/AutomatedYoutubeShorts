'''
This is the main file that will be run to generate the final videos. 
The .csv file must include column "title" and "body" for the program to work.
'''

import pandas as pd
import os
import mutagen.mp3 as MP3
import voice, final_video

csv_file = './scrape-text.csv'	
audio_path = './audio'
video_path = './videos'
export_path = './final'

#generate audios from a specified path (.txt files)
def generateAudio(filePath, title, exportPath): #filepath to the txt file, the title of the export file, export path

    with open(filePath, "r") as f:
        content = f.read()    
        voice.generateVoice(content, f'{exportPath}/{title}.mp3')
        print("Successfully generated audio for {}.txt".format(title))
        
        #trim audio to 60s
        audio = MP3.MP3(f'{exportPath}/{title}.mp3')
        if audio.info.length > 60:
            audio.info.length = 60
            audio.save()
            print(f"{title}.mp3 is trimmed to 60s")


def main(filePath, audioPath, videoPath, exportPath): #filepath to the csv file, export path
    if os.path.exists(exportPath) == False:
        os.mkdir(exportPath)

    # Read the csv file
    df = pd.read_csv(filePath)
    data = df[['title', 'body']]

    # Write data to the file
    for index, row in data.iterrows():
        #get the title and body of the article
        title = row['title']
        body = row['body']
        #write the title and body to the file
        with open(f"{audioPath}/{index}.txt", 'w') as f:
            f.write(title +'.\n')
            f.write(body +'.\n')
            print("Extracted {} successfully to {}".format(f"{index}.txt",audioPath))
        
        #generate audio from the file
        generateAudio(f"{audioPath}/{index}.txt", index, exportPath)
        final_video.finalize(videoPath, f'{audioPath}/{index}.mp3', index, exportPath)
        #delete txt file when finished generating audio
        os.remove(f"{exportPath}/{index}.txt")


        
if __name__ == '__main__':
    # check if file paths exist
    if os.path.exists(audio_path) == False:
        os.mkdir(audio_path)
    if os.path.exists(video_path) == False:
        os.mkdir(video_path)

    main(csv_file, audio_path, video_path, export_path)
    print("Program finished with 0 errors")
