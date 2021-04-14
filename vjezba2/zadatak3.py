# Napisati program koji izrezati dio slike i kopirati ga na određenu poziciju.

import cv2 as cv
from os.path import dirname

cv.namedWindow('Formula', cv.WINDOW_NORMAL)

image = cv.imread(cv.samples.findFile(dirname(__file__) + "/formula1.jpg"))

image_part =  image[300:400, 500:600]

image[100:200, 600:700] = image_part

cv.imshow('Formula', image)
cv.waitKey(0)