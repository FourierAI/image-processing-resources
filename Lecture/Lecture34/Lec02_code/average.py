# load image
from skimage import io
import matplotlib.pyplot as plt

image = io.imread('lenna512.bmp')
len_, width_ = image.shape

# plt.imshow(image, cmap='gray')
# plt.show()

# generate noise image
import numpy as np

mu = 0
sigma = 200

noise_image = np.random.normal(mu, sigma, (len_, width_))

# plt.imshow(noise_image, cmap='gray')
# plt.show()

# add noise
# new_image = image+noise_image
# plt.imshow(new_image, cmap='gray')
# plt.show()


# reconstruction
K=300
recover_sum = 0
for i in range(K):
    noise_image = np.random.normal(mu, sigma, (len_, width_))
    new_image = image+noise_image
    recover_sum = recover_sum + new_image
    if (i+1) % 50 == 0:
        re_image = recover_sum/(i+1)
        plt.imshow(re_image, cmap='gray')
        plt.title(i+1)
        plt.show()
