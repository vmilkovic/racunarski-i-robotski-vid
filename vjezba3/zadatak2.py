# Za monokromatsku sliku po želji ( poželjno sliku ujednačenog intenziteta) primijenite medodu izjednačavanja histograma. Prikažite sliku  histogram prije i poslije izjednačavanja. Pomoć: https://docs.opencv.org/4.5.2/de/db2/tutorial_py_table_of_contents_histograms.html

import numpy as np
import cv2 as cv
from os.path import dirname

img = cv.imread(cv.samples.findFile(dirname(__file__) + "/city.jpg"), 0)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ))

cv.imwrite('./vjezba3/compare.png',res)

compare = cv.imread(cv.samples.findFile(dirname(__file__) + "/compare.png"), 0)

cv.imshow('Izjednačavanje slika', compare)
cv.waitKey()