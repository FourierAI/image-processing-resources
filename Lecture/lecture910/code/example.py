from skimage import measure
import numpy as np

im = np.array([
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,7,1,1,1,1,0,0],
    [0,7,5,5,5,5,2,2],
    [0,7,0,0,0,0,2,2],
    [0,7,2,2,2,2,2,2],
    [0,0,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0]
])

entr = measure.shannon_entropy(im)
print(entr)