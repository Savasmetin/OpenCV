import cv2
import numpy as np
import time

img = cv2.imread("metin uygulama.png",)

ret,treshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY_INV)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
"""gaus = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,155,3)"""
ret,tresholdgray = cv2.threshold(gray_img,12,255,cv2.THRESH_BINARY)
ret,Treshold1= cv2.threshold(gray_img,12,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(img.shape)
for block_size in range(255, 555, 2):

    gaus = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, 3)
    a = str(block_size)
    cv2.imshow(a,gaus)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # Sonuçları gözlemleyerek en iyi `blockSize` değerini seçebilirsiniz.

"""blur = cv2.medianBlur(gaus,1)
cv2.imshow("orjinal",img)
cv2.imshow("binary",treshold)
cv2.imshow("tresholdgray",tresholdgray)
cv2.imshow("gaus",gaus)
cv2.imshow("otsu",Treshold1)
cv2.imshow("blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""




























"""img =cv2.imread("metinnetleştirme.png")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


ret, Threshold = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
cv2.imshow("orjinal",img)
cv2.imshow("threshold",Threshold)
cv2.waitKey()
cv2.destroyAllWindows()"""