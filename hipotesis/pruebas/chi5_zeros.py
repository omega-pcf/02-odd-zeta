"""chi5_zeros.py — ceros de L(s, chi_5) en la recta, 0 < t < T, por cambios de signo de la funcion Z real.
chi_5 es par: Lambda(s) = (5/pi)^{s/2} Gamma(s/2) L(s, chi_5) = Lambda(1-s). Uso: python3 -I chi5_zeros.py [T]"""
import mpmath as mp, json, sys, time
mp.mp.dps = 15
T = float(sys.argv[1]) if len(sys.argv) > 1 else 330.0
chi = [0, 1, -1, -1, 1]
def Z(t):
    s = mp.mpc(0.5, t)
    th = mp.im(mp.loggamma(s / 2)) + t / 2 * mp.log(5 / mp.pi)
    return mp.re(mp.exp(1j * th) * mp.dirichlet(s, chi))
h = 0.03; t0 = time.time()
ts = [0.5 + h * k for k in range(int((T - 0.5) / h) + 1)]; vals = [Z(t) for t in ts]
zs = [float(mp.findroot(Z, (a, b), solver='illinois')) for a, b, va, vb in zip(ts, ts[1:], vals, vals[1:]) if va * vb < 0]
NT = T / (2 * mp.pi) * mp.log(5 * T / (2 * mp.pi * mp.e)) + 7 / 8.0
print(len(zs), "ceros en la recta; conteo esperado ~", float(NT), "; primer cero", zs[0], "; seg", round(time.time() - t0))
json.dump(zs, open("chi5_zeros.json", "w"))
