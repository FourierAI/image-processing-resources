import scipy.io as scio
data = scio.loadmat('data_for_labC.mat')
eignfaces_blk = data['eignfaces_blk']
employees_DB = data['employees_DB']
print(eignfaces_blk)