from bs4 import BeautifulSoup as BS 
import requests  

city=input("Enter City: ")
print("Searching...")


try:
    data = requests.get("https://www.fresherslive.com/gold-rate-today/"+city.lower()) 

    soup = BS(data.text, 'html.parser') 

    ans = soup.find("td",class_="center-text").text

    print("1 gram 22 carat gold price in " + city.upper()+ " today: "+ans) 

except:

    print("Not Found!")

print()
input("Press enter to exit.")
