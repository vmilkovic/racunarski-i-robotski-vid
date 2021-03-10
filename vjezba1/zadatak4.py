# Preuzeti sliku s interneta po želji
# Otvoriti je pomoću cv2.imread(putanja do slike)
# Spremiti je pomoću cv2.imwrite("novaslika.format(.jpg.png)", slika)
# Pročitati kratki OpenCV tutorial: https://docs.opencv.org/4.5.1/db/deb/tutorial_display_image.html

import cv2 as cv
import sys
from os.path import dirname

slika = cv.imread(cv.samples.findFile(dirname(__file__) + "/python.jpg"))

if slika is None:
    sys.exit("Could not read the image.")

cv.imwrite("./vjezba1/createdPython.jpg", slika)
