"""dedekind.py — W3, ssec:field-positivity: la suma de Fejer de Q(i,sqrt5), el campo de las cuatro fibras de G.
zeta_K = zeta * L(s,chi_4) * L(s,chi_5) * L(s,chi_20) para K = Q(i,sqrt5) (conductor 20, Galois Z2 x Z2, cuyo
mapa de Artin es G).  Su suma de Fejer es la suma de las cuatro, cada una desde los primos:
  Z_psi(L) = [polo] + A_psi(L) - 2 sum_n Lambda(n) psi(n) n^{-1/2} g_L(log n),   g_L(u) = (1-|u|/2L)^+,
con el polo h_L(i/2)+h_L(-i/2) solo para zeta, A_psi con su conductor (1, 4, 5, 20) y paridad.
La de zeta se contrasta con los 3000 primeros ceros de zeta (zeta_zeros_3000.npy).
El articulo: cae de 0.398 (2L = 6) a 0.118 (2L = 18), con cada parte positiva.
Uso: python3 -I dedekind.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from comun_pruebas import fejer_por_caracter
tz = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zeta_zeros_3000.npy'))
print("  2L     zeta      chi_4     chi_5     chi_20    suma (Q(i,sqrt5))   zeta desde sus ceros")
todo_pos = True
for L in (3, 4, 5, 6, 7, 8, 9):
    d = fejer_por_caracter(L)
    hz = 2*np.sum(2*L*(np.sin(L*tz)/(L*tz))**2); T = tz[-1]
    hz += (2/L)*(math.log(T/(2*math.pi)) + 1)/(2*math.pi*T)
    todo_pos &= all(v > 0 for v in d.values())
    print(f"  {2*L:3d}  {d['zeta']:.5f}  {d['chi_4']:.5f}  {d['chi_5']:.5f}  {d['chi_20']:.5f}     {sum(d.values()):.5f}          {hz:.5f}")
print("cada parte positiva:", todo_pos, "; articulo: de 0.398 (2L=6) a 0.118 (2L=18)")
