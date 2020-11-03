
import cv2
import datetime
 
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    
    #Print Current Date/Time
    now = datetime.datetime.now()
    current_time = now.strftime("%D %H:%M:%S")

    
    frame = cv2.putText(frame,current_time, (0,30), font, 1, (0,255,255),1,cv2.LINE_AA)
    cv2.imshow("Capture",frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
