# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:32:42 2020

@author: Sourick
"""

import cv2
import pymsgbox

text = ""

def message():
    global text    
    text = pymsgbox.prompt('Enter Message : ')


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    
    
   # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    font = cv2.FONT_HERSHEY_PLAIN
    frame = cv2.putText(frame,text, (10,80), font, 4, (0,255,255))
    
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    
    
    if key == ord('q') or key == ord('Q'):
        break
    elif key == ord('m') or key == ord('M'):
        message()
        
    

cap.release()
cv2.destroyAllWindows()

