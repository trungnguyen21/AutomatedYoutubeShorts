"""
Fetch videso from Pexels API using pexelsPy
"""

import requests, config
from pexelsPy import api

PEXEL_API_KEY = config.pexelKey

api = api.API(PEXEL_API_KEY)

def getVideo(videoPath, num):
    api.search_videos("drone shot of the sea", orientation='portrait', page=1, results_per_page=num)
    videos = api.get_videos()
    
    for video in videos:
        download_url = "https://pexels.com/video/" + str(video.id) + "/download"
        r = requests.get(download_url)
        with open(videoPath+video.url.split('/')[-2]+'.mp4', 'wb') as out:
            out.write(r.content)
            print(f"{video.url.split('/')[-2]}.mp4 is downloaded successfully!")
    return 0

getVideo('./components/videos/', 1)