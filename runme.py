import argparse
import os
import cv2
from VideoGet import VideoGet
from VideoShow import VideoShow

# LIVE Youtube video saver
# cReated at Currus AI for data collection purposes

def threadBoth(source="",outputfilename="videoDemo.avi"):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """
    if source == "":
        return
        # ifthe source is empty then nothing to do
    
    # Default size of the video
    sizeTuple = (1280,720)
    video_getter = VideoGet(source).start()
    video_shower = VideoShow(video_getter.frame,outputfilename,sizeTuple).start()
    f=0
    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        video_shower.frame = frame
        f+=1
    print(f"{f} frames written")    

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", "-s", default="none",
        help="Input url")
    ap.add_argument("--outfile", "-o", default="videoDemo.avi",
        help="Output file")
    args = vars(ap.parse_args())
    #live video example "https://www.youtube.com/watch?v=5_XSYlAfJZM"
    if args.get("source",None) is None:
        print("Source arguement is missing")
    else:
        threadBoth(args["source"], args["outfile"])
