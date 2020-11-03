# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:31:08 2020

@author: Sourick
"""


import cv2

capture = cv2.VideoCapture(0)

face_casecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_casecade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

while capture.isOpened():
    _,frame = capture.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face = face_casecade.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0))
        
        roi_gray = gray[y:y+h,x:x+w]
        roi_frame = frame[y:y+h,x:x+w] 
        
        eyes = eye_casecade.detectMultiScale(roi_gray) 
    
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_frame, (ex,ey), (ex+ew,ey+eh), (0,255,0))
    
    cv2.imshow("Frame",frame)
    
    if(cv2.waitKey(1) == 27):
        break
    
capture.release()
cv2.destroyAllWindows()