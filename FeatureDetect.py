import cv2
import numpy as np 
from stack import *

dialiteration=2
w=800
h=600

kernel = np.ones((5,5))

def preProcess(img):
	imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
	imgCanny = cv2.Canny(imgBlur,200,200)
	imgDilation = cv2.dilate(imgCanny,kernel,iterations=dialiteration)
	imgThres = cv2.erode(imgDilation,kernel,iterations=1)
	return imgThres

def getBiggContours(img):
	big = np.array([])
	maxArea = 0
	contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area>5000:
			cv2.drawContours(imgContours,cnt,-1,(0,255,0),5)
			peri = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,0.02*peri,True)
			objCorner = len(approx)

			if objCorner==4 and area>=maxArea:
				big = approx
				maxArea = area
	
	return big

def reorder(points):
	points = points.reshape((4,2))
	newpoints = np.zeros((4,1,2),np.int32)
	add = points.sum(1)

	newpoints[0]=points[np.argmin(add)]	#top left point is minimum
	newpoints[3]=points[np.argmax(add)] #bottom right is maximum

	diff=np.diff(points,axis=1)
	newpoints[1]=points[np.argmin(diff)]
	newpoints[2]=points[np.argmax(diff)]

	return newpoints

def warp(img,biggestCP):
	biggestCorrectOrder = reorder(biggestCP)
	pt1 = np.float32(biggestCorrectOrder)
	pt2 = np.float32([[0,0],[h,0],[0,w],[h,w]])
	warpMatrix = cv2.getPerspectiveTransform(pt1,pt2)
	imgWarp = cv2.warpPerspective(img,warpMatrix,(h,w))

	imgWarp = imgWarp[20:imgWarp.shape[0]-20,20:imgWarp.shape[1]-20]
	imgWarp = cv2.resize(imgWarp,(h,w))

	return imgWarp


while True:
	#success,img = vdo.read()
	img = cv2.imread("ed.jpg")
	img = cv2.resize(img,(w,h))
	imgContours = img.copy()
	imgF = preProcess(img)
	
	biggest = getBiggContours(imgF)

	if biggest.size!=0:
		imgWrp = warp(img,biggest)
		
		imgStack = stackImages(0.6,([img,imgF],[imgContours,imgWrp]))
		cv2.putText(imgStack,"Original",(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.putText(imgStack,"Threshold",(385,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.putText(imgStack,"Contours",(0,310),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.putText(imgStack,"Warp",(385,310),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

	else:
		imgStack = stackImages(0.6,([img,imgF],[img,imgF]))
		cv2.putText(imgStack,"Original",(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.putText(imgStack,"Threshold",(385,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.putText(imgStack,"Original",(0,310),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.putText(imgStack,"Threshold",(385,310),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

	cv2.imshow("op",imgStack)

	if cv2.waitKey(1) & 0xFF==ord('x'):
		cv2.destroyAllWindows()
		break
