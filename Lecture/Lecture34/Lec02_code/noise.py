import numpy as np
from skimage import io

mu = 0
sigma = 50


im = io.imread('lenna512.bmp')
noise = np.random.normal(mu, sigma, im.shape)

import matplotlib.pyplot as plt

plt.imshow(noise, cmap='gray')
plt.show()

im_noise = im + noise
plt.imshow(im_noise, cmap='gray')
plt.show()

import matplotlib.pyplot as plt

plt.hist(im_noise.flatten(),bins=256,density=True)
plt.show()