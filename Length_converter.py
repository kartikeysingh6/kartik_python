from math import*
from tkinter import*

root=Tk()
root.title("Length Converter v1")

Label(root, text="Lenth Height(cm)").pack()
e=Entry(root, width=50, borderwidth=7)
e.pack()

def myclick():
	ft=floor(float(e.get())/30.48)
	Label(root, text=str(ft) + "ft " + str(round((12*(float(e.get())/30.48 - ft)),2)) + "in").pack()

Button(root, text="Convert", command=myclick, fg='black', bg='yellow').pack()

root.mainloop()