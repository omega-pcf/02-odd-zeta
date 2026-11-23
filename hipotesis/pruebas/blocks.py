"""blocks.py — W3, ssec:field-positivity: los tres bloques del lado de los primos y el limite forzado.
Con la ventana de Fejer g_L(u) = (1-|u|/2L)^+, el lado de los primos de L(s,chi_5) se parte en
  k_1 = -2 sum_p chi_5(p) (log p/sqrt p) g_L(log p)           (el bloque con caracter),
  k_2 = -2 sum_(p != 5) (log p/p) g_L(2 log p)                 (cuadrados: chi_5(p^2) = 1, sin caracter),
  k_3 = -2 sum_(p, k>=3) chi_5(p)^k (log p/p^(k/2)) g_L(k log p) (potencias altas).
Por Mertens, k_2 + L -> c_2 = -2(B - log5/5), con B = lim(sum_(p<=x) log p/p - log x) = -1.3325822757...;
k_3 -> c_3 (suma absolutamente convergente).  El total Z(L) = A(L) + k_1 + k_2 + k_3 tiende a 0 si la
linea vale, y A(L) -> kappa = log(5/pi) + psi(1/4) = -3.76274... (thm:first-window).  Luego el
limite de k_1 - L esta forzado: -kappa - c_2 - c_3 (F1PaperTorus.forcedLimit).
El articulo: -kappa - c_2 - c_3 = -0.0802, con -kappa = gamma_E + log 8 + pi/2 + log pi - log 5.
Uso: python3 -I blocks.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, mpmath as mp
from comun_pruebas import criba, lado_primos, arch_fejer, CHI5
mp.mp.dps = 30
kappa = mp.log(5/mp.pi) + mp.digamma(mp.mpf(1)/4)
mk = mp.euler + mp.log(8) + mp.pi/2 + mp.log(mp.pi) - mp.log(5)
B = mp.mpf('-1.332582275733220881765828776071027748')      # Mertens: sum log p/p = log x + B + o(1)
c2 = -2*(B - mp.log(5)/5)
# c_3: -2 sum_p log p * x^3/(1-x), x = chi_5(p)/sqrt(p); primos hasta 10^7 y cola por PNT
P = criba(10**7).astype(float); c = CHI5(P.astype(np.int64)).astype(float)
x = c/np.sqrt(P); m = c != 0
c3_fin = -2*np.sum(np.log(P[m])*x[m]**3/(1 - x[m]))
# la cola p > 10^7 cambia c_3 en menos de 10^-6 (primos hasta 10^6, 10^7, 10^8: 0.533973, 0.533972, 0.533972)
c3 = c3_fin
print(f"-kappa = {float(-kappa):.6f}  (= gamma_E+log8+pi/2+log pi-log5 = {float(mk):.6f})")
print(f"c_2 = -2(B - log5/5) = {float(c2):.4f};  c_3 = {c3:.4f}")
lim = float(-kappa - c2) - c3
print(f"limite forzado -kappa - c_2 - c_3 = {lim:.4f}   (articulo: -0.0802)")
# medida: k_1 - L, k_2 + L y k_3 a lo largo de L, y el total Z(L)
print("   2L     k_1 - L     k_2 + L     k_3        A(L)       Z(L)")
fil = []
for L in (3, 4, 5, 6, 7, 8, 9):
    d = lado_primos(L, CHI5); A = arch_fejer(L)
    k1 = d['partidos'] + d['inertes']
    fil.append((L, k1 - L, d['cuadrados'] + L))
    print(f"  {2*L:3d}  {k1 - L:10.4f}  {d['cuadrados'] + L:10.4f}  {d['altas']:9.4f}  {A:9.4f}  {A + d['total']:9.4f}")
# extrapolacion lineal en 1/L de los dos bloques con los tres ultimos puntos
Ls = np.array([f[0] for f in fil[-3:]], float)
e1 = np.polyfit(1/Ls, [f[1] for f in fil[-3:]], 1)[1]
e2 = np.polyfit(1/Ls, [f[2] for f in fil[-3:]], 1)[1]
print(f"extrapolacion en 1/L (2L = 14, 16, 18): k_1 - L -> {e1:.3f};  k_2 + L -> {e2:.3f} (exacto {float(c2):.4f}, error {e2 - float(c2):+.3f})")
