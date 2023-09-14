#~/bin/bash
#starts a record with current day (the file name will be the date)
CURRENTDATE=`date +"%m_%d_%Y_%H_%M_%S"`
#with a video link
VIDEOLINK="https://www.youtube.com/watch?v=YyvdDQ60qJw"
python runme.py --source ${VIDEOLINK} --outfile file${CURRENTDATE}.avi
