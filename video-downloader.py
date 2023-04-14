'''
This script downloads videos from pexels.com. Uses this to get videos background
in case you need more.
'''

from pexelsPy import API 
import requests, config

PEXEL_API_KEY = config.pexelKey

api = API(PEXEL_API_KEY)

def getVideo(num):
    api.search_videos("drone shot of the sea", orientation='portrait', page=1, results_per_page=num)
    videos = api.get_videos()
    
    for video in videos:
        download_url = "https://pexels.com/video/" + str(video.id) + "/download"
        r = requests.get(download_url)
        with open(f"./videos/"+video.url.split('/')[-2]+'.mp4', 'wb') as out:
            out.write(r.content)
            print(f"{video.url.split('/')[-2]}.mp4 is downloaded successfully!")

