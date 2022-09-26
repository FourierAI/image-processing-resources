from skimage import io, color
import matplotlib.pyplot as plt
import numpy as np

im_color = io.imread('lenna512color.bmp')
im_gray = io.imread('lenna512.bmp')

print(im_color.shape)
print(im_gray.shape)

# image 的灰度范围 0-255 或者 0-1

# im_gray = im_gray / 255
# print(im_gray)
# plt.imshow(im_gray, cmap='gray')
# plt.show()
#
# im_gray = (im_gray * 255).astype('int')
# print(im_gray)
# plt.imshow(im_gray, cmap='gray')
# plt.show()

# 读取彩色图像通道
# im_red = im_color[:,:,0]
# im_green = im_color[:,:,1]
# im_blue = im_color[:,:,2]
#
# plt.figure()
# plt.subplot(1,3,1)
# plt.imshow(im_red, cmap='gray')
# plt.subplot(1,3,2)
# plt.imshow(im_green, cmap='gray')
# plt.subplot(1,3,3)
# plt.imshow(im_blue, cmap='gray')
# plt.show()

# 图像的下采样 1/2
im_gray = im_gray / 255
length, width = im_gray.shape
length_down, width_down = length // 2, width // 2
im_down = np.zeros((length_down, width_down))

for i in range(length_down):
    for j in range(width_down):
        im_down[i][j] = np.mean(im_gray[2*i:2*i+2, 2*j:2*j+2])

plt.imshow(im_down, cmap='gray')
plt.show()
print(im_down.shape)