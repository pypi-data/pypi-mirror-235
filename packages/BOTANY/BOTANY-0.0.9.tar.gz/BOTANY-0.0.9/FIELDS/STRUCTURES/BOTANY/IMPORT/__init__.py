
'''
	from BOTANY.IMPORT import IMPORT
	STRUCTURE = IMPORT ("/STRUCTURES/STRUCTURE.py")
	
	STRUCTURE.START ()
'''

from importlib.machinery import SourceFileLoader
import os
	
import inspect
import os


	
def IMPORT (MODULE_PATH):	
	print ("IMPORTING")

	if (MODULE_PATH [ 0 ] == "/"):
		FULL_PATH = MODULE_PATH;
		
	else:
		FILE_OF_CALLING_FUNCTION = os.path.abspath (
			(inspect.stack () [1]) [1]
		)
		FOLDER_OF_CALLING_FUNCTION = os.path.dirname (
			FILE_OF_CALLING_FUNCTION
		)	
	
		DIR_PATH = os.path.dirname (os.path.realpath (__file__))
		FULL_PATH = os.path.normpath (FOLDER_OF_CALLING_FUNCTION + "/" + MODULE_PATH)

	print ("FULL PATH:", FULL_PATH)

	return SourceFileLoader (FULL_PATH, FULL_PATH).load_module ()

