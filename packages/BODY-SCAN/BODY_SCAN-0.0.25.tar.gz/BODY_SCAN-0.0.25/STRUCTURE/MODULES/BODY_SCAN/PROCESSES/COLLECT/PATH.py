



'''
	import BODY_SCAN.PROCESSES.COLLECT.PATH as COLLECT_PATH
	COLLECT_PATH.FIND ()
'''

def FIND ():
	import pathlib
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath

	return normpath (join (THIS_FOLDER, "START.PROC.PY"))