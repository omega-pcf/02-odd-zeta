"""retro67.py — Sprint 67: la positividad de Weil nivel por nivel.

Formula explicita (Guinand-Weil) para L con Lambda(s) = q^{s/2} Gamma_R(s)^d L(s) y polo en 1:
  sum_gamma h(gamma) = h(i/2) + h(-i/2) + g(0)(log q - d log pi) + (d/2pi) int h(r) Re psi(1/4 + i r/2) dr
                       - sum_m Lambda_L(m) m^{-1/2} (g(log m) + g(-log m)),
  h(r) = int g(u) e^{iru} du.  zeta: q = 1, d = 1.  zeta_K, K = Q(phi): q = 5, d = 2, suma sobre ideales.
Con g = h0 * h0~ y h0 de soporte en [-L/2, L/2], el lado izquierdo es sum |h0^(gamma)|^2 >= 0 bajo GRH (Weil).
Base: escalones en N celdas; W = Pole + c0 G0 + Psi - sum_n P_n, con P_n la contribucion del nivel n del reloj.
"""
import math, random, warnings
warnings.filterwarnings('ignore')
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.special import psi as cpsi
from sympy import primerange, sqrt_mod, n_order, factorint, mobius
from collections import defaultdict, Counter

LEDGER = []
def check(b, c, name, cond):
    assert cond, name
    LEDGER.append((b, c, name))

# ---------------- 0: la formula, contra los ceros de zeta
ell = 2.0
def h0(x): return math.cos(math.pi * x / ell) ** 2 if abs(x) <= ell / 2 else 0.0
def g0(u): return quad(lambda x: h0(x) * h0(x - u), max(-ell / 2, u - ell / 2), min(ell / 2, u + ell / 2), limit=200)[0] if abs(u) < ell else 0.0
_a = 2 * math.pi / ell
def _s(w):  # int_{-ell/2}^{ell/2} cos(w x) dx / 2 ... = sin(w ell/2)/w, con limite ell/2
    return ell / 2 if abs(w) < 1e-12 else math.sin(w * ell / 2) / w
def h0hat(r):  # transformada exacta de cos^2(pi x/ell) en [-ell/2, ell/2]
    return _s(r) + 0.5 * (_s(r - _a) + _s(r + _a))
def hz(r): return h0hat(r) ** 2
a_p = quad(lambda x: h0(x) * math.exp(x / 2), -ell / 2, ell / 2)[0]
a_m = quad(lambda x: h0(x) * math.exp(-x / 2), -ell / 2, ell / 2)[0]
def repsi(r): return float(np.real(cpsi(0.25 + 0.5j * r)))
arch_z = quad(lambda r: hz(r) * repsi(r), 0, 400, limit=400)[0] / math.pi    # (1/2pi) int_R = (1/pi) int_0^inf
primes_side = 0.0
for p in primerange(2, int(math.exp(ell)) + 1):
    k, pk = 1, p
    while math.log(pk) < ell:
        primes_side += math.log(p) / math.sqrt(pk) * 2 * g0(math.log(pk)); k += 1; pk *= p
rhs = 2 * a_p * a_m - g0(0) * math.log(math.pi) + arch_z - primes_side
mp.mp.dps = 20
zeros = [float(mp.zetazero(k).imag) for k in range(1, 81)]
lhs = 2 * sum(hz(t) for t in zeros)
tail = 2 * quad(lambda r: hz(r) * math.log(r / (2 * math.pi)) / (2 * math.pi), zeros[-1], 5000, limit=2000)[0]
check("0", "T", f"formula explicita de zeta con un bump (terminos de orden 1 que se cancelan): lado de ceros {lhs:.8f} (+cola {tail:.1e}) = lado de primos {rhs:.8f}",
      abs(lhs + tail - rhs) < 1e-8 and max(abs(2 * a_p * a_m), abs(arch_z), abs(primes_side)) > 0.1)
SANITY = dict(ceros=lhs, primos=rhs, dif=lhs + tail - rhs, polo=2 * a_p * a_m, g0=-g0(0) * math.log(math.pi), arq=arch_z, primos_lado=-primes_side)

# ---------------- 1: la forma cuadratica para zeta_K por niveles
def chi5(p): return {1: 1, 4: 1, 2: -1, 3: -1}.get(p % 5, 0)
def _gmul(x, y, m): return ((x[0]*y[0] + x[1]*y[1]) % m, (x[0]*y[1] + x[1]*y[0] + x[1]*y[1]) % m)
def _gpow(x, e, m):
    r = (1, 0)
    while e:
        if e & 1: r = _gmul(r, x, m)
        x = _gmul(x, x, m); e >>= 1
    return r
def inert_order(p):
    m = 2 * (p + 1); o = m
    for q in factorint(m):
        while o % q == 0 and _gpow((0, 1), o // q, p) == (1, 0): o //= q
    return o
def ideals_upto(X):
    out = [(4, "2"), (5, "5")]          # 2 inerte (norma 4) y sqrt5 ramificado: fuera del reloj
    for p in primerange(3, X + 1):
        if p == 5: continue
        if chi5(p) == 1:
            inv2 = pow(2, -1, p)
            for s in sqrt_mod(5, p, all_roots=True): out.append((p, n_order((1 + s) * inv2 % p, p)))
        elif p * p <= X: out.append((p * p, inert_order(p)))
    return out

def build(L, N):
    D = L / N
    x = -L / 2 + (np.arange(N) + 0.5) * D
    d = x[:, None] - x[None, :]
    T = lambda v: np.maximum(0.0, D - np.abs(v))
    G0 = D * np.eye(N)
    vp = np.array([(math.exp((xj + D / 2) / 2) - math.exp((xj - D / 2) / 2)) * 2 for xj in x])
    vm = np.array([-(math.exp(-(xj + D / 2) / 2) - math.exp(-(xj - D / 2) / 2)) * 2 for xj in x])
    Pole = np.outer(vp, vm) + np.outer(vm, vp)
    def f(r, m=0): return D * D * (np.sinc(r * D / (2 * math.pi))) ** 2 * repsi(r) * math.cos(m * D * r)
    def lowm(m, R=1e5):   # tramos de medio periodo hasta R + cola analitica de la componente de frecuencia 0
        step = math.pi / ((m + 1) * D); s_ = 0.0; a_ = 0.0
        while a_ < R:
            b_ = min(a_ + step, R); s_ += quad(f, a_, b_, args=(m,), epsabs=1e-14, epsrel=1e-12)[0]; a_ = b_
        return s_ + {0: 1.0, 1: -0.5}.get(m, 0.0) * 2 * (math.log(R / 2) + 1) / R
    def qawf(m): return quad(lambda r: f(r), 0, np.inf, weight="cos", wvar=m * D, limlst=400)[0]
    psim = [(lowm(m) if m <= 4 else qawf(m)) / math.pi for m in range(N)]
    JOIN = abs(lowm(5) - qawf(5))
    Psi1 = np.array([[psim[abs(i - j)] for j in range(N)] for i in range(N)])
    def Pform(lst):
        M = np.zeros((N, N))
        for Nrm in lst:
            k, Nk = 1, Nrm
            while math.log(Nk) < L:
                w = math.log(Nrm) / math.sqrt(Nk); u = math.log(Nk)
                M += w * (T(u - d) + T(-u - d)); k += 1; Nk *= Nrm
        return M
    return dict(x=x, D=D, G0=G0, Pole=Pole, Psi1=Psi1, Pform=Pform, JOIN=JOIN)

X = 1000; L = math.log(X); N = 48
B = build(L, N)
ids = ideals_upto(X)
groups = defaultdict(list)
for Nrm, lev in ids: groups[lev].append(Nrm)
A = B["Pole"] + (math.log(5) - 2 * math.log(math.pi)) * B["G0"] + 2 * B["Psi1"]
Pn = {lev: B["Pform"](v) for lev, v in groups.items()}
P = sum(Pn.values())
W = A - P
eW = np.linalg.eigvalsh(W); eA = np.linalg.eigvalsh(A)
check("1", "T", f"integrales de psi: el metodo por tramos y QAWF empalman en m = 5 (dif {B['JOIN']:.1e})", B["JOIN"] < 1e-8)
check("1", "T", f"W de zeta_K es semidefinida (GRH para zeta_K, verificada numericamente a gran altura): lambda_min = {eW[0]:.2e}",
      eW[0] > -1e-8 * abs(eW[-1]))
# misma prueba con zeta sola, como control de la maquinaria matricial
Bz = B
Az = Bz["Pole"] - math.log(math.pi) * Bz["G0"] + Bz["Psi1"]
Pz = Bz["Pform"]([p for p in primerange(2, X + 1) for _ in [0]])
eWz = np.linalg.eigvalsh(Az - Pz)
check("1", "T", f"control: la misma maquinaria con zeta da W semidefinida, lambda_min = {eWz[0]:.2e}", eWz[0] > -1e-8 * abs(eWz[-1]))

# ---------------- 2: diagnosticos por nivel
lmin = lambda M: float(np.linalg.eigvalsh(M)[0])
check("2", "T", "sin primos no hay positividad: A (arquimediana + polo) tiene lambda_min < 0", eA[0] < -1)
# (a) dejar fuera un nivel: W + P_n
loo = {lev: lmin(W + M) for lev, M in Pn.items()}
need = sorted((v, lev) for lev, v in loo.items() if v < 0)
# (b) caminos: niveles en orden de reloj contra grupos en orden de tamano con los mismos tamanos de grupo
clock = sorted(Pn, key=lambda v: (v is None, v if isinstance(v, int) else 10**9))
def path(order_groups):
    M = A.copy(); out = []
    for G in order_groups: M = M - G; out.append(lmin(M))
    return out
pc = path([Pn[l] for l in clock])
allN = sorted(Nrm for Nrm, _ in ids)
sizes = [len(groups[l]) for l in clock]
sz_groups, k = [], 0
for t in sizes: sz_groups.append(B["Pform"](allN[k:k + t])); k += t
ps = path(sz_groups)
first_pos = lambda pth: next((i + 1 for i, v in enumerate(pth) if v >= 0), None)
check("2", "T", "los dos caminos terminan en la misma W", abs(pc[-1] - ps[-1]) < 1e-9 and abs(pc[-1] - eW[0]) < 1e-9)
# (c) reparto escalar: max_t lambda_min(t A - P_n) para cada nivel
def best_share(M):
    lo, hi = 0.0, 50.0
    for _ in range(80):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if lmin(m1 * A - M) < lmin(m2 * A - M): lo = m1
        else: hi = m2
    return lo, lmin(lo * A - M)
shares = {lev: best_share(M) for lev, M in Pn.items()}
nofeas = [lev for lev, (t, v) in shares.items() if v < -1e-10]
check("2", "T", "reparto escalar A_n = t_n A: ningun nivel admite t_n con t_n A - P_n semidefinida", len(nofeas) == len(Pn))

# (d) la direccion decisiva: autovector negativo de A (la del polo, impar tipo senh)
evA, VA = np.linalg.eigh(A)
v1 = VA[:, 0]
odd = np.allclose(v1, -v1[::-1], atol=1e-6) or np.allclose(v1, v1[::-1], atol=1e-6)
contrib = {lev: float(-v1 @ M @ v1) for lev, M in Pn.items()}   # aporte de -P_n a lo largo de v1
pos = sum(1 for c in contrib.values() if c > 0)
def sign_analysis(Bx, Ax, Lx, idsx):
    ev, V = np.linalg.eigh(Ax); w1 = V[:, 0]
    D_ = Bx["D"]; xx = Bx["x"]; dd = xx[:, None] - xx[None, :]
    T_ = lambda v: np.maximum(0.0, D_ - np.abs(v))
    cu = lambda u: float(-w1 @ (T_(u - dd) + T_(-u - dd)) @ w1)       # aporte de peso 1 en u = log N
    us = np.linspace(0.01, Lx, 2000); cs = [cu(u) for u in us]
    zc = [float(us[i]) for i in range(len(us) - 1) if cs[i] * cs[i + 1] < 0]
    neg = sorted({lev for Nrm, lev in idsx if cu(math.log(Nrm)) * math.log(Nrm) / math.sqrt(Nrm) < 0}, key=str)
    gx = defaultdict(list)
    for Nrm, lev in idsx: gx[lev].append(Nrm)
    gneg = sorted([lev for lev, v in gx.items() if float(-w1 @ Bx["Pform"](v) @ w1) < 0], key=str)
    return ev[0], zc, neg, gneg, len(gx)
SIGN = {}
for Xs in (1000, 3000, 10000, 30000):
    Ls = math.log(Xs); Bs = build(Ls, N)
    As = Bs["Pole"] + (math.log(5) - 2 * math.log(math.pi)) * Bs["G0"] + 2 * Bs["Psi1"]
    SIGN[Xs] = sign_analysis(Bs, As, Ls, ideals_upto(Xs))
check("2", "T", "X = 1000: en la direccion del polo, solo los dos grupos fuera del reloj (2 y sqrt5) aportan en negativo", sorted(map(str, SIGN[1000][3])) == ["2", "5"] and pos == len(contrib) - 2)
check("2", "T", "pero el signo lo fija el tamano: un ideal suelto aporta en negativo si log N < u*, con u*/L entre 0.36 y 0.39 en las cuatro ventanas",
      all(len(v[1]) == 1 and 0.36 < v[1][0] / math.log(Xs) < 0.39 for Xs, v in SIGN.items()))
check("2", "T", "al crecer la ventana, niveles completos del reloj pasan a aportar en negativo", len(SIGN[30000][3]) > 2)
check("2", "T", "y la suma de los aportes compensa al polo: lambda_1(A) + sum = v1' W v1 >= 0", abs(evA[0] + sum(contrib.values()) - float(v1 @ W @ v1)) < 1e-9 and float(v1 @ W @ v1) > 0)
# el signo, ¿es del nivel o del tamano? aporte de un ideal suelto en funcion de log N
single = sorted((math.log(Nrm), float(-v1 @ B["Pform"]([Nrm]) @ v1)) for Nrm, _ in ids)
check("R", "R", "lectura: ver tabla de umbrales por X en el reporte", True)
# en la segunda direccion negativa de A
v2 = VA[:, 1]
c2 = {lev: float(-v2 @ M @ v2) for lev, M in Pn.items()}
pos2 = sum(1 for c in c2.values() if c > 0)

if __name__ == "__main__":
    print(f"2d) v1 simetrica o antisimetrica: {odd}; aportes positivos {pos}/{len(contrib)}; suma {sum(contrib.values()):.4f} contra lambda_1(A) = {evA[0]:.4f}")
    for Xs, (l1, zc, neg, gneg, ng) in SIGN.items(): print(f"    X={Xs}: lambda_1(A)={l1:.2f}, umbral u*={zc[0]:.3f} (u*/L={zc[0] / math.log(Xs):.3f}); grupos con aporte negativo {len(gneg)}/{ng}: {gneg}")
    print(f"    segunda direccion (lambda = {evA[1]:.4f}): aportes positivos {pos2}/{len(c2)}, suma {sum(c2.values()):.4f}")
    print(f"2a) niveles cuya ausencia rompe la positividad: {len(need)} de {len(Pn)}; los peores:", [(lev, round(v, 4)) for v, lev in need[:8]])
    print(f"2b) camino reloj: primer paso positivo {first_pos(pc)} de {len(pc)}; camino tamano: {first_pos(ps)}")
    print("    lambda_min reloj (cada 10):", [round(v, 3) for v in pc[::10]])
    print("    lambda_min tamano (cada 10):", [round(v, 3) for v in ps[::10]])
    print("2c) mejor reparto escalar, los 6 menos malos:", sorted((round(v, 4), lev, round(t, 3)) for lev, (t, v) in shares.items())[-6:])
    print("    orden de reloj:", clock[:12])
    print("0) ceros", SANITY)
    print(f"1) X={X}, L={L:.3f}, N={N}: niveles {len(groups)}; espectro W: {eW[:4]} ... {eW[-1]:.3g}")
    print(f"   espectro A: {eA[:4]} ... {eA[-1]:.3g}")
    print(f"   zeta: W {eWz[:3]}")
    print(f"{len(LEDGER)} aserciones, 0 fallas")
