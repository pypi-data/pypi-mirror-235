
'''
	import pathlib
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()

	from os.path import dirname, join, normpath
	SEARCH = normpath (join (THIS_FOLDER, "../.."))

	import BODY_SCAN
	BODY_SCAN.START (
		GLOB 		= SEARCH + '/**/*STATUS.py'
	)
'''

import glob

from BODY_SCAN.AGGREGATE import START as AGGREGATE_START
import BODY_SCAN.PROCESSES.SCAN as SCAN

def START (
	GLOB = "",
	
	RELATIVE_PATH = False,
	
	MODULE_PATHS = [],
	
	SIMULTANEOUS = False,
	
	RECORDS = 0	
):
	FINDS = glob.glob (GLOB, recursive = True)
		
	if (RECORDS >= 1):
		print ()
		print ("SEARCHING FOR GLOB:")
		print ("	", GLOB)
		print ()
	
	if (RECORDS >= 1):
		print ()
		print ("	FINDS:", FINDS)
		print ("	FINDS COUNT:", len (FINDS))
		print ();
	
	def START_IN_PARALLEL ():
		OUTPUT = []
	
		def FN (PATH):
			[ STATUS ] = SCAN.START (		
				PATH = PATH,
				MODULE_PATHS = MODULE_PATHS,
				RELATIVE_PATH = RELATIVE_PATH,
				RECORDS = RECORDS
			)
		
			return STATUS;
		
		from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
		with ThreadPoolExecutor () as executor:
			RETURNS = executor.map (
				FN, 
				FINDS
			)
			
			executor.shutdown (wait = True)
			
			for RETURN in RETURNS:
				OUTPUT.append (RETURN)
				
			#print ("STATUSES:", STATUSES)
			
		return OUTPUT;
	
	
	def START_SEQUENTIALLY ():
		'''
			STARTS MULTIPLE SCANS, SEQUENTIALLY...
		'''
		PATH_STATUSES = []
		for PATH in FINDS:	
			[ STATUS ] = SCAN.START (		
				PATH = PATH,
				MODULE_PATHS = MODULE_PATHS,
				RELATIVE_PATH = RELATIVE_PATH,
				RECORDS = RECORDS
			)
			
			PATH_STATUSES.append (STATUS)
			
		return PATH_STATUSES;


	if (SIMULTANEOUS == True):
		PATH_STATUSES = START_IN_PARALLEL ()
	else:
		PATH_STATUSES = START_SEQUENTIALLY ()

	STATUS = AGGREGATE_START (
		PATH_STATUSES
	)


	import json
	print ("STATUS:", json.dumps (STATUS, indent = 4))
	
	
	return {
		"STATUS": STATUS
	}
	
