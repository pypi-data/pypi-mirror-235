

'''
	python3 STATUS.py "FS/DIRECTORY/CHECK_EQ/STATUS_1/STATUS_1.py"
'''

import BOTANY.FS.DIRECTORY.CHECK_EQ as CHECK_EQ

def PATH (DIRECTORY):
	import pathlib
	FIELD = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	import sys
	return normpath (join (FIELD, DIRECTORY))

def CHECK_1 ():
	DIRECTORY_1 = PATH ("DIRECTORIES/EQ_1")
	DIRECTORY_2 = PATH ("DIRECTORIES/EQ_2")

	REPORT = CHECK_EQ.START (
		DIRECTORY_1,
		DIRECTORY_2
	)	
	assert (
		{'1': {}, '2': {}} ==
		REPORT
	)
	
CHECKS = {
	"EQ check without differences": CHECK_1
}