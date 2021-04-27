# Na proizvodnoj liniji kamera slika tiskane pločice. Na navedenim pločicama kontrolira se kvaliteta lema komponenti. Zbog problema s analogno digitalnom pretvorbom došlo je do šuma na slici. Iz naveden slike potrebno je dobiti rubove prikazane primjerom kako bi se obavila daljina kontrola lema.

import cv2 as cv
from os.path import dirname

image = cv.imread(cv.samples.findFile(dirname(__file__) + "/circuitboard-saltandpep.tif"))
circuitBoard = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.namedWindow('Circuit board edges')

img_blur = cv.blur(circuitBoard, (3,3))
detected_edges = cv.Canny(img_blur, 100, 100, 5)
mask = detected_edges != 0
dst = image * (mask[:,:,None].astype(image.dtype))

cv.imshow('Circuit board edges', dst)
cv.waitKey()