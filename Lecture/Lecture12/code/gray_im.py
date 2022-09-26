from skimage import io

im = io.imread('lenna512.bmp')

import matplotlib.pyplot as plt

plt.imshow(im, cmap='gray')
plt.show()

threshold = 100

im = im > threshold

plt.imshow(im, cmap='gray')
plt.show()