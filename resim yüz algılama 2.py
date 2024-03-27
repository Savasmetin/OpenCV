import cv2
import numpy as np

img = cv2.imread("beyza.jpg")
print(img.shape)

yuz_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
griTon = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
yuzler = yuz_casc.detectMultiScale(griTon,1.1,6)

for (x,y,w,h) in yuzler:

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    eye_casc =cv2.CascadeClassifier("haarcascade_eye.xml")
    eyes = eye_casc.detectMultiScale(griTon,1.1,12)
    for(x1,y1,w1,h1) in eyes:
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,0,255),1)

cv2.imshow("yuzler",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

