


'''
import CYTE.FOOD.USDA.FORM_1 as FORM_1
RETURN = FORM_1.MAKE ()
'''

from CYTE.FOOD.NIH.FORM_1.CALC.DIVISIONS import CALC_DIVISIONS



def MAKE (
	NIH_FOOD_DATA
):
	REFORMATTED = {
		"PRODUCT": {
			"NAME": "",
			"UPC": ""
		},
		
		"DIVISIONS": []
	}

	NOTES = []

	DIVISIONS = CALC_DIVISIONS (NIH_FOOD_DATA)

	'''
	if ("description" in USDA_FOOD_DATA):
		REFORMATTED ["PRODUCT"] ["NAME"] = USDA_FOOD_DATA ["description"]
	else:
		NOTES.append ("'description' was not found.")
	
	if ("fdcId" in USDA_FOOD_DATA):
		REFORMATTED ["PRODUCT"] ["FDC ID"] = USDA_FOOD_DATA ["fdcId"]
	else:
		NOTES.append ("'fdcId' was not found.")
	'''

	return {
		"FORM": REFORMATTED,
		"NOTES": NOTES
	}