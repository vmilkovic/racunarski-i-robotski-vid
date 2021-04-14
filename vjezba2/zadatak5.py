# Prema uputama i primjeru s dokumentacije OpenCV(https://docs.opencv.org/4.5.1/d0/d86/tutorial_py_image_arithmetics.html) ostvarite stapanje slika pomoću funkcije addWeighted

import cv2 as cv
from os.path import dirname

img1 = cv.imread(cv.samples.findFile(dirname(__file__) + '/LinuxLogo.jpg'))
img2 = cv.imread(cv.samples.findFile(dirname(__file__) + '/WindowsLogo.jpg'))

alpha = 0.5
beta = (1.0 - alpha)

blend = cv.addWeighted(img1, alpha, img2, beta, 0.0)

cv.imshow('Blending', blend)
cv.waitKey(0)
cv.destroyAllWindows()