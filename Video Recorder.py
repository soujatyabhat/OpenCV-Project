# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 09:38:49 2020

@author: Sourick
"""


import cv2

vid = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ouput.avi',fourcc,20.0,(640,480))

while vid.isOpened():
    ret, frame = vid.read() 

	# Display the resulting frame 
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
	
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    
    #print text on frame
    frame = cv2.putText(frame, "Open CV", (0,255), font, 4, (0,255,255),4,cv2.LINE_AA)
    
    cv2.imshow('frame', frame) 
    
    #save frame in storage
    out.write(frame)
    
	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 
    if(cv2.waitKey(1) == ord('q')):
        break
    
vid.release()
out.release()
cv2.destroyAllWindows()