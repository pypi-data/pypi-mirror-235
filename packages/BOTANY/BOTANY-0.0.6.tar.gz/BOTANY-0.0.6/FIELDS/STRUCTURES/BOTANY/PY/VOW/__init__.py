



'''
	import BOTANY.PY.VOW as VOW
	VOW.EQUAL (1, 2, lambda VALUES : (print VALUES))
'''


'''
	SIMILAR:
		FUNGIBLE
		INTERCHANGEABLE
'''
def EQUAL (PARAM_1, PARAM_2, FN):
	if (PARAM_1 == PARAM_2):
		return True;
		
	FN ([ PARAM_1, PARAM_2 ])

	print (PARAM_1, PARAM_2);
	raise Exception ("Params are not fungible.")