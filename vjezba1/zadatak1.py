# Napraviti 5 x 5 NumPy matricu
# Ispisati sve osnovne informacije o matrici (dimenzije, vrijednosti, oblik, tip podatka, ukupno zauzeće memorije)
# Korisne info: https://numpy.org/devdocs/user/quickstart.html

import numpy as np

arr = np.arange(25).reshape(5, 5)

for i in [arr, arr.shape, arr.itemsize, arr.dtype.name, arr.size, type(arr)]:
    print(i)
