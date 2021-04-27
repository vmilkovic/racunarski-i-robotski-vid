# Za sliku po želji primijenite Canny edge detector. Više informacija na: https://docs.opencv.org/master/da/d22/tutorial_py_canny.html

import cv2 as cv
from os.path import dirname
from matplotlib import pyplot as plt

img = cv.imread(cv.samples.findFile(dirname(__file__) + "/floor.jpg"), 0)

edges = cv.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
