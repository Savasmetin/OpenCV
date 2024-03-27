import cv2

kamera = cv2.VideoCapture(0)
"""kamera.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)
"""

while True:
    ret, goruntu = kamera.read()
    griton = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    yuz_casc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    griTon = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_casc.detectMultiScale(griTon, 1.1, 6)
    for (x, y, w, h) in yuzler:
        cv2.rectangle(goruntu, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if ret:
        cv2.imshow("goruntu", goruntu)

    else:
        print("görüntü başarılı alınamamıştır")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()
