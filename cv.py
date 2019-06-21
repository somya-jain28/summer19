import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)    
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('live1',gray_frame)
    #time to draw liens
    #cv2.line(frame,(0,0),(200,200),(0,0,255),2)
    if cv2.waitKey(0)& 0xff==ord('q'):
        break
cv2.destroyAllWindows()    
cap.release()

