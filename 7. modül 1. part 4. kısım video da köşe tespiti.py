import cv2
import numpy as np

# Kamera bağlantısını aç
cap = cv2.VideoCapture(0)

# Shi-Tomasi köşe tespiti parametreleri
feature_params = dict(maxCorners=0, qualityLevel=0.02, minDistance=7)

# İlk köşe için önceki koordinatları ve çizgi çizilen köşeyi tutacak değişkenler
prev_corner = None
prev_drawn_corner = None

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()

    # Gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Shi-Tomasi köşe tespiti uygula
    corners = cv2.goodFeaturesToTrack(gray, **feature_params)

    # Köşeleri işaretle
    if corners is not None:
        corners = np.intp(corners)
        for corner in corners:
            x, y = corner.ravel()

            # İlk köşe için sadece işaretle
            if prev_corner is None:
                cv2.circle(gray, (x, y), 3, (255, 255, 255), -1)
                prev_corner = (x, y)
            else:
                # İki nokta arasındaki mesafeyi kontrol et
                distance = np.sqrt((x - prev_corner[0])**2 + (y - prev_corner[1])**2)

                # Eğer önceki noktaya çizgi çizilmediyse ve mesafe 50 pikselden az ise
                if prev_drawn_corner is not None and distance < 50:
                    cv2.line(gray, (prev_corner[0], prev_corner[1]), (x, y), (255, 255, 255), 2)
                    prev_drawn_corner = (x, y)
                else:
                    # Eğer önceki noktaya çizgi çizilmediyse ve mesafe 50 pikselden fazlaysa
                    cv2.circle(gray, (x, y), 3, (255, 255, 255), -1)
                    prev_corner = (x, y)
                    prev_drawn_corner = None

    ret, th1 = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)
    cv2.imshow('Shi-Tomasi Corner Detection', th1)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()
