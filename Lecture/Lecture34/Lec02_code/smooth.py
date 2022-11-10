import numpy as np
from skimage import io
import matplotlib.pyplot as plt

im_ = io.imread('lenna512.bmp')

height, width = im_.shape

kernel = np.ones((3,3))
print(kernel)

im_padding = np.zeros((height + 2, width + 2))
im_padding[1:height+1, 1:width+1] = im_

im_smooth = np.zeros(im_.shape)
for i in range(height):
    for j in range(width):
        result = im_padding[i:i + 3, j:j + 3] * kernel
        im_smooth[i][j] = np.sum(result)/9

plt.imshow(im_smooth, cmap='gray')
plt.show()



