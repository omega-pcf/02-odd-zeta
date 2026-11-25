"""retro83.py — Sprint 83: (A) la demostracion por la formula del caracter; (B) el caso 5^k con fase exacta.
(A) Caracter de la representacion de Weil W de SL2(F_p), p >= 5, normalizada (unico levantamiento):
    g regular escindido, autovalor a in F_p:      tr W(g) = (a/p)            [C, se verifica]
    g eliptico, autovalor l in T = ker N, |T|=p+1: tr W(g) = -nu(l), nu el caracter cuadratico de T   [C, se verifica]
  De ahi, con g = M^{2n}: escindido tr = 1 (phi^{2n} es cuadrado); inerte tr = -(-1)^n (nu(phi^2) = phi^{p+1} = N(phi) = -1).
  Multiplicidades por Fourier finito: m_j = (1/e) sum_{n<e} tr(U^n) zeta^{-jn}  =>  (ii) y (iii)."""
import math, random
import numpy as np
from sympy import legendre_symbol, isprime
_g = {"__name__": "r81"}; exec(compile(open(__file__.replace("retro83.py", "retro81.py")).read().split("B = ((1, 1), (1, 2))")[0], "r81", "exec"), _g)
weil, mm, order = _g["weil"], _g["mm"], _g["order"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
def gauss(k, N): return sum(np.exp(2j * np.pi * (k * x * x % N) / N) for x in range(N))
def Wn(g, N): return math.sqrt(N) / gauss(pow(2 * g[0][1], -1, N), N) * weil(g, N)
def rand_sl2(N, rng, bunit=True):
    while True:
        a, b, c = rng.randrange(N), rng.randrange(N), rng.randrange(N)
        if math.gcd(a, N) != 1 or (bunit and math.gcd(b, N) != 1): continue
        return ((a, b), (c, (1 + b * c) * pow(a, -1, N) % N))
rng = random.Random(83)
# ---------------- A1: la formula del caracter, verificada sobre elementos al azar
def eig_class(g, p):
    t = (g[0][0] + g[1][1]) % p; D = (t * t - 4) % p
    if D == 0: return "par", None
    if legendre_symbol(D, p) == 1:
        s = next(x for x in range(p) if x * x % p == D); a = (t + s) * pow(2, -1, p) % p
        return "esc", a
    return "eli", t
def nu_of_trace(t, p):
    """caracter cuadratico de T en l, con l + 1/l = t: nu(l) = l^{(p+1)/2} calculado en F_{p^2} = F_p[x]/(x^2 - t x + 1)"""
    def mul(u, v): return ((u[0] * v[0] - u[1] * v[1]) % p, (u[0] * v[1] + u[1] * v[0] + t * u[1] * v[1]) % p)   # x^2 = t x - 1
    r, b_, e = (1, 0), (0, 1), (p + 1) // 2
    while e:
        if e & 1: r = mul(r, b_)
        b_ = mul(b_, b_); e >>= 1
    assert r[1] == 0 and r[0] in (1, p - 1); return 1 if r[0] == 1 else -1
cnt = {"esc": 0, "eli": 0}
for p in (7, 11, 13, 17, 19, 23):
    for _ in range(60):
        g = rand_sl2(p, rng); kind, x = eig_class(g, p)
        if kind == "par": continue
        tr = complex(np.trace(Wn(g, p)))
        pred = legendre_symbol(x, p) if kind == "esc" else -nu_of_trace(x, p)
        check("A1", "T", f"p={p} {kind}: tr W(g) = {pred}", abs(tr - pred) < 1e-7); cnt[kind] += 1
# ---------------- A2: los valores en las potencias de M^2
B = ((1, 1), (1, 2)); chi = lambda p: {1: 1, 4: 1, 2: -1, 3: -1}[p % 5]
PR = [p for p in range(7, 400) if isprime(p) and p != 5]
for p in PR:
    e = order(B, p)
    if chi(p) == 1:
        check("A2", "T", f"p={p} escindido: phi^2 es cuadrado en F_p, luego tr W(M^(2n)) = 1 para 0<n<e", all(legendre_symbol(pow(r, 2 * n, p), p) == 1 for r in [_g["np"] and next(x for x in range(p) if (x * x - x - 1) % p == 0)] for n in range(1, e)))
    else:
        check("A2", "T", f"p={p} inerte: nu(phi^2) = N(phi) = -1, luego tr W(M^(2n)) = -(-1)^n; y e es par", e % 2 == 0 and nu_of_trace(3 % p, p) == -1)   # traza de phi^2 = 3
# ---------------- A3: la formula de Fourier da (ii) y (iii), comparada con la diagonalizacion
def mult_from_traces(p, e):
    z = np.exp(2j * np.pi / e)
    tr = [p] + [1 if chi(p) == 1 else -(-1) ** n for n in range(1, e)]
    return [round((sum(tr[n] * z ** (-j * n) for n in range(e)) / e).real) for j in range(e)]
for p in PR:
    e = order(B, p); m = mult_from_traces(p, e)
    if chi(p) == 1: ok = m[0] == (p - 1) // e + 1 and all(x == (p - 1) // e for x in m[1:])
    else: ok = m[e // 2] == (p + 1) // e - 1 and all(x == (p + 1) // e for j, x in enumerate(m) if j != e // 2)
    check("A3", "P", f"p={p}: la formula de Fourier da (ii) y (iii)", ok)
for p in (7, 11, 13, 19, 29, 31, 41, 47):
    e = order(B, p); U = Wn(B, p); ev = np.linalg.eigvals(U)
    k = np.round(np.angle(ev) / (2 * np.pi) * e).astype(int) % e
    check("A3", "T", f"p={p}: coincide con la diagonalizacion", np.bincount(k, minlength=e).tolist() == mult_from_traces(p, e))
# ---------------- B: 5^k
res5 = {}
for N in (5, 25, 125):
    hom = True
    for _ in range(25):
        g, h = rand_sl2(N, rng), rand_sl2(N, rng); gh = mm(g, h, N)
        if math.gcd(gh[0][1], N) != 1: continue
        hom &= np.allclose(Wn(g, N) @ Wn(h, N), Wn(gh, N), atol=1e-7)
    check("B", "T", f"N={N}: la normalizacion por la suma de Gauss es homomorfismo exacto tambien en 5^k", hom)
    U = Wn(B, N); e = order(B, N)
    check("B", "T", f"N={N}: U^e = 1 sin fase", np.allclose(np.linalg.matrix_power(U, e), np.eye(N), atol=1e-6))
    trs = [complex(np.trace(np.linalg.matrix_power(U, n))) for n in range(e)]
    ev = np.linalg.eigvals(U); k = np.round(np.angle(ev) / (2 * np.pi) * e).astype(int) % e
    mult = np.bincount(k, minlength=e)
    z = np.exp(2j * np.pi / e)
    mF = [round((sum(trs[n] * z ** (-j * n) for n in range(e)) / e).real) for j in range(e)]
    check("B", "T", f"N={N}: la formula de Fourier con las trazas medidas reproduce el espectro", mF == mult.tolist())
    occ = sorted(j for j in range(e) if mult[j])
    res5[N] = dict(e=e, occ=occ, trs=trs, mult=mult)
    check("B", "T", f"N={N}: espectro simple que ocupa la mitad del circulo", set(mult.tolist()) == {0, 1} and len(occ) == N == e // 2)
    def tr_pred(n):
        if n % 2: return 1
        m = n // 2
        if m % N == 0: return N
        v = 0
        while m % 5 == 0: m //= 5; v += 1
        return 5 ** v * math.sqrt(5) * legendre_symbol(m % 5, 5)
    check("B", "T", f"N={N}: tr U^n = 1 para n impar; tr U^(2m) = 5^v sqrt5 (m'/5) con m = 5^v m' (la suma de Gauss del primo ramificado)", all(abs(trs[n] - tr_pred(n)) < 1e-6 for n in range(e)))
    chi5 = lambda j: {1: 1, 4: 1, 2: -1, 3: -1, 0: 0}[j % 5]
    check("B", "T", f"N={N}: fuera de los multiplos de 5, la fase j esta ocupada si y solo si chi5(j) = +1", all((mult[j] == 1) == (chi5(j) == 1) for j in range(e) if j % 5))
    res5[N]["occ5"] = [j // 5 for j in occ if j % 5 == 0]
check("B", "T", "autosimilaridad: las fases ocupadas multiplos de 5 en N=25 son las ocupadas en N=5, escaladas por 5", res5[25]["occ5"] == res5[5]["occ"])
check("B", "T", "autosimilaridad: y las de N=125 son las de N=25", res5[125]["occ5"] == res5[25]["occ"])
check("B", "T", "N=5: los multiplos de 5 ocupados son solo j=0 (j=5, el medio giro, esta vacio)", res5[5]["occ5"] == [0])
if __name__ == "__main__":
    print(f"A1: formula del caracter verificada en {cnt['esc']} escindidos y {cnt['eli']} elipticos")
    print(f"A2-A3: {len(PR)} primos hasta 400")
    for N, r in res5.items():
        t = [complex(np.round(x, 4)) for x in r["trs"][:12]]
        print(f"B N={N}: e={r['e']}, ocupadas {r['occ'][:16]}..., multiplos de 5 ocupados /5: {r['occ5'][:12]}; trazas n<12: {t}")
    print(f"{len(LEDGER)} aserciones, 0 fallas")
