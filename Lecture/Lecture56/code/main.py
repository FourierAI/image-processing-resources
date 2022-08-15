import numpy as np
N = 16
bases = []
for k in range(N):
    basis = []
    for n in range(N):
        value = np.e**(1j*2*np.pi*n*k/N)
        basis.append(value)
    bases.append(basis)
bases = np.array(bases)
vec1 = bases[3]
vec2 = bases[2]
inner_pro = vec1.dot(vec2.conjugate())
print(inner_pro)