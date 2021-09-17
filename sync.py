#!/usr/bin/env python

import os
import sys
import glob
import datetime


devicefolder = "/Users/mhuwiler/.AFTVolumes/samsung SM-A520F/storage/3565-3062/DCIM/Camera/"

localfolder = "/Users/mhuwiler/Pictures/Camera_Phone/"


for file in os.listdir(devicefolder): 
	if (os.path.isfile(devicefolder+file)): 
		#print file

		date = os.path.getmtime(devicefolder+file)

		print "File {} modified at {}".format(file, date)

