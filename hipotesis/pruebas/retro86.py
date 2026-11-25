"""retro86.py — Sprint 86: las trazas en 5^k por suma de Gauss binaria, exacta (enteros y simbolos de Legendre).
U(g)[i,j] = s(g) N^{-1/2} e(k(a j^2 - 2ij + d i^2)/N), k = (2b)^{-1}, s(g) = sqrt(N)/G(k) = (k/5)^K para N = 5^K.
tr U(g1)U(g2) = s1 s2 N^{-1} S(Q),  Q(i,j) = (k1 d1 + k2 a2) i^2 - 2(k1+k2) ij + (k1 a1 + k2 d2) j^2.
S(Q) se evalua exacto: valor = signo * 5^(e/2)."""
import math
import numpy as np
from sympy import legendre_symbol
_g = {"__name__": "r83", "__file__": __file__.replace("retro86.py", "retro83.py")}
exec(compile(open(__file__.replace("retro86.py", "retro83.py")).read().split("rng = random.Random(83)")[0], "r83", "exec"), _g)
Wn, mm, order = _g["Wn"], _g["mm"], _g["order"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
L5 = lambda x: int(legendre_symbol(x % 5, 5))
def v5(x):
    v = 0
    while x % 5 == 0 and x: x //= 5; v += 1
    return v, x
def G1(c, K):                      # sum_{x mod 5^K} e(c x^2 / 5^K) = (sgn, e2), valor sgn*5^(e2/2)
    c %= 5 ** K
    if c == 0: return (1, 2 * K)
    v, u = v5(c)
    return (L5(u) ** (K - v), 2 * v + (K - v))
def mul(*xs):
    s, e = 1, 0
    for a, b in xs: s *= a; e += b
    return (s, e)
def S2(A, Bc, C, K):               # sum_{x,y mod 5^K} e((A x^2 + Bc xy + C y^2)/5^K), Bc el coeficiente de xy
    N = 5 ** K; A, Bc, C = A % N, Bc % N, C % N
    if K == 0: return (1, 0)
    if A % 5 == 0 and Bc % 5 == 0 and C % 5 == 0:
        if (A, Bc, C) == (0, 0, 0): return (1, 4 * K)
        s, e = S2(A // 5, Bc // 5, C // 5, K - 1); return (s, e + 4)       # 25 * S_{K-1}
    if A % 5 == 0 and C % 5 != 0: A, C = C, A
    if A % 5 == 0:                 # A, C no unidades, Bc unidad: x -> x + y
        A, Bc, C = A, (2 * A + Bc) % N, (A + Bc + C) % N
        A, C = C, A
    inv = pow(4 * A, -1, N)
    return mul(G1(A, K), G1(C - Bc * Bc * inv, K))
def tr_pair(g1, g2, K):
    N = 5 ** K
    (a1, b1), (c1, d1) = g1; (a2, b2), (c2, d2) = g2
    k1, k2 = pow(2 * b1, -1, N), pow(2 * b2, -1, N)
    s1, s2 = L5(k1) ** K, L5(k2) ** K
    sg, e = S2(k1 * d1 + k2 * a2, -2 * (k1 + k2), k1 * a1 + k2 * d2, K)
    return (s1 * s2 * sg, e - 2 * K)                                          # / N
def val(x): return x[0] * 5 ** (x[1] / 2)
def bpow(n, N):
    g = ((1, 0), (0, 1))
    for _ in range(n): g = mm(g, ((1, 1), (1, 2)), N)
    return g
def tr_pred(n, N):
    if n % 2: return (1, 0)
    m = n // 2
    if m % N == 0: return (1, 2 * int(round(math.log(N, 5))))
    v, mp = v5(m)
    return (L5(mp), 2 * v + 1)
# validacion contra la diagonalizacion
for K in (1, 2, 3):
    N = 5 ** K; U = Wn(((1, 1), (1, 2)), N); P = np.eye(N, dtype=complex)
    for n in range(1, 2 * N):
        P = P @ U
        split = 1 if bpow(n - 1, N)[0][1] % 5 else 2
        g1, g2 = bpow(split, N), bpow(n - split, N)
        if g2[0][1] % 5 == 0: continue
        check("V", "T", f"K={K} n={n}: la suma binaria exacta reproduce tr U^n", abs(val(tr_pair(g1, g2, K)) - np.trace(P)) < 1e-6)
# la formula, exacta, hasta K = 9
for K in range(1, 10):
    N = 5 ** K; e = 2 * N; ok = True; nm5 = 0
    B = ((1, 1), (1, 2)); g = B
    pw = [((1, 0), (0, 1)), B]
    for n in range(2, e): pw.append(mm(pw[-1], B, N))
    for n in range(1, e):
        split = 1 if pw[n - 1][0][1] % 5 else 2
        g1, g2 = pw[split], pw[n - split]
        if g2[0][1] % 5 == 0:
            split = 3; g1, g2 = pw[split], pw[n - split]
        assert g1[0][1] % 5 and g2[0][1] % 5
        t = tr_pair(g1, g2, K); p_ = tr_pred(n, N)
        ok &= (t == p_)
        nm5 += (n % 2 == 0 and (n // 2) % 5 == 0)
    check("E", "P", f"K={K}: las {e-1} trazas tr U^n, n < 2*5^K, cumplen la formula exacta (incluidas las {nm5} con 5 | m)", ok)
if __name__ == "__main__":
    from collections import Counter
    print(dict(Counter(b for b, _, _ in LEDGER)))
    print(f"{len(LEDGER)} aserciones, 0 fallas")
