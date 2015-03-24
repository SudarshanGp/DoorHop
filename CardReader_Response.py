import json
from pprint import pprint
import sys
import os
import math
import shutil
from time import sleep

from twilio.rest import TwilioRestClient

def file_is_empty(path):
    return os.stat(path).st_size==0

global json_data
nfo = "32814e24"
a = 4
account_sid = "SID"
auth_token  = "AUTHTOKEN"
nfo = " "
nfo1 = " "
sendto = " "
data = " "
b = 1
while b==1:
	sleep(5)
	nfo = "0"
	if file_is_empty('report.json') != True:
		json_data=open('report.json', "r+")
		data = json.load(json_data)
		json_data.flush()
		json_data.close()
		nfo = data["Uid"]
	else:
		continue

	if nfo != '32814e24':
		continue
	else: 
			sendto = "+12177787996"
			pprint(nfo)
			pprint(sendto)
			client = TwilioRestClient(account_sid, auth_token)
			message = client.messages.create(body="Hi! I'm away, please leave a message :)",
				    to=sendto,    # Replace with your phone number
				    from_="+13394995660") # Replace with your Twilio number
			open('report.json', 'w').close()
