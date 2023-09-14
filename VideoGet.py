from threading import Thread
import cv2
import pafy
   
class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """
    def get_youtube_cap(self):
        play = pafy.new(self.vurl).streams[-1] # we will take the lowest quality stream
        assert play is not None # makes sure we get an error if the video failed to load
        return cv2.VideoCapture(play.url)
    
    def __init__(self, url):
        self.vurl=url
        self.stream = self.get_youtube_cap()
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True

