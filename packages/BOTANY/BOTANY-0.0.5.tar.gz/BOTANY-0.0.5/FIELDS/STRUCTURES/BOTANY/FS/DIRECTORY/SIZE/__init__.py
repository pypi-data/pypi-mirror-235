


'''
CAUTION: HAS ACCESS TO SHELL
'''

'''
import BOTANY.FS.DIRECTORY.SIZE as SIZE
SIZE.FIND ({
	"DIRECTORY PATH": ""
})
'''

import subprocess
from os.path import dirname, join, normpath

def FIND (SHARES):
	FOLDER_PATH = SHARES ["DIRECTORY PATH"]
		
	SIZE = subprocess.run (
		f"du -sh '{ FOLDER }'",
		
		shell = True, 
		check = True,
		
		capture_output = True, 
		text = True,
		cwd = normpath (join (dirname (__file__)))
	).stdout.strip ("\n")
	
	return SIZE
