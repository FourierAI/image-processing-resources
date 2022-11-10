from skimage import io, metrics
import numpy as np
import math
import copy

im = io.imread('lenna512.bmp')

mu = 0
sigma = math.sqrt(10)

noise = np.random.normal(mu, sigma, im.shape)

im_noise = im + noise

psnr1 = metrics.peak_signal_noise_ratio(im, im_noise)
print(psnr1)


im_salt = copy.deepcopy(im)
ratio = 0.1
threshold = 0.5
heigh, width = im.shape
num = heigh*width
noise_num = int(num*0.1)

for i in range(noise_num):
    xi = np.random.randint(0, heigh)
    xj = np.random.randint(0, width)
    if np.random.random() < threshold:
        im_salt[xi, xj] = 255
    else:
        im_salt[xi, xj] = 0

psnr2 = metrics.peak_signal_noise_ratio(im, im_salt)
print(psnr2)

im_low = io.imread('im_low_dynamic_range.bmp')

psnr3 = metrics.peak_signal_noise_ratio(im, im_low)
print(psnr3)

import matplotlib.pyplot as plt

plt.hist(im.flatten(), bins=256, density=True)
plt.title('im')
plt.show()

plt.hist(im_noise.flatten(), bins=256, density=True)
plt.title('im_noise')
plt.show()

plt.hist(im_salt.flatten(), bins=256, density=True)
plt.title('im_salt')
plt.show()

plt.hist(im_low.flatten(), bins=256, density=True)
plt.title('im_low')
plt.show()

def add_noise(im):
    mu = 0
    sigma = math.sqrt(10)
    noise = np.random.normal(mu, sigma, im.shape)
    return im + noise

def average_im(k, im):
    sum = 0
    for i in range(k):
        sum += add_noise(im)
    return sum/k

im_10 = average_im(10, im[:])
im_100 = average_im(100, im[:])
im_1000 = average_im(1000, im[:])

print(metrics.peak_signal_noise_ratio(im, im_10),
    metrics.peak_signal_noise_ratio(im, im_100),
      metrics.peak_signal_noise_ratio(im,im_1000))

from skimage import exposure

im_enhance = exposure.equalize_hist(im_low)

plt.imshow(im_enhance, cmap='gray')
plt.show()
print(metrics.peak_signal_noise_ratio(im/255, im_enhance))