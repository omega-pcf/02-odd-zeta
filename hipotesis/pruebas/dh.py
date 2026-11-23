"""dh.py — W1–W2, ssec:two-sides: las sumas parciales de la inversa de Davenport–Heilbronn y de mu·chi_5.
La sucesion de Davenport–Heilbronn es periodica modulo 5 con valores 1, kappa, -kappa, -1, 0
(n = 1, 2, 3, 4, 0 mod 5), kappa = (sqrt(10-2 sqrt5)-2)/(sqrt5-1).  Su serie tiene la ecuacion funcional
de conductor 5 y sumas parciales acotadas, pero no producto de Euler.  Los coeficientes de su inversa
1/f(s) son la inversa de Dirichlet b = a^{-1}; los de 1/L(s,chi_5) son mu(n) chi_5(n).
Se mide el exponente de crecimiento del maximo de las sumas parciales, max_{n<=y}|B(n)|, B(y) = sum_{n<=y} b(n), y de
max_{n<=y}|M(n)|, M(y) = sum_{n<=y} mu(n)chi_5(n), hasta y = 3*10^6 (la nota [N] de F1PaperTorus.PeriodicBoundedIsNotEnough):
la pendiente de log max contra log y en 60 puntos logaritmicos de 10^4 a 3*10^6.
El articulo: la inversa de DH crece como y^0.788; mu·chi_5 como y^0.443.
Uso: python3 -I dh.py [Y]   (Y = 3*10^6 por defecto)"""
import numpy as np, sys
Y = int(float(sys.argv[1])) if len(sys.argv) > 1 else 3*10**6
kap = (np.sqrt(10 - 2*np.sqrt(5)) - 2) / (np.sqrt(5) - 1)
n = np.arange(Y + 1)
a = np.array([0.0, 1.0, kap, -kap, -1.0])[n % 5]; a[0] = 0.0
# inversa de Dirichlet: b(1) = 1, sum_{d|n} b(d) a(n/d) = 0 para n > 1
b = np.zeros(Y + 1); b[1] = 1.0
acc = np.zeros(Y + 1)                    # acc[n] = sum_{d|n, d<n} b(d) a(n/d)
for d in range(1, Y // 2 + 1):
    if d > 1: b[d] = -acc[d]             # a(1) = 1
    if b[d] != 0.0:
        k = np.arange(2, Y // d + 1)
        acc[d*k] += b[d] * a[k]
for d in range(Y // 2 + 1, Y + 1): b[d] = -acc[d]
# mu por criba
mu = np.ones(Y + 1, dtype=np.int8); mu[0] = 0
is_p = np.ones(Y + 1, bool); is_p[:2] = False
for p in range(2, int(Y**.5) + 1):
    if is_p[p]: is_p[p*p::p] = False
for p in np.nonzero(is_p)[0]:
    mu[p::p] *= -1
    mu[p*p::p*p] = 0
c5 = np.array([0, 1, -1, -1, 1])[n % 5]
m = mu.astype(float) * c5
# comprobaciones: b es la inversa de a; mu*chi5 es la inversa de chi5 (n <= 2000)
def conv(x, y, N=2000):
    z = np.zeros(N + 1)
    for d in range(1, N + 1): z[d::d] += x[d] * y[1:N // d + 1]
    return z
e1 = conv(a, b); e2 = conv(c5.astype(float), m)
ok1 = abs(e1[1] - 1) < 1e-12 and np.max(np.abs(e1[2:])) < 1e-9
ok2 = abs(e2[1] - 1) < 1e-12 and np.max(np.abs(e2[2:])) < 1e-12
def exponente(x, y0=10**4):
    S = np.cumsum(x); R = np.maximum.accumulate(np.abs(S))
    ys = np.unique(np.logspace(np.log10(y0), np.log10(Y), 60).astype(int))
    sl = np.polyfit(np.log(ys), np.log(R[ys]), 1)[0]
    return sl, R[Y]
eb, Rb = exponente(b); em, Rm = exponente(m)
print(f"kappa_DH = {kap:.10f};  inversas comprobadas hasta 2000: DH {ok1}, chi5 {ok2}")
print(f"inversa de DH:  max_(n<=y)|B| ~ y^{eb:.3f}   (max hasta {Y}: {Rb:.4g})")
print(f"mu*chi_5:       max_(n<=y)|M| ~ y^{em:.3f}   (max hasta {Y}: {Rm:.4g})")
print("articulo: 0.788 y 0.443")
