import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

# HSV RENK FİLTRELEMEDE KOLAYLIK SAĞLAR O YÜZDEN TERCİH EDİLİR
while True:
    ret, frame = kamera.read()
    # FORMAT OLARAK  ALDIĞIMIZ GÖRÜNTÜ HSV OLARAK YENİDEN ŞEKİLLENDİRİLİYOR
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #
    düsük_kırımızı = np.array([40,30,30])
    ust_kırmızı = np.array([80,255,255])

    mask = cv2.inRange(hsv,düsük_kırımızı,ust_kırmızı)
    son_resim = cv2.bitwise_and(frame,frame,mask= mask)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations=1) # görüntüdeki gürültüyü azaltıyor
    dilation = cv2.dilate(mask, kernel, iterations=1) # görüntüdeki gürültü belirginleşiyor
    opening = cv2.morphologyEx(frame,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    gradient = cv2.morphologyEx(frame,cv2.MORPH_GRADIENT,kernel)


    """
    cv2.imshow("son", son_resim)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("opening", opening)
    cv2.imshow("closing", closing)
    """
    cv2.imshow("gradient",opening)
    cv2.imshow("normal",frame)


    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()