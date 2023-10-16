

'''
	import BODY_SCAN.PROCESSES.SCAN.PATH as SCAN_PATH
	SCAN_PATH.FIND ()
'''

def FIND ():
	import pathlib
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath

	return normpath (join (THIS_FOLDER, "SCAN.PROC.PY"))