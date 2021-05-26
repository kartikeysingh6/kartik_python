import requests
from tkinter import *
import json

token="9a502828655cb1b6e6fa1c63733290bf"
root = Tk()
root.title("Weather App")

city="noida"
def submit():
	city=ctentry.get()
	try:
		weather="http://api.weatherstack.com/current?access_key="+token+"&query="+city
		response = requests.get(weather)

		uvindx = response.json()['current']['uv_index']
		longi=float(response.json()['location']['lon'])
		lati=float(response.json()['location']['lat'])
		humi=response.json()['current']['humidity']
		naam=response.json()['location']['name']	
		tempp=response.json()['current']['temperature']
		info=response.json()['current']['weather_descriptions'][0]
		winspeed=int(response.json()['current']['wind_speed'])
		windir=response.json()['current']['wind_dir']
		visi=response.json()['current']['visibility']


		#status based on numbers
		
		uvstatus=""
		uvcolor=""
		if(uvindx <= 2):
			uvstatus="Good"
			uvcolor="#68bb59"
		if(3<=uvindx<=5):
			uvstatus="Moderate"
			uvcolor="yellow"
		if(6<=uvindx<=7):
			uvstatus="Poor"
			uvcolor="orange"
		if(8<=uvindx<=10):
			uvstatus="Very Poor"
			uvcolor="#ff007f"
		if(uvindx>10):
			uvstatus="Severe"
			uvcolor="maroon"

		
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

		humistatus=""
		humicolor=""
		if (humi<25):
			humistatus="Bad, Low Humid"
			humicolor="#ff007f"
		if (humi>=75):
			humistatus="Bad, Highly Humid"
			humicolor="#ff007f"
		if (25<=humi<30):
			humistatus="Fair"
			humicolor="yellow"
		if (60<=humi<75):
			humistatus="Fair"
			humicolor="yellow"
		if (30<=humi<60):
			humistatus="Good"
			humicolor="#acdf87"

		windcolor=""
		if(winspeed<2):
			windcolor="white"
		if(2<=winspeed<10):
			windcolor="lightblue"
		if(10<=winspeed<40):
			windcolor="lime"
		if(40<=winspeed<60):
			windcolor="yellow"
		if(60<=winspeed<90):
			windcolor="#ff007f"
		if(winspeed>=90):
			windcolor="maroon"


		Label(root, text="").pack()
		Label(root, text="City Name: "+str(naam), font=('Helvetica bold',25),fg="#0F52BA").pack()
		Label(root, text=str(longi)+longidir+", "+str(lati)+latidir, font=25, fg="#0F52BA").pack()
		Label(root, text="").pack()
		Label(root, text="Temperature: "+str(tempp) +" Celcius", font=25).pack()
		Label(root, text="UV Index: "+str(uvindx)+" "+uvstatus, font=25, bg=uvcolor).pack()
		Label(root, text="Humidity: " +str(humi)+" "+humistatus, font=25, bg=humicolor).pack()
		Label(root, text="Weather: " +info, font=25).pack()
		Label(root, text="Wind Status: "+str(winspeed)+"km/hr ("+str(windir)+")", font=25, bg=windcolor).pack()
		Label(root, text="Visibility: "+str(visi), font=25).pack()
		Label(root, text="").pack()

	except:
		Label(root, text="Error Not Found!", fg="red").pack()


ctentry=Entry(root,width=50)
ctentry.pack()
ctentry.insert(0, "Varanasi ")

Button(root, text="Submit", command=submit).pack()


root.mainloop()