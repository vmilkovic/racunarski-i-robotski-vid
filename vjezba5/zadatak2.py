#Nastavno na prethodni zadatak, pomoću biblioteke matplotlib prikažite odzivnu sliku funkcije za detekciju ćoškova. Pomoć: https://matplotlib.org/stable/tutorials/introductory/images.html

from os.path import dirname
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

filename = 'checkerboard-noisy2.tif'
img = mpimg.imread(dirname(__file__) + '/' + filename)
lum_img = img[:, :]
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()