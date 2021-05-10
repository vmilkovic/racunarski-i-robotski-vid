# Nastavno na prethodni zadatak, za značajke slike (target) izračunajte podudaranje značajki između objekta kojega tražimo i ostalih slika koje su dane. Vizualno pronađite najbolju sliku, na kojoj je najviše značajka prepoznatoga objekta. 

from os.path import dirname
import numpy as np
import cv2
from matplotlib import pyplot as plt

def target_detection(imageName, outputImage):
    target = cv2.imread(dirname(__file__) + '/' + 'target.jpg', 0)
    image = cv2.imread(dirname(__file__) + '/' + imageName, 0)
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(target, None)
    kp2, des2 = sift.detectAndCompute(image, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])

    keypointsImage = cv2.drawMatchesKnn(target, kp1, image, kp2, good, outImg=True, flags=2)
    plt.imshow(keypointsImage), plt.show()
    cv2.imwrite(dirname(__file__) + '/' + outputImage, keypointsImage)

target_detection('IMG_1046.jpg', 'IMG_1046_keypoints.jpg')
target_detection('IMG_1047.jpg', 'IMG_1047_keypoints.jpg')
target_detection('IMG_1049.jpg', 'IMG_1049_keypoints.jpg')
target_detection('IMG_1050.jpg', 'IMG_1050_keypoints.jpg')
target_detection('IMG_1052.jpg', 'IMG_1052_keypoints.jpg')
target_detection('IMG_1054.jpg', 'IMG_1054_keypoints.jpg')