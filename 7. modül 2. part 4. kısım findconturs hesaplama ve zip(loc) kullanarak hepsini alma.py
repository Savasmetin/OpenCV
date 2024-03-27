import cv2
import numpy as np
def nesne_tespit(ana_resim_yolu, template_yolu, threshold=0.8):
    # Ana resmi yükle
    img = cv2.imread(ana_resim_yolu)
    # Gri tonlamalıya dönüştür
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_yolu, 0)
    w, h = template.shape[::-1]
    # Konturları bul
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Tüm eşleşmeleri depolamak için bir liste oluştur
    eşleşmeler = []

    # Konturları döngüye al
    for contour in contours:
        # Konturun sınırlayıcı dikdörtgenini al
        x, y, width, height = cv2.boundingRect(contour)
        # Template ile eşleştir
        roi = gray[y:y + height, x:x + width]
        res = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
        # Eşleşme değerlerini ve konumları al
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            # Eşleşen nesnenin etrafına dikdörtgen çiz
            cv2.rectangle(img, (x + pt[0], y + pt[1]), (x + pt[0] + w, y + pt[1] + h), (0, 255, 255), 2)
            # Eşleşmenin koordinatlarını kaydet
            eşleşmeler.append((x + pt[0], y + pt[1]))

    # Sonucu göster
    cv2.imshow('Nesne Tespiti', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Tüm eşleşmeleri döndür
    return eşleşmeler

# Ana resim dosya yolu
ana_resim_yolu = "ana_resim.jpg"
template_yolu = "template.jpg"

# Nesne tespitini gerçekleştir
tüm_eşleşmeler = nesne_tespit(ana_resim_yolu, template_yolu)
print("Tüm eşleşmeler:", tüm_eşleşmeler)
