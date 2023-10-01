import time

lightRed='#FF7F7F'

#just Add sleep and drawInfo whenever you do something

def selsort(data,drawInfo,speed):
	for i in range(len(data)-1):
		imin=i
		for j in range(i+1,len(data)):
			if(data[j]<data[imin]):
				imin=j
		data[i],data[imin]=data[imin],data[i]
		drawInfo(data,colorArrSel(data,imin,i))
		time.sleep(float(speed))

def colorArrSel(data,imin,curr):
	colorar=[lightRed for x in range(len(data))]
	for i in range(len(data)):
		if i==imin:
			colorar[i]=('green')
		elif i==curr:
			colorar[i]=('blue')

	return colorar

#-----------------------------------------------------------------------------------------

def bubsort(data,drawInfo,speed):
	for p in range(len(data)-1):
		flag=False
		for i in range(len(data)-1-p):
			if data[i]>data[i+1]:
				data[i],data[i+1]=data[i+1],data[i]
				flag = True
				drawInfo(data,['green' if x==i or x==i+1 else lightRed for x in range(len(data))])
				time.sleep(float(speed))
		if flag:
			break

#-----------------------------------------------------------------------------------------

def inssort(data,drawInfo,speed):
	for i in range(1,len(data)):
		hole=i;
		key=data[hole]
		#drawInfo(data, ColorArrIns(data,hole))
		while(hole>0 and data[hole-1]>key):
			data[hole],data[hole-1]=data[hole-1],data[hole]
			hole-=1
			drawInfo(data, ColorArrIns(data,hole))
			time.sleep(float(speed))
		data[hole]=key


def ColorArrIns(data,hole):
	clrarr=[]
	for i in range(len(data)):
		if i<hole and i>=0:
			clrarr.append('lightgreen')
		else:
			clrarr.append(lightRed)

		if i==hole:
			clrarr[i]='blue'

	return clrarr


#-----------------------------------------------------------------------------------------

def merge_sort(data, left, right, drawInfo, speed):
    if left < right:
        middle = (left + right) // 2
        merge_sort(data, left, middle, drawInfo, speed)
        merge_sort(data, middle+1, right, drawInfo, speed)
        merge(data, left, middle, right, drawInfo, speed)

def merge(data, left, middle, right, drawInfo, speed):
    drawInfo(data, ColorArrMerge(len(data), left, middle, right))
    time.sleep(speed)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    drawInfo(data, ["lightgreen" if x >= left and x <= right else lightRed for x in range(len(data))])
    time.sleep(speed)

def ColorArrMerge(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append(lightRed)

    return colorArray

#-----------------------------------------------------------------------------------------


def partition(data, head, tail, drawInfo, speed):
    border = head
    pivot = data[tail]

    drawInfo(data, ColorArrQuick(len(data), head, tail, border, border))
    time.sleep(speed)

    for j in range(head, tail):
        if data[j] < pivot:
            drawInfo(data, ColorArrQuick(len(data), head, tail, border, j, True))
            time.sleep(speed)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawInfo(data, ColorArrQuick(len(data), head, tail, border, j))
        time.sleep(speed)


    #swap pivot with border value
    drawInfo(data, ColorArrQuick(len(data), head, tail, border, tail, True))
    time.sleep(speed)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawInfo, speed):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawInfo, speed)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawInfo, speed)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawInfo, speed)


def ColorArrQuick(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append(lightRed)

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'lightgreen'

    return colorArray
