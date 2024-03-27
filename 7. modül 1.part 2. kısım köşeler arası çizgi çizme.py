import numpy as np
import cv2

# Görüntüyü oku
img = cv2.imread("kose_bulma.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

# Köşe tespiti yap
koseler = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 20)
koseler = np.intp(koseler)

# En yakın komşuyu bul ve çizgileri çiz
for kose1 in koseler:
    x1, y1 = kose1.ravel()

    # En yakın komşuyu bul
    min_distance = float('inf')
    nearest_kose = None

    for kose2 in koseler:
        x2, y2 = kose2.ravel()
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if distance > 0 and distance < min_distance:
            min_distance = distance
            nearest_kose = kose2

    # Çizgi çiz
    x2, y2 = nearest_kose.ravel()
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

# Köşeleri işaretle
for kose in koseler:
    x, y = kose.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

# Sonucu göster
cv2.imshow("En Yakın Köşe Çizgileri", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

