from threading import Thread
import cv2

class RTSPVideoWriterObject(object):
    def __init__(self, name, src=0 ):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)
        self.name = name
        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv2.VideoWriter(self.name + '.avi', self.codec, 30, (self.frame_width, self.frame_height))

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Display frames in main program
        if self.status:
            cv2.imshow(self.name, self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # Save obtained frame into video output file
        self.output_video.write(self.frame)

if __name__ == '__main__':
    rtsp_stream_link = 'rtsp://user:password@172.20.10.8/1'
    rtsp_stream_link2 = 'rtsp://user:password@172.20.10.12/1'
    video_stream_widget = RTSPVideoWriterObject("one Camera", rtsp_stream_link)
    video_stream_widget2 = RTSPVideoWriterObject("two Camera", rtsp_stream_link2)
    while True:
        try:
            video_stream_widget.show_frame()
            video_stream_widget.save_frame()
            video_stream_widget2.show_frame()
            video_stream_widget2.save_frame()


        except AttributeError:
            pass
