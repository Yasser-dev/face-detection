import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)
while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4,)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
        cv2.putText(img, '"FACE"', (int(x+(w/4)), y+h+35),
                    cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 3)
    cv2.imshow('Face Detection', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
