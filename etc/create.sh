CLASSNAME="${1:-MyCopyMode}"

echo "#!/usr/bin/env python


from CopyMode import CopyMode


class ${CLASSNAME}(CopyMode): 
	@staticmethod
	def getFolderName(file, destfolder): 
		raise NotImplementedError() # replace this line with your implementation

	#@staticmethod
	#def myHelperMethod(): 
	#	pass


" > ${CLASSNAME}.py

echo "
Created skeleton copy mode: ${CLASSNAME}.py
" #Please modify it according to the instructions found inside. 