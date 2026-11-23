"""circle_and_detect.py — W4–W5, ssec:weil-closure: la densidad de Fejer en el circulo de p = 3, y lo que el
barrido puede detectar.
1. Densidad de Fejer de la orbita de p = 3 en cada uno de los ocho bloques (sweep.py), con el ancho a = 0.3 de
   zeroside.py:  F(theta) = sum_{|k|<=K} (1 - |k|/(K+1)) t_k e^{i k theta},  K maximo con K log 3 + 2a <= 14.2;
   su minimo sobre theta.
2. Deteccion: el cero de L(s,chi_5) mas cercano a la altura gamma se desplaza a Re rho = 1/2 + delta: en la orbita de
   chi_5 se quita su par +-gamma_0 (2 ghat_a(gamma_0)^2 cos(s gamma_0)) y se pone el cuadruple +-gamma_0 +- i delta
   (sum_z ghat_a(z)^2 e^{i s z}, s = k log p); se busca el menor delta en (0, 1/2) que vuelve indefinida alguna
   matriz de Toeplitz del barrido (anchos y primos de sweep.py).
El articulo: densidad positiva en los ocho bloques, minimos de 1.2e-4 (zeta) a 0.032 (chi_20); un cero detectado
desde delta >= 0.001 en gamma = 30, 0.057 en gamma = 100, 0.31 en gamma = 200; sobre gamma ~ 300 ninguno.
Version d: 3. la deteccion con orbitas mas largas que las del barrido (k log p <= s_max), desde el lado de los
ceros (397 ceros de chi_5 hasta 500), que con s_max = 14.2 da la misma Toeplitz que el lado de los primos.  Lo
unico que cambia el delta detectado es la longitud de la orbita.
Uso: python3 -I circle_and_detect.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, functools, cmath
from comun_pruebas import potencias, ocho_caracteres, A_tri, orbita, CHI5
import comun_pruebas as C
n, p, k = potencias(int(math.exp(14.2)) + 1)
pp = (n, np.log(p.astype(float))/np.sqrt(n.astype(float)), np.log(n.astype(float)))
_ad = C.arch_desplazada
@functools.lru_cache(maxsize=None)
def arch_base(a, s, par): return _ad(a, s, 1, par)
C.arch_desplazada = lambda a, s, q, par: arch_base(a, s, par) + float(A_tri(-s, a))*math.log(q)
anchos = (0.1, 0.2, 0.3, 0.5, 0.8, 1.2); primos = (2, 3, 7, 11, 13)
th = np.linspace(0, 2*np.pi, 4001)
print("1. densidad de Fejer en el circulo de p = 3, a = 0.3 (minimo sobre theta):")
a = 0.3; K = int((14.2 - 2*a)/math.log(3)); mins = {}
for nm, chi, q, par in ocho_caracteres():
    t = np.array([orbita(a, kk*math.log(3), chi, q, par, pp) for kk in range(K + 1)])
    F = t[0].real + 2*sum((1 - kk/(K + 1))*(t[kk]*np.exp(1j*kk*th)).real for kk in range(1, K + 1))
    mins[nm] = F.min()
    print(f"   {nm:14s}: minimo {F.min():.3e}")
print(f"   todas positivas: {min(mins.values()) > 0}; de {min(mins.values()):.1e} ({min(mins, key=mins.get)}) a "
      f"{max(mins.values()):.3f} ({max(mins, key=mins.get)})")
# 2. deteccion en el bloque de chi_5
chi5 = [x for x in ocho_caracteres() if x[0] == 'chi_5'][0]
base = {}
for a in anchos:
    for p0 in primos:
        K = int((14.2 - 2*a)/math.log(p0))
        base[(a, p0)] = np.array([orbita(a, kk*math.log(p0), chi5[1], 5, 0, pp) for kk in range(K + 1)])
def ghat(z, a): return a*(cmath.sin(a*z/2)/(a*z/2))**2
from comun_pruebas import ceros_chi5
ceros = ceros_chi5()
def indefinida(gam, d):
    for (a, p0), t in base.items():
        K = len(t) - 1
        tt = t.copy()
        for kk in range(K + 1):
            s = kk*math.log(p0)
            tt[kk] -= 2*ghat(gam, a).real**2*math.cos(s*gam)
            tt[kk] += sum(ghat(z, a)**2*cmath.exp(1j*s*z) for z in (complex(gam, -d), complex(gam, d), complex(-gam, -d), complex(-gam, d)))
        T = np.array([[tt[j - i] if j >= i else np.conj(tt[i - j]) for j in range(K + 1)] for i in range(K + 1)])
        if np.linalg.eigvalsh(T)[0] < 0: return True
    return False
print("2. menor delta detectado (alguna Toeplitz del barrido indefinida):")
for g0 in (30, 100, 200, 300, 400):
    gam = float(ceros[np.argmin(np.abs(ceros - g0))])
    ds = np.concatenate([np.arange(0.0005, 0.01, 0.0005), np.arange(0.01, 0.5, 0.001)])
    hit = next((d for d in ds if indefinida(gam, d)), None)
    print(f"   gamma ~ {g0} (cero en {gam:.3f}): " + (f"delta >= {hit:.4f}" if hit is not None else "ninguno con delta < 1/2"))
print("articulo: minimos de 1.2e-4 (zeta) a 0.032 (chi_20); delta >= 0.001 (30), 0.057 (100), 0.31 (200); ninguno sobre ~300")

# 3. version d: longitud de la orbita, lado de los ceros
import json
Z = np.array(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chi5_zeros_500.json'))))
gh = lambda z, a: a*np.sinc(a*np.asarray(z)/(2*np.pi))**2
def mineig(tt):
    K = len(tt) - 1; ix = np.arange(K + 1); D = ix[None, :] - ix[:, None]
    return np.linalg.eigvalsh(np.where(D >= 0, tt[np.abs(D)], np.conj(tt[np.abs(D)])))[0]
def det_largo(g0, smax, ds):
    i = np.argmin(np.abs(Z - g0)); gam = Z[i]; rest = np.delete(Z, i); pre = []
    for a in anchos:
        for p0 in primos:
            K = int((smax - 2*a)/math.log(p0)); sk = np.arange(K + 1)*math.log(p0)
            pre.append((a, sk, (2*np.cos(np.outer(sk, rest)) @ (gh(rest, a)**2)).astype(complex)))
    for d in ds:
        for a, sk, t in pre:
            q = sum(ghat(z, a)**2*np.exp(1j*sk*z) for z in (complex(gam, -d), complex(gam, d), complex(-gam, -d), complex(-gam, d)))
            if mineig(t + q) < 0: return d
    return None
ds = np.concatenate([np.arange(0.001, 0.01, 0.001), np.arange(0.01, 0.5, 0.003)])
print("3. lado de los ceros: menor delta detectado segun la longitud de la orbita s_max:")
for smax in (14.2, 25, 60, 120):
    r = [det_largo(g0, smax, ds) for g0 in (30, 100, 200, 300)]
    print(f"   s_max = {smax:5}: " + ", ".join(f"gamma~{g0}: " + (f"{d:.3f}" if d is not None else "ninguno") for g0, d in zip((30, 100, 200, 300), r)))
print("articulo: 0.001 (30), 0.057 (100), 0.31 (200), ninguno sobre ~300")
