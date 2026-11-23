"""testB1b.py — W1–W2, ssec:fluct-geometry: los valores individuales piden log p con precision ~1/T.
La fluctuacion suavizada de testGeom.py, F(T) = -4 sum chi_5(p)^k (log p) p^{-k/2} g(k log p) cos(k T log p),
g(u) = e^{-u^2/2}/sqrt(2pi).  Se cambia cada log p por log p + eps*xi_p (xi_p normal estandar) y se mide el
error cuadratico medio de F en una ventana [T, T+20] a cada altura T.  Si el error es lineal en eps*T, la
precision que hace falta para reproducir los valores a la altura T es ~1/T; la ley (desviacion, sesgo,
curtosis) no cambia con eps.
El articulo: reproducir los valores a la altura T requiere log p con precision ~1/T.
Uso: python3 -I testB1b.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from scipy.stats import skew, kurtosis
from comun_pruebas import potencias, CHI5
rng = np.random.default_rng(7)
n, p, k = potencias(3000)
c = CHI5(n).astype(float)
a = -4*c*np.log(p.astype(float))/np.sqrt(n.astype(float))*np.exp(-np.log(n.astype(float))**2/2)/math.sqrt(2*math.pi)
m = c != 0; n, p, k, a = n[m], p[m], k[m], a[m]
P = np.unique(p); ip = np.searchsorted(P, p); lp = np.log(P.astype(float))
xi = rng.standard_normal(len(P))
def F(T, l): return (np.cos(k*np.outer(T, l)[:, ip])*a).sum(1)
sd = F(np.linspace(10, 490, 4000), lp).std()
print(f"desviacion de F: {sd:.3f}")
print("   T     eps donde el error rms = desviacion/2     eps*T")
prod = []
for T0 in (25, 50, 100, 200, 400, 800):
    Ts = np.linspace(T0, T0 + 20, 400); F0 = F(Ts, lp)
    eps = np.logspace(-6, 0, 121)
    err = np.array([np.sqrt(np.mean((F(Ts, lp + e*xi) - F0)**2)) for e in eps])
    e_half = np.interp(sd/2, err, eps)            # err crece con eps
    prod.append(e_half*T0)
    print(f"  {T0:4d}   {e_half:.2e}                                  {e_half*T0:.3f}")
print(f"eps*T casi constante: de {min(prod):.3f} a {max(prod):.3f}  => precision necesaria ~ {np.mean(prod):.2f}/T")
X = F(np.linspace(10, 490, 4000), lp + 1e-2*xi)
print(f"la ley con eps = 1e-2: desv. {X.std():.3f}, sesgo {skew(X):+.3f}, curtosis {kurtosis(X):+.3f} (sin cambio)")
print("articulo: precision de log p ~1/T")
