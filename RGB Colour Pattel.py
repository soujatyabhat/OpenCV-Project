# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 10:49:15 2020

@author: Sourick
"""


import cv2

import numpy as np
image = np.zeros((300,512,3),np.uint8)



def nothing(x):
    pass

cv2.namedWindow("image")

cv2.createTrackbar("b", "image", 0, 255, nothing)
cv2.createTrackbar("g", "image", 0, 255, nothing)
cv2.createTrackbar("r", "image", 0, 255, nothing)

cv2.createTrackbar("test", "image", 0, 1, nothing)
    

while 1:
   
    
    
    b = cv2.getTrackbarPos("b","image") 
    print(b)
    g = cv2.getTrackbarPos("g","image") 
    r = cv2.getTrackbarPos("r","image") 
    
    test = cv2.getTrackbarPos("test", "image")
 
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(image, str(test), (50, 150), font, 4, (0, 0, 255))
    
    #cv2.putText(image,str(text),(30,100), font, 3, (0,0,255))
    
    image[:] = [b,g,r]
    
    #cv2.imshow("image",image)
    
    cv2.imshow("image",image)
    
      
    key = cv2.waitKey(1)
      
    if key == 27:
        break


"""
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    image = cv2.putText(image,str(b),(30,80),font,3,(0,0,255))
"""

    
    
  
  
  
   
cv2.destroyAllWindows()
