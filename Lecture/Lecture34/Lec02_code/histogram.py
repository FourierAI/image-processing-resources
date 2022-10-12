import matplotlib.pyplot as plt
from skimage import io
image = io.imread('lenna512.bmp')
image_ = image.flatten()
plt.hist(image_, bins=256)
plt.show()

# normalized
# plt.hist(image_, bins=256, density=True)
# plt.show()