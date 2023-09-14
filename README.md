# ytubeLdownloader

Live youtube video downloader Python script


- This program crops the frame to 1280 x 720. See videoshow.py for more detail
- The default FPS(frames per second) is 30, which is stated in the videoshow.py
- The program saves the video given in the url as input arguement to specified file name
- If you use shell file to run the recorder program, you only need to specify the youtube link as the command line parameter while calling the shell file. The file will be saved with name as current timestamp in the same directory where runvideo.sh is located.
- Ex: *bash runvideo.sh https://youtu.be/?watch=XABCDEFGHIJKLMNO*
- While saving the video, you will be able to watch the video also 
- Stops saving when the user pushes "q" or 10 minutes passed since start, whichever is earlier
