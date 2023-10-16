
'''
	python3 STATUS/STATUS.py MASS/CONVERT
'''

import CYTE.MASS.SWAP as MASS_SWAP

def CHECK_1 ():
	assert (
		float (MASS_SWAP.START ([ 453.59237, "GRAMS" ], "POUNDS")) == 1.0
	)
	
	assert (
		float (MASS_SWAP.START ([ 10, "OUNCES" ], "POUNDS")) == 0.625
	)
	
	assert (
		float (MASS_SWAP.START ([ 10, "OUNCES" ], "GRAMS")) == 283.49523125
	)	

	return;
	
CHECKS = {
	"CHECK 1": CHECK_1
}