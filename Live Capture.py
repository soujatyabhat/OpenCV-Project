# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:17:08 2020

@author: Sourick
"""


import cv2
import numpy as np
import pymsgbox


#Message 
text = ""


#Dummy Function
def nothing(x):
    pass


#Camera Plugin
cap = cv2.VideoCapture(0)



#Brightness Trackbar
cv2.namedWindow("Live Capture")
cv2.createTrackbar("Brightness", "Live Capture", 0, 100, nothing)


#Text Mover for (X,Y) axis 
cv2.createTrackbar("x", "Live Capture", 0, 500, nothing)
cv2.createTrackbar("y", "Live Capture", 0, 500, nothing)


#B/W & Color Mode
cv2.createTrackbar("B/W", "Live Capture", 0, 1, nothing)


#Create Dim Image
image = np.zeros((420,640,3),np.uint8)



while cap.isOpened():

   #Video Input
   ret,frame = cap.read()
   
   
   #Text Mover
   font = cv2.FONT_HERSHEY_COMPLEX_SMALL
   x = cv2.getTrackbarPos("x","Live Capture")
   y = cv2.getTrackbarPos("y","Live Capture")
   cv2.putText(frame, text, (x,y), font, 5, (0,255,255))
   
   
   
   #Image and Camera frame Resize 
   image = cv2.resize(image,(640,420))
   frame = cv2.resize(frame,(640,420))
   
   
   #Image Darkness controller
   Brightness = cv2.getTrackbarPos("Brightness","Live Capture") 
   merge = cv2.addWeighted(frame, (Brightness / 100), image, 1, 0)
   
   
   #Convert Colour to B/W or Viseversa
   mode = cv2.getTrackbarPos("B/W","Live Capture") 
   if mode == 0:
       pass
   else:
       merge = cv2.cvtColor(merge, cv2.COLOR_BGR2GRAY)     

   
   #Show Video
   cv2.imshow("Live Capture",merge)
   

   
   #Key Input
   key = cv2.waitKey(1)
   
   
   #Control for control
   if key == ord('q'):
       print("Quit")
       break
   elif key == ord('m'):
       text = pymsgbox.prompt('Enter Message : ','Message')
   else:
       pass
       
   
#Release Camera Control 
#Destroy All Window
cap.release()
cv2.destroyAllWindows()