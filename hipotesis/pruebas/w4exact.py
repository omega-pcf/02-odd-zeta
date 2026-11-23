"""w4exact.py — W4–W5, prop:W4-from-W3 (i): (W4) es (W3) en los planos de la orbita, exactamente.
(El articulo lista w4exact.py entre los scripts sin atarlo a un numero; este comprueba la identidad exacta de
prop:W4-from-W3 (i) en las orbitas de zeroside.py.)  Para g = g_a (triangulo de semiancho a) y f = tau_u g -+ g:
  W(tau_u g - g) = 2 t(0) - 2 t(u),   W(tau_u g + g) = 2 t(0) + 2 t(u),
donde W(f) se calcula directamente con la autocorrelacion de f, h_f(v) = 2A(v) -+ (A(v-u) + A(v+u)), y t(u) con la orbita.
Luego |t(u)| <= t(0) si y solo si W >= 0 en el plano <g, tau_u g>.  En el lado de los ceros (chi_5, 397 ceros),
W(tau_u g - g) = sum_rho |ghat(gamma)|^2 (2 - 2 cos(gamma u)) >= 0 termino a termino.
Uso: python3 -I w4exact.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, mpmath as mp
from comun_pruebas import potencias, CHI5, A_tri, arch_desplazada, ceros_chi5, EG
a, p0, K = 0.3, 3, 12
n, p, k = potencias(int(math.exp(K*math.log(p0) + 2*a)) + 2)
ln = np.log(n.astype(float)); w = np.log(p.astype(float))*CHI5(n)/np.sqrt(n.astype(float))
def t(u): return arch_desplazada(a, u, 5, 0) - np.sum(w*(A_tri(ln - u, a) + A_tri(ln + u, a)))
def W_directo(u, sg):
    hf = lambda v: 2*A_tri(v, a) + sg*(A_tri(v - u, a) + A_tri(v + u, a))
    h0 = float(hf(0.0))
    kn = sorted(set([0.0] + [x for x in (u - 2*a, u - a, u, u + a, u + 2*a, a, 2*a) if x > 0]))
    I = mp.quad(lambda v: (mp.e**(-2*v)*h0 - mp.e**(-v/2)*float(hf(float(v))))/(1 - mp.e**(-2*v)), [mp.mpf(x) for x in kn] + [mp.inf])
    A = h0*(math.log(5/math.pi) - EG) + 2*float(I)
    return A - 2*np.sum(w*hf(ln))
g = ceros_chi5(); G2 = (a*(np.sin(a*g/2)/(a*g/2))**2)**2
t0 = t(0.0); peor = 0
print("  k    W(tau g - g)   2t0 - 2t_k     W(tau g + g)   2t0 + 2t_k    |t_k|<=t_0   ceros: sum |g^|^2(2-2cos) >= 0")
for kk in range(1, K + 1):
    u = kk*math.log(p0); tk = t(u)
    wm, wp = W_directo(u, -1), W_directo(u, +1)
    peor = max(peor, abs(wm - (2*t0 - 2*tk)), abs(wp - (2*t0 + 2*tk)))
    zc = 2*np.sum(G2*(2 - 2*np.cos(g*u)))
    print(f" {kk:2d}  {wm:+.8f}   {2*t0 - 2*tk:+.8f}   {wp:+.8f}   {2*t0 + 2*tk:+.8f}   {abs(tk) <= t0}         {zc:.6f}")
print(f"maxima diferencia de la identidad: {peor:.1e}")
