import cv2
import numpy as np
from matplotlib import pyplot as plt
kamera = cv2.VideoCapture(0)


"""
gradyan tespiti için sonksiyon veri tipleri 
cv2.CV_64F:
64 bitlik ondalık sayı (float).
Hassas türev hesaplamaları için kullanılır ve negatif değerleri de içerebilir.

cv2.CV_16S:
16 bitlik işaretli tamsayı.
Hesaplamalar sırasında daha büyük değerleri tutabilir, ancak daha fazla bellek kullanır. 


cv2.CV_8U:
8 bitlik işaretsiz tamsayı (0 ile 255 arasında değerler).
Görüntü işleme uygulamalarında genellikle piksel değerlerinin bu aralıkta olduğu durumlarda kullanılır.

kenarların bir düzleme çarpması ile malzeme sayımı araç sayımı gibi örnekler projeler yapılabilir.
 
 """

# HSV RENK FİLTRELEMEDE KOLAYLIK SAĞLAR O YÜZDEN TERCİH EDİLİR
while True:
    ret, frame = kamera.read()
    # FORMAT OLARAK  ALDIĞIMIZ GÖRÜNTÜ HSV OLARAK YENİDEN ŞEKİLLENDİRİLİYOR
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #
    düsük_kırımızı = np.array([150,30,30])
    ust_kırmızı = np.array([190,255,255])
    düsük_mavi = np.array([100, 40, 40])
    ust_mavi = np.array([140, 255, 255])
    düsük_yesil = np.array([40, 40, 40])
    ust_yesil = np.array([80, 255, 255])
    mask = cv2.inRange(hsv,düsük_kırımızı,ust_kırmızı)
    son_resim = cv2.bitwise_and(frame,frame,mask= mask)
    mask1 = cv2.inRange(hsv, düsük_yesil, ust_yesil)
    son_resim1 = cv2.bitwise_and(frame, frame, mask=mask1)

    mask2 = cv2.inRange(hsv, düsük_mavi, ust_mavi)
    son_resim2 = cv2.bitwise_and(frame, frame, mask=mask2)


    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=3)

    kenarlar = cv2.Canny(frame,100,200)

    cv2.imshow("sobel y", sobely)
    cv2.imshow("laplac", laplacian)
    cv2.imshow("sobel x", sobelx)
    cv2.imshow("kenarlar",kenarlar)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()