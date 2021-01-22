from pynput.keyboard import Key, Controller
import random
import time
keyboard = Controller()

try:
	file = open("text.txt","r")

	string = file.readline()
	val = int(file.readline())
	pauss = float(file.readline())
except:
	val=1
	string = "Error!"
	pauss = 0.1

time.sleep(5)
for x in range(0,val):
	keyboard.type(string)
	time.sleep(pauss)
