import cv2

eye = cv2.CascadeClassifier('eye.xml')

#starting camera
video_capture=cv2.VideoCapture(0)

while True:
    status,frame=video_capture.read()  

    eyes = eye.detectMultiScale(frame,1.15,5)
    print(eyes)

    #draw rectangle around the eyes
    for x,y,w,h in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    # displaying the frame
    cv2.imshow('video',frame)

    if cv2.waitKey(10)& 0xff==ord('q'):
        break

    
# realeasr the capture
video_capture.release()
cv2.destroyAllWindows()
