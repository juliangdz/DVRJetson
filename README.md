# DVR JETSON





## Context

------------------------------------------------------------------------------------------------------------------------------------------------------
Add the rtsp streams to the rtsp.txt file in supporting_scripts in the form of:

*rtsp://.............. , cameraname**


Then use crontab to invoke the scripts and run.

------------------------------------------------------------------------------------------------------------------------------------------------------

step :1 -- save video in 10 mins duration

*Saving video*

Save video file with name : The below command saves the video from an rtsp link in 5Min segments and also saves it with the epoch time it was first generated with 


ffmpeg -i rtsp:// -c copy -map 0 -f segment -segment_time 300 -segment_format mp4 -strftime 1 "%s.mp4"

**Check VideoDVR.sh**

1.	The script VideoDVR.sh will create bash scripts based on the info from the rtsp.txt.

2.	The scipt will create the Bash scripts to save 10 minute video chunks for each camera in the respective camera folder.


Step : 2

*To Create video to send to user*

--there will be a 20 min delay maximum in each case since in the previous step we take 10 min video chunk to be saved.

**Check VGen.py**

1.	Filehandler : Returns a Sorted Array of Videonames , sorted based on time of creation

2.	ArrGen : Returns a List of of Only the Epochtime from the videoname

3.	inEpochRange : Returns videoname satifying the conditions and the last duration of the video (in epoch)
		
			Here we create a Range of Epochtimes in a List format with the list of Epochname we got from the ArrGen function , then we compare with the compTime and allowedTime. 

4.	SliceVideo_A : This function is called when the Person Detected Time is within a single video , then ffmpeg to slice that part of the video with 2 mins before detection as start time and 2 mins after detection as end time.

5. SliceVideo_B : This function is called when Person Detected Time is in two videos , then ffmpeg slice gets the chunks from both the videos.

6. ConcatVideo : This function Concats the two videos we sliced up in B condition.





