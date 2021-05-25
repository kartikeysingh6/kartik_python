import requests
import json

cities=["Varanasi","Kanpur","Tokyo","Mumbai","London","Moscow","Bhopal","New Delhi","Brisbane","Agra"]

for city in cities:
	try:
		weather='http://api.weatherstack.com/current?access_key=e6b95e941372917c9a80ff3929113dd5&query='+city
		response = requests.get(weather)

		#status based on numbers
		uvindx = response.json()['current']['uv_index']
		uvstatus=""
		if(uvindx <= 2):
			uvstatus="Good"
		if(3<=uvindx<=5):
			uvstatus="Moderate"
		if(6<=uvindx<=7):
			uvstatus="Poor"
		if(8<=uvindx<=10):
			uvstatus="Very Poor"
		if(uvindx>10):
			uvstatus="Severe"


		longi=float(response.json()['location']['lon'])
		lati=float(response.json()['location']['lat'])
		longidir=""
		latidir=""
		if(longi>=0):
			longidir="E"
		if(lati>=0):
			latidir="N"
		if(longi<0):
			longidir="W"
			longi=longi*-1;
		if(lati<0):
			latidir="S"
			lati=lati*-1;


		humi=response.json()['current']['humidity']
		humistatus=""
		if (humi<25):
			humistatus="Bad, Low Humidity"
		if (humi>=75):
			humistatus="Bad, High Humidity"
		if (25<=humi<30):
			humistatus="Fair"
		if (60<=humi<75):
			humistatus="Fair"
		if (30<=humi<60):
			humistatus="Good"


		print("Name       :", response.json()['location']['name'],"("+str(longi)+longidir+", "+str(lati)+latidir+")")
		print("Temperature:", response.json()['current']['temperature'],"Celcius")
		print("Weather    :", response.json()['current']['weather_descriptions'][0])
		print("Wind Speed :", response.json()['current']['wind_speed'])
		print("Wind Direc :", response.json()['current']['wind_dir'])
		print("Humidity   :", str(humi)+"%","("+humistatus+")")
		print("UV Index   :", uvindx,"("+uvstatus+")")
		print("Visibility :", response.json()['current']['visibility'])
		print()
	except:
		print("Failed for",city)
		print()


input()