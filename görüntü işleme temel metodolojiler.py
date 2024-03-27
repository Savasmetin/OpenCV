import cv2

img = cv2.imread("bee.jpg")
img2 = cv2.imread("bee.jpg",0)


"""
blue = img[:,:,0]
green = img[:,:,1]
red = img[:,:,2]
blue = 255
cv2.imshow("mavi resim",blue)
cv2.imshow("yeşil resim",green)
cv2.imshow("kırmızı resim",red)

b,g,r = cv2.split(img)
cv2.imshow("mavi1 resim",b)
cv2.imshow("yesişl1 resim",g)
cv2.imshow("kırmızı1 resim",r)
img[:,:,2] = 255
cv2.imshow("blue doyum",img)
"""

ROI = img[150:450,230:600]
img[150:450,630:1000] = ROI
isim = input("isim giriniz")
cv2.rectangle(img,(0,0),(1000,665),(0,255,0),5)
cv2.circle(img,(300,300),100,(255,255,255),5,cv2.LINE_4)
cv2.line(img,(150,100),(450,600),(0,0,255),5)


cv2.putText(img2,isim,(600,300),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),4,cv2.LINE_AA)
cv2.imshow("roı eklenti",img)

print(img.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()




