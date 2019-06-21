import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    
    #time to draw liens
    cv2.line(frame,(0,0),(100,100),(255,0,0),2)

    # drawing multiple lines
    cv2.line(frame,(100,100),(200,200),(0,100,100),4)
    # drawing rectangle
    cv2.rectangle(frame,(100,200),(400,600),(0,0,255),4)
    cv2.imshow('live',frame)
    if cv2.waitKey(0)& 0xff==ord('q'):
        break
cv2.destroyAllWindows()    
cap.release()

