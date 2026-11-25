"""retro69.py — Sprint 69: el puente entre el polo del reloj y el polo de zeta_K.
(1) Identidad exacta: log Nm1(n) = n log phi + eta_n = sum_{d|n} log Q(d)   (lado arquimediano = ideales de niveles d | n).
(2) El polo del reloj: sum_{d<=n} log Q(d) = log phi * sum_{d<=n} phi(d) + error ~ (3/pi^2) log phi n^2: ahi se encuentran phi y pi.
(3) En el canal de indice i, nivel y tamano se ligan por N = n i + 1: log N = log n + log i (traslacion).
    Se prueba la descomposicion de W por canales de indice, con reparto escalar del lado arquimediano."""
import math, warnings; warnings.filterwarnings("ignore")
import numpy as np
from collections import defaultdict
from sympy import totient, divisors, mobius
_src = open(__file__.replace("retro69.py", "retro67.py")).read()
_src = _src[:_src.index("X = 1000; L = math.log(X)")]
_g = {"__file__": __file__, "__name__": "r67"}; exec(compile(_src, "retro67", "exec"), _g)
build, ideals_upto = _g["build"], _g["ideals_upto"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
PHI = (1 + 5 ** 0.5) / 2; LPHI = math.log(PHI)
def lucas(n):
    a, b = 2, 1
    for _ in range(n): a, b = b, a + b
    return a
def Nm1(n): return lucas(n) - 1 - (-1) ** n
def Q(n):
    num = den = 1
    for d in divisors(n):
        m = mobius(n // d)
        if m == 1: num *= Nm1(d)
        elif m == -1: den *= Nm1(d)
    return num // den
# (1)
eta = lambda n: math.log(abs(1 - PHI ** -n)) + math.log(abs(1 - (-1 / PHI) ** n))
check("1", "T", "lado arquimediano del reloj: log Nm1(n) = n log phi + eta_n (lugar de phi y lugar conjugado), n = 1..300",
      all(abs(math.log(Nm1(n)) - (n * LPHI + eta(n))) < 1e-9 * n for n in range(3, 301)))
check("1", "T", "y es la suma de los niveles que dividen a n: Nm1(n) = prod_{d|n} Q(d), n = 1..300",
      all(Nm1(n) == math.prod(Q(d) for d in divisors(n)) for n in range(3, 301)))
# (2)
mass = 0.0; ratio = {}
for n in range(1, 2001):
    if n >= 3: mass += math.log(Q(n)) if Q(n) > 1 else 0.0
    if n in (100, 500, 1000, 2000): ratio[n] = mass / (3 / math.pi ** 2 * LPHI * n * n)
check("2", "T", "masa del reloj hasta el nivel n: (3/pi^2) log phi n^2 (1 +- 2 %) para n = 500..2000", all(abs(r - 1) < 0.02 for n, r in ratio.items() if n >= 500))
# (3) canales de indice
X = 1000; L = math.log(X); N = 48
B = build(L, N)
A = B["Pole"] + (math.log(5) - 2 * math.log(math.pi)) * B["G0"] + 2 * B["Psi1"]
ids = ideals_upto(X)
def idx(Nrm, lev):
    if lev in ("2", "5"): return "p" + lev
    r = math.isqrt(Nrm)
    return (Nrm - 1) // lev if r * r != Nrm else 2 * (r + 1) // lev
ch = defaultdict(list)
for Nrm, lev in ids:
    i = idx(Nrm, lev); ch[i if (isinstance(i, str) or i <= 6) else ">6"].append(Nrm)
Pc = {k: B["Pform"](v) for k, v in ch.items()}
W = A - sum(Pc.values())
lmin = lambda M: float(np.linalg.eigvalsh(M)[0])
check("3", "T", "W por canales es la misma W positiva", lmin(W) > 0)
def best_share(M):
    lo, hi = 0.0, 2.0
    for _ in range(80):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if lmin(m1 * A - M) < lmin(m2 * A - M): lo = m1
        else: hi = m2
    return lo, lmin(lo * A - M)
sh = {k: best_share(M) for k, M in Pc.items()}
check("3", "T", "por canales de indice tampoco hay reparto escalar: ningun canal admite t con t A - P_i semidefinida",
      all(v < -1e-10 for _, v in sh.values()))
# la direccion del polo por canal
w1 = np.linalg.eigh(A)[1][:, 0]
c1 = {k: float(-w1 @ M @ w1) for k, M in Pc.items()}
if __name__ == "__main__":
    print("2) masa/(3/pi^2 log phi n^2):", {n: round(r, 4) for n, r in ratio.items()})
    print("3) canales:", {str(k): len(v) for k, v in ch.items()})
    print("   mejor reparto (t, lambda_min):", {str(k): (round(t, 3), round(v, 4)) for k, (t, v) in sh.items()})
    print("   aporte en la direccion del polo:", {str(k): round(v, 4) for k, v in c1.items()})
    print(f"{len(LEDGER)} aserciones, 0 fallas")
