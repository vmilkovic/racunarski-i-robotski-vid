# Napisati program koji će napraviti masku pravokutnika dimenzija 100 x 200 i iskoristiti ju za fokus na središte slike  slike po želji. Navedeno ostvarite korištenjem logičko "i" odnosno "AND". 

import numpy as np
import cv2 as cv
from os.path import dirname

image = cv.imread(cv.samples.findFile(dirname(__file__) + "/formula1.jpg"))

imageHeight = np.size(image, 0)
imageWidth = np.size(image, 1)

boxHeight = 100
boxWidth = 200

centerX = int((imageWidth / 2) - boxWidth / 2)
centerY = int((imageHeight / 2) - boxHeight / 2)

mask = np.zeros(image.shape[:2],np.uint8)
mask[centerY:centerY + boxHeight, centerX:centerX + boxWidth] = 255
result = cv.bitwise_and(image,image, mask=mask)

cv.imshow('Mask Applied to image', result)
cv.waitKey(0)