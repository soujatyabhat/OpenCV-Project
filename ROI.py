# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:33:27 2020

@author: Sourick
"""


import cv2

im = cv2.imread("Samples/HappyFish_bw.jpg")

roi = cv2.selectROI(im)

print(roi)

im_cropped = im[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]

cv2.imshow("Cropped Image", im_cropped)
if cv2.waitKey(0) == ord('s'):
    cv2.imwrite("sample.png",im_cropped)


cv2.destroyAllWindows()