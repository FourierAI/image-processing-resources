from skimage import io, measure

image1 = io.imread('boundary_extr.png')
image2 = io.imread('lenna512.bmp')

image1_entropy = measure.shannon_entropy(image1)
image2_entropy = measure.shannon_entropy(image2)

print(f'image 1 entropy:{image1_entropy}, image 2 entropy:{image2_entropy}')
