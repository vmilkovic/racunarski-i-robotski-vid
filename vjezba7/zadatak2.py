# Napišite program koji ostvaruje funkciju oduzimanja pozadine (engl. background substraction). Zadatak za doma, predavač će ga demonstrirati.
import cv2 as cv

backSubMOG = cv.createBackgroundSubtractorMOG2()

capture = cv.VideoCapture(0)
if not capture.isOpened:
    print('Unable to open camera')
    exit(0)

while True:
    ret, frame = capture.read()
    if frame is None:
        break
    fgMask = backSubMOG.apply(frame)

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
