# Preuzeti sliku s interneta po želji
# Otvoriti je pomoću cv2.imread(putanja do slike)
# Prikazati je na zaslonu cv2.imshow(“Naslov”, slika)
# Ostaviti prozor otvorenim cv2.waitkey(0)
# Koristeći .shape[] ispisati osnovne numeričke informacije o slici (visina, širina, broj kanala, broj elemenata)
# Izračunajte koliko točno elemenata ima u cijeloj slici

import cv2 as cv
import sys
from os.path import dirname

slika = cv.imread(cv.samples.findFile(dirname(__file__) + "/python.jpg"))

if slika is None:
    sys.exit("Could not read the image.")

cv.imshow("Naslov", slika)
cv.waitKey(0)

print("Visina={}, Širina={}, Broj kanala={}, Broj elemenata={}".format(*slika.shape, slika.shape[0] * slika.shape[1]))
print("Ukupan broj elemenata=%d" % slika.size)
