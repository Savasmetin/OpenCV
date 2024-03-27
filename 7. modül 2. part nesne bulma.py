import cv2
import numpy as np

img_rgb = cv2.imread("ana_resim.jpg")
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

nesne = cv2.imread("template.jpg",0)

w,h = nesne.shape[::-1]

src = cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED)
threshold = 0.74

loc = np.where(src>threshold)

for i in zip(*loc[::-1]):

    cv2.rectangle(img_rgb,i,(i[0]+w,i[1]+h),(0,255,255),2)
cv2.imshow("nesneler bulundu",img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()