import scipy.io as scio
data = scio.loadmat('data_for_labC.mat')
eignfaces_blk = data['eignfaces_blk']
db = data["employees_DB"]

for i in range(len(db)):
    print(db[i])