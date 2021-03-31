# Napisati program koji mijenja vrijednost jednog retka i stupca po želji u zelenu boju

import cv2 as cv
from os.path import dirname

cv.namedWindow('Formula', cv.WINDOW_NORMAL)

image = cv.imread(cv.samples.findFile(dirname(__file__) + "/formula1.jpg"))

image[50, 0:] = (0, 255, 0)
image[0:, 50] = (0, 255, 0)

cv.imshow('Formula', image)
cv.waitKey(0)