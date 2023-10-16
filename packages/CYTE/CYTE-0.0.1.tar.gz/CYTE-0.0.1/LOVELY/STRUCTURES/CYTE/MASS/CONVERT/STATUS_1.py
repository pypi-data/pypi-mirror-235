
'''
	python3 STATUS/STATUS.py MASS/CONVERT
'''

from SPANS.MASS.CONVERT import CONVERT_MASS

def CHECK_1 ():
	assert (float (CONVERT_MASS ("GRAMS", "POUNDS", 453.59237)) == 1.0)
	
	assert (float (CONVERT_MASS ("OUNCES", "POUNDS", 10)) == 0.625)
	assert (float (CONVERT_MASS ("OUNCES", "GRAMS", 10)) == 283.49523125)	

	return;
	
CHECKS = {
	"CHECK 1": CHECK_1
}