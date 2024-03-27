import cv2
import numpy as np

# Kamera bağlantısını aç
cap = cv2.VideoCapture(0)

# Shi-Tomasi köşe tespiti parametreleri
feature_params = dict(maxCorners=0, qualityLevel=0.02, minDistance=7)

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
            cv2.circle(gray, (x, y), 3, (255,255,255), -1)

    ret,th1 = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
    cv2.imshow('Shi-Tomasi Corner Detection',th1 )

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()