# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:11:29 2020

@author: Sourick
"""


import cv2
import numpy as np

def nothing(x):
    pass


#image = cv2.imread("opencv\samples\data\smarties.png",-1)

#Camera plugin
cap = cv2.VideoCapture(0)

#Create names window
cv2.namedWindow("Mask")

#Lower HSV values
cv2.createTrackbar("LH", "Mask", 0, 255, nothing)
cv2.createTrackbar("LS", "Mask", 0, 255, nothing)
cv2.createTrackbar("LV", "Mask", 0, 255, nothing)
    
#Upper HSV values
cv2.createTrackbar("UH", "Mask", 255, 255, nothing)
cv2.createTrackbar("US", "Mask", 255, 255, nothing)
cv2.createTrackbar("UV", "Mask", 255, 255, nothing)

while True:
    
    #Frame Capture
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Adjust Lower HSV Value
    LH = cv2.getTrackbarPos("LH","Mask")
    LS = cv2.getTrackbarPos("LS","Mask")
    LV = cv2.getTrackbarPos("LV","Mask")
    
    #Adjust Upper HSV Value
    UH = cv2.getTrackbarPos("UH","Mask")
    US = cv2.getTrackbarPos("US","Mask")
    UV = cv2.getTrackbarPos("UV","Mask")
    
   
    
    l_b = np.array([LH,LS,LV])
    u_b = np.array([UH,US,UV])

    mask = cv2.inRange(hsv,l_b,u_b)
  
    res = cv2.bitwise_or(frame, frame,mask=mask)
    
    #cv2.imshow("Object Detection",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("res",res)
    
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()