# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:24:55 2020

@author: Sourick
"""
import cv2

img = cv2.imread("IMG_5956.jpg",-1)


ask = cv2.imshow('Display Image',img)
print(img)

key_input = cv2.waitKey(0)
if key_input == 27:
    cv2.destroyAllWindows()
    
elif key_input == 83 or key_input == 115:
    if(cv2.imwrite('HappyFish_bw.jpg',img)):
        print("File has saved")
        cv2.destroyAllWindows()
    else:
        print("File has not saved")
        cv2.destroyAllWindows()

    


