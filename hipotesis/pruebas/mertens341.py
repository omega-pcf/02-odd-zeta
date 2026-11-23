"""mertens341.py — W1–W2, ssec:two-sides: hasta donde llega la desigualdad 3-4-1 de Mertens para L(s,chi_5).
Para sigma > 1 el producto de Euler converge absolutamente y, primo por primo,
3 + 4c cos x + cos 2x = 2(1 + c cos x)^2 >= 0 da
    P(sigma, t) = |L(chi0,sigma)|^3 |L(chi_5,sigma+it)|^4 |L(chi_5^2,sigma+2it)| >= 1,
con chi0 = chi_5^2 el caracter principal modulo 5 (L(s,chi0) = zeta(s)(1-5^{-s})).
Debajo de sigma = 1 cada producto finito de Euler sigue siendo >= 1 (la desigualdad es primo por primo),
pero la funcion continuada no: se busca el menor sigma con min_{0<t<=T} P(sigma,t) >= 1.
Metodo (como en la nota [N] de F1PaperTorus.MertensPositivity: minimo en t <= 120): barrido de t en (0,120] con paso
0.1 y refinamiento de cada minimo local, a sigma = 0.95, 0.9, 0.85, 0.8, 0.7, 0.6; y el sigma en que el minimo cruza 1.
El articulo: el producto se mantiene >= 1 solo hasta sigma ~ 0.9.
Uso: python3 -I mertens341.py [T]  (T = 120 por defecto)"""
import mpmath as mp, sys, math
from multiprocessing import Pool
mp.mp.dps = 15
T = float(sys.argv[1]) if len(sys.argv) > 1 else 120.0
c5 = [0, 1, -1, -1, 1]; c0 = [0, 1, 1, 1, 1]
def P(s, t):
    s = mp.mpf(s)
    return float(abs(mp.dirichlet(s, c0))**3 * abs(mp.dirichlet(mp.mpc(s, t), c5))**4
                 * abs(mp.dirichlet(mp.mpc(s, 2*t), c0)))
def barrido(arg):
    s, ts = arg
    return [P(s, t) for t in ts]
def tmin(s, t0, h=0.1):
    a, b = t0 - h, t0 + h
    for _ in range(30):
        m1, m2 = a + (b-a)/3, b - (b-a)/3
        if P(s, m1) < P(s, m2): b = m2
        else: a = m1
    return (a+b)/2
def minimo(s, pool):
    ts = [0.1*k for k in range(1, int(T/0.1) + 1)]
    v = sum(pool.map(barrido, [(s, ts[i::2]) for i in range(2)]), [])
    par = sorted(zip(ts[0::2] + ts[1::2], v)); ts = [a for a, b in par]; v = [b for a, b in par]
    loc = sorted([i for i in range(1, len(v) - 1) if v[i] <= v[i-1] and v[i] <= v[i+1]], key=v.__getitem__)[:6]
    best = min((P(s, tmin(s, ts[i])), tmin(s, ts[i])) for i in loc)
    return best
if __name__ == '__main__':
    ok = all(3 + 4*c*math.cos(x) + math.cos(2*x) >= -1e-15 for c in (1, -1) for x in [k*0.01 for k in range(629)])
    print("3 + 4c cos x + cos 2x >= 0 para c = +-1:", ok)
    with Pool(2) as pool:
        res = {}
        for s in (0.95, 0.9, 0.85, 0.8, 0.7, 0.6):
            m, t = minimo(s, pool); res[s] = m
            print(f"  sigma = {s:.2f}: min_(0<t<={T:g}) P = {m:.4g}  (en t = {t:.3f})")
        lo, hi = 0.8, 0.9
        for _ in range(12):
            mid = (lo + hi)/2
            if minimo(mid, pool)[0] >= 1: hi = mid
            else: lo = mid
    print(f"P >= 1 en 0 < t <= {T:g} hasta sigma = {hi:.4f}  (articulo: ~0.9; nota [N]: 0.148 en 0.8 y 3e-4 en 0.6)")
