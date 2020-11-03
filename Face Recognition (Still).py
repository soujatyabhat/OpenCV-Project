# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:31:08 2020

@author: Sourick
"""


import cv2

#Import image from drive
image = cv2.imread("HappyFish_bw.jpg",-1)

#Add haardascade from drive
face_casecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Convert colour image into grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#Detect face using given function
face = face_casecade.detectMultiScale(gray,1.1,4)
    
#Fint where human faces are visible using given coordinates 
for (x,y,w,h) in face:
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0))
    
#Display Image
cv2.imshow("Frame",image)
    
#Hold the window
cv2.waitKey(0)

#Destro the window
cv2.destroyAllWindows()