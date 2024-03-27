import cv2

def nesne_tespit(ana_resim_yolu, template_yolu, threshold=0.5):
    # Ana resmi yükle
    img = cv2.imread(ana_resim_yolu)
    # Gri tonlamalıya dönüştür
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_yolu, 0)
    w, h = template.shape[::-1]
    # Konturları bul
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Konturları döngüye al
    for contour in contours:
        # Konturun sınırlayıcı dikdörtgenini al
        x, y, width, height = cv2.boundingRect(contour)
        # Template ile eşleştir
        roi = gray[y:y + height, x:x + width]
        res = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(f"Kontur alanı: {cv2.contourArea(contour)}, Eşleşme değeri: {max_val}")

        if max_val >= threshold:
            # Eşleşen nesnenin etrafına dikdörtgen çiz
            # Template'in konumunu ve boyutunu belirle
            template_x = x + max_loc[0]
            template_y = y + max_loc[1]
            cv2.rectangle(img, (template_x, template_y),
                          (template_x + w, template_y + h),
                          (0, 255, 255), 2)

    # Sonucu göster
    cv2.imshow('Nesne Tespiti', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ana resim dosya yolu
ana_resim_yolu = "ana_resim.jpg"
template_yolu = "template.jpg"

# Nesne tespitini gerçekleştir
nesne_tespit(ana_resim_yolu, template_yolu)
