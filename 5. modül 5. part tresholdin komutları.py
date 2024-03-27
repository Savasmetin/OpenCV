import cv2
import numpy as np
from  matplotlib import pyplot as plt

resim = cv2.imread("QT7LV.png")

ret ,Tresh1 = cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
ret ,Tresh2 = cv2.threshold(resim,127,255,cv2.THRESH_TRUNC)
ret ,Tresh3 = cv2.threshold(resim,127,255,cv2.THRESH_TOZERO)
ret ,Tresh4 = cv2.threshold(resim,127,255,cv2.THRESH_TOZERO_INV)
ret ,Tresh5 = cv2.threshold(resim,127,255,cv2.THRESH_BINARY_INV)

basliklar = ["orjinal","binary","Trunc","Tozero","tozero_inv","binary_inv"]

resimler = [resim,Tresh1,Tresh2,Tresh3,Tresh4,Tresh5]
for i in range(6):


    plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray")
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()

"""for i in range(6):
    cv2.imshow(basliklar[i],resimler[i])
cv2.waitKey()
cv2.destroyAllWindows()"""