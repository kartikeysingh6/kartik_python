from bs4 import BeautifulSoup as BS 
import requests 
import winsound

city=input("Enter City: ")
print("Searching...")


try:
    data = requests.get("https://www.fresherslive.com/gold-rate-today/"+city.lower()) 
    soup = BS(data.text, 'html.parser') 

    price = soup.find("td",class_="center-text").text
    cost = soup.findAll("td",class_="center-text")[1].text

    print("1gm 22k gold price in " + city.upper().capitalize()+ ": "+price+" change: "+cost)
    
    #for testing if it works for negative change change value of cost
    
    if(cost[0]=="-"):
    	winsound.Beep(2000, 1250)		#creates sound of frequency 2000hz for 1.25 seconds

except:
    print("Not Found!")

print()
input("Press enter to exit.")
