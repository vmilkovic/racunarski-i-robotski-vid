# Za monokromatsku sliku po želi primijenite usrednjavanje običnim i gaussovim filterom. Pritom mijenjajte vrijednost veličine jezgre i primijetite što se događa. 

import numpy as np
import cv2 as cv
from os.path import dirname

cv.namedWindow('Gauss filter', cv.WINDOW_FREERATIO)

img = cv.imread(cv.samples.findFile(dirname(__file__) + "/city.jpg"), 0)

blurred = np.hstack([
    cv.blur(img, (3, 3), cv.BORDER_REPLICATE),
    cv.blur(img, (5, 5), cv.BORDER_REPLICATE),
    cv.blur(img, (11, 11), cv.BORDER_REPLICATE)
])

cv.imshow('Gauss filter', blurred)
cv.waitKey()
