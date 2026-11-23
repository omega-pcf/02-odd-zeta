"""arch_window.py — W3, ssec:golden-field: la forma arquimediana de zeta_K, K = Q(sqrt5), explicitamente.
Para g con h = g * g~, la parte sin primos de la forma de Weil de zeta_K es
  Q_inf(g) = 2 ghat(i/2) ghat(-i/2) + C_0 ||g||^2 + D(g),   D(g) = 4 int_0^inf w(u)(h(0) - h(u)) du,
  w(u) = e^{-u/2}/(1-e^{-2u}),  C_0 = log5 - 2 log pi - 2 gamma_E + 4 int_0^inf (e^{-2u}-e^{-u/2})/(1-e^{-2u}) du,
con D >= 0 porque h(0) - h(u) = (1/2) int (g(x) - g(x+u))^2 dx (F1PaperTorus.autocorrelation_le_energy).
En L^2 de un intervalo de longitud S (polinomios de Legendre ortonormales de grado < 50, matriz de Galerkin exacta
como en rigorous_chain.py, sin primos): el menor autovalor de C_0 + D (sin el polo) y el segundo autovalor de D frente
a |C_0| (el polo quita el modo fundamental); y, como dato, el menor autovalor de C_0 + D + polo.
El articulo: C_0 = -9.13493; sin el polo la forma es negativa desde soporte ~0.45; con el polo, la positividad pide
que el segundo autovalor de D supere |C_0|, lo que vale hasta soporte ~1.65, mas alla del rango sin primos [0, log 4].
(Nota [N] de F1PaperTorus.GoldenArchimedeanHodge, con elementos finitos: lambda_2(D) = 9.509 en log 4, 9.207 en 1.6,
9.078 en 1.7.)
Uso: python3 -I arch_window.py"""
import numpy as np, math, mpmath as mp
from numpy.polynomial.legendre import leggauss, legvander
mp.mp.dps = 30
C0 = float(mp.log(5) - 2*mp.log(mp.pi) - 2*mp.euler + 4*mp.quad(lambda u: (mp.e**(-2*u) - mp.e**(-u/2))/(1 - mp.e**(-2*u)), [0, 1, mp.inf]))
print(f"C_0 = {C0:.5f}  (articulo -9.13493)")
w = lambda u: np.exp(-u/2)/(-np.expm1(-2*u))
Wtail = lambda d: np.arctanh(np.exp(-d/2)) + np.arctan(np.exp(-d/2))
def phi(N, L, x): return legvander(np.clip(x/L, -1, 1), N - 1)*np.sqrt((2*np.arange(N) + 1)/(2*L))*((np.abs(x) <= L)[:, None])
def cruz(N, L, u, Q):
    if u >= 2*L: return np.zeros((N, N))
    t, wt = leggauss(Q); a, b = -L, L - u
    x = (b - a)/2*t + (a + b)/2; ww = wt*(b - a)/2
    H = (phi(N, L, x)*ww[:, None]).T @ phi(N, L, x + u)
    return (H + H.T)/2
def formas(S, N=50):
    L = S/2; Q = N + 20
    tu, wu = leggauss(N + 60); U = L*(tu + 1); WU = wu*L
    D = sum(4*ww*w(u)*(np.eye(N) - cruz(N, L, u, Q)) for u, ww in zip(U, WU)) + 4*Wtail(2*L)*np.eye(N)
    t, wt = leggauss(Q); x = L*t; F = phi(N, L, x); ww = wt*L
    a = F.T @ (ww*np.exp(-x/2)); b = F.T @ (ww*np.exp(x/2))
    return D, np.outer(a, b) + np.outer(b, a)
def biseca(f, a, b):
    for _ in range(25):
        m = (a + b)/2
        if f(m) > 0: a = m
        else: b = m
    return (a + b)/2
print("  S       lambda_2(D)   C_0 + lambda_1(D)   min(C_0 + D + polo)")
for S in (math.log(4), 1.5, 1.6, 1.65, 1.7):
    D, Pl = formas(S); d = np.linalg.eigvalsh(D)
    print(f"  {S:.3f}   {d[1]:.3f}        {C0 + d[0]:+.3f}             {np.linalg.eigvalsh(C0*np.eye(len(d)) + D + Pl)[0]:+.4f}")
s0 = biseca(lambda S: C0 + np.linalg.eigvalsh(formas(S, 30)[0])[0], 0.2, 1.0)
s2 = biseca(lambda S: np.linalg.eigvalsh(formas(S, 30)[0])[1] + C0, 1.2, 2.0)
s1 = biseca(lambda S: (lambda D, Pl: np.linalg.eigvalsh(C0*np.eye(len(D)) + D + Pl)[0])(*formas(S, 30)), 1.2, 2.0)
print(f"sin el polo: C_0 + D deja de ser positiva en S = {s0:.3f}  (articulo ~0.45)")
print(f"segundo autovalor de D = |C_0| en S = {s2:.3f}  (articulo ~1.65);  log 4 = {math.log(4):.3f}")
print(f"C_0 + D + polo, positiva hasta S = {s1:.3f}")
