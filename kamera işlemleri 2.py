import cv2

# Kamera bağlantısını yap
cap = cv2.VideoCapture(0)  # 0, bilgisayarınızdaki birincil kamerayı temsil eder
face_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray = cv2.cvtColor()
# Kamera başarıyla açılıp açılmadığını kontrol et
if not cap.isOpened():
    print("Kamera bağlantısı başarısız. Lütfen kamera sürücülerini kontrol edin.")
    exit()

# Sonsuz bir döngü içinde görüntü al
while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()

    # Görüntü başarıyla okunmuşsa işlemleri gerçekleştir
    if ret:
        # Görüntüyü ekrana göster
        cv2.imshow("Kamera Görüntüsü", frame)

    # Klavyeden "q" tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kullanılan kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()