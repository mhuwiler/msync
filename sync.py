#!/usr/bin/env python

import os
import sys
import glob
from datetime import datetime
import shutil
import hashlib


devicefolder = "/Users/mhuwiler/.AFTVolumes/samsung SM-A520F/storage/3565-3062/DCIM/Camera/"

localfolder = "/Users/mhuwiler/Pictures/Camera_Phone/"


for file in sorted(filter(os.path.isfile, [devicefolder+f for f in os.listdir(devicefolder)]), key=os.path.getmtime): #Getting files sorted by date
#for file in os.listdir(devicefolder): 
	file = os.path.basename(file)
	if (os.path.isfile(devicefolder+file)): 
		#print file

		# Based on modification time
		date = os.path.getmtime(devicefolder+file)

		print "File {} modified at {}".format(file, date)

		foldername = datetime.fromtimestamp(date).strftime("%Y_%m_%d")

		print "Folder: {}".format(foldername)

		# Based on filename
		framedate = file.split("_")[0]

		print framedate

		stamp = datetime.strptime(framedate, "%Y%m%d")

		foldername = stamp.strftime("%Y_%m_%d")

		print "Name: {}".format(foldername)

		checksum = hashlib.md5(open(devicefolder+file, "rb").read()).hexdigest()

		print checksum


		currentdest = localfolder+foldername

		if not os.path.isdir(currentdest): 
			os.makedirs(currentdest) # for python 3:  exist_ok = True

		shutil.copy2(devicefolder+file, currentdest)

