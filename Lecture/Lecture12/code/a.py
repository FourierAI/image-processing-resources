import numpy as np
def PSNR(mse):
    mse = (255**2) / mse
    mse = np.log(mse) / np.log(10)
    mse = mse * 10
    return mse

def MSE(ri,ci):
    N = sum(ri.shape)
    return np.sum(np.square(ri - ci))/N

a = MSE(np.random.random((123,123,3)),np.random.random((123,123,3)))
print(a)