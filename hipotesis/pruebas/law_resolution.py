"""law_resolution.py — W4–W5, ssec:weil-closure: lo que la ley tiene que dar.  (version d)
El operador corregido: t_n = E^{-1}(n - 1/2 - S(b_n)), b_n = E^{-1}(n - 1/2) la posicion estructural y
S(t) = -(1/pi) sum_(n<=X) (1 - log n/log X) sin(t log n)/(k sqrt n) sobre las potencias de primo n = p^k (peso de
Fejer), X = 500.  Error en espaciamientos 2pi/log(t/2pi), n = 100..3000, contra los ceros de zeta.
Cambio de la version d: se dan la MEDIANA y la media del error.  Las cifras de referencia del articulo
(0.20 sin correccion, 0.020 primo por primo) salen con la mediana; con la media no salen con ningun X ni peso.
La ley por ventanas: cada primo se cambia por su ventana de ancho delta en log p.  Tres formas:
  (R) rejilla fija [j delta, (j+1) delta), el primo en el promedio uniforme de su ventana: sin(t k c) sinc(t k delta/2);
  (C) ventana centrada en cada primo (solo el amortiguamiento): sin(t k log p) sinc(t k delta/2);
  (T) la rejilla de la torre, anchos log(phi)/(12*5^n), X = 300 (la del nodo NUM11 del corpus).
El articulo: 0.183 (delta = 1e-2), 0.087 (3e-3), 0.053 (1e-3), 0.028 (3e-4), 0.023 (1e-4); 0.20 sin correccion y
0.020 primo por primo.  NUM11: 0.209, 0.194, 0.150, 0.040, 0.030 (n = 0..4); primo a primo 0.030.
Uso: python3 -I law_resolution.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from comun_pruebas import zeta_ceros, Einv, potencias, S_primos
tz = zeta_ceros(); N = np.arange(1, len(tz) + 1).astype(float)
s = (N >= 100) & (N <= 3000); nn = N[s]; g = tz[s]; sp = 2*np.pi/np.log(g/(2*np.pi))
b = Einv(nn - 0.5, g)
med = lambda t: np.median(np.abs(t - g)/sp); mea = lambda t: np.mean(np.abs(t - g)/sp)
def S_vent(t, d, X, n, p, k, modo):
    lp = np.log(p.astype(float)); ln = np.log(n.astype(float))
    a = (1 - ln/math.log(X))/(k*np.sqrt(n.astype(float)))
    fase = k*(np.floor(lp/d) + 0.5)*d if modo == 'R' else ln
    return -((np.sin(np.outer(t, fase))*np.sinc(np.outer(t, k*d/2)/np.pi)) @ a)/np.pi
for X in (500, 300):
    n, p, k = potencias(X)
    tp = Einv(nn - 0.5 - S_primos(b, X, n, p, k), b)
    print(f"X = {X}: sin correccion mediana {med(b):.3f} (media {mea(b):.3f});  primo por primo mediana {med(tp):.3f} (media {mea(tp):.3f})")
n, p, k = potencias(500)
D = (1e-2, 3e-3, 1e-3, 3e-4, 1e-4)
for modo, nom in (('R', 'rejilla fija, promedio en la ventana'), ('C', 'ventana centrada en cada primo')):
    r = [Einv(nn - 0.5 - S_vent(b, d, 500, n, p, k, modo), b) for d in D]
    print(f"ley por ventanas ({nom}), X = 500:")
    print("   delta   " + "  ".join(f"{d:.0e}" for d in D))
    print("   mediana " + "  ".join(f"{med(t):.3f}" for t in r))
    print("   media   " + "  ".join(f"{mea(t):.3f}" for t in r))
n, p, k = potencias(300); phi = (1 + 5**.5)/2
r = [Einv(nn - 0.5 - S_vent(b, math.log(phi)/(12*5**m), 300, n, p, k, 'R'), b) for m in range(5)]
print("rejilla de la torre (NUM11), X = 300, n = 0..4:  mediana " + ", ".join(f"{med(t):.3f}" for t in r)
      + ";  media " + ", ".join(f"{mea(t):.3f}" for t in r))
print("articulo: 0.183, 0.087, 0.053, 0.028, 0.023; sin correccion 0.20; primo por primo 0.020")
print("NUM11:    0.209, 0.194, 0.150, 0.040, 0.030; primo a primo 0.030")
