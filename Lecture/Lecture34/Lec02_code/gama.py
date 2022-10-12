from skimage import io
import matplotlib.pyplot as plt

image = io.imread('lenna512.bmp')/255
plt.imshow(image, cmap='gray')
plt.title('original')
plt.show()

image_gamma_2 = image**2
plt.imshow(image_gamma_2, cmap='gray')
plt.title('gamma=2')
plt.show()


image_gamma2_ = image**(1/2)
plt.imshow(image_gamma2_, cmap='gray')
plt.title('gamma=1/2')
plt.show()
