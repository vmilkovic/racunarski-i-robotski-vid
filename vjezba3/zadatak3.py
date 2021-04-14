# Za sliku po želji napravite sve vrste rubova na  slici i pokažite ih na zaslonu. 
# Reflect, Replicate, Wrap, Constant

import cv2 as cv
from os.path import dirname

img = cv.imread(cv.samples.findFile(dirname(__file__) + "/city.jpg"), 0)

CONSTANT = cv.copyMakeBorder(img, 30, 30, 30, 30, cv.BORDER_CONSTANT, (0, 0, 0))
WRAP = cv.copyMakeBorder(img, 30, 30, 30, 30, cv.BORDER_WRAP)
REPLICATE = cv.copyMakeBorder(img, 30 , 30, 30, 30, cv.BORDER_REPLICATE)
REFLECT = cv.copyMakeBorder(img, 30, 30, 30, 30, cv.BORDER_REFLECT)

cv.imshow('REFLECT', REFLECT)
cv.imshow('REPLICATE', REPLICATE)
cv.imshow('WRAP', WRAP)
cv.imshow('CONSTANT', CONSTANT)
cv.waitKey()
