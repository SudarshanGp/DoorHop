import json
from pprint import pprint
import sys
import os
import math
import urllib2
import urllib
import shutil
from time import sleep

while 1:
	sleep(1)
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	top_level_url = 'https://api.twilio.com/2010-04-01/Accounts/ACf63cb15b6b337a1fdd5205c0fe74798d'
	password_mgr.add_password(None, top_level_url, 'ACf63cb15b6b337a1fdd5205c0fe74798d', '29e6213ee69da90ea4867ced037193f4')
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	request = urllib2.Request('https://api.twilio.com/2010-04-01/Accounts/ACf63cb15b6b337a1fdd5205c0fe74798d/SMS/Messages.json')
	f = opener.open(request)
	data = f.read()
	pprint(data)
	f.close()
	opener.close()
	data1 = json.loads(data)
	length = data1["end"]
	FILE = open('Messages.json', "w+")

	print "length is %d" % length
	while(length >0):
		FILE.write("From : " + data1["sms_messages"][length]["from"]+"\n"+ "Message : " + data1["sms_messages"][length]["body"]+"\n"+ "To " +data1["sms_messages"][length]["to"] +"\n" + "EOT" + "\n")
		length = length -1

	FILE.close()
