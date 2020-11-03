# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:31:08 2020

@author: Sourick


@Description:
    
    Here atfirst you have to find faces.
    after detecting the faces you have to find eyes of these face using given coodinates
"""


import cv2


#Import images
image = cv2.imread("Samples/HappyFish_bw.jpg",-1)

#Add Face and Eyes casecade file
face_casecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_casecade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

#Convert Colour image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
#Find face 
face = face_casecade.detectMultiScale(gray,1.1,4)
    
#Display rectangle on detected faces
for (x,y,w,h) in face:
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0))
    

#Store coordinates to find eyes
roi_gray = gray[y:y+h,x:x+w]
roi_frame = image[y:y+h,x:x+w] 
        
#Find Eyes
eyes = eye_casecade.detectMultiScale(roi_gray) 
    
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_frame, (ex,ey), (ex+ew,ey+eh), (0,255,0))
    
#Display total result
cv2.imshow("Frame",image)
    
#Hold the window
cv2.waitKey(0)

#Destro the window
cv2.destroyAllWindows()