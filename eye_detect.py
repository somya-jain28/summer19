#!/usr/bin/python3
import cv2
print(cv2.__version__)

# detecting images
car_cascade = cv2.CascadeClassifier('eye.xml')
img=cv2.imread('eye.jpg')
print(img.shape)

cars=car_cascade.detectMultiScale(img,1.1,2)
print(cars)

for x,y,w,h in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('all',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
