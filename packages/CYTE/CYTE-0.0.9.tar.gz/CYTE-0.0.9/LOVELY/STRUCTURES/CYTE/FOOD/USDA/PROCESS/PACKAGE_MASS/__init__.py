



'''
	import CYTE.FOOD.USDA.PROCESS.PACKAGE_MASS as PACKAGE_MASS
	PROCESSED = PACKAGE_MASS.PROCESS ("4 oz/113 g")
'''

'''
	packageWeight
		4 oz/113 g ->
		
			"MASS": {
				"REPORTED": "4 oz/113 g",
				"POUNDS_E_NOTE": [ "0.25E+0", "POUNDS" ],
				"GRAMS_E_NOTE": [ "113.4E+0", "GRAMS" ]
			}
			
			
		10 oz/283 g
		
		
	nutrient mass:
		
'''

'''
	
'''

'''
	oz -> OUNCES
	lb -> POUNDS
	
	g -> GRAMS
'''

UNIT_LEGEND = {
	"iu": "IU",
	
	"oz": "OUNCES",
	"lb": "POUNDS",
	
	"g": "GRAMS",
	"kg": "KILOGRAMS",
	"mg": "MICROGRAMS",
	"mcg": "MILLIGRAMS"
}

def PROCESS (PARAM):
	if (type (PARAM) != str):
		return [ "?", "POUNDS" ]
		
	SPRUCED_WEIGHTS = {}
		
	SPLITS = PARAM.split ("/")
	for SPLIT in SPLITS:
		[ AMOUNT, UNIT ] = SPLIT.split (" ")
		
		print (AMOUNT, UNIT)
		
		assert (UNIT in UNIT_LEGEND)
		SPRUCE_UNIT = UNIT_LEGEND [ UNIT ]

	
		
	

	return;