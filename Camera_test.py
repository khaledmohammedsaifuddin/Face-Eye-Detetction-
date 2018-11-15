import numpy as np
import cv2
vdo = cv2.VideoCapture(0) # capturing video and 0 index indicates my first camera
vdo.set(3,640) # set Width
vdo.set(4,480) # set Height
while(True):
    retu, img_frame = vdo.read()#it's return boolean true and false
    img_frame = cv2.flip(img_frame, -1) # If u want to flip
    gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('img_frame', img_frame) #original image 

    cv2.imshow('gray', gray)# gray image
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
vdo.release()
cv2.destroyAllWindows()
