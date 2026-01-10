# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 19:50:11 2026

@author: karam
"""

from tkinter import*
from tkinter import messagebox
import random

root=Tk()
root.title("Tic Tac Toe")

user_cord=[]
comp_cord=[]


def clicked(r,c,m):
	w=0
	Button(root, text="X",padx=40,pady=40, bg='#fdff79', state=DISABLED).grid(row=r, column=c)
	if(len(user_cord)!=5):
		rr=random.randint(0,2)
		rc=random.randint(0,2)
		rm=3*rr + rc +1																						#formula to conver m into rows and columns
	if(rm!=m and (str(rm) not in comp_cord) and (str(rm) not in user_cord)):
		comp_cord.append(str(rm))
		user_cord.append(str(m))
		print("USER Input: ")
		print(user_cord)
		print("COMPUTER Input: ")
		print(comp_cord)
		Button(root, text="O",padx=40,pady=40, bg='#99faff',state=DISABLED).grid(row=rr, column=rc)
		#for player
		if('1' in user_cord and '2' in user_cord and '3'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			w=1
			disable()
		elif('4' in user_cord and '5' in user_cord and '6'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif('7' in user_cord and '8' in user_cord and '9'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif('1' in user_cord and '4' in user_cord and '7'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif('2' in user_cord and '5' in user_cord and '8'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif('3' in user_cord and '6' in user_cord and '9'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif('1' in user_cord and '5' in user_cord and '9'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif('3' in user_cord and '5' in user_cord and '7'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
			w=1
		elif(len(comp_cord) + len(user_cord) == 9): # fixed code
			messagebox.showwarning("Game result: draw", "Game result: draw")
			disable()
			w=1
                

		#for computer
		if(w!=1):
			if('1' in comp_cord and '2' in comp_cord and '3'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('4' in comp_cord and '5' in comp_cord and '6'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('7' in comp_cord and '8' in comp_cord and '9'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('1' in comp_cord and '4' in comp_cord and '7'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('2' in comp_cord and '5' in comp_cord and '8'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('3' in comp_cord and '6' in comp_cord and '9'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('1' in comp_cord and '5' in comp_cord and '9'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif('3' in comp_cord and '5' in comp_cord and '7'  in comp_cord):
				messagebox.showwarning("O Won!", "Computer Won!")
				disable()
			elif(len(comp_cord) + len(user_cord) == 9): # fixed code
				messagebox.showwarning("Game result: draw", "Game result: draw")
				disable()               

	elif(len(user_cord)>3):
		user_cord.append(str(m))
		print(user_cord)
		print(comp_cord)

		#for player
		if('1' in user_cord and '2' in user_cord and '3'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('4' in user_cord and '5' in user_cord and '6'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('7' in user_cord and '8' in user_cord and '9'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('1' in user_cord and '4' in user_cord and '7'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('2' in user_cord and '5' in user_cord and '8'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('3' in user_cord and '6' in user_cord and '9'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('1' in user_cord and '5' in user_cord and '9'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif('3' in user_cord and '5' in user_cord and '7'  in user_cord):
			messagebox.showwarning("X Won!", "Player Won!")
			disable()
		elif(len(comp_cord) + len(user_cord) == 9): # fixed code
			messagebox.showwarning("Game result: draw", "Game result: draw")
			disable()            
	else:
		clicked(r,c,m)

Button(root, text="",padx=40,pady=40, command=lambda: clicked(0,0,1)).grid(row=0, column=0)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(0,1,2)).grid(row=0, column=1)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(0,2,3)).grid(row=0, column=2)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(1,0,4)).grid(row=1, column=0)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(1,1,5)).grid(row=1, column=1)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(1,2,6)).grid(row=1, column=2)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(2,0,7)).grid(row=2, column=0)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(2,1,8)).grid(row=2, column=1)
Button(root, text="",padx=40,pady=40, command=lambda: clicked(2,2,9)).grid(row=2, column=2)

def disable():
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=0, column=0)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=0, column=1)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=0, column=2)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=1, column=0)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=1, column=1)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=1, column=2)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=2, column=0)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=2, column=1)
	Button(root, text="",padx=40,pady=40, bg='#99ffa4', state=DISABLED).grid(row=2, column=2)

root.mainloop()
