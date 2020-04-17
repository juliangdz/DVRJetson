import numpy as np 
import cv2
import os 
import sys
from pathlib import Path
import time
import datetime

def Filehandler(folder):
	os.chdir(folder)
	files = filter(os.path.isfile,os.listdir(folder))
	files = [os.path.join(folder,f) for f in files]
	files.sort(key=lambda x: os.path.getmtime(x))
	return files

def ArrGen(files):
	epochname = []
	for i in range(len(files)):
		filename = str(files[i]).split('/')[-1].split('.mp4')[0]
		epochname.append(int(filename))
	return epochname

def inEpochRange(epochname,compTime,allowedTime):
	for eP in range(len(epochname)):
		a = epochname[eP]
		if eP < len(epochname):
			b = epochname[eP + 1]
			Crange = list(range(int(a),int(b)))
			if compTime in  Crange:
				diffA = int(compTime) - int(a)
				diffB = int(b) - int(compTime)
				if diffA < allowedTime:
					print("in a condition",diffA)
					return a ,Crange[-1]
				elif diffB < allowedTime:
					print("in b condition",diffB)
					return b , Crange[-1]	

def SliceVideo_A(vidname,folder,Rpth,startime,endtime):
	try:
		vname = str(vidname) + str('.mp4')
		videoname = folder + vname
		stTime = startime - vidname
		eTime = endtime - vidname
		print(stTime)
		print(eTime)
		os.system("ffmpeg -i" + " " + str(videoname) + " " + "-ss" + " " + str(stTime) + " " + "-t" + " " + str(eTime) + " "+ "-c"+ " " + "copy" + " " + str(Rpth))
		return True

	except Exception as e:
		print("Error in A ",e)
		return False

def SliceVideo_B(vidname,folder,rpth,stTime,eTime):
	try:
		vname = str(vidname) + str('.mp4')
		videoname = folder + vname
		os.system("ffmpeg -i" + " " + str(videoname) + " " + "-ss" + " " + str(stTime) + " " + "-t" + " " + str(eTime) + " "+ "-c"+ " " + "copy" + " " + str(rpth))
		return True

	except Exception as e:
		print("Error in B",e)
		return False

def ConcatVideo(rpth1,rpth2,finalR):
	try:
		os.system("ffmpeg" +" " + "-i" +" "+ "\"concat:"+ rpth1 +"|"+rpth2 +"\""+ " " +"-c" + " " + "copy" + " " + finalR)
		return True

	except Exception as e:
		print("Error in Concat",e)
		return False

def main():
	folder = "/home/ubuntu/Desktop/PIKIT-5_WORKING/DVRJetson/DVR/Support/"
	results = "/home/ubuntu/Desktop/PIKIT-5_WORKING/DVRJetson/results/"
	files = Filehandler(folder)
	epochname = ArrGen(files)
	
	nowepochtime = 1587112980   #For testing Case B #	nowepochtime = 1587023494    # For tesstinng case A

	startime  = nowepochtime - 120
	endtime  = nowepochtime + 120
	allowedTime = 600

	videoname1 , Fvalue1 = inEpochRange(epochname,startime,allowedTime)
	videoname2 , Fvalue2 = inEpochRange(epochname,endtime,allowedTime)

	if videoname1 == videoname2:
		Rpth = results + "persondetected.mp4"
		Status_A = SliceVideo_A(videoname1,folder,Rpth,startime,endtime)
		print("in Condition A : Done Video Creation",Status_A)
	else : 
		#Cut 1st video
		rpth1 = results + str(videoname1) + ".mp4"
		stTime1 = startime - videoname1		
		eTime1  = Fvalue1 - videoname1
		print(videoname1)
		Status_B1 = SliceVideo_B(videoname1,folder,rpth1,stTime1,eTime1)
		#cut 2nd video
		rpth2 = results + str(videoname2) + ".mp4"
		stTime2 = videoname2 - Fvalue1
		eTime2 = endtime - videoname2
		print(videoname2)
		print(stTime2)
		print(eTime2)
		Status_B2 = SliceVideo_B(videoname2,folder,rpth2,stTime2,eTime2)
		if Status_B1 == True and Status_B2 == True:
			#concat video 
			finalR = results + "output.mp4"
			Status_C = ConcatVideo(rpth1,rpth2,finalR)
			print(" In Condition B : Concat Done ",Status_C)
#			os.system("rm " + " " + rpth1)
#			os.system("rm" + " " + rpth2)

if __name__ == '__main__':
	main()




