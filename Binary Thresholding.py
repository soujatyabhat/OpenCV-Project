# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:22:49 2020

@author: Sourick
"""


import cv2
#import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("opencv\samples\data\gradient.png",-1)

#cap = cv2.VideoCapture(0)

while 1:
    
    #_,frame = cap.read()
    #Here you check that if any pixel value will be greter than 90 then that segment be assign 0 (black) if not then 255 value (white) will be assign
   
  
    _,th1 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY)
    _,th2 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY_INV)
    _,th3 = cv2.threshold(image,127, 255, cv2.THRESH_TRUNC)
    _,th4 = cv2.threshold(image,127, 255, cv2.THRESH_TOZERO)
    
   
     
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    th5 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,2)
    
   
    """
    cv2.imshow("Video Capture",frame)
    
  
    cv2.imshow("Th1",th1)
    cv2.imshow("Th2",th2)
    cv2.imshow("Th3",th3)
    cv2.imshow("Th4",th4)
    
    
    cv2.imshow("Th5",th5)
    """
    
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','adaptiveThreshold']
    images = [image, th1 ,th2 ,th3 ,th4, th5]

    for i in range(6):
        plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
      
    
    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
#cap.release()
cv2.destroyAllWindows()


