



'''
from CYTE.FOOD.NIH.FORM_1.CALC.DIVISIONS import CALC_DIVISIONS
DIVISIONS = CALC_DIVISIONS ()
'''

'''
#
#	{ STATISTICS, SUMMARY, COMPOSITION } PER { DIVISION }
#
"DIVISIONS": [{
	"DIVISION": "PACKAGE"
},{
	"DIVISION": "TABLET",
	"QUANTITY": 90
}]
'''

'''
	EXAMPLE:
		INPUTS:
		
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
			
			"servingsPerContainer": "30",
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
			
			"userGroups": [
				{
				  "dailyValueTargetGroupName": "Adults and children 4 or more years of age",
				  "langualCode": "P0250",
				  "langualCodeDescription": "Adults and Children 4 years and above"
				}
			  ]
			
		OUTPUTS:
			"DIVISIONS": [{
				"UNIT": "PACKAGE"
			},{
				"UNIT": "Tablet(s)",
				"QUANTITY": 90
			},{
				"UNIT": "SERVINGS",
				"GROUP": "",
				"QUANTITY": 90
			}],
'''

def CALC_DIVISIONS (USDA_FOOD_DATA):
	DIVISIONS = [{
		"UNIT": "PACKAGE"
	}]
	
	assert ("netContents" in USDA_FOOD_DATA)
	assert ("physicalState" in USDA_FOOD_DATA)
	assert ("servingSizes" in USDA_FOOD_DATA)
	
	NET_CONTENTS = USDA_FOOD_DATA ["netContents"]
	
	print ("NET_CONTENTS:", NET_CONTENTS)
	
	for NET_CONTENT in NET_CONTENTS:
		print (NET_CONTENT)
		
		DIVISIONS.append ({
			"UNIT": NET_CONTENT ["unit"],
			"QUANTITY": NET_CONTENT ["quantity"]
		})

	return DIVISIONS