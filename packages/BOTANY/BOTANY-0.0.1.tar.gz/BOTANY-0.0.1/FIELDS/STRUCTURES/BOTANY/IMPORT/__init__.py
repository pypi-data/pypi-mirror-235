
'''
	import BOTANY.IMPORT as IMPORT
	STRUCTURE = IMPORT ("/STRUCTURES/STRUCTURE.py")
	
	STRUCTURE.START ()
'''

from importlib.machinery import SourceFileLoader
import os
	
def IMPORT (MODULE_PATH):	
	if (MODULE_PATH [ 0 ] == "/"):
		FULL_PATH = MODULE_PATH;
	else:
		DIR_PATH = os.path.dirname (os.path.realpath (__file__))
		FULL_PATH = os.path.normpath (DIR_PATH + "/" + MODULE_PATH)

	return SourceFileLoader (FULL_PATH, FULL_PATH).load_module ()

