# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:51:47 2020

@author: Sourick
"""

import cv2
import numpy as np
import os
import pymsgbox

color_temp = (0,0,255)
color = ""

#This Function Works Whens mouse right click has pressed
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255),-1)
            
        #Append straight line points in points List
        points.append((x,y))

        if len(points) >= 2:
             if color == "" or color == "red":
                cv2.line(img, points[-2], points[-1], (0,0,255),5)  
             elif color == "blue":
                cv2.line(img, points[-2], points[-1], (255,0,0),5) 
             elif color == "yellow":
                cv2.line(img, points[-2], points[-1], (0,255,255),5) 
             elif color == "green":
                cv2.line(img, points[-2], points[-1], (0,255,0),5) 
             elif color == "white":
                cv2.line(img, points[-2], points[-1], (255,255,255),5)
             elif color == "black":
                cv2.line(img, points[-2], points[-1], (0,0,0),5)
          
            
        cv2.imshow('Display Image',img)
        
#Black Board
img = np.zeros((420,640,3),np.uint8)

#Point's coodinates are stores in this list
points = []

while 1:
    
    cv2.imshow('Display Image',img)
    cv2.setMouseCallback('Display Image', click_event)
    key = cv2.waitKey(0)

    # color combination 
    
    if key == ord("r"):
        color = "red"
        print("Now Color is Red")
        
    elif key == ord("b"):
        color = "blue"
        print("Now Color is Blue")
        
    elif key == ord("y"):
        color = "yellow"
        print("Now Color is Yellow")
        
    elif key == ord("g"):
        color = "green"
        print("Now Color is Green")
        
    elif key == ord("w"):
        color = "white"
        print("Now Color is White")
        
    elif key == ord("B"):
        color = "black"
        print("Now Color is Black")
        
    elif key == ord("c"):
        print("Key C has pressed")
        img = np.zeros((420,640,3),np.uint8)
        points.clear()
        
    elif key == ord("Q"):
        print("Quit")
        break
    
    #Paint Saving Section
    elif key == ord("s"):
        print("Key S has pressed")
        path = pymsgbox.prompt('Enter Saving Path : ')
        os.chdir(path)
        cv2.imwrite("sample.png",img)
    
cv2.destroyAllWindows()