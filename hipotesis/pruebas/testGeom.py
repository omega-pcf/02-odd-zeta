"""testGeom.py — W1–W2, ssec:fluct-geometry: la ley de la fluctuacion es geometrica.
La fluctuacion suavizada (F1PaperTorus.flucTorus) en el punto theta del toro de los circulos de los primos:
  F(theta) = -4 sum_p sum_k chi_5(p)^k (log p) p^{-k/2} g(k log p) cos(k theta_p),
con g la gaussiana g(u) = e^{-u^2/2}/sqrt(2pi) (h(r) = e^{-r^2/2}).  Sobre la recta, theta_p = T log p
(prop:torus-line (iv)), y por la formula explicita es tambien el lado de los ceros:
  F(T) = sum_rho [h(T - gamma_rho) + h(T + gamma_rho)] - A(T),  A(T) = (1/2pi) int [h(r-T)+h(r+T)] W(r) dr,
W(r) = log(5/pi) + Re psi(1/4 + ir/2), sobre los ceros +-gamma.
Cuatro muestras de 480 puntos: (a) la recta verdadera en T al azar en [10, 490]; (b) puntos al azar del
toro; (c) una recta con primos sustitutos de las mismas clases (cada p se cambia por un entero q al azar
con q = p mod 20 y |q - p| < p/10, con el peso de p); (d) el lado de los ceros (397 ceros bajo 500) en
otros T al azar en [10, 490].  Se comparan desviacion, sesgo, curtosis y Kolmogorov–Smirnov contra (a).
El articulo: desviacion ~0.62, sesgo ~-0.33, curtosis ~-0.55; valores p de KS entre 0.14 y 0.69.
Uso: python3 -I testGeom.py [semilla]"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from scipy.stats import skew, kurtosis, ks_2samp
from comun_pruebas import potencias, CHI5, ceros_chi5
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
rng = np.random.default_rng(seed)
M = 480
n, p, k = potencias(3000)                         # g(log n) < 1e-14 mas alla de log n = 8
c = CHI5(n).astype(float)
a = -4*c*np.log(p.astype(float))/np.sqrt(n.astype(float))*np.exp(-np.log(n.astype(float))**2/2)/math.sqrt(2*math.pi)
m = c != 0; n, p, k, a = n[m], p[m], k[m], a[m]
P = np.unique(p); ip = np.searchsorted(P, p)
def F_theta(th): return (np.cos(k*th[..., ip])*a).sum(-1)
# (a) la recta
Ta = rng.uniform(10, 490, M)
Fa = F_theta(np.outer(Ta, np.log(P.astype(float))))
# (b) el toro
Fb = F_theta(rng.uniform(0, 2*np.pi, (M, len(P))))
# (c) primos sustitutos de las mismas clases
Q = np.array([q + 20*rng.integers(-max(1, q//200), max(1, q//200) + 1) for q in P])
Q = np.where(Q > 1, Q, P)
Tc = rng.uniform(10, 490, M)
Fc = F_theta(np.outer(Tc, np.log(Q.astype(float))))
# (d) el lado de los ceros
g = ceros_chi5(); G = np.concatenate([g, -g])
from scipy.special import psi as digamma
xs = np.linspace(-9, 9, 721); hx = np.exp(-xs**2/2)
def A(T):
    W = lambda r: math.log(5/math.pi) + digamma(0.25 + 0.5j*r).real
    return (np.trapezoid(hx*W(T + xs), xs) + np.trapezoid(hx*W(-T + xs), xs))/(2*math.pi)
Td = rng.uniform(10, 490, M)
Fd = np.array([np.sum(np.exp(-(T - G)**2/2) + np.exp(-(T + G)**2/2)) - A(T) for T in Td])
# comprobacion: en la recta, lado de los primos = lado de los ceros (formula explicita)
chk = max(abs(F_theta(np.log(P.astype(float))*T) - (np.sum(np.exp(-(T - G)**2/2) + np.exp(-(T + G)**2/2)) - A(T)))
          for T in (37.0, 211.3, 433.9))
print(f"formula explicita en la recta (T = 37, 211.3, 433.9): |primos - ceros| <= {chk:.1e}")
print("muestra                         desv.   sesgo   curtosis   KS contra (a): valor p")
for nm, X in (("(a) recta verdadera", Fa), ("(b) toro al azar", Fb), ("(c) primos sustitutos", Fc), ("(d) lado de los ceros", Fd)):
    pv = "" if X is Fa else f"{ks_2samp(Fa, X).pvalue:.2f}"
    print(f"{nm:30s}  {X.std():.3f}  {skew(X):+.3f}  {kurtosis(X):+.3f}     {pv}")
Fr = F_theta(rng.uniform(0, 2*np.pi, (20000, len(P))))
print(f"ley del toro (20000 puntos):     {Fr.std():.3f}  {skew(Fr):+.3f}  {kurtosis(Fr):+.3f}")
print("articulo: desv. ~0.62, sesgo ~-0.33, curtosis ~-0.55; KS entre 0.14 y 0.69")
