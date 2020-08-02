from tkinter import *
from math import *

root=Tk()
root.title("Interest Calculator")

def work(P,R,T,N):
	nt = float(N)*float(T)
	frac=float(R)/(100*float(N))
	fin=1+frac
	finS=float(P)*(1+(float(R)*float(T))/100)
	res=float(P)*(pow(fin,nt))
	doub=log(2)/(float(N)*log(fin))
	doubS=100/float(R)
	gain=res - float(P)
	gainS=finS - float(P)
	Label(root, text = "COMPOUND INTEREST RESULT").pack()
	Label(root, text = "--------------------------------------").pack()
	Label(root,text="Final Amount: " + str(round(res,3))).pack()
	Label(root, text = "Amount Gained: "+ str(round(gain,3))).pack()
	Label(root, text = "Multiplication Factor: " + str(round(res/float(P),3))).pack()
	Label(root, text="Amount Doubles every "+str(round(doub,3))+" unit time").pack()

	Label(root, text = "").pack()
	Label(root, text = "SIMPLE INTEREST RESULT").pack()
	Label(root, text = "--------------------------------------").pack()
	Label(root,text="Final Amount: " + str(round(finS,3))).pack()
	Label(root, text = "Amount Gained: "+ str(round(gainS,3))).pack()
	Label(root, text="Amount Doubles in "+str(round(doubS,3))+" unit time").pack()

Label(root,text="Principal Amount").pack()
Pri=Entry(root,width=50)
Pri.pack()
Label(root,text="Interest rate per unit time").pack()
Rat=Entry(root,width=50)
Rat.pack()
Label(root,text="Time").pack()
Tim=Entry(root,width=50)
Tim.pack()
Label(root,text="No. of times Interest given per unit time").pack()
Num=Entry(root,width=50)
Num.pack()
Label(root,text="").pack()
Button(root,text="SUBMIT",padx=10,pady=10,bg='#99ffa4', command=lambda: work(Pri.get(),Rat.get(),Tim.get(),Num.get())).pack()
Label(root, text = "").pack()

root.mainloop()
