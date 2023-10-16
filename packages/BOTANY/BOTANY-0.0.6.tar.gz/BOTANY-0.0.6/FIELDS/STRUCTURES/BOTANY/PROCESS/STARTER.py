



'''
import BOTANY.PROCESS.START as PROCESS_STARTER
PROCESS_STARTER.START ("lsblk")
'''

import subprocess

def START (
	PERFORMANCE, 
	ALLOW = [ 0 ]
):
	try:
		EXIT_CODE = subprocess.call (
			PERFORMANCE,
			shell = True
		)

		if (EXIT_CODE not in ALLOW):
			print (f'Exit code "{ EXIT_CODE }" not allowed');
			print ("\nexiting <- failure");
			exit ();

	except Exception as x:
		print ("Anomaly Occurred")
		print (x)
		exit ();

	print ()
	print (PERFORMANCE, EXIT_CODE)
	print ()

	return;