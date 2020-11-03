# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:05:17 2020

@author: Sourick
"""


import cv2

image = cv2.imread("opencv\samples\data\sudoku.png",0)

_,th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)

th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2);

cv2.imshow("Image",image)

cv2.imshow("Th1",th1)
cv2.imshow("Th2",th2)
cv2.imshow("Th3",th3)

cv2.waitKey(0)

cv2.destroyAllWindows()

