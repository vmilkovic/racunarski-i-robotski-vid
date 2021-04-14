# Otvoriti sliku po želji i napisati program koji mijenja vrijednost 50 redaka i stupaca u svim ćoškovima i samom centru slike u crnu boju. 

import cv2 as cv
from os.path import dirname

cv.namedWindow('Formula', cv.WINDOW_NORMAL)

image = cv.imread(cv.samples.findFile(dirname(__file__) + "/formula1.jpg"))

image[:50, :50] = (0, 0, 0)
image[:50, -50:] = (0, 0, 0)
image[-50:, :50] = (0, 0, 0)
image[-50:, -50:] = (0, 0, 0)

cv.imshow('Formula', image)
cv.waitKey(0)