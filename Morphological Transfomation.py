# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:28:40 2020

@author: Sourick
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt 

kernel = np.ones((3,3),np.uint8)

image = cv2.imread("opencv\samples\data\smarties.png",0)

_,th1 = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY_INV)

dilation = cv2.dilate(th1,kernel,iterations=3)
erosion = cv2.erode(th1, kernel,iterations=1)
opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)
mg = cv2.morphologyEx(th1, cv2.MORPH_GRADIENT, kernel)


titles = ["Dilation","Erosion","Opening","Closing"]
images = [dilation,erosion,opening,closing]

for i in range(len(titles)):
    plt.subplot(1, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
"""
cv2.imshow("Image",image)
cv2.imshow("Th1",th1)

cv2.imshow("Delation",dilation)
cv2.imshow("Erosion",erosion)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.imshow("MG",mg)

"""
cv2.waitKey(0)

cv2.destroyAllWindows()