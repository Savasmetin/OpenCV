import cv2
import numpy as np

# Resmi oku
img = cv2.imread("kose_bulma.jpg")

# Gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris köşe tespiti için parametreleri ayarla
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Köşelerin belirginleştirilmesi için eşikleme
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Sonuçları göster
cv2.imshow("Harris Corner Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

