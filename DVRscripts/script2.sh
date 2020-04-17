#!/bin/bash
while true
do
    sudo ffmpeg -i "rtsp://python:India123@192.168.75.18/Streaming/Channels/1001" -c copy -map 0 -f segment -segment_time 600 -strftime 1 "/home/ubuntu/Desktop/PIKIT-5_WORKING/DVRJetson/DVR/Entrance/%s.mp4"
    sudo chmod -R 777 *
done
