import copy
from skimage import io

im = io.imread('lenna512color.bmp')
print(im)


import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.imshow(im)


im_red = copy.copy(im)
im_red[:,:,1:3] = 0

plt.subplot(2,2,2)
plt.imshow(im_red)

im_green = copy.copy(im)
im_green[:,:,0] = 0
im_green[:,:,2] = 0

plt.subplot(2,2,3)
plt.imshow(im_green)

im_blue = copy.copy(im)
im_blue[:,:,0:2] = 0

plt.subplot(2,2,4)
plt.imshow(im_blue)
plt.show()