

'''
	import CYTE.STRUCTS.DB.PATH as STRUCTS_DB_PATH
	PATH = STRUCTS_DB_PATH.FIND ()
'''

import pathlib
from os.path import dirname, join, normpath

def FIND ():
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (THIS_FOLDER, "STRUCTS.JSON"))




