import numpy as np
import cv2
import os


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

test=face_cascade.load('haarcascade_frontalface_default.xml')
print(test)
img = cv2.imread('100_0750.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print (face_cascade)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = img[y:y+h, x:x+w]
   eyes = eye_cascade.detectMultiScale(roi_gray)
for (ex,ey,ew,eh) in eyes:
   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

files = [image for image in os.listdir('.') if os.pathisfile(image) and (image.endswith('jpg') or image.endswith('jpeg'))]
for f in files:
	pic = cv2.imread(f)
	cv2.imshow('100_0750',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()