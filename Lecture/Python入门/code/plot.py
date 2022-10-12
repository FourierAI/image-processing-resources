import matplotlib.pyplot as plt
from skimage import io

# 图像显示
im_color = io.imread('lenna512color.bmp')
plt.imshow(im_color)
plt.show()

im_gray = io.imread('lenna512.bmp')
plt.imshow(im_gray, cmap='gray')
plt.show()

# 子图显示
# plt.figure()
# plt.subplot(1,2,1)
# plt.title('color')
# plt.imshow(im_color)
#
# plt.subplot(1,2,2)
# plt.title('gray')
# plt.imshow(im_gray, cmap='gray')
#
# plt.savefig('test')
# plt.show()
