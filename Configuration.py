#!/usr/bin/env python

import os
from datetime import datetime


class CopyMode: 
	@staticmethod
	def getFolderName(file, destfolder): 
		raise NotImplementedError()

	@staticmethod
	def folderNameFromMtime(file): 
		# Based on modification time
		date = os.path.getmtime(file)
		foldername = datetime.fromtimestamp(date).strftime("%Y_%m_%d")
		return foldername


class GalaxyA52017(CopyMode): 
	@staticmethod
	def getFolderName(file, destfolder): 
		return destfolder + GalaxyA52017.folderNameFromFileName(os.path.basename(file))

	@staticmethod
	def folderNameFromFileName(filename): 
		# Based on filename
		framedate = filename.split("_")[0]
		foldername = datetime.strptime(framedate, "%Y%m%d").strftime("%Y_%m_%d")
		return foldername


class default(CopyMode): 
	@staticmethod
	def getFolderName(file, destfolder): 
		return destfolder


copyMode = { "plain": default, 
			 "CanonCameraWindow": GalaxyA52017
			}

