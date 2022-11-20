import scipy.io as scio
data = scio.loadmat('data_for_labC.mat')
eignfaces_blk = data['eignfaces_blk']

db = data["employees_DB"]
print(f"ID: {db[0][0][0]}")
print(f"weight: {db[0][0][1].shape}")