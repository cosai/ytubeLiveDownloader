from threading import Thread
import cv2
import time
import numpy as np
class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None,pathOut="",sizeg=(1280,720)):
        fps=30
        self.size=sizeg
        self.frame = frame
        self.stopped = False
        self.out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, sizeg)
        # self.out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc('M','J','P','G'),fps,sizeg)
        self.now=time.time()
        self.prev=0

    def start(self):
        Thread(target=self.show, args=()).start()
        self.now=time.time()
        return self

    def show(self):
        while not self.stopped:
            limit=int(self.size[1])
            currentFrameVal=np.sum(self.frame[:limit,:]) %255
            if currentFrameVal - self.prev != 0:
                cv2.imshow("Video", self.frame[:limit,:])
                self.out.write(self.frame[:limit,:])
            self.prev = currentFrameVal
            if time.time() - self.now > 600 or cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True
        self.out.release()
