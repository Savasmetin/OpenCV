import cv2
import numpy as np
kamera = cv2.VideoCapture(0)

# HSV RENK FİLTRELEMEDE KOLAYLIK SAĞLAR O YÜZDEN TERCİH EDİLİR
while True:
    ret, frame = kamera.read()
    # FORMAT OLARAK  ALDIĞIMIZ GÖRÜNTÜ HSV OLARAK YENİDEN ŞEKİLLENDİRİLİYOR
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #
    düsük_kırımızı = np.array([140,30,30])
    ust_kırmızı = np.array([180,255,255])
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


    cv2.imshow("son", son_resim)
    cv2.imshow("son1", son_resim1)
    cv2.imshow("son2", son_resim2)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()