# -*- coding: utf-8 -*- 
import requests
import json
from urllib2 import urlopen
import datetime
import time
import sys
import traceback

mURL="https://your-dns"

# api_func
class api_funcClass:
	def __init__(self):
		print ""

#	def update(self, field,wnum, bnum):
	def update(self, key, field ,wnum, bnum):
		sUrl =mURL +'/yosoku/aidats/update?apikey='+ key
		sUrl +='&field='+str(field)
		sUrl +='&wnum='+ str(wnum)
		sUrl +='&bnum='+ str(bnum)
		sUrl +='&sttm=1&endtm=1'
		print (sUrl)
		#return
		try:
			r = requests.get(sUrl ,  timeout=10 )
			print r.status_code
			sText= r.text
			print sText
		except:
			print "Error, api_send"
			raise
		finally:
			print "End , api_send"
		return
	#
#	def get_apiData(self ,fnum ):
	def get_apiData(self , key,fnum ):
		print('#get-traning Data.')
		ret=[]
		iCt=0
		#s='[{"Sensor":{"f1":"11"}},{"Sensor":{"f1":"12"}},{"Sensor":{"f1":"13"}}]'
		url =  mURL+'/yosoku/apis/get_items?apikey=' +key
		url +='&field=' +str(fnum)
	#	sJson = urllib.request.urlopen(url).read()
		sJson = urlopen(url).read()
		#print(sJson )
		json_dict = json.loads(sJson )
		#print ( json.dumps(json_dict ))
		for item in json_dict:
			ret.append(0)
			#print (item['Sensor']['f1'])
			sNum=0
			if (fnum==1):
				sNum = item['Sensor']['f1']
			if (fnum==2):
				sNum = item['Sensor']['f2']
			if (fnum==3):
				sNum = item['Sensor']['f3']
			if(fnum ==4):
				sNum = item['Sensor']['f4']
			ret[iCt]= float( sNum ) / float(100)
			iCt+=1
	#	print(ret)
		print('dim.ren='+ str(len(ret)))
		return ret
	#	print("{}".format(json.dumps(jsons ,indent=4)))
	

