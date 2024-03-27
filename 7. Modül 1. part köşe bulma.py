import numpy as np
import cv2

img = cv2.imread("kose_bulma.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

koseler = cv2.goodFeaturesToTrack(gray_img,50 ,0.01,20)
koseler = np.intp(koseler)

for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("koseler",img)
cv2.waitKey(0)
cv2.destroyAllWindows()