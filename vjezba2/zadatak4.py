# Napisati program koji će dodati i oduzeti vrijednost 10, 50,100 pojedinom pikselu RGB slike po želji. Slike prikazati i na zaslonu i primijetiti razlike. Potrebno je napisati program korištenjem OpenCV metode i Numpy operatora + i - .

import numpy as np
import cv2 as cv
from os.path import dirname

image = cv.imread(cv.samples.findFile(dirname(__file__) + "/formula1.jpg"))

MPlus10 = np.ones(image.shape, dtype='uint8') + 10
added10 = cv.add(image, MPlus10)
cv.imshow('CV Added 10', added10)

MPlus50 = np.ones(image.shape, dtype='uint8') + 50
added50 = cv.add(image, MPlus50)
cv.imshow('CV Added 50', added50)

MPlus100 = np.ones(image.shape, dtype='uint8') + 100
added100 = cv.add(image, MPlus100)
cv.imshow('CV Added 100', added100)

MMinus10 = np.ones(image.shape, dtype='uint8') - 10
substracted10 = cv.add(image, MMinus10)
cv.imshow('CV Substracted 10', substracted10)

MMinus50 = np.ones(image.shape, dtype='uint8') - 50
substracted50 = cv.add(image, MMinus50)
cv.imshow('CV Substracted 50', substracted50)

MMinus100 = np.ones(image.shape, dtype='uint8') - 100
substracted100 = cv.add(image, MMinus100)
cv.imshow('CV Substracted 100', substracted100)

npAdd10Image = image
npAdd10Image[:1, :1] = npAdd10Image[:1, :1] + np.uint8([10])
cv.imshow('NP Add 10', npAdd10Image)

npAdd50Image = image
npAdd50Image[:1, :1] = npAdd50Image[:1, :1] + np.uint8([50])
cv.imshow('NP Add 50', npAdd50Image)

npAdd100Image = image
npAdd100Image[:1, :1] = npAdd100Image[:1, :1] + np.uint8([100])
cv.imshow('NP Add 100', npAdd100Image)

npSubstract10Image = image
npSubstract10Image[:1, :1] = npSubstract10Image[:1, :1] - np.uint8([10])
cv.imshow('NP Substract 10', npSubstract10Image)

npSubstract50Image = image
npSubstract50Image[:1, :1] = npSubstract50Image[:1, :1] - np.uint8([50])
cv.imshow('NP Substract 50', npSubstract50Image)

npSubstract100Image = image
npSubstract100Image[:1, :1] = npSubstract100Image[:1, :1] - np.uint8([100])
cv.imshow('NP Substract 100', npSubstract100Image)

cv.waitKey(0)