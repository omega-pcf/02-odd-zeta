"""retro66.py — Sprint 66: quitar la hipotesis H del sprint 65.

Ruta 1 (soporte, marco de Weil). Para g con soporte en [-L, L] el lado de primos de la formula explicita de
zeta_K (K = Q(phi)) solo tiene ideales primos con N(P)^k <= X = e^L. En el nivel n esos ideales tienen indice
i <= 2(X + 1)/n. La criba por niveles con esa cota da el lado de primos EXACTO, sin hipotesis.

Ruta 2 (altura). Los ceros de zeta_K = zeta * L(chi5) ven TODOS los ideales primos, no solo los del nivel.
Medimos el vecino real (cualquier norma de ideal primo) contra el vecino admisible del nivel (hipotesis H).
"""
import math, time
from collections import Counter, defaultdict
from sympy import sqrt_mod, primerange, nextprime, isprime, factorint, n_order

LEDGER = []
def check(b, c, name, cond):
    assert cond, name
    LEDGER.append((b, c, name))

def _gmul(x, y, m): return ((x[0]*y[0] + x[1]*y[1]) % m, (x[0]*y[1] + x[1]*y[0] + x[1]*y[1]) % m)
def _gpow(x, e, m):
    r = (1, 0)
    while e:
        if e & 1: r = _gmul(r, x, m)
        x = _gmul(x, x, m); e >>= 1
    return r
def chi5(p): return {1: 1, 4: 1, 2: -1, 3: -1}.get(p % 5, 0)
def split_roots(p):
    inv2 = pow(2, -1, p)
    return [(1 + s) * inv2 % p for s in sqrt_mod(5, p, all_roots=True)]
def inert_order(p):
    m = 2 * (p + 1); o = m
    for q in factorint(m):
        while o % q == 0 and _gpow((0, 1), o // q, p) == (1, 0): o //= q
    return o

# ---------------- S: ruta 1, soporte compacto
X = 10 ** 6; L = math.log(X)
t0 = time.time()
ideals = []           # (norma, nivel, indice, tipo)
for p in primerange(3, X + 1):
    if p == 5: continue
    if chi5(p) == 1:
        for r in split_roots(p):
            n = n_order(r, p); ideals.append((p, n, (p - 1) // n, "e"))
    elif p * p <= X:
        n = inert_order(p); ideals.append((p * p, n, 2 * (p + 1) // n, "i"))
special = [(4, None, None, "2"), (5, None, None, "5")]   # 2 inerte (norma 4) y 5 ramificado: fuera del reloj
tS = time.time() - t0
check("S", "T", "todo ideal primo de norma <= X (salvo 2 y 5) tiene nivel n >= 3", all(n >= 3 for _, n, _, _ in ideals))
check("S", "T", "cota de indice: N(P) <= X  =>  i <= 2(X + 1)/n en todo ideal",
      all(i <= 2 * (X + 1) / n for _, n, i, _ in ideals))
check("S", "T", "escindido: p = n i + 1; inerte: 2(p + 1) = n i (la forma de la criba)",
      all((t == "e" and N == n * i + 1) or (t == "i" and 2 * (math.isqrt(N) + 1) == n * i) for N, n, i, t in ideals))

# la criba por niveles: candidatos con la forma del nivel e indice <= 2(X+1)/n, primo y de orden n
PR = bytearray(X + 2)
for q in primerange(2, X + 2): PR[q] = 1
order_cache = {}
def level_of_split(p):
    if p not in order_cache: order_cache[p] = sorted(n_order(r, p) for r in split_roots(p))
    return order_cache[p]
t1 = time.time()
sieved = []; ncand = 0
RX = math.isqrt(X)
for n in range(3, 2 * (X + 1) + 1):
    for i in range(1, (X - 1) // n + 1):          # escindidos: p = n i + 1 <= X
        p = n * i + 1; ncand += 1
        if PR[p] and p != 5 and chi5(p) == 1:
            sieved += [(p, n, i, "e")] * level_of_split(p).count(n)
    for i in range(1, 2 * (RX + 1) // n + 1):     # inertes: q = n i / 2 - 1, q^2 <= X
        if (n * i) % 2: continue
        q = n * i // 2 - 1; ncand += 1
        if 2 < q and q * q <= X and PR[q] and q != 5 and chi5(q) == -1 and inert_order(q) == n:
            sieved.append((q * q, n, i, "i"))
tC = time.time() - t1
check("S", "T", "la criba por niveles con i <= 2(X+1)/n da exactamente los ideales primos de norma <= X",
      Counter(sieved) == Counter(ideals))

# lado de primos con g triangulo de soporte [-L, L] (g = 1_[-L/2,L/2] * 1_[-L/2,L/2], g^ = sinc^2 >= 0: clase de Weil)
def g(u): return max(0.0, 1 - abs(u) / L)
def prime_side(lst):
    s = 0.0
    for N, _, _, _ in lst:
        k, Nk = 1, N
        while Nk <= X:
            s += math.log(N) * g(k * math.log(N)) / math.sqrt(Nk); k += 1; Nk *= N
    return s
ps_direct = prime_side(ideals + special)
by_level = defaultdict(list)
for t in sieved: by_level[t[1]].append(t)
ps_levels = prime_side(special) + sum(prime_side(v) for v in by_level.values())
check("S", "T", "el lado de primos de Weil, sumado nivel por nivel desde la criba, es el directo (error < 1e-9)",
      abs(ps_direct - ps_levels) < 1e-9 * max(1.0, abs(ps_direct)))
nprimes = sum(1 for _ in primerange(2, X + 1))
check("S", "T", "costo: los candidatos son del orden X ln X (casi lineal en X = e^L)",
      0.5 < ncand / (X * math.log(X)) < 2)

# ---------------- H: ruta 2, el vecino real contra el admisible
_src = open(__file__.replace("retro66.py", "retro65.py")).read()
_g = {"__file__": __file__.replace("retro66.py", "retro65.py"), "__name__": "retro65"}
exec(compile(_src, "retro65", "exec"), _g)
rows = _g["rows"]      # (n, p, split, i, s_adm, T_adm) con c = 2 pi
c = 2 * math.pi
def next_norm(p):
    """siguiente norma de ideal primo de Q(phi) mayor que p (escindido q, inerte q^2, 4, 5)."""
    q = nextprime(p)
    while chi5(q) != 1 and q != 5: q = nextprime(q)
    best = q
    r = math.isqrt(p) + 1
    while r * r <= best:
        if isprime(r) and chi5(r) == -1 and r * r > p: best = min(best, r * r); break
        r += 1
    return best
H = []
for n, p, sp, i, s, Ta in rows:
    N = p if sp else p * p
    gall = next_norm(N) - N
    Tall = c / math.log1p(gall / N)
    H.append((n, p, sp, i, s, gall, Ta, Tall))
ratio = sorted(h[7] / h[6] for h in H)
check("H", "T", "en mas del 90 % de los primos el vecino real (cualquier ideal primo) esta mas cerca que el admisible del nivel",
      sum(1 for h in H if h[5] < (h[4] if h[2] else h[4] * (2 * h[1]))) >= 0.9 * len(H))
check("H", "T", "la altura con vecinos reales supera a la del modelo H en la mediana por mas de 10 veces", ratio[len(ratio) // 2] > 10)
same_i = defaultdict(list)
for h in H: same_i[h[3]].append(h[7])
spread = max(max(v) / min(v) for v in same_i.values() if len(v) >= 2)
check("H", "T", "con vecinos reales la altura no es funcion del indice: con el mismo i varia mas de 100 veces (514 con i = 1)", spread > 100)
check("H", "T", "con vecinos reales la altura escala como p / hueco entre primos (T_all >= c N / (hueco))",
      all(h[7] >= c * (h[1] if h[2] else h[1] ** 2) / h[5] * (1 - 1e-12) for h in H))

if __name__ == "__main__":
    print(f"S) X = 1e6 (L = {L:.2f}): {len(ideals)} ideales primos del reloj ({tS:.1f}s); criba {ncand} candidatos ({tC:.1f}s), "
          f"{ncand/nprimes:.0f} por primo; lado de primos {ps_direct:.6f} = {ps_levels:.6f}")
    print(f"   niveles con ideales de norma <= X: {len(by_level)}")
    print(f"H) {len(H)} primos; T_real / T_H: min {ratio[0]:.2g}, mediana {ratio[len(ratio)//2]:.3g}, max {ratio[-1]:.3g}")
    print("   ejemplos (n, p, i, hueco adm, hueco real, T_H, T_real):",
          [(h[0], h[1], h[3], h[4], h[5], f"{h[6]:.0f}", f"{h[7]:.3g}") for h in sorted(H, key=lambda h: h[1])[:6]])
    print(f"   mismo indice, dispersion maxima de T_real: {spread:.3g}")
    print(dict(Counter((b, c_) for b, c_, _ in LEDGER)))
    print(f"{len(LEDGER)} aserciones, 0 fallas")
