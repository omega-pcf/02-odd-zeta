# Zero-side check of the window floor: Q(f) = sum over zeros (both signs) |f^(gamma)|^2
import numpy as np, sys
sys.argv=['x']
from opcert import phihat
z=np.array([float(x) for x in open('zeros.txt').read().split()])
g=np.concatenate([z,-z])
for L in [0.6,1.0,1.2,1.3]:
    for J in [20,40,80]:
        F=phihat(g,L,J)              # f^_j at +-gamma, sine basis orthonormal on interval of length L
        M=np.real(F.conj().T@F)
        print(f"L={L} J={J}: zero-side lambda_min (40 zeros, tail omitted) = {np.linalg.eigvalsh(M)[0]:.3e}")
