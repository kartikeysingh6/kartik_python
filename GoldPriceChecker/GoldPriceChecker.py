from bs4 import BeautifulSoup as BS     #For Website Grabbing
import requests                         #For Sending Requests
import winsound                         #For Beeping Sounds (pip install )
import win10toast                       #For Desktop Notifications
import time                             #For Sleep
import os.path                          #To Check if file exits or not     
from twilio.rest import Client          #For Twilio API
from datetime import datetime           #For date and time

#Twilio API Information
account_sid = "SID HERE"
auth_token  = "TOKEN HERE"
frm="SENDER NO. HERE"
to="RECEIVER NO. HERE"

#API Function
def SENDAPI():
    client = Client(account_sid, auth_token)
    message = client.messages.create(to=to, from_=frm,body="GOLD PRICE DROPPED!\n"+final)
k=1
while(k):
    k-=1
    #City Name from city.txt if fails default is delhi
    if(os.path.exists('city.txt')):
        city_file=open("city.txt","r")
        city=city_file.readline().lower()
        city_file.close()
    else:
        city="delhi"

    print("Looking for gold price in "+city.capitalize()+"...")

    #Try and Except for Error Handling
    try:
        
        #Grabs data from the site and parses the HTML
        data = requests.get("https://www.fresherslive.com/gold-rate-today/"+city.lower()) 
        soup = BS(data.text, 'html.parser') 

        
        #To locate the data from site
        price = soup.findAll("td",class_="center-text")[1].text
        change = soup.find_all('b')[11].text

        #Statement to print
        final="1g 22k Price in " + city.upper().capitalize()+ ": "+price+" change: "+change
        print(final)

        
        #For external file
        tosave="1gm 22k Price in " + city.upper().capitalize()+ ": Rs."+price.split('₹')[1]+" change: "+change
        now=datetime.now()
        s1=now.strftime("%m-%d-%Y , %H:%M:%S ")
        file_i=open("data.txt","a")
        tosave="on "+s1+tosave
        file_i.write(tosave+'\n')
        file_i.close()

        
        #For sound effect, desktop notification and WhatsApp/SMS Alert
        if(change[0]=="-"):
            winsound.Beep(2000, 1000)
            if(os.path.exists('gold.ico')):
                toaster = win10toast.ToastNotifier().show_toast("Gold Price DROPPED!",final , duration=5, icon_path="gold.ico")
            else:
                toaster = win10toast.ToastNotifier().show_toast("Gold Price DROPPED!",final , duration=5)
            
            try:
                #API FUNCTION CALL DISABLE THIS TO DISABLE API
                #SENDAPI()
                print()
            except:
                print("\nWhatsApp Alert Failed!")

        if(change[0]=="+"):
            winsound.Beep(1000, 350)
            winsound.Beep(1000, 350)
            if(os.path.exists('gold.ico')):
                toaster = win10toast.ToastNotifier().show_toast("Gold Price INCREASED!",final , duration=5, icon_path="gold.ico")
            else:
                toaster = win10toast.ToastNotifier().show_toast("Gold Price INCREASED!",final , duration=5)

    except:
        print("Not Found!")

    time.sleep(2)      #Loops over every given seconds
