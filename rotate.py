import cv2
import numpy as np 
image=cv2.imread('car.jpg')
(h,w) = image.shape[:2]
center=(w/2,h/2)

#rotate the image by 180 degrees
a=cv2.getRotationMatrix2D(center, 120,1.0)
rotated = cv2.warpAffine(image,a,(w,h))
comb=np.concatenate((image,rotated),axis=1)
cv2.imshow('frame',comb)
#cv2.imshow('rotated',rotated)
cv2.waitKey(0)
