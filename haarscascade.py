import cv2
kamera = cv2.VideoCapture(0)

face_casc = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret ,Frame = kamera.read()
    gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    faces = face_casc.detectMultiScale(gray, 1.3, 3, minSize = (50,50))
    for (x,y,h,w) in faces:
        cv2.rectangle(Frame,(x,y),(x+w,y+h),(255,0,0),2,cv2.LINE_8)
        cv2.imshow("ekrasn",Frame)

    if cv2.waitKey(23) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()

