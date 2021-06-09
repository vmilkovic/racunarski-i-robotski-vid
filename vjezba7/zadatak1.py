# Napišite program koji će na slici detektirati lice i oči. Preuzmite sliku s licem i primijenite Viola & Jones algoritam baziran radu: link na rad. Za pomoć koristite  dokumentaciju OpenCV: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html.
import cv2 as cv

face_cascade = cv.CascadeClassifier(
    "./vjezba7/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier('./vjezba7/haarcascade_eye.xml')

capture = cv.VideoCapture(0)
if not capture.isOpened:
    print('Unable to open camera')
    exit(0)

while True:
    ret, frame = capture.read()
    if frame is None:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey),
                         (ex + ew, ey + eh), (0, 255, 0), 2)

    cv.imshow('Frame', frame)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
