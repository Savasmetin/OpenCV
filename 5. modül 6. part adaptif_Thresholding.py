import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("adaptif .png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img_gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img_gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
blur = cv2.medianBlur(src=img_gray,ksize=1)
th4 = cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

basliklar = ["orjinal","basit Thresh","mean_c","Gaussıan_c","blur","gaussıan and  blur"]

resimler = [img,th1,th2,th3,blur,th4]
for i in range(6):


    plt.subplot(3,2,i+1),plt.imshow(resimler[i],"gray")
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()