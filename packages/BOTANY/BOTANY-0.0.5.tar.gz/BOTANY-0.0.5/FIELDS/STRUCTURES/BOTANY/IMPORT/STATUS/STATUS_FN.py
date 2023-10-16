



from BOTANY.IMPORT import IMPORT

def FN ():
	STRUCTURE = IMPORT ("EXAMPLE.py")
	RETURNS = STRUCTURE.START ()

	assert (RETURNS == 998)

	return;