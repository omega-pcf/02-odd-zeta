"""retro87.py — Sprint 87: la prueba uniforme en k de las trazas con 5 | m.
Formula LDT: si a (entrada superior izquierda de g) es unidad, g = L(c/a) D(a) T(b/a) y
  tr W(g) = (a/5)^K N^{-1} sum_{x,xi mod N} e( (A x^2 + Bc x xi + C xi^2)/N ),
con (A, Bc, C) una de las variantes de signo; se determina cual probando contra la traza real."""
import math, random, itertools
import numpy as np
from sympy import legendre_symbol
_g = {"__name__": "r86", "__file__": __file__.replace("retro87.py", "retro83.py")}
exec(compile(open(__file__.replace("retro87.py", "retro86.py")).read().split("# validacion contra la diagonalizacion")[0], "r86", "exec"), _g)
Wn, mm, S2, val, L5, v5, bpow = (_g[k] for k in ("Wn", "mm", "S2", "val", "L5", "v5", "bpow"))
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
def true_trace(g, K):
    N = 5 ** K
    if g[0][1] % 5: return np.trace(Wn(g, N))
    for h in (((1, 1), (0, 1)), ((1, 2), (0, 1)), ((2, 1), (1, 1)), ((1, 1), (1, 2))):
        hi = ((h[1][1] % N, -h[0][1] % N), (-h[1][0] % N, h[0][0] % N)); g2 = mm(hi, g, N)
        if g2[0][1] % 5: return np.trace(Wn(h, N) @ Wn(g2, N))
    raise ValueError
VARIANTS = list(itertools.product((1, -1), (1, -1), (0, 1), (1, -1)))   # signo de beta, de gamma, a o a^-1, signo cruzado
def form(g, K, var):
    N = 5 ** K; (a, b), (c, d) = g; ai = pow(a, -1, N); i2 = pow(2, -1, N)
    sb, sg, inv, sx = var
    beta, gamma = b * ai % N, c * ai % N
    return (sb * beta * i2 % N, sx * (1 - (ai if inv else a)) % N, sg * gamma * i2 % N)
def ldt(g, K, var):
    s, e = S2(*form(g, K, var), K); return L5(g[0][0]) ** K * s * 5 ** (e / 2 - K)
rng = random.Random(87)
def rand_g(K, cong=0):
    N = 5 ** K
    while True:
        a = rng.randrange(N); b = rng.randrange(N); c = rng.randrange(N)
        if cong: a = (1 + 5 ** cong * a) % N; b = 5 ** cong * b % N; c = 5 ** cong * c % N
        if a % 5 == 0: continue
        return ((a, b), (c, (1 + b * c) * pow(a, -1, N) % N))
tests = [(rand_g(K), K) for K in (1, 2, 3) for _ in range(25)] + [(rand_g(K, 1), K) for K in (2, 3) for _ in range(25)] + [(rand_g(3, 2), 3) for _ in range(15)]
truth = [true_trace(g, K) for g, K in tests]
good = [var for var in VARIANTS if all(abs(ldt(g, K, var) - t) < 1e-6 for (g, K), t in zip(tests, truth))]
check("F", "T", f"la formula LDT reproduce la traza en {len(tests)} elementos (unidades y congruentes a 1 mod 5, 25): variantes validas {good}", len(good) >= 1)
VAR = good[0]
# ---- la cadena de la prueba, para g = B^(2m) = M^(4m), m = 5^v m', v >= 1
B = ((1, 1), (1, 2))
for K in range(2, 8):
    N = 5 ** K
    for v in range(1, K):
        for mp in (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14):
            m = 5 ** v * mp
            a, b, c, d = fib(4 * m - 1) % N, fib(4 * m) % N, fib(4 * m) % N, fib(4 * m + 1) % N
            g = ((a, b), (c, d))
            check("C1", "P", f"K={K} v={v} m'={mp}: g = 1 (mod 5^v) y v5(b) = v", (a - 1) % 5 ** v == 0 and (d - 1) % 5 ** v == 0 and v5(fib(4 * m))[0] == v)
            A, X, Cc = form(g, K, VAR)
            check("C2", "P", f"K={K} v={v} m'={mp}: los tres coeficientes son multiplos de 5^v y A/5^v es unidad", A % 5 ** v == 0 and X % 5 ** v == 0 and Cc % 5 ** v == 0 and (A // 5 ** v) % 5 != 0)
            if K - v >= 2:
                A1, X1, C1 = A // 5 ** v, X // 5 ** v, Cc // 5 ** v; M_ = 5 ** (K - v)
                w = (C1 - X1 * X1 * pow(4 * A1, -1, M_)) % M_
                vw, wu = v5(w)
                check("C3", "P", f"K={K} v={v} m'={mp}: el segundo coeficiente tras completar el cuadrado tiene valuacion exactamente 1", vw == 1)
                check("C4", "P", f"K={K} v={v} m'={mp}: (A1 w'/5) = +1  [el producto de los dos simbolos no depende de K]", L5(A1) * L5(wu) == 1)
            check("C5", "P", f"K={K} v={v} m'={mp}: (A1/5) = chi5(m')  [F(4m)/5^v = 3m' (mod 5)]", L5(form(g, K, VAR)[0] // 5 ** v) == L5(mp) and (fib(4 * m) // 5 ** v) % 5 == 3 * mp % 5)
            s, e = S2(A, X, Cc, K)
            check("C6", "P", f"K={K} v={v} m'={mp}: tr = 5^v sqrt5 chi5(m')", (L5(a) ** K * s, e - 2 * K) == (L5(mp), 2 * v + 1))
# identidad usada en C5: F(5n) = F(n) (25 F(n)^4 + 25 (-1)^n F(n)^2 + 5)
check("I", "P", "F(5n) = F(n)(25 F(n)^4 + 25(-1)^n F(n)^2 + 5), n = 1..60: F(5n)/(5F(n)) = 1 (mod 5)", all(fib(5 * n) == fib(n) * (25 * fib(n) ** 4 + 25 * (-1) ** n * fib(n) ** 2 + 5) for n in range(1, 61)))
if __name__ == "__main__":
    from collections import Counter
    print("variante:", VAR, dict(Counter(b for b, _, _ in LEDGER)))
    print(f"{len(LEDGER)} aserciones, 0 fallas")
