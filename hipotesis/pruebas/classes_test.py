"""classes_test.py — W4–W5, ssec:weil-closure: las ocho clases modulo 20 hacen falta en la correccion.
El operador corregido de law_resolution.py (S desde los primos hasta X = 500, peso de Fejer, n = 100..3000 de zeta).
Se quita de S, una por una, cada una de las ocho clases a de (Z/20)^* (las potencias p^k con p = a mod 20) y se mide
el error medio en espaciamientos.
El articulo: quitar cualquiera de las ocho empeora el error.
Uso: python3 -I classes_test.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from comun_pruebas import zeta_ceros, Einv, potencias, S_primos
tz = zeta_ceros(); N = np.arange(1, len(tz) + 1).astype(float)
s = (N >= 100) & (N <= 3000); nn = N[s]; g = tz[s]; sp = 2*np.pi/np.log(g/(2*np.pi))
X = 500; n, p, k = potencias(X); b = Einv(nn - 0.5, g)
err = lambda t: np.mean(np.abs(t - g)/sp)
e0 = err(Einv(nn - 0.5 - S_primos(b, X, n, p, k), b))
print(f"con las ocho clases: {e0:.4f}")
peor = True
for a in (1, 3, 7, 9, 11, 13, 17, 19):
    m = (p % 20) != a
    e = err(Einv(nn - 0.5 - S_primos(b, X, n[m], p[m], k[m]), b))
    peor &= e > e0
    print(f"  sin la clase {a:2d}: {e:.4f}  ({'peor' if e > e0 else 'NO peor'})")
print("quitar cualquiera empeora:", peor, "; articulo: si")
