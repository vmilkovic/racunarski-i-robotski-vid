# Uzmite monokromatsku sliku i analizirajte statističke podatke slike korištenjem histograma. Iz navedene slike generirajte histogram koji ćete prikazati pomoću biblioteke matplotlib. Pomoć: https://docs.opencv.org/4.5.2/de/db2/tutorial_py_table_of_contents_histograms.html

import cv2 as cv
from os.path import dirname
from matplotlib import pyplot as plt

img = cv.imread(cv.samples.findFile(dirname(__file__) + "/city.jpg"), 0)

fig, ax = plt.subplots()
fig.canvas.set_window_title('Histogram')

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('Histogram')
ax.legend()

plt.hist(img.ravel(),256,[0,256])

plt.show()