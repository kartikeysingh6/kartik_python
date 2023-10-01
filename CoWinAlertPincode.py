import requests
import json
import winsound
import time
from datetime import date
from datetime import datetime

#change this according to your need
pin="110006"
loop_time_inseconds=30

while(1):
	currtime = datetime.now().strftime("%H:%M:%S")
	today = date.today().strftime("%d-%m-%y")

	apiURL="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pin+"&date="+today
	response = requests.get(apiURL, headers={"accept-language": "en-US"})

	print("Current Time:", currtime+"\n")
	print(today+"\n")

	for place in response.json()['sessions']:
		if(place['available_capacity']>0 or place['available_capacity_dose1']>0):
			winsound.Beep(1000, 500)
			winsound.Beep(1000, 500)
			print(place['name'],", "+(place['address'] or "varanasi"))
			print("Total Capacity: ",place['available_capacity'], ", Dose1: ",place['available_capacity_dose1'])
			print(place['slots'])
			print()
		else:
			print("No available Dose")

	time.sleep(loop_time_inseconds)
