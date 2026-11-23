"""mobius.py — W1–W2, ssec:two-sides: la inversa de la estructura, sum_{n<=y} mu(n) chi_5(n).
1/L(s,chi_5) = sum mu(n)chi_5(n) n^{-s} (chi_5 completamente multiplicativo, prop:multiplicative-side (i)).
El enunciado abierto F1PaperTorus.InverseStructureBound es M(y) = O(y^{1/2+eps}); aqui se mide
max |M(y)|/sqrt(y) hasta 3*10^7, en todo el rango y a partir de varios y0.
El articulo: medido <= 1.23 sqrt(y) hasta 3*10^7.
Uso: python3 -I mobius.py [Y]"""
import numpy as np, sys
Y = int(float(sys.argv[1])) if len(sys.argv) > 1 else 3*10**7
mu = np.ones(Y + 1, dtype=np.int8); mu[0] = 0
isp = np.ones(Y + 1, bool); isp[:2] = False
for p in range(2, int(Y**.5) + 1):
    if isp[p]: isp[p*p::p] = False
for p in np.nonzero(isp)[0]:
    mu[p::p] *= -1
    if p*p <= Y: mu[p*p::p*p] = 0
n = np.arange(Y + 1)
c5 = np.array([0, 1, -1, -1, 1], dtype=np.int8)[n % 5]
M = np.cumsum(mu.astype(np.int64) * c5)
r = np.abs(M[1:]) / np.sqrt(n[1:])
for y0 in (1, 10, 100, 1000, 10**4, 10**5, 10**6):
    k = np.argmax(r[y0-1:]) + y0
    print(f"y >= {y0:>7}: max |M(y)|/sqrt(y) = {r[k-1]:.4f}  en y = {k}  (M = {M[k]})")
print(f"M({Y}) = {M[Y]};  articulo: <= 1.23 sqrt(y) hasta 3*10^7")
