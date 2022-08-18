from skimage import io
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np

image = io.imread('boundary_extr.png', as_gray=True)
image = image > 0.4
image = image.astype('uint8')
plt.imshow(image, cmap='gray')
plt.show()

se = np.ones((5, 5))
image_di = ndi.binary_dilation(image, se)
boundary = image_di - image
plt.imshow(boundary, cmap='gray')
plt.show()

