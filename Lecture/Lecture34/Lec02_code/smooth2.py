import numpy as np
from skimage import io
import matplotlib.pyplot as plt

im_ = io.imread('lenna512.bmp')

height, width = im_.shape

kernel = np.ones((7, 7))
print(kernel)

# O = I + 2* padding - F + 1

im_padding = np.zeros((height + 6, width + 6))
im_padding[1:height+1, 1:width+1] = im_

im_smooth = np.zeros(im_.shape)
for i in range(height):
    for j in range(width):
        result = im_padding[i:i + 7, j:j + 7] * kernel
        im_smooth[i][j] = np.sum(result)/49

plt.imshow(im_smooth, cmap='gray')
plt.show()



