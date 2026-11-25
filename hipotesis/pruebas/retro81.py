"""retro81.py — Sprint 81: el gato cuantizado de M^2 = [[1,1],[1,2]] (M = [[0,1],[1,1]], det M = -1) en N = 5^k y otros N,
con su grupo de Hecke C(N) = {x I + y B : det = 1} (unidades de norma 1 de Z[phi]/N), por la representacion de Weil (N impar).
Nucleo para g = [[a,b],[c,d]] con b unidad: U[y,x] = N^{-1/2} e((2b)^{-1}(a x^2 - 2 x y + d y^2)/N)."""
import math, itertools
import numpy as np
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
def mm(g, h, N): return tuple(tuple(sum(g[i][k] * h[k][j] for k in range(2)) % N for j in range(2)) for i in range(2))
I2 = ((1, 0), (0, 1))
def order(g, N, proj=False):
    h, n = g, 1
    while not (h == I2 or (proj and h == ((N - 1, 0), (0, N - 1)))): h = mm(h, g, N); n += 1
    return n
def weil(g, N):
    (a, b), (c, d) = g
    assert math.gcd(b, N) == 1
    k = pow(2 * b, -1, N); x = np.arange(N)
    ph = (k * (a * x[None, :] ** 2 - 2 * np.outer(x, x) + d * x[:, None] ** 2)) % N
    return np.exp(2j * np.pi * ph / N) / math.sqrt(N)
def prop_to(U, V):   # U = c V con |c| = 1
    i = np.unravel_index(np.argmax(np.abs(V)), V.shape); c = U[i] / V[i]
    return abs(abs(c) - 1) < 1e-8 and np.allclose(U, c * V, atol=1e-8), c
def uperiod(U, maxn):
    P = np.eye(len(U), dtype=complex)
    for n in range(1, maxn + 1):
        P = P @ U
        ok, c = prop_to(P, np.eye(len(U)))
        if ok: return n, c
    return None, None
B = ((1, 1), (1, 2))     # M^2
M = ((0, 1), (1, 1))
rows = {}
for N in (5, 25, 125, 3, 7, 9, 11, 19, 29, 31):
    U = weil(B, N)
    check("W", "T", f"N={N}: U(B) unitaria", np.allclose(U @ U.conj().T, np.eye(N), atol=1e-9))
    # homomorfismo proyectivo sobre potencias con b unidad
    g2 = mm(B, B, N)
    if math.gcd(g2[0][1], N) == 1:
        check("W", "T", f"N={N}: U(B)U(B) ~ U(B^2) (Weil es representacion proyectiva)", prop_to(U @ U, weil(g2, N))[0])
    oB, oBp, oM = order(B, N), order(B, N, True), order(M, N)
    per, c = uperiod(U, 4 * oB)
    # espectro: fases propias y multiplicidades
    ev = np.linalg.eigvals(U)
    ang = np.round(np.angle(ev / c ** (1 / per) if False else ev) / (2 * np.pi) * per * 8) / 8   # en unidades de 1/per de vuelta
    lam = c ** (1.0 / per)
    k_ = np.round(np.angle(ev / lam) / (2 * np.pi) * per).astype(int) % per
    check("W", "T", f"N={N}: las fases propias son raices {per}-esimas de la unidad (salvo fase global)", np.allclose(ev, lam * np.exp(2j * np.pi * k_ / per), atol=1e-6))
    mult = np.bincount(k_, minlength=per)
    # grupo de Hecke
    C = [((x_ + y_) % N, y_ % N) for x_ in range(N) for y_ in range(N) if ((x_ + y_) * (x_ + 2 * y_) - y_ * y_) % N == 1]   # x I + y B, det = 1
    # donde cae la anomalia, en fase absoluta (autovalor = e(k/per) * lam)
    base = int(np.bincount(mult).argmax()) if N % 5 else 1
    anom = [(int(j), complex(np.round(lam * np.exp(2j * np.pi * j / per), 6))) for j in range(per) if mult[j] != base]
    rows[N] = dict(oM=oM, oB=oB, per=per, mult=mult, hecke=len(C), base=base, anom=anom)
for k, N in ((1, 5), (2, 25), (3, 125)):
    r = rows[N]
    check("R", "T", f"N=5^{k}: el orden de M modulo 5^{k} es 4*5^{k} = {4 * 5 ** k} (el periodo de Pisano) y el de M^2 es 2*5^{k}", r["oM"] == 4 * 5 ** k and r["oB"] == 2 * 5 ** k)
    check("R", "T", f"N=5^{k}: el periodo del propagador U(M^2) es el orden de M^2 modulo 5^{k}", r["per"] == r["oB"])
    check("H", "T", f"N=5^{k}: el grupo de Hecke tiene orden 2*5^{k} = {2 * 5 ** k}, igual al periodo: lo generan las potencias de M^2", r["hecke"] == 2 * 5 ** k == r["per"])
    check("D", "T", f"N=5^{k}: N/periodo = 1/2: hay el doble de fases posibles que de dimension; cada fase aparece 0 o 1 veces", set(np.unique(r["mult"])) <= {0, 1} and int(r["mult"].sum()) == N)
chi = lambda p: {1: 1, 4: 1, 2: -1, 3: -1}[p % 5]
for p in (3, 7, 11, 19, 29, 31):
    r = rows[p]
    check("D", "T", f"p={p}: N = periodo * m + chi5(p), con m = {r['base']} la multiplicidad comun: sobra un estado si p escinde, falta uno si es inerte", p == r["per"] * r["base"] + chi(p) and len(r["anom"]) == 1)
    check("D", "T", f"p={p}: m es el indice de phi^2 en el grupo del lugar: (p - chi5(p)) / periodo", r["base"] == (p - chi(p)) // r["per"])
if __name__ == "__main__":
    print("anomalias (indice de fase, autovalor):", {N: r["anom"] if N % 5 else ("vacias: " + str([j for j, _ in r["anom"]][:10])) for N, r in rows.items()})
    for N, r in rows.items():
        m = r["mult"]
        print(f"N={N:>4}: reloj de phi {r['oM']:>4}, orden de M^2 {r['oB']:>4}, periodo de U {r['per']:>4}, |Hecke| {r['hecke']:>4}, N/periodo {N / r['per']:.2f}, multiplicidades {dict(zip(*np.unique(m, return_counts=True)))}")
    print(f"{len(LEDGER)} aserciones, 0 fallas")
