# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:09:06 2020

@author: Sourick
"""


import cv2
import pymsgbox

# path = pymsgbox.prompt('Enter Image Path : ')


def click_event(event,x,y,flags,param):
      if event == cv2.EVENT_LBUTTONDOWN:
        blue = frame[y,x,0]
        green = frame[y,x,1]
        red = frame[y,x,2]
        
        rgb = str(red) + ' , ' + str(green) + ' , ' + str(blue)
        
        """
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(image,rgb,(x,y), font, 1, (255,0,0))
        cv2.imshow("Display Image",image)
        """
        pymsgbox.alert(rgb)
        
"""
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        strexis = str(x) + ' , ' + str(y)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(image,strexis,(x,y), font, 1, (255,0,0))
        cv2.imshow("Display Image",image)
"""
  
        
#image = cv2.imread("opencv\samples\data\HappyFish.jpg",-1)

cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('Display Image',frame)
    
    cv2.setMouseCallback('Display Image', click_event)
    key = cv2.waitKey(1)
    
    if key == ord('Q') or key == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()