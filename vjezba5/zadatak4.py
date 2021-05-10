# Za sliku iz priloga (target.jpg) izračunajte  i prikažite sve SIFT značajke na slici. Pomoć:
from os.path import dirname
import numpy as np
import cv2 as cv

filename = 'target.jpg'
img = cv.imread(dirname(__file__) + '/' + filename)
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite(dirname(__file__) + '/' + 'target_keypoints.jpg',img)