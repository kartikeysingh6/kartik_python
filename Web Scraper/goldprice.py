from bs4 import BeautifulSoup as BS     #For Website Grabbing
import requests                         #For Sending Requests
import winsound                         #For Beeping Sounds
import win10toast                       #For Desktop Notifications
import time                             #For Sleep
from twilio.rest import Client          #For API


#API Information
account_sid = "AC3d156f0265d90fd04876279b30fec24a"
auth_token  = "ab76df78c958c7dfdde31ec1e9514ec4"
SMSfrom="+12057758172"
WAfrom="whatsapp:+14155238886"
WAto="whatsapp:+917985414735"
SMSto="+917985414735"

#API Function
def SENDAPI():
    client = Client(account_sid, auth_token)
    message = client.messages.create(to=WAto, from_=WAfrom,body="GOLD PRICE DROPPED!\n"+final)


while(1):
    #City Name from city.txt if fails default is delhi
    try:
        city_file=open("city.txt","r")
        city=city_file.readline().lower()
        city_file.close()
    except:
        city="delhi"

    print("Looking for gold price in "+city.capitalize()+"...")

    #Try and Except for Error Handling
    try:
        
        #Grabs data from the site and parses the HTML
        data = requests.get("https://www.fresherslive.com/gold-rate-today/"+city.lower()) 
        soup = BS(data.text, 'html.parser') 

        
        #To locate the data from site
        price = soup.find("td",class_="center-text").text
        change = soup.findAll("td",class_="center-text")[1].text
        

        #Statement to print
        final="1gm 22k Price in " + city.upper().capitalize()+ ": "+price+" change: "+change
        print(final)

        
        #For external file
        tosave="1gm 22k Price in " + city.upper().capitalize()+ ": Rs."+price.split('₹')[1]+" change: "+change
        file_i=open("data.txt","a")
        file_i.write(tosave+'\n')
        file_i.close()

        
        #For sound effect, desktop notification and WhatsApp/SMS Alert
        if(change[0]=="-"):
            winsound.Beep(2000, 1250) 
            toaster = win10toast.ToastNotifier().show_toast("Gold Price DROPPED!",final , duration=5)
            try:
                
                #API FUNCTION CALL DISABLE THIS TO DISABLE API
                SENDAPI()
            except:
                print("\nWhatsApp Alert Failed!")

        if(change[0]=="+"):
        	winsound.Beep(1000, 350)
        	winsound.Beep(1000, 350)
        	toaster = win10toast.ToastNotifier().show_toast("Gold Price INCREASED!",final , duration=5)

    except:
        print("Not Found!")

    time.sleep(3600)      #Loops over every given seconds
