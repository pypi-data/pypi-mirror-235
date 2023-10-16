






'''
	python3 STATUS.py "FOOD/NIH/FORM_1/CALC/DIVISIONS/STATUS/STATUS_TABLETS_1.py"
'''

import CYTE.FOOD.NIH.EXAMPLES as NIH_EXAMPLES
from CYTE.FOOD.NIH.FORM_1.CALC.DIVISIONS import CALC_DIVISIONS

def CHECK_1 ():
	'''
	"netContents": [
		{
			"order": 1,
			"quantity": 90,
			"unit": "Tablet(s)",
			"display": "90 Tablet(s)"
		}
	],
	"physicalState": {
		"langualCode": "E0155",
		"langualCodeDescription": "Tablet or Pill"
	},
	"servingSizes": [
		{
			"order": 1,
			"minQuantity": 3,
			"maxQuantity": 3,
			"minDailyServings": 1,
			"maxDailyServings": 1,
			"unit": "Tablet(s)",
			"notes": "",
			"inSFB": true
		}
	]
	'''

	EXAMPLE = NIH_EXAMPLES.RETRIEVE ("TABLETS/CALCIUM_261967.JSON")
	
	DIVISIONS = CALC_DIVISIONS (EXAMPLE)

	assert (
		DIVISIONS ==
		[{
			"DIVISION": "PACKAGE"
		},{
			"DIVISION": "Tablet(s)",
			"QUANTITY": 90
		}]
	)


	return;
	
	
CHECKS = {
	#"MULTIVITAMIN 2642759": CHECK_1
}