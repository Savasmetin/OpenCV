import cv2

kamera = cv2.VideoCapture(0)

def coz_1080():
    kamera.set(3,1920)
    kamera.set(4,1080)

def coz_480():
    kamera.set(3,640)
    kamera.set(4,480)

def scalalama(frame, percent = 75):
    witdh = int(frame.shape[1]* percent/100)
    height = int(frame.shape[0] * percent / 100)
    boyut = (witdh,height)
    return cv2.resize(frame, boyut, interpolation=cv2.INTER_AREA)


while True:
    ret, frame = kamera.read()
    Frame = scalalama(frame,75)
    cv2.imshow("göruntu",frame)
    cv2.imshow("görunnntu", Frame)
    if cv2.waitKey(1) &  0xFF == ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()
