import matplotlib.pyplot as plt
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
image = io.imread('lenna512.bmp')
image = image/255

# 纵向边缘检测
kernel_h = np.array([-1, 0, 1])

m, n = image.shape
image_h = np.zeros((m, n))

for i in range(n):
    for j in range(1,m-1):
        image_h[i][j] = np.sum(image[i, j - 1:j + 2] * kernel_h)

# 负梯度也是边缘信息，所以需要保留
image_h = abs(image_h)

theshold = 0.1
# image_h = image_h > theshold
plt.imshow(image_h, cmap='gray')
plt.title('vertical')
plt.show()

# 横向边缘检测
kernel_v = kernel_h.reshape(-1, 1)

image_v = np.zeros((m, n))

for i in range(1, n-1):
    for j in range(m):
        image_v[i][j] = np.sum(image[i-1:i+2, j].reshape(-1, 1)*kernel_v)

image_v = abs(image_v)
# image_v = image_v > theshold

plt.imshow(image_v, cmap='gray')
plt.title('horizontal')
plt.show()

print(image_h.shape)
print(image_v.shape)