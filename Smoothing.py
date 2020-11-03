# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:10:35 2020

@author: Sourick
"""


import cv2
import numpy as np
image = cv2.imread("opencv\samples\data\lena.jpg",-1)


kernel = np.ones((5,5),np.float32)/9


#Low pas filter is used to remove noices from the images and make the image sharper
#High pass filter is used to find edges of an image

#print(kernel)

cv2.imshow("Image",image)

dst = cv2.filter2D(image, -1, kernel)
blur = cv2.blur(image, (5,5))
gvblur = cv2.GaussianBlur(image, (5,5), 0)

#For Salt - papper blur removal
medium = cv2.medianBlur(image,5)

#To keep blur but maintain sharpness of an image
bilateralfilter = cv2.bilateralFilter(image, 9, 75, 75)



#cv2.imshow("Image",dst)

cv2.imshow("2D",dst)
cv2.imshow("Blur",blur)
cv2.imshow("GvBlur",gvblur)
cv2.imshow("Bilateral Filter",bilateralfilter)

cv2.imshow("Medium",medium)

cv2.waitKey(0)

cv2.destroyAllWindows()

