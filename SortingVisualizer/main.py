from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from insertionSort import insertion_sort

root = Tk()
root.title('Sorting Algorithm Visualizer')
root.geometry("825x550")
root.resizable(FALSE,FALSE)
root.config(bg='black')

#variables
selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1) +3
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['#ff615d' for x in range(len(data))]) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    if not data: return
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])


#frame / base lauout
UI_frame = Frame(root, width=800, height=200, bg='#00003f')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#Row[0]
Label(UI_frame, text="Sorting Algorithm: ", bg='#00003f', fg="White").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Insertion Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=10)

Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=50, resolution=1, bg="White", orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, bg="White",  orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1)

maxEntry = Scale(UI_frame, from_=11, to=100, resolution=1, bg="White",  orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2)

Button(UI_frame, text="Generate Data", command=Generate, bg='light green').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
