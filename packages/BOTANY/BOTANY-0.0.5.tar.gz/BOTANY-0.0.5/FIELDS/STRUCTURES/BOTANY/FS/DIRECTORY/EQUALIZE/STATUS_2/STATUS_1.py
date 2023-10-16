

'''
	python3 STATUS.py "FS/DIRECTORY/EQUALIZE/STATUS_2/STATUS_1.py"
'''

import BOTANY.FS.DIRECTORY.DEALLOCATE as DEALLOCATE	
import BOTANY.FS.DIRECTORY.EQUALIZE as EQUALIZE
import BOTANY.PY.VOW as VOW

def PATH (DIRECTORY):
	import pathlib
	FIELD = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	import sys
	return normpath (join (FIELD, DIRECTORY))

def CHECK_1 ():
	START = PATH ("START")
	END = PATH ("END")

	print ("START:", START)
	print ("END:", END)

	try:
		DEALLOCATE.DIRECTORY (END)
	except Exception as E:
		print (E)

	EQUALIZE.MULTIPLE ({
		"DIRECTORY 1": START,
		"DIRECTORY 2": END,
		
		"DIRECTORIES": [
			"1",
			"2",
			"3"
		],
		
		"START": "yes"	
	})
	
	DEALLOCATE.DIRECTORY (END)

	return;
	
	
CHECKS = {
	"CHECK 1": CHECK_1
}