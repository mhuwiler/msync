#!/usr/bin/env python


import os
from datetime import datetime
from CopyMode import CopyMode


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

