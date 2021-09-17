#!/usr/bin/env python

import os
import sys
import glob
from datetime import datetime


devicefolder = "/Users/mhuwiler/.AFTVolumes/samsung SM-A520F/storage/3565-3062/DCIM/Camera/"

localfolder = "/Users/mhuwiler/Pictures/Camera_Phone/"


for file in os.listdir(devicefolder): 
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

		print "Name: {}".format(stamp.strftime("%Y_%m_%d"))

		

