# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:23:05 2020

@author: Sourick
"""

import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    switch,frame = capture.read()
    
    
    cv2.imshow("Frame",frame)
    
    cv2.waitKey(1)
    
capture.release()
cv2.destroyAllWindows()

