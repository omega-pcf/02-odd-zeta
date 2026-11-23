"""corrected_operator.py — W4–W5, ssec:weil-closure y prop:positions: las posiciones, desde la estructura.
Para zeta: el operador de gonzalez25hp tiene autovalores T*(n) = c(n) pi n / log(mu n + sigma),
c(n) = 2 + alpha_0/(1 + beta_0 log n), alpha_0 = 59/40, beta_0 = 1/8, mu = 1/2, sigma = 3/2 (tstar.py); la envolvente
exacta E(t) = theta(t)/pi + 1 (sin primos ni ceros) da la posicion estructural E^{-1}(n - 1/2).  Los ceros
(zeta_zeros_3000.npy) solo miden: error en espaciamientos medios 2pi/log(t/2pi) y error relativo.
El articulo: error medio de T*(n) ~4.9 espaciamientos; con la envolvente exacta 0.20 espaciamientos, error relativo
de 3e-3 en altura baja a 5e-5 en n = 2000.  (Nota [N] de F1PaperTorus.OperatorRealization: en n = 1000 el error relativo de
T* es 0.64% y el de la envolvente exacta 0.007%.)
Version d: se da tambien la mediana del error de la envolvente (la medida con la que law_resolution.py
reproduce el 0.20).
Uso: python3 -I corrected_operator.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from comun_pruebas import zeta_ceros, Einv
tz = zeta_ceros(); N = np.arange(1, len(tz) + 1).astype(float)
a0, b0, mu, sg = 59/40, 1/8, 1/2, 3/2
Tst = lambda n: (2 + a0/(1 + b0*np.log(n)))*np.pi*n/np.log(mu*n + sg)
for lo, hi in ((1, 1000), (1, 2000), (100, 3000)):
    s = (N >= lo) & (N <= hi); n = N[s]; g = tz[s]; sp = 2*np.pi/np.log(g/(2*np.pi))
    eT = (Tst(n) - g)/sp; eE = (Einv(n - 0.5, g) - g)/sp
    print(f"n = {lo}..{hi}: T*: error medio {np.mean(np.abs(eT)):.2f} espaciamientos (con signo {np.mean(eT):+.2f});"
          f"  envolvente exacta: media {np.mean(np.abs(eE)):.3f}, mediana {np.median(np.abs(eE)):.3f} espaciamientos")
for m in (10, 50, 100, 500, 1000, 2000):
    g = tz[m - 1]; r = abs(Einv(np.array([m - 0.5]), np.array([g]))[0] - g)/g
    print(f"  error relativo de E^-1(n - 1/2) en n = {m}: {r:.1e}")
g = tz[999]
print(f"  en n = 1000: error relativo de T* {100*abs(Tst(1000.0) - g)/g:.2f}%, de la envolvente exacta {100*abs(Einv(np.array([999.5]), np.array([g]))[0] - g)/g:.4f}%  (nota: 0.64% y 0.007%)")
print("articulo: T* ~4.9 espaciamientos; envolvente 0.20; relativo 3e-3 (altura baja) a 5e-5 (n = 2000)")
