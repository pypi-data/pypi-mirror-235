

'''
	PLAN:

import BOTANY.FS.DIRECTORY.EQUALIZE as EQUALIZE

EQUALIZE.MULTIPLE ({
	"DIRECTORY 1": "",
	"DIRECTORY 2": "",
	
	"DIRECTORIES": [
			
	],
	
	"START": "no"	
})
'''

import BOTANY.FS.DIRECTORY.RSYNC as RSYNC
import BOTANY.FS.DIRECTORY.CHECK_EQ as CHECK_EQ
import BOTANY.FS.DIRECTORY.SIZE as SIZE

import BOTANY.PY.VOW as VOW

from os.path import dirname, join, normpath

def MULTIPLE (SHARES):
	DIRECTORY_1 = SHARES ["DIRECTORY 1"]
	DIRECTORY_2 = SHARES ["DIRECTORY 2"]
	
	DIRECTORIES = SHARES ["DIRECTORIES"]
	
	if ("START" in SHARES and SHARES ["START"] == "yes"):
		START = "yes"
	else:
		START = "no"
	
	OUTPUT = []
	
	for DIRECTORY in DIRECTORIES:	
		FROM = normpath (join (DIRECTORY_1, DIRECTORY))
		TO = normpath (join (DIRECTORY_2, DIRECTORY))
	
		STRING = RSYNC.PROCESS ({
			"FROM": FROM,
			"TO": TO,
			
			"START": START
		})
		
		if (START == "no"):
			print ("STRING:", STRING)
			
		REPORT = CHECK_EQ.START (
			FROM,
			TO
		)	
		VOW.EQUAL (
			REPORT,
			{'1': {}, '2': {}},
			lambda PARAMS : print (PARAMS)
		)
		
		
		
		SIZE_FROM = SIZE.FIND ({
			"DIRECTORY PATH": FROM
		})
		SIZE_TO = SIZE.FIND ({
			"DIRECTORY PATH": TO
		})
		
		OUTPUT.append ({
			"EQ CHECK": REPORT,
			"SIZES": {
				"FROM": SIZE_FROM,
				"TO": SIZE_TO
			}
		})
		
	return OUTPUT