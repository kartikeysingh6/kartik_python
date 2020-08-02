from bs4 import BeautifulSoup as BS 
import requests 
import winsound

city=input("Enter City: ")
print("Searching...")


try:
    data = requests.get("https://www.fresherslive.com/gold-rate-today/"+city.lower()) 
    soup = BS(data.text, 'html.parser') 

    price = soup.find("td",class_="center-text").text[1:]
    cost = soup.findAll("td",class_="center-text")[1].text

    message=("1gm 22k gold price in " + city.upper().capitalize()+ ": Rs."+price+" change: "+cost)
    
    #for testing if it works for negative change change value of cost
    
    if(cost[0]=="-"):
    	winsound.Beep(2000, 1250)		#creates sound of frequency 2000hz for 1.25 seconds

except:
    message=("Not Found!")

if(message!="Not Found!"):
  file_i=open("data.txt","a")
  file_i.write(message)
  file_i.close()
print(message)


print()
input("Press enter to exit.")
