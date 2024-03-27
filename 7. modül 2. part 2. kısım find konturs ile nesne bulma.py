import cv2
import numpy as np


def nesne_tespit(ana_resim_yolu, template_yolu, threshold=0.7):
    # Ana resmi yükle
    img_rgb = cv2.imread(ana_resim_yolu)
    # Gri tonlamalıya dönüştür
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Template'i yükle
    template = cv2.imread(template_yolu, 0)
    # Template'in boyutunu al
    w, h = template.shape[::-1]

    # Ana resim üzerinde konturları bul
    contours = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Template ile eşleşen konturları bul
    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)
        roi = img_gray[y:y + height, x:x + width]
        res = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >= threshold:
            cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 255), 2)

    # Sonucu görselleştir
    cv2.imshow("Nesne Tespiti", img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Ana resim ve template dosya yolları
ana_resim_yolu = "ana_resim.jpg"
template_yolu = "template.jpg"

# Nesne tespitini gerçekleştir
nesne_tespit(ana_resim_yolu, template_yolu)
