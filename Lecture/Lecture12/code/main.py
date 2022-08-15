import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np

image = io.imread('lenna512.bmp')

image_x_len, image_y_len = image.shape

plt.imshow(image,cmap='gray', vmin=0, vmax=255)
plt.show()

from mpl_toolkits.mplot3d import Axes3D

#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')


xx = np.arange(0, image_x_len, 1)
yy = np.arange(0, image_y_len, 1)

X, Y = np.meshgrid(xx, yy)

Z = image

ax1.plot_surface(X,Y,Z,cmap='rainbow')
#ax3.contour(X,Y,Z, zdim='z',offset=-2，cmap='rainbow)   #等高线图，要设置offset，为Z的最小值
plt.show()