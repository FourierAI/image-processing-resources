import numpy as np
import matplotlib.pyplot as plt
from skimage import io

im_ = io.imread('lenna512.bmp')
im_fre = np.abs(np.fft.fft2(im_))

im_fre = np.log(1+im_fre)

plt.imshow(im_fre, cmap = 'gray')
plt.show()