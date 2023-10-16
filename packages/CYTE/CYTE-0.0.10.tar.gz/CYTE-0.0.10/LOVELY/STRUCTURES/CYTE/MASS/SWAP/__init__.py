

'''
	https://www.wolframalpha.com/input?i=gram+to+pound
'''

'''
	GOAL:
		MASS ([ 432, "GRAMS" ], "POUNDS")
'''

'''
	import CYTE.MASS.SWAP as MASS_SWAP
	MASS_SWAP.START ()
'''

from fractions import Fraction 

CONVERSIONS = {
	"OUNCES": {
		"POUNDS": Fraction (1, 16),
		"GRAMS": Fraction (28.349523125)
	},
	"POUNDS": {
		"OUNCES": 16,
		"GRAMS": Fraction (453.59237)
	},
	"GRAMS": {
		"POUNDS": Fraction (1, Fraction (453.59237))
	}
}

def START (FROM, TO_UNIT):
	[ FROM_AMOUNT, FROM_UNIT ] = FROM;

	assert (FROM_UNIT in CONVERSIONS)
	assert (TO_UNIT in CONVERSIONS [ FROM_UNIT ])

	return CONVERSIONS [ FROM_UNIT ] [ TO_UNIT ] * Fraction (FROM_AMOUNT);