import numpy as np
import cv2
from scipy.spatial import distance

# Görüntüyü oku
img = cv2.imread("kose_bulma.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

# Köşe tespiti yap
koseler = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 20)
koseler = np.int0(koseler)

# En yakın komşuları bul ve çizgileri çiz
for i, kose1 in enumerate(koseler):
    x1, y1 = kose1.ravel()

    # En yakın komşuyu bul
    min_distance = float('inf')
    nearest_kose_index = None

    for j, kose2 in enumerate(koseler):
        if i != j:  # Aynı köşe değilse devam et
            x2, y2 = kose2.ravel()
            d = distance.euclidean((x1, y1), (x2, y2))

            if d < min_distance:
                min_distance = d
                nearest_kose_index = j

    # Çizgi çiz
    if nearest_kose_index is not None:
        x2, y2 = koseler[nearest_kose_index].ravel()
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

# Köşeleri işaretle
for kose in koseler:
    x, y = kose.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

# Sonucu göster
cv2.imshow("En Yakın Köşe Çizgileri", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
