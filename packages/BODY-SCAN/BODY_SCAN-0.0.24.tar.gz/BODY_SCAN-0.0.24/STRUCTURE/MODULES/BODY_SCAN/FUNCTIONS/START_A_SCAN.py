

'''
	STEPS:
		1. STARTS NEW SCAN PROCESS WITH A FLASK (KEG, RESERVOIR)
		2. SEND A REQUEST TO THE PROCESS TO RUNS CHECKS FOUND IN A PATH
		3. RETURNS THE STATUS FOUND WITH THE REQUEST
'''

from BOTANIST.PORTS.FIND_AN_OPEN_PORT 	import FIND_AN_OPEN_PORT
from BOTANIST.PROCESSES.START_MULTIPLE import START_MULTIPLE as START_MULTIPLE_PROCESSES

from BODY_SCAN.FUNCTIONS.CHECK_STATUS_LOCATION 	import CHECK_STATUS_LOCATION
import BODY_SCAN.PROCESSES.SCAN.PATH as SCAN_PATH
	
import sys
import json
def ATTEMPT_TAP_KEG (
	MODULE_PATHS
):
	PORT = FIND_AN_OPEN_PORT ()
	SCAN_PROCESS_PATH = SCAN_PATH.FIND ()

	#SYS_PATH = sys.path
	#DETAILS = json.dumps ({ "MODULE_PATHS": MODULE_PATHS })
	DETAILS = json.dumps ({ "MODULE_PATHS": sys.path })

	PROCS = START_MULTIPLE_PROCESSES (
		PROCESSES = [{
			"STRING": f'''python3 { SCAN_PROCESS_PATH } KEG OPEN --port { PORT } --details \'{ DETAILS }\' ''',
			"CWD": None
		}]
	)

	return [ PORT, PROCS ]

def START_A_SCAN (
	PATH,
	MODULE_PATHS = [],
	RELATIVE_PATH = False,
	RECORDS = 0
):
	[ PORT, PROCS ] = ATTEMPT_TAP_KEG (
		MODULE_PATHS
	)
	
	import time
	time.sleep (0.5)
	
	REQUEST_ADDRESS = f'http://127.0.0.1:{ PORT }'
	
	import json
	import requests
	r = requests.put (
		REQUEST_ADDRESS, 
		data = json.dumps ({ 
			"FINDS": [ PATH ],
			"MODULE PATHS": MODULE_PATHS,
			"RELATIVE PATH": RELATIVE_PATH
		})
	)
	
	def FORMAT_RESPONSE (TEXT):
		import json
		return json.loads (TEXT)
	
	STATUS = FORMAT_RESPONSE (r.text)

	if (RECORDS >= 1):
		print ()
		print ("REQUEST ADDRESS :", REQUEST_ADDRESS)
		print ("REQUEST STATUS  :", r.status_code)
		print ("REQUEST TEXT  :", json.dumps (STATUS, indent = 4))
		print ()


	EXIT 			= PROCS ["EXIT"]
	PROCESSES 		= PROCS ["PROCESSES"]
	
	return [ STATUS ]