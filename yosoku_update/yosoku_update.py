#import tensorflow as tf
import json
from urllib2 import urlopen
import datetime
import threading
import time
import sys
import traceback

import api_func
import ai_func
import timeZone

#define
mTimeMax    =1800

def proc_learning():
	clsAI =ai_func.ai_funcClass()
	key='u2c1'
	try:
		field=1
#		clsAI.proc_run(field)
		clsAI.proc_run(key , field)
		field=2
		clsAI.proc_run(key , field)
		field=4
		clsAI.proc_run(key , field)
	except:
		print "--------------------------------------------"
		print traceback.format_exc(sys.exc_info()[2])
		print "--------------------------------------------"

if __name__ == "__main__":
	#cls = api_func.api_funcClass()
	proc_learning()
	from datetime import datetime
	clsJST= timeZone.timeZoneClass()
	nowJST = datetime.now(tz=clsJST )
	print(nowJST )
	tmBef     = nowJST

	while True:
		time.sleep(1.0)
		tmNow = datetime.now(tz=clsJST )
		tmSpan = tmNow - tmBef
		iSpan     = tmSpan.total_seconds()
		sTime = tmNow.strftime("%Y-%m-%d %H:%M:%S")
		print("time=" +sTime)
		if iSpan > mTimeMax:
			tmBef = datetime.now(tz=clsJST )
			proc_learning()

	