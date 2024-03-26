# Pexels Website:   https://www.pexels.com
# class information:
#     Video's data stucture
class Video:
    def __init__(self, json_video):
        self.__video = json_video
    @property
    def id(self):
        return int(self.__video["id"])
    @property
    def width(self):
        return int(self.__video["width"])
    @property
    def height(self):
        return int(self.__video["height"])
    @property
    def url(self):
        return self.__video["url"]
    @property
    def image(self):
        return self.__video["image"]
    @property
    def duration(self):
        return self.__video["duration"]
    @property
    def userID(self):
        return int(self.__video["user"]["id"])
    @property
    def userName(self):
        return self.__video["user"]["name"]
    @property
    def userURL(self):
        return self.__video["user"]["url"]
    @property
    def videoFilesID(self):
        return int(self.__video["video_files"]["id"])
    @property
    def videoQuality(self):
        return self.__video["video_files"]["quality"]
    @property
    def videoFileType(self):
        return self.__video["video_files"]["file_type"]
    @property
    def videoFileWidth(self):
        return int(ideo["video_files"]["width"])
    @property
    def videoFilesHeight(self):
        return int(self.__video["video_files"]["height"])
    @property
    def videoFilesLink(self):
        return self.__video["video_files"]["link"]
    @property
    def videoPictures(self):
        return int(self.__video["video_pictures"]["id"])
    @property
    def videoPictures(self):
        return self.__video["video_pictures"]["picture"]
    @property
    def videoNumber(self):
        return int(self.__video["video_pictures"]["nr"])
    

    