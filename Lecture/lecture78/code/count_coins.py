from skimage import io, color, measure
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
import numpy as np

def pre_process():
    global ima, ima_binary
    ima = color.rgba2rgb(ima)
    ima[:, :, 0] = 0
    ima = color.rgb2gray(ima)
    ima_binary = ima > 0.30
    ima_binary[0:150, 500:] = 0
    ima_binary[:20] = 0
    ima_binary[390:] = 0
    ima_binary[:, :20] = 0
    ima_binary[:, 560:] = 0

if __name__ == '__main__':
    ima = io.imread('coins.png')
    # 预处理
    pre_process()

    plt.imshow(ima_binary, cmap='gray')
    plt.show()

    # 膨胀
    se1 = np.ones((13,13))
    ima_binary = ndi.binary_dilation(ima_binary, se1)
    plt.imshow(ima_binary, cmap='gray')
    plt.show()

    # 腐蚀
    se2 = np.ones((61,61))
    ima_binary = ndi.binary_erosion(ima_binary, se2)
    plt.imshow(ima_binary, cmap='gray')
    plt.show()

    # 连通区域统计
    _, num = measure.label(ima_binary, return_num=True)
    print(f'The number of coins is {num}')