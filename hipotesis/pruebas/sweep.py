"""sweep.py — W4–W5, ssec:weil-closure y prop:eight-classes: la cota (W4) en las ocho clases, barrida.
Para cada uno de los ocho caracteres chi_4^a psi_5^b de (Z/20)^* (primitivos; psi_5(2) = i; el trivial es zeta con
su polo), cada ancho a en {0.1, 0.2, 0.3, 0.5, 0.8, 1.2}, cada primo p en {2, 3, 7, 11, 13} y cada k >= 1 con
k log p + 2a <= 14.2 (primos bajo e^14.2): la orbita t_k = W(g_a, tau_{k log p} g_a) (forma de Weil bilineal de
L(s,chi), g_a el triangulo de semiancho a; ver zeroside.py), con t_{-k} = conj(t_k).
Se miden max_k |t_k|/t_0 y el menor autovalor de la matriz de Toeplitz (t_{j-k})_{j,k=0..K} relativo a t_0.
El articulo: 2208 valores; la cota vale en todos, con max|t_k|/t_0 entre 0.929 (zeta) y 0.986 (psi_5, psi_5^3);
toda matriz de Toeplitz definida positiva, con menor autovalor >= 1.27e-4 t_0.
Uso: python3 -I sweep.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, functools
from comun_pruebas import potencias, ocho_caracteres, A_tri, arch_desplazada, orbita
import comun_pruebas as C
n, p, k = potencias(int(math.exp(14.2)) + 1)
pp = (n, np.log(p.astype(float))/np.sqrt(n.astype(float)), np.log(n.astype(float)))
_ad = C.arch_desplazada
@functools.lru_cache(maxsize=None)
def arch_base(a, s, par): return _ad(a, s, 1, par)
C.arch_desplazada = lambda a, s, q, par: arch_base(a, s, par) + float(A_tri(-s, a))*math.log(q)
anchos = (0.1, 0.2, 0.3, 0.5, 0.8, 1.2); primos = (2, 3, 7, 11, 13)
res = {}; nval = 0; peor_eig = (1e9, None)
for nm, chi, q, par in ocho_caracteres():
    mx = 0
    for a in anchos:
        for p0 in primos:
            K = int((14.2 - 2*a)/math.log(p0))
            t = np.array([orbita(a, kk*math.log(p0), chi, q, par, pp) for kk in range(K + 1)])
            nval += K
            r = np.abs(t[1:])/t[0].real
            mx = max(mx, r.max())
            T = np.array([[t[j - i] if j >= i else np.conj(t[i - j]) for j in range(K + 1)] for i in range(K + 1)])
            e = np.linalg.eigvalsh(T)[0]/t[0].real
            if e < peor_eig[0]: peor_eig = (e, (nm, a, p0))
    res[nm] = mx
    print(f"{nm:14s}: max_k |t_k|/t_0 = {mx:.4f}")
print(f"valores de la orbita (k >= 1): {nval};  max|t_k|/t_0 entre {min(res.values()):.3f} ({min(res, key=res.get)}) y "
      f"{max(res.values()):.3f} ({max(res, key=res.get)})")
print(f"menor autovalor de Toeplitz / t_0: {peor_eig[0]:.3e} en {peor_eig[1]}  ({'todas definidas positivas' if peor_eig[0] > 0 else 'NO'})")
print("articulo: 2208 valores; entre 0.929 (zeta) y 0.986 (psi_5, psi_5^3); menor autovalor >= 1.27e-4 t_0")
