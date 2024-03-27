import cv2
import numpy as np


img = cv2.imread("j1.png")
img2 = cv2.imread("j2.png")


kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1)
deliation = cv2.dilate(img2,kernel,iterations=1)

cv2.imshow("resim1",img)
cv2.imshow("resim2",img2)
cv2.imshow("erosion",erosion)
cv2.imshow("delition",deliation)

cv2.waitKey(0)
cv2.destroyAllWindows()
