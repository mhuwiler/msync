#!/usr/bin/env python

import os
import sys
import glob
from datetime import datetime
import shutil
import hashlib
import json


devicefolder = "/Users/mhuwiler/.AFTVolumes/samsung SM-A520F/storage/3565-3062/DCIM/Camera/"

localfolder = "/Users/mhuwiler/Pictures/Camera_Phone/"


def getmd5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def getsha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def folderNameFromMtime(file): 
	# Based on modification time
	date = os.path.getmtime(file)
	foldername = datetime.fromtimestamp(date).strftime("%Y_%m_%d")
	return foldername

def folderNameFromFileName(filename): 
	# Based on filename
	framedate = filename.split("_")[0]
	foldername = datetime.strptime(framedate, "%Y%m%d").strftime("%Y_%m_%d")
	return foldername

def copyFile(src, dest): 
	if not os.path.isdir(dest): 
		os.makedirs(dest) # for python 3:  exist_ok = True

	shutil.copy2(src, dest)


bookkeeping = {}


for file in sorted(filter(os.path.isfile, [devicefolder+f for f in os.listdir(devicefolder)]), key=os.path.getmtime): #Getting files sorted by date
#for file in os.listdir(devicefolder): 
	#file = os.path.basename(file)
	if (os.path.isfile(file)): 
		#print file

		filename = os.path.basename(file)
		foldername = folderNameFromFileName(filename)

		#checksum = hashlib.sha256(open(file, "rb").read()).hexdigest()
		checksum = getsha256(file)

		bookkeeping.update({filename:checksum})




		currentdest = localfolder+foldername

		print "Copying file {}".format(filename)
		copyFile(file, currentdest)
		


print bookkeeping

