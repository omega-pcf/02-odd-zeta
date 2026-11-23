"""fibres.py — W3, ssec:field-positivity y prop:four-fibres: la suma de Fejer de cada fibra de G.
Para cada fibra F de G : (Z/20)^* -> Z2 x Z2 ((0,0) = {1,9}, (0,1) = {13,17}, (1,0) = {11,19}, (1,1) = {3,7}),
  S_F(L) = sum_(p primo, p mod 20 en F) (log p/sqrt p) g_L(log p),   g_L(u) = (1-|u|/2L)^+,
y el total S(L) = sum_(p no divide 10) (log p/sqrt p) g_L(log p).  Con 1_F = (1/4) sum_psi psi(g) psi
(psi en {1, chi_4, chi_5, chi_20}, g en F) y la formula explicita de cada L(s,psi) primitiva,
  Z_psi = A_psi - 2 sum_n Lambda(n) psi(n) n^{-1/2} g_L(log n),
la desviacion S_F - S/4 es exactamente
  (1/4) sum_(psi != 1) psi(g) [A_psi/2 - (potencias k >= 2 de psi) - (terminos de 2 y 5 de psi primitiva)]
  - (1/8) sum_(psi != 1) psi(g) Z_psi:
la predicen los tres conductores (A_psi: q = 4 impar, 5 par, 20 impar), los cuadrados y los primos 2 y 5,
salvo el resto -(1/8) sum psi(g) Z_psi.
El articulo, a 2L = 18: medido -2.7954, 0.6963, 0.7488, 1.3504; predicho -2.7815, 0.6871, 0.7376, 1.3568;
restos -(1/8) sum psi(g) Z_psi con Z_4 = 0.019, Z_5 = 0.0113, Z_20 = 0.0814.
Uso: python3 -I fibres.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from comun_pruebas import potencias_hasta, arch_fejer, CHI4, CHI5, CHI20, FIBRAS
L = 9.0
n, p, k = potencias_hasta(int(math.exp(2*L)) + 1)
m = np.log(n.astype(float)) < 2*L; n, p, k = n[m], p[m], k[m]
w = np.log(p.astype(float))/np.sqrt(n.astype(float))*(1 - np.log(n.astype(float))/(2*L))
cop = (n % 2 != 0) & (n % 5 != 0); pr = k == 1
S = np.sum(w[pr & cop])
med = {F: np.sum(w[pr & np.isin(n % 20, cl)]) - S/4 for F, cl in FIBRAS.items()}
# las tres L primitivas: chi_4 (conductor 4, impar), chi_5 (5, par), chi_20 (20, impar)
chis = {'4': (CHI4, 4, 1), '5': (CHI5, 5, 0), '20': (CHI20, 20, 1)}
Zs, pred_psi = {}, {}
for nm, (chi, q, par) in chis.items():
    c = chi(n).astype(float)
    A = arch_fejer(L, q, par)
    Ptot = -2*np.sum(w*c)                       # lado de los primos de la L primitiva (todas las potencias)
    Zs[nm] = A + Ptot
    resto_pp = np.sum((w*c)[(k >= 2) | ~cop])   # potencias k>=2 y los primos 2 y 5 (lo que no es primo p nmid 10)
    pred_psi[nm] = A/2 - resto_pp               # = sum_(p nmid 10) psi(p) log p/sqrt p g_L + Z_psi/2
print(f"2L = {2*L:g}: Z_4 = {Zs['4']:.4f}, Z_5 = {Zs['5']:.4f}, Z_20 = {Zs['20']:.4f}   (articulo 0.019, 0.0113, 0.0814)")
print(" fibra      clases     medido     predicho    medido-predicho   -(1/8) sum psi(g) Z_psi")
for F, cl in FIBRAS.items():
    g = cl[0]
    sg = {nm: float(chi(np.array([g]))[0]) for nm, (chi, q, par) in chis.items()}
    pred = 0.25*sum(sg[nm]*pred_psi[nm] for nm in chis)
    rem = -0.125*sum(sg[nm]*Zs[nm] for nm in chis)
    print(f" {str(F):7s} {str(cl):9s}  {med[F]:9.5f}   {pred:9.5f}      {med[F]-pred:+.5f}          {rem:+.5f}")
print("articulo: medido -2.7954, 0.6963, 0.7488, 1.3504; predicho -2.7815, 0.6871, 0.7376, 1.3568")
