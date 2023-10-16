



'''
	python3 STATUS.py "FOOD/NIH/FORM_1/CALC/DIVISIONS/STATUS_POWDER_PACKETS/STATUS_246811.py"
'''

import CYTE.FOOD.NIH.EXAMPLES as NIH_EXAMPLES
from CYTE.FOOD.NIH.FORM_1.CALC.DIVISIONS import CALC_DIVISIONS


'''

"netContents": [
	{
		"order": 1,
		"quantity": 5.29,
		"unit": "Ounce(s)",
		"display": "5.29 Ounce(s)"
	},
	{
		"order": 2,
		"quantity": 150,
		"unit": "Gram(s)",
		"display": "150 Gram(s)"
	},
	{
		"order": 3,
		"quantity": 30,
		"unit": "Powder Packet(s)",
		"display": "30 Powder Packet(s)"
	}
],
"physicalState": {
	"langualCode": "E0162",
	"langualCodeDescription": "Powder"
},


"servingsPerContainer": "30",
"servingSizes": [
	{
		"order": 1,
		"minQuantity": 5,
		"maxQuantity": 5,
		"minDailyServings": 1,
		"maxDailyServings": 3,
		"unit": "Gram(s)",
		"notes": "adults; 1 packet",
		"inSFB": true
	},
	{
		"order": 2,
		"minQuantity": 0.25,
		"maxQuantity": 0.25,
		"minDailyServings": 1,
		"maxDailyServings": 1,
		"unit": "Teaspoon(s)",
		"notes": "children (age 6+)"
	}
]
"userGroups": [
	{
		"dailyValueTargetGroupName": "Adults and children 4 or more years of age",
		"langualCode": "P0250",
		"langualCodeDescription": "Adults and Children 4 years and above"
	}
]
'''
def CHECK_1 ():
	EXAMPLE = NIH_EXAMPLES.RETRIEVE ("POWDER_PACKETS/MULTIVITAMIN_246811.JSON")
	DIVISIONS = CALC_DIVISIONS (EXAMPLE)

	print ("DIVISIONS:", DIVISIONS)

	assert (
		DIVISIONS ==
		[{
			"UNIT": "PACKAGE"
		},{
			"UNIT": "Ounce(s)",
			"QUANTITY": 5.29
		},{
			"UNIT": "Gram(s)",
			"QUANTITY": 150
		},{
			"UNIT": "Powder Packet(s)",
			"QUANTITY": 30
		}]
	)


	return;
	
	
CHECKS = {
	"MULTIVITAMIN 2642759": CHECK_1
}