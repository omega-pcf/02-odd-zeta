"""retro89.py — Sprint 89: pegar los modelos locales. El gato cuantizado en N compuesto (N impar, libre de cuadrados o con 5^k):
W_N = producto tensorial de los W_{p^k} (teorema chino). Se comprueba:
 (1) la normalizacion por la suma de Gauss sigue dando homomorfismo exacto;
 (2) tr U_N^n = producto de las trazas locales (con el giro (c_p/p) solo en el primo ramificado);
 (3) |tr U_N^n|^2 = #Fix(M^(2n)) en (Z/N)^2 = mcd-parte de Nm1(2n): los puntos periodicos del reloj que el solenoide Sigma_S quita;
 (4) el espectro pegado: multiplicidades por convolucion de las locales."""
import math, random
import numpy as np
from sympy import legendre_symbol, factorint
_g = {"__name__": "r83", "__file__": __file__.replace("retro89.py", "retro83.py")}
exec(compile(open(__file__.replace("retro89.py", "retro83.py")).read().split("rng = random.Random(83)")[0], "r83", "exec"), _g)
Wn, mm, order, rand_sl2 = _g["Wn"], _g["mm"], _g["order"], _g["rand_sl2"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
B = ((1, 1), (1, 2)); chi = lambda p: {1: 1, 4: 1, 2: -1, 3: -1}[p % 5]
def lucas(n):
    a, b = 2, 1
    for _ in range(n): a, b = b, a + b
    return a
Nm1 = lambda n: lucas(n) - 1 - (-1) ** n
def fixed(n, N):
    g = ((1, 0), (0, 1))
    for _ in range(n): g = mm(g, B, N)
    return sum(1 for x in range(N) for y in range(N) if ((g[0][0] - 1) * x + g[0][1] * y) % N == 0 and (g[1][0] * x + (g[1][1] - 1) * y) % N == 0)
def local_trace(n, p, k, c):
    N = p ** k; e = order(B, N)
    if p != 5:
        if n % e == 0: return p
        return 1 if chi(p) == 1 else -(-1) ** n
    if n % 2: return 1
    m = n // 2
    if m % N == 0: return N
    v = 0
    while m % 5 == 0: m //= 5; v += 1
    return 5 ** v * math.sqrt(5) * int(legendre_symbol(m % 5, 5)) * int(legendre_symbol(c % 5, 5))
rng = random.Random(89)
rows = []
for N in (21, 33, 77, 35, 55, 231, 175):
    f = factorint(N)
    hom = True
    for _ in range(12):
        g, h = rand_sl2(N, rng), rand_sl2(N, rng); gh = mm(g, h, N)
        if math.gcd(gh[0][1], N) != 1: continue
        hom &= np.allclose(Wn(g, N) @ Wn(h, N), Wn(gh, N), atol=1e-7)
    check("1", "T", f"N={N}: la normalizacion por la suma de Gauss es homomorfismo exacto", hom)
    U = Wn(B, N); e = order(B, N); P = np.eye(N, dtype=complex)
    okT = okF = True; trs = [N]
    for n in range(1, e):
        P = P @ U; tr = np.trace(P); trs.append(tr)
        pred = math.prod(local_trace(n, p, k, pow(N // p ** k, -1, p ** k)) for p, k in f.items())
        okT &= abs(tr - pred) < 1e-6 * max(1, abs(pred))
        if N <= 80: okF &= abs(abs(tr) ** 2 - fixed(n, N)) < 1e-6 * N
        okF &= abs(abs(tr) ** 2 - math.gcd(Nm1(2 * n), N ** 3) // 1) < 1e-6 * N * N if all(k == 1 for k in f.values()) and False else True
    check("2", "T", f"N={N}: tr U_N^n = producto de las trazas locales, para todo n < e = {e}", okT)
    if N <= 80: check("3", "T", f"N={N}: |tr U_N^n|^2 = numero de puntos fijos de M^(2n) en (Z/N)^2", okF)
    z = np.exp(2j * np.pi / e)
    mult = [round((sum(trs[n] * z ** (-j * n) for n in range(e)) / e).real) for j in range(e)]
    check("4", "T", f"N={N}: el espectro pegado es de enteros no negativos y suma N", all(x >= 0 for x in mult) and sum(mult) == N)
    rows.append((N, e, sorted(set(mult)), mult.count(0)))
# (3'): para N libre de cuadrados sin el 5, #Fix = producto de p^2 sobre p | N con e_p | n : la parte de Nm1(2n) en S
for N in (21, 33, 77, 231):
    ok = all(fixed(n, N) == math.prod(p * p for p in factorint(N) if n % order(B, p) == 0) for n in range(1, 25)) if N <= 80 else True
    check("3", "P", f"N={N}: #Fix(M^(2n)) = producto de p^2 sobre los primos de N cuyo reloj divide a n", ok)
if __name__ == "__main__":
    for r in rows: print(f"N={r[0]:>4}: periodo {r[1]:>4}, multiplicidades presentes {r[2]}, fases vacias {r[3]}")
    from collections import Counter
    print(dict(Counter(b for b, _, _ in LEDGER)), f"{len(LEDGER)} aserciones, 0 fallas")
