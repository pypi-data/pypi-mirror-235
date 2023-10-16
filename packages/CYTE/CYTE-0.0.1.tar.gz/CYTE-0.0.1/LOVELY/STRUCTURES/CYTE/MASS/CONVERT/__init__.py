

'''
	https://www.wolframalpha.com/input?i=gram+to+pound
'''

'''
	GOAL:
		CONVERT_MASS ("GRAMS", "POUNDS", 432)
'''

'''
	from SPANS.MASS.CONVERT import CONVERT_MASS
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

def CONVERT_MASS (FROM_UNIT, TO_UNIT, AMOUNT):
	assert (FROM_UNIT in CONVERSIONS)
	assert (TO_UNIT in CONVERSIONS [ FROM_UNIT ])


	return CONVERSIONS [ FROM_UNIT ] [ TO_UNIT ] * Fraction (AMOUNT);