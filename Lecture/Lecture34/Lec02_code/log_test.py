import numpy as np
import matplotlib.pyplot as plt

shape = (512, 512)
im_ = np.random.random(shape) / 1000

im_ = np.log(im_)

im_ = im_.astype('int')

plt.imshow(im_, cmap = 'gray')
plt.show()