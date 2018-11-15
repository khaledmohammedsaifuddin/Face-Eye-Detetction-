import numpy as np
import cv2


face_c = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_c = cv2.CascadeClassifier('haarcascade_eye.xml')
#we may create our own classifier but here I have used trained classifier from OpenCv

vdo = cv2.Videovdoture(0)# capturing video and 0 index indicates my first camera

while 1:
    retu, img_frame = vdo.read()#it's return boolean true and false
    gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)# convert into gray scale
    faces = face_c.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img_frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_frame[y:y+h, x:x+w]
        
        eyes = eye_c.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img_frame',img_frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

vdo.release()
cv2.destroyAllWindows()
