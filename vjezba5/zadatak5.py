# Otvoriti video ulaz i pomoću video ulaza napraviti kalibraciju kamere. Zadatak za doma. -> Nedovršena kalibracija -> Camera Calibration with Python – OpenCV
import cv2
from os.path import dirname

cap = cv2.VideoCapture(0)
ret,frame = cap.read()

while(True):
    cv2.imshow('Camera capture',frame)
    if cv2.waitKey(0) & 0xFF == ord('y'):
        cv2.imwrite(dirname(__file__) + '/camera_capture.png',frame)
        cv2.destroyAllWindows()
        break

cap.release()