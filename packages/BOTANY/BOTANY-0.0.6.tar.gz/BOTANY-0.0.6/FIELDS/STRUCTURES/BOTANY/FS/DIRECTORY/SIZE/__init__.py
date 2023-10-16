


'''
CAUTION: HAS ACCESS TO SHELL
'''

'''
import BOTANY.FS.DIRECTORY.SIZE as SIZE
SIZE.FIND ({
	"DIRECTORY PATH": ""
})
'''

'''
https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
'''

import subprocess
from os.path import dirname, join, normpath

from pathlib import Path

def FIND (SHARES):
	DIRECTORY_PATH = SHARES ["DIRECTORY PATH"]
	return sum (
		p.stat().st_size for p in Path (DIRECTORY_PATH).rglob ('*')
	)

