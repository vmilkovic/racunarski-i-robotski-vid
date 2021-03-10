# Učitajte sliku pomoću prethodno spomenutih metoda i promijenite vrijednost piksela na 0.
# Navedeno napravite za piksele u redku: 100 i stupac: 100, 101 i 102. 
# Stvorite prozor za prikaz slike pomoću funkcije cv.namedWindow("Naslov", cv.WINDOW_FREERATIO) raširite sliku i vizualno pronađite 3 crna piksela. 

import cv2 as cv
import sys
from os.path import dirname

slika = cv.imread(cv.samples.findFile(dirname(__file__) + "/python.jpg"))

if slika is None:
    sys.exit("Could not read the image.")

black = [0, 0, 0]
slika[100, 100] = black
slika[100, 101] = black
slika[100, 102] = black

cv.namedWindow("Python", cv.WINDOW_FREERATIO)
cv.imshow("Python", slika)
cv.waitKey(0)