import cv2
import numpy as np
frame1=cv2.imread('ff.jpg')
# converting normal image to gray image
# gray color have 1 channel (B,G,R), so coverting norma image fro 3 channel to 1(gray) and ten again to 3 channel for compatibility            
frame2=cv2.cvtColor(cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY),cv2.COLOR_GRAY2BGR)

blur=cv2.blur(frame1,(5,5))
img=np.concatenate((frame1,blur),axis=1)
cv2.imshow('live',img)
cv2.waitKey(0)& 0xff==ord('q')
cv2.destroyAllWindows()    


