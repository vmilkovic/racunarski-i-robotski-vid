# Za sliku iz priloga (checkerboard-noisy2.tif) napraviti detekciju ćoškova na slici. Na navedenoj slici označiti ćoškove. Mijenjati vrijednost slobodnog parametra k i threshold vrijednost odzivne funkcije R. Pomoć: link https://docs.opencv.org/4.5.2/dc/d0d/tutorial_py_features_harris.html

from os.path import dirname
import numpy as np
import cv2 as cv

filename = 'checkerboard-noisy2.tif'
img = cv.imread(cv.samples.findFile(dirname(__file__) + '/' + filename))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]

cv.imshow('Corners detect',img)
if cv.waitKey(0):
    cv.destroyAllWindows()