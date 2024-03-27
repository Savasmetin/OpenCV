import cv2
import pywhatkit as kit
import time

# Kamera objesini oluştur
cap = cv2.VideoCapture(0)

# Kamera görüntüsünü al
ret, frame = cap.read()

# Fotoğrafı kaydet
cv2.imwrite("captured_photo.jpg", frame)

# Kamerayı kapat
cap.release()

# WhatsApp mesajını gönder
phone_number = "+905051516275"  # Hedef telefon numarasını girin
message = "İşte anlık fotoğraf!"
image_path = "captured_photo.jpg"

# Gönderilecek fotoğrafın ismi ve numara arasında boşluk olmamalıdır.
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H-%M-%S", current_time)
image_new_path = f"captured_photo_{formatted_time}.jpg"

# Fotoğrafı yeniden adlandır
import os
os.rename("captured_photo.jpg", image_new_path)

# WhatsApp üzerinden fotoğraf gönder
kit.sendwhats_image(phone_number, image_new_path, message, 12, 0)

# Bekleme süresi
time.sleep(5)

# Programı sonlandır
cv2.destroyAllWindows()