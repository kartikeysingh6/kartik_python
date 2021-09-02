from tkinter import *
from tkinter import ttk
import random
from sortingAlgos import *

root=Tk()
root.title("Sorting Visualizer")
root.config(bg='black')

#VariablesNFuncs
cWidth=1800
cHeight=600
mxx=cHeight-50
mxsize=cWidth/20
data = []
lightRed='#FF7F7F'
lightBlue='#ADD8E6'

def drawInfo(data,colorArr):
	canvas.delete("all")
	sizeofdata=len(data)
	spacing=70/sizeofdata
	
	xWidth=cWidth/sizeofdata
	
	for i,height in enumerate(data):
		#top left
		x0=i*xWidth + 2*spacing 
		y0=cHeight - data[i]
		#bottom right
		x1=x0+xWidth - 2*spacing
		y1=cHeight
		canvas.create_rectangle(x0,y0,x1,y1,fill=colorArr[i])
		canvas.create_text((x0),y0,anchor=SW,text=str(data[i]),fill='white')

	root.update_idletasks()


def execute(minval,maxval,lengt):
	global data
	if(maxval<minval):
		maxval,minval=minval,maxval
	
	data=[]
	try:
		if cusEntry.get()=="":
			for x in range(lengt):
				data.append(random.randint(minval,maxval))
		else:
			for x in cusEntry.get().split(','):
				if(int(x)<0):
					data.append(0)
				elif(int(x)>mxx):
					data.append(mxx)
				else:
					data.append(int(x))
	except:
		print("Invalid Custom Input")
		for x in range(lengt):
			data.append(random.randint(minval,maxval))

	print(data)
	drawInfo(data,[lightRed for x in range(len(data))]) #data[0] 'red', data[1] 'red'..... data[n-1] 'red'

def StartAlgo():
	global data
	if(algoMenu.get()=="Bubble Sort"):
		bubsort(data,drawInfo,speedScale.get())
		drawInfo(data, ["lightgreen" for x in range(len(data))])
	elif(algoMenu.get()=="Selection Sort"):
		selsort(data,drawInfo,speedScale.get())
		drawInfo(data, ["lightgreen" for x in range(len(data))])
	elif(algoMenu.get()=="Insertion Sort"):
		inssort(data,drawInfo,speedScale.get())
		drawInfo(data, ["lightgreen" for x in range(len(data))])
	elif(algoMenu.get()=="Merge Sort"):
		merge_sort(data,0, len(data)-1, drawInfo, speedScale.get())
		drawInfo(data, ["lightgreen" for x in range(len(data))])
	elif(algoMenu.get()=="Quick Sort"):
		quick_sort(data,0,len(data)-1,drawInfo,speedScale.get())
		drawInfo(data, ["lightgreen" for x in range(len(data))])

#User Interface ---------------------

UiFrame = Frame(root, width=cWidth,height=200,bg=lightBlue)
UiFrame.grid(row=0,column=0,padx=7,pady=7)

#for Custom Data
UiFrame2 = Frame(root, width=cWidth,height=70,bg=lightBlue)
UiFrame2.grid(row=1,column=0,padx=7,pady=3)

#for bars
canvas = Canvas(root, width=cWidth,height=cHeight,bg='black', highlightthickness=0)
canvas.grid(row=2,column=0,padx=7,pady=0)

#Content----------------------

#Algo Menu Row
Label(UiFrame,text="Algorithm: ",bg=lightBlue).grid(row=0, column=0, padx=5,pady=5, sticky=W)
algoMenu=ttk.Combobox(UiFrame,values=['Selection Sort', 'Bubble Sort', 'Insertion Sort','Merge Sort', 'Quick Sort'])
algoMenu.grid(row=0,column=1, padx=7,pady=7)
algoMenu.current(0)

#Size Row
Label(UiFrame,text="Bar Quantity: ",bg=lightBlue).grid(row=1, column=0, padx=5,pady=5, sticky=W)
SizeScale = Scale(UiFrame, from_ = 2, to = mxsize, orient = HORIZONTAL)
SizeScale.grid(row=1,column=1,padx=5,pady=5, sticky=W)

#Min Row
Label(UiFrame,text="Min Value: ",bg=lightBlue).grid(row=1, column=2, padx=5,pady=5, sticky=W)
minScale = Scale(UiFrame, from_ = 0, to = mxx, orient = HORIZONTAL,length=200)
minScale.grid(row=1,column=3,padx=5,pady=5, sticky=W)

#Max Row
Label(UiFrame,text="Max Value: ",bg=lightBlue).grid(row=1, column=4, padx=5,pady=5, sticky=W)
maxScale = Scale(UiFrame, from_ = 0, to = mxx, orient = HORIZONTAL,length=200)
maxScale.grid(row=1,column=5,padx=5,pady=5, sticky=W)

#Custom Entry Row
Label(UiFrame2,text="Custom Data: ",bg=lightBlue).grid(row=2, column=0, padx=5,pady=5, sticky=W)
cusEntry=Entry(UiFrame2,width=50)
cusEntry.grid(row=2, column=1, padx=5,pady=5, sticky=W)

#Speed Row
Label(UiFrame,text="Speed(s): ",bg=lightBlue).grid(row=0, column=4, padx=5,pady=5, sticky=W)
speedScale = Scale(UiFrame, from_ = 0.0, to = 3.0,resolution=0.1, orient = HORIZONTAL)
speedScale.grid(row=0,column=5,padx=5,pady=5, sticky=W)

#Buttons
btn=Button(UiFrame,text="Generate",command=lambda:execute(int(minScale.get()),int(maxScale.get()),int(SizeScale.get())),bg='red',fg='white')
btn.grid(row=0,column=2,padx=5,pady=5)
btnstrt=Button(UiFrame,text="Start",command=StartAlgo,bg='lightgreen',fg='black')
btnstrt.grid(row=0,column=3,padx=5,pady=5)

root.mainloop()
