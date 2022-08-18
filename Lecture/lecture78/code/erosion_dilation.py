from skimage import morphology
import numpy as np
from scipy import ndimage as ndi


se = np.ones((3,3)).astype('uint8')
f = np.array([[0,1,1,1,1,0,0,0],
              [0,1,1,1,1,0,0,0],
              [0,0,1,1,1,0,0,0],
              [0,1,0,1,0,0,0,0],
              [0,1,1,1,1,1,1,0],
              [0,1,1,0,0,0,1,0],
              [0,1,1,1,1,1,1,0],
              [1,1,1,1,1,1,1,0]])

# out = morphology.erosion(f, se)
# out = ndi.binary_erosion(f, se, border_value=0).astype('uint8')
out = ndi.binary_dilation(f, se, border_value=0).astype('uint8')
print(out)
