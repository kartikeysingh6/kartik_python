from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title("Rock Paper Scissors v1")
root.geometry("286x240")
root.resizable(FALSE,FALSE)
try:
        root.iconbitmap("rock.ico")
except:
        print("error")

a=random.randint(1,3)
d=0
w=0
l=0

def click(n):
    global d
    global w
    global l
    a=random.randint(1,3)
    if a==n:
        if a==1:
            lbl=messagebox.showinfo("It's a Draw!","You choosed Rock, \nComputer also choosed Rock. ")
            d+=1
        if a==2:
            lbl=messagebox.showinfo("It's a Draw!", "You choosed Paper, \nComputer also choosed Paper.")
            d+=1
        if a==3:
            lbl=messagebox.showinfo("It's a Draw!", "You choosed Scissor, \nComputer also choosed Scissor.")
            d+=1

    if (a==1 and n==2):
            lbl=messagebox.showwarning("You Win!","You choosed Paper, \nComputer choosed Rock.")
            w+=1
    if (a==1 and n==3):
            lbl=messagebox.showerror("Computer Win!","You choosed Scissor, \nComputer choosed Rock.")
            l+=1
    if (a==2 and n==1):
            lbl=messagebox.showerror("Computer Win!","You choosed Rock, \nComputer choosed Paper.")
            l+=1
    if (a==2 and n==3):
            lbl=messagebox.showwarning("You Win!","You choosed Scissor, \nComputer choosed Paper.")
            w+=1
    if (a==3 and n==1):
            lbl=messagebox.showwarning("You Win!","You choosed Rock, \nComputer choosed Scissor.")
            w+=1
    if (a==3 and n==2):
            lbl=messagebox.showerror("Computer Win!","You choosed Paper,\nComputer choosed Scissor.")
            l+=1

def sub():
    messagebox.showinfo("Stats","\nTotal Plays: "+str((w+l+d))+"\n\nWins: "+str(w)+" ("+str((w/(w+l+d))*100)+"%)"+"\nLose: "+str(l)+" ("+str((l/(w+l+d))*100)+"%)"+"\nDraws: "+str(d)+" ("+str((d/(w+l+d))*100)+"%)")

Label(root, text="Welcome to Rock Paper Scissors v1").pack()
Label(root, text="Pick your choice: \n").pack()
Button(root, text="Rock", command=lambda: click(1)).pack()
Label(root, text="").pack()
Button(root, text="Paper", command=lambda: click(2)).pack()
Label(root, text="").pack()
Button(root, text="Scissor", command=lambda: click(3)).pack()
Label(root, text="").pack()
Button(root, text="Stats", command=sub).pack()

root.mainloop()