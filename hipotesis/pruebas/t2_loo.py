"""t2_loo.py — W4–W5, prop:what-fluctuation-takes: dejar un primo fuera de la correccion.
Para cada primo p <= X = 500, el uso de p en la correccion es u_p = err(sin p) - err(con todos), con el operador
corregido de law_resolution.py (zeta, n = 100..3000).  Se ajusta u_p por la posicion de p (1/sqrt p y log p, el peso y
la frecuencia de su termino) y se prueba si el orden angular de phi en p (el indice i_p y log e_p, t1_index.py)
explica algo del resto: incremento de R^2 y prueba F.
El articulo: una vez contada la posicion, el orden angular no explica el uso de ningun primo en la correccion.
Uso: python3 -I t2_loo.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from scipy import stats
from comun_pruebas import zeta_ceros, Einv, potencias, S_primos
from comun import orden
tz = zeta_ceros(); N = np.arange(1, len(tz) + 1).astype(float)
s = (N >= 100) & (N <= 3000); nn = N[s]; g = tz[s]; sp = 2*np.pi/np.log(g/(2*np.pi))
X = 500; n, p, k = potencias(X); b = Einv(nn - 0.5, g)
err = lambda t: np.mean(np.abs(t - g)/sp)
e0 = err(Einv(nn - 0.5 - S_primos(b, X, n, p, k), b))
P = sorted(set(int(x) for x in p if x not in (2, 3, 5)))
u = []
for q in P:
    m = p != q
    u.append(err(Einv(nn - 0.5 - S_primos(b, X, n[m], p[m], k[m]), b)) - e0)
u = np.array(u); Pa = np.array(P, float)
Np_e = [orden(q) for q in P]
idx = np.array([Nq/e for Nq, e in Np_e], float); le = np.log([e for Nq, e in Np_e])
def ajuste(cols):
    A = np.column_stack([np.ones(len(u))] + cols)
    c, *_ = np.linalg.lstsq(A, u, rcond=None)
    r = u - A @ c
    return 1 - r @ r/((u - u.mean()) @ (u - u.mean())), r @ r, A.shape[1]
R1, S1, k1 = ajuste([1/np.sqrt(Pa), np.log(Pa)])
R2, S2, k2 = ajuste([1/np.sqrt(Pa), np.log(Pa), np.log(idx), le])
F = ((S1 - S2)/(k2 - k1))/(S2/(len(u) - k2)); pv = 1 - stats.f.cdf(F, k2 - k1, len(u) - k2)
print(f"{len(P)} primos 7 <= p <= {X}; u_p > 0 (quitar p empeora) en {np.sum(u > 0)}")
print(f"R^2 con la posicion (1/sqrt p, log p): {R1:.3f};  agregando el orden angular (log i_p, log e_p): {R2:.3f}")
print(f"prueba F del orden angular dada la posicion: F = {F:.2f}, p = {pv:.2f}")
print("articulo: dada la posicion, el orden angular no explica el uso de ningun primo")
