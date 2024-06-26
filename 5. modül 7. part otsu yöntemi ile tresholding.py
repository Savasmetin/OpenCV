import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("otsu resim3.png",0)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)
ret,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

"""cv2.imshow("normalresim",img)
cv2.imshow("normalthresh",th1)
cv2.imshow("otsu",th2)
cv2.imshow("blur",blur)
cv2.imshow("blurotsu",th3)


cv2.waitKey()
cv2.destroyAllWindows()"""

resimler =[ img,0,th1,img,0,th2,blur,0,th3]
basliklar =["orijinal resim","histogram","binar tresholding","orijinal resim","histogram","otsu tresholding","blur resim","histogram","blur otsu tresholding"]

for i in  range(3):

    plt.subplot(3,3,i*3+1),plt.imshow(resimler[i*3],"gray")
    plt.title(basliklar[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(resimler[i * 3].ravel(),256)
    plt.title(basliklar[i * 3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(resimler[i * 3+2], "gray")
    plt.title(basliklar[i * 3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()