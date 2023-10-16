


def CHECK_STATUS_LOCATION ():
	import pathlib
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	CHECK_STATUS = normpath (join (THIS_FOLDER, "../PROCESSES/SCAN/SCAN.PROC.PY"))

	return CHECK_STATUS