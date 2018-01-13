# -*- coding: utf-8 -*- 
import requests
import json
import datetime
import time
import sys
import traceback
import timeZone

#mURL="http://kuc-arc-f.com"
mURL="http://192.168.10.100"
#mAPI_KEY="VJUA0Z625TNRAN1N"
mAPI_KEY="u2c1"

# com_func
class com_funcClass:
	def __init__(self):
		print ""

	def get_nowTime(self):
		sRet=""
		from datetime import datetime
		clsJST= timeZone.timeZoneClass()
		nowJST = datetime.now(tz=clsJST )
		sTime = nowJST.strftime("%Y-%m-%d %H:%M:%S")
		#print(sTime )
	
		return sRet


