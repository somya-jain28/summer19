#!/usr/bin/python3
import cv2
print(cv2.__version__)

# detecting images
smile_cascade = cv2.CascadeClassifier('smile.xml')
face_cascade=cv2.CascadeClassifier('face.xml')
img=cv2.imread('smile.jpg')
print(img.shape)
face=face_cascade.detectMultiScale(img,1.15,5)
smiles=smile_cascade.detectMultiScale(img,1.35,5)
print(smiles)

for x,y,w,h in smiles:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('all',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
