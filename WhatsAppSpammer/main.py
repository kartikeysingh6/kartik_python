import random
import os
from tkinter import*

root=Tk()
root.title("WhatsApp Spammer v1.0")
root.geometry("330x170")
root.resizable(FALSE,FALSE)

def killf():
	os.startfile("killer.bat")	
	show = Label(root, text="Process was killed and file was deleted!")

def make():
	wait=waite.get()
	delay=delaye.get()
	intel=intele.get()
	loop=str(int(loope.get()) -1)
	datafile = open("temp"+value+".vbs","w+")
	datafile.write("wscript.sleep "+wait+"\nSet wshShell =wscript.CreateObject(\"WScript.Shell\")\nDim a : a = "+loop+"\nFor i = 0 to a Step 1\nwshshell.sendkeys \""+intel+"\"\nwscript.sleep "+delay+"\nwshshell.sendkeys \"{ENTER}\"\nNEXT")
	os.startfile("temp"+value+".vbs")


value=str(random.randint(0,1000))

Label(root, text=" ").grid(row=0,column=0)

Label(root, text="Enter Initial Wait(ms): ").grid(row=1,column=0)
waite=Entry(root, width=25)
waite.grid(row=1,column=1)

Label(root, text="Enter Delay in Spam(ms): ").grid(row=2,column=0)
delaye=Entry(root, width=25)
delaye.grid(row=2,column=1)

Label(root, text="Enter String to Spam: ").grid(row=3,column=0)
intele=Entry(root, width=25)
intele.grid(row=3,column=1)

Label(root, text="Enter Loop Length: ").grid(row=4,column=0)
loope=Entry(root, width=25)
loope.grid(row=4,column=1)

Label(root, text=" ").grid(row=5,column=0)

subButton=Button(root,text="Execute", command=make)
subButton.grid(row=6,column=0)

killButton=Button(root,text="Kill Script", command=killf)
killButton.grid(row=6,column=1)


root.mainloop()

