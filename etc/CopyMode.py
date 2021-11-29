#!/usr/bin/env python


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


class default(CopyMode): 
	@staticmethod
	def getFolderName(file, destfolder): 
		return destfolder


