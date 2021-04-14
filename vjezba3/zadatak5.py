# Na monokromatskoj slici po želji primijenite binarno ograničenje (Thresholding), sa vrijednostima 50, 100, 200. Nakon toga primijenite adaptivno binarno ograničenje po želji i primijetite razlike.

import numpy as np
import cv2 as cv
from os.path import dirname

img = cv.imread(cv.samples.findFile(dirname(__file__) + "/city.jpg"), 0)

ret,binary50 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
ret,binary100 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
ret,binary200 = cv.threshold(img, 200, 255, cv.THRESH_BINARY)


titles = ['Original','Binary 50', 'Binary 100', 'Binary 200']

images = [img, binary50, binary100, binary200]

binaryCompare = np.hstack(images)

cv.imshow('Binary Thresholding', binaryCompare)
cv.waitKey()
