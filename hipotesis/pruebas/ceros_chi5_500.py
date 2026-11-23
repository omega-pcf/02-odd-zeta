"""ceros_chi5_500.py — los ceros de L(s,chi_5) en 0 < t < 500 (dato común de hipotesis/pruebas/).
chi_5 = (·/5) es par y de conductor 5: Z(t) = e^{i theta(t)} L(1/2+it, chi_5) es real, con
theta(t) = Im log Gamma(1/4+it/2) + (t/2) log(5/pi).  Los ceros son los cambios de signo de Z,
refinados con findroot; el conteo se contrasta con N(T) = (T/2pi) log(5T/(2pi e)) + 7/8.
Salida: chi5_zeros_500.json.  Uso: python3 -I ceros_chi5_500.py"""
import mpmath as mp, json, sys
from multiprocessing import Pool
mp.mp.dps = 20
T = 500.0; H = 0.04
chi = [0, 1, -1, -1, 1]
def Z(t):
    t = mp.mpf(t); s = mp.mpc(0.5, t)
    th = mp.im(mp.loggamma(s / 2)) + t / 2 * mp.log(mp.mpf(5) / mp.pi)
    return mp.re(mp.exp(1j * th) * mp.dirichlet(s, chi))
def tramo(k0):
    ts = [0.5 + H * k for k in range(k0, min(k0 + 500, NK) + 1)]
    v = [Z(t) for t in ts]
    out = []
    for a, b, va, vb in zip(ts, ts[1:], v, v[1:]):
        if va * vb < 0:
            out.append(float(mp.findroot(Z, (a, b), solver='anderson')))
    return out
NK = int((T - 0.5) / H)
if __name__ == '__main__':
    with Pool(2) as P:
        res = P.map(tramo, range(0, NK, 500))
    zs = sorted(set(round(z, 13) for r in res for z in r))
    zs = [z for z in zs if z < T]
    NT = T / (2 * mp.pi) * mp.log(5 * T / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8
    print(len(zs), 'ceros en 0<t<500; N(T) suave =', float(NT), '; primero', zs[0])
    json.dump(zs, open('chi5_zeros_500.json', 'w'))
