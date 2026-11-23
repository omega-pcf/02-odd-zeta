"""amplitud_clausula_ii.py — W4–W5, prop:closure-amplitude: la amplitud de la clausula (ii).
(i) V_chi = log(q/pi) + Re Gamma'/Gamma((1+e)/2) + 2 Re L'/L(1,chi*) para los ocho caracteres modulo 20 (primitivos,
    conductores 1, 4, 5, 20), V = 2 + gamma_E - log 4pi para el trivial; sum V_chi = 2.4056 y (1/64) sum V_chi = 0.0376.
(iii) Con theta(x;20,a) = sum_(p<=x, p=a mod 20) log p, la funcion E_a(x) = (theta(x;20,a) - x/8)/sqrt(x) tiene media
    logaritmica -n_2(a)/8 (n_2(a) = numero de raices cuadradas de a modulo 20) y varianza logaritmica (1/64) sum V_chi.
    Medidas con primos hasta 10^8: integrales exactas de E y E^2 contra dx/x entre primos consecutivos.
El articulo: sum V = 2.4056, 0.0376; medias -0.497 y -0.500 en las clases 1 y 9 y |media| < 0.04 en las otras; la media de
las ocho varianzas 0.0379 en [10^4, 10^8], a menos de 3.5% de 0.0376 en otros cinco rangos; las clases sueltas se desvian
de -54% a +68% (nota [N] de W4Isometria.class_parseval: seis rangos hasta 10^8).  Rangos usados: [1e4,1e8] y
[1e4,1e6], [1e6,1e8], [1e4,1e7], [1e5,1e8], [1e3,1e8].
Uso: python3 -I amplitud_clausula_ii.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, mpmath as mp
from comun_pruebas import criba, ocho_caracteres
mp.mp.dps = 30
# (i)
tot = mp.mpf(0)
for nm, f, q, par in ocho_caracteres():
    if q == 1: V = 2 + mp.euler - mp.log(4*mp.pi)
    else:
        ch = [complex(f(np.array([b]))[0]) for b in range(1, q + 1)]
        g0 = sum(c*(-mp.digamma(mp.mpf(b)/q)) for b, c in zip(range(1, q + 1), ch))     # gamma_0 = -psi
        g1 = sum(c*mp.stieltjes(1, mp.mpf(b)/q) for b, c in zip(range(1, q + 1), ch))   # Stieltjes generalizado
        V = mp.log(q/mp.pi) + mp.re(mp.digamma((1 + par)/mp.mpf(2))) + 2*mp.re(-mp.log(q) - g1/g0)
    tot += V
    print(f"   V({nm:13s}) = {float(V):+.5f}")
print(f"(i) sum V_chi = {float(tot):.4f};  (1/64) sum = {float(tot/64):.4f}   (articulo 2.4056, 0.0376)")
# (iii)
P = criba(10**8).astype(np.int64)
P = P[(P != 2) & (P != 5)]
x = P.astype(float); lp = np.log(x)
def momentos(a, X1, X2):
    m = (P % 20) == a
    th = np.cumsum(lp*m)                       # theta(x;20,a) en cada primo
    xs = np.concatenate([[X1], x[(x > X1) & (x < X2)], [X2]])
    i0 = np.searchsorted(x, X1, side='right') - 1
    thv = th[i0:i0 + len(xs) - 1] if i0 >= 0 else np.concatenate([[0.0], th[:len(xs) - 2]])
    A, B = xs[:-1], xs[1:]
    # int (th - x/8) x^{-3/2} dx  y  int (th - x/8)^2 x^{-2} dx  en [A, B]
    I1 = thv*(2/np.sqrt(A) - 2/np.sqrt(B)) - (np.sqrt(B) - np.sqrt(A))/4
    I2 = thv**2*(1/A - 1/B) - thv/4*np.log(B/A) + (B - A)/64
    W = math.log(X2/X1)
    mu = I1.sum()/W; var = I2.sum()/W - mu**2
    return mu, var
clases = (1, 3, 7, 9, 11, 13, 17, 19)
print("(iii) clase  n_2   media log   -n_2/8    varianza log")
vs = []
for a in clases:
    mu, var = momentos(a, 1e4, 1e8); vs.append(var)
    n2 = sum(1 for b in range(20) if (b*b - a) % 20 == 0)
    print(f"       {a:2d}    {n2}    {mu:+.3f}    {-n2/8:+.3f}     {var:.4f}")
V0 = float(tot/64); mv = np.mean(vs); extremos = [min(vs), max(vs)]
print(f"     media de las ocho varianzas en [1e4, 1e8]: {mv:.4f} ({100*(mv/V0 - 1):+.1f}% de {V0:.4f})")
for X1, X2 in ((1e4, 1e6), (1e6, 1e8), (1e4, 1e7), (1e5, 1e8), (1e3, 1e8)):
    v = [momentos(a, X1, X2)[1] for a in clases]; extremos += [min(v), max(v)]
    print(f"     [{X1:.0e}, {X2:.0e}]: media de las varianzas {np.mean(v):.4f} ({100*(np.mean(v)/V0 - 1):+.1f}%);"
          f"  clases de {100*(min(v)/V0 - 1):+.0f}% a {100*(max(v)/V0 - 1):+.0f}%")
print(f"     en los seis rangos, las clases sueltas se desvian de {100*(min(extremos)/V0 - 1):+.0f}% a {100*(max(extremos)/V0 - 1):+.0f}%")
print("articulo: -0.497, -0.500; |media| < 0.04; 0.0379; 3.5%; -54% a +68%")
