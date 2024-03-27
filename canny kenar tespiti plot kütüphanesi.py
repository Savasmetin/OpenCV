import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle
img = cv2.imread('görüntü.jpg', cv2.IMREAD_GRAYSCALE)

# Gauss Filtresi
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Gradyan Hesaplama
grad_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

# Kenar Gücü ve Yönü Hesaplama
magnitude = np.sqrt(grad_x**2 + grad_y**2)
angle = np.arctan2(grad_y, grad_x) * (180/np.pi)

# Kenar İzleme
edge_magnitude = cv2.nonMaxSuppression(magnitude, angle, 100, 200)

# Histerizis Eşikleme
edges = cv2.Canny(blur, 100, 200)

# Sonuçları Görselleştirme
plt.figure(figsize=(10, 5))

plt.subplot(131), plt.imshow(blur, cmap='gray'), plt.title('Gauss Filtre')
plt.subplot(132), plt.imshow(edge_magnitude, cmap='gray'), plt.title('Kenar Gücü')
plt.subplot(133), plt.imshow(edges, cmap='gray'), plt.title('Canny Kenar Tespiti')

plt.show()
