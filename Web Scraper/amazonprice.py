from bs4 import BeautifulSoup
import requests

url=input("Enter Amazon URL: ")

source = requests.get(url).text

soup = BeautifulSoup(source,'lxml')

title = soup.title.text

try:
	value = soup.find('span', id ='priceblock_ourprice').text
except:
	if(title=="Robot Check"):
		value = "Stuck at Robot Check"
	else:
		value = "Currently Unavailable"

print(title)
print()
print("Price: "+value)
print()
input("Press enter to exit.")
