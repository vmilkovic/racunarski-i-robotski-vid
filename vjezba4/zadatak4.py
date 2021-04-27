# Za danu sliku napišite program koji će detektirati liniju na slici. Pritom se koristite Hough transform algoritmom za detekciju linija. Pomoć: https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html

import cv2 as cv
import math
import numpy as np
from os.path import dirname

cv.namedWindow("Hough transform", cv.WINDOW_FREERATIO)
floorImg = cv.imread(cv.samples.findFile(dirname(__file__) + "/floor.jpg"),  cv.IMREAD_GRAYSCALE)
canny = cv.Canny(floorImg, 100, 200, L2gradient=True)
lines = cv.HoughLines(canny, 1, np.pi / 180, 250)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(floorImg, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

h = np.hstack([floorImg, canny])
cv.imshow("Hough transform", h)
cv.waitKey()