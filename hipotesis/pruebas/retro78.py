"""retro78.py — Sprint 78: la rotacion (B) en las dos caras.
Cara geometrica: el toro T^2 con el automorfismo dorado A = [[1,1],[1,0]]. Las traslaciones por puntos de torsion
tau in T^2[m] son la rotacion; Lefschetz: #Fix(tau o A^n) = |det(A^n - I)| = Nm1(n) para TODO tau: partes exactamente iguales.
Cara de Weil: los ideales primos de norma p = 1 (mod 5) se parten por el simbolo quintico de phi, y phi fija la
identificacion de mu_5: zeta5 + zeta5^{-1} = phi - 1 (2cos(2pi/5) = 1/phi), salvo la conjugacion. Clases canonicas:
{1}, {zeta^{+-1}}, {zeta^{+-2}}. Se mide si la rotacion da partes iguales en la forma de Weil."""
import math, warnings, itertools; warnings.filterwarnings("ignore")
import numpy as np
from fractions import Fraction
from collections import defaultdict
from sympy import sqrt_mod, primerange, nthroot_mod
_src = open(__file__.replace("retro78.py", "retro67.py")).read()
_src = _src[:_src.index("X = 1000; L = math.log(X)")]
_g = {"__file__": __file__, "__name__": "r67"}; exec(compile(_src, "retro67", "exec"), _g)
build, ideals_upto = _g["build"], _g["ideals_upto"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
def lucas(n):
    a, b = 2, 1
    for _ in range(n): a, b = b, a + b
    return a
Nm1 = lambda n: lucas(n) - 1 - (-1) ** n
# ---------------- G: cara geometrica, conteo exacto de puntos fijos de tau o A^n
def An(n):
    M = np.array([[1, 0], [0, 1]], dtype=object); A = np.array([[1, 1], [1, 0]], dtype=object)
    for _ in range(n): M = M.dot(A)
    return M
for n in range(3, 8):
    M = An(n) - np.array([[1, 0], [0, 1]], dtype=object)
    D = abs(int(M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]))
    for m in (2, 3, 5):
        counts = set()
        for t1, t2 in itertools.product(range(m), repeat=2):
            G = D * m; c = 0
            for x1, x2 in itertools.product(range(G), repeat=2):        # x = (x1, x2)/G mod 1
                y1 = M[0, 0] * x1 + M[0, 1] * x2 + t1 * D; y2 = M[1, 0] * x1 + M[1, 1] * x2 + t2 * D
                if y1 % G == 0 and y2 % G == 0: c += 1
            counts.add(c)
        check("G", "T", f"n={n}, m={m}: #Fix(tau o A^n) = {D} = Nm1(n) para los {m*m} tau de T^2[{m}] (partes exactamente iguales)", counts == {D} and D == Nm1(n))
# ---------------- W: cara de Weil, partes por el simbolo quintico
def chi5(p): return {1: 1, 4: 1, 2: -1, 3: -1}.get(p % 5, 0)
def zeta5_from_phi(p, r):
    """raiz quinta primitiva de la unidad en F_p con z + 1/z = r - 1 (la que phi fija); devuelve (z, 1/z)"""
    for z in nthroot_mod(1, 5, p, all_roots=True):
        if z != 1 and (z + pow(z, -1, p)) % p == (r - 1) % p: return z
    return None
X = 10 ** 6
parts = defaultdict(list); ambig = 0; checked = 0
for p in primerange(11, X + 1):
    if p % 5 != 1: continue
    inv2 = pow(2, -1, p)
    for s in sqrt_mod(5, p, all_roots=True):
        r = (1 + s) * inv2 % p
        z = zeta5_from_phi(p, r)
        if z is None: ambig += 1; continue
        checked += 1
        sym = pow(r, (p - 1) // 5, p)
        e = next(j for j in range(5) if pow(z, j, p) == sym)
        parts[min(e, 5 - e)].append(p)
check("W", "T", f"phi fija la identificacion de mu_5 en cada ideal (zeta + 1/zeta = phi - 1): {checked} ideales, 0 ambiguos", ambig == 0)
tot = sum(len(v) for v in parts.values())
fr = {k: len(v) / tot for k, v in parts.items()}
check("W", "T", "las clases {1}, {zeta^+-1}, {zeta^+-2} tienen densidades 1/5, 2/5, 2/5 (Chebotarev)", abs(fr[0] - 0.2) < 0.01 and abs(fr[1] - 0.4) < 0.01 and abs(fr[2] - 0.4) < 0.01)
# la forma de Weil de cada parte en la ventana e^L = 10^6
L = math.log(X); B = build(L, 48)
F = {k: B["Pform"](v) for k, v in parts.items()}
nrm = lambda M: float(np.abs(np.linalg.eigvalsh(M)).max())
d12 = nrm(F[1] - F[2]) / nrm(F[1]); d01 = nrm(2 * F[0] - F[1]) / nrm(F[1])
# control: particion aleatoria de los mismos ideales con los mismos tamanos
rng = np.random.default_rng(7)
allp = parts[1] + parts[2]; rng.shuffle(allp)
Ra, Rb = B["Pform"](allp[: len(parts[1])]), B["Pform"](allp[len(parts[1]):])
dR = nrm(Ra - Rb) / nrm(Ra)
# el par de ideales conjugados sobre p: uno en {zeta^+-1} y otro en {zeta^+-2}, o los dos en {1}
pair = defaultdict(list)
for k, v in parts.items():
    for p in v: pair[p].append(k)
check("W", "T", "la conjugacion phi <-> phi-bar manda {zeta^+-1} a {zeta^+-2} (porque phi-bar - 1 = -phi = zeta5^2 + zeta5^-2): cada p da un ideal en cada una, o los dos en {1}",
      all(sorted(v) in ([1, 2], [0, 0]) for v in pair.values()))
check("W", "T", "por eso las dos partes son exactamente iguales en la forma de Weil (diferencia 0): isometria exacta de orden 2", d12 == 0.0)
check("W", "T", "la rotacion de orden 5 no es isometria: 2*{1} contra {zeta^+-1} difiere como una particion al azar", 0.5 < d01 / dR < 3)
if __name__ == "__main__":
    print(f"G) Lefschetz verificado para n = 3..7 y m = 2, 3, 5: todas las traslaciones dan Nm1(n) puntos fijos")
    print(f"W) {checked} ideales con p = 1 mod 5 hasta 10^6; densidades {dict((k, round(v, 4)) for k, v in fr.items())}")
    print(f"   diferencia relativa de las formas: {{zeta^+-1}} vs {{zeta^+-2}} = {d12:.4f}; 2*{{1}} vs {{zeta^+-1}} = {d01:.4f}; particion al azar = {dR:.4f}")
    print(f"{len(LEDGER)} aserciones, 0 fallas")
