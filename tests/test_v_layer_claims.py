r"""The five v-layer scripts behind the v-layer statements of the corpus.

Sites covered (statement line numbers as measured — snapshots, the convention
of `docs/numerical-port.md`):

* ``04-bridges:1302`` — ``v12_pitagoras_raiz_X.py``: "measured $0.993$,
  $0.998$ and $1.000$ up to $10^6$" — the Schur-orthogonality ratio
  $\sum_{p\leq X}|a_p|^2\log p / X$ of the three symbols.
* ``04-bridges:1303`` — same script: "$\Sigma(X)^2<\mathcal E(X)$ at every
  scale measured".
* ``03-mechanisms:1398-1399`` — ``v27_reloj_ciclotomico.py``: the scope of
  (ii) ($1\,355\,192$ pairs, $752$ of the $2260$ primes with two clocks) and
  the size of (vi) ($3.6\cdot10^{-12}$).
* ``03-mechanisms:1453`` — same script: $v_5$ of
  $N(\Phi_{4\cdot5^k}(\golden))$ is $1,2,2,2$ for $k=0,1,2,3$.
* ``03-mechanisms:1671-1673`` — ``v28_hiperbola_reloj_tamano.py``: the
  $78\,495$ primes $7\leq p\leq10^6$ with $N_p\leq2(p+1)$, zero mass above
  $X^{3/4}$ at $X=10^6$ and the tower bound $1.00\sqrt X$.
* ``04-bridges:1320-1321`` — ``v30_vertice_al_azar.py``: the vertex model
  within $8\%$ for $3\leq j\leq1000$ and the layer densities $0.1237$/$0.1666$
  against $0.1243$/$0.1667$.
* ``04-bridges:1322-1323`` — ``v33_capas_1e9.py``: the level-135 and quintic
  families to $2\cdot10^{-10}$ and $6\cdot10^{-12}$ in the sums up to $10^9$.
* ``04-bridges:1485-1487`` — same script: twenty layers $2\leq i\leq60$
  with no systematic term, mean exponent $0.520$ (range $0.42$--$0.59$).

None of the five scripts is imported by another script and none writes a
committed ``salidas/*.txt``, so every test owns its computation. The inputs are
the committed caches of ``tests/fixtures/datos/`` — ``ordenes_1000000.pkl``
(v28, v30), ``capas_hasta_1000000000.json`` and ``familias_hasta_1000000000.json``
(v33) — the same files the scripts read, and the arithmetic of ``comun.py`` is
ported here (prime sieve, $\mathbb{Z}[\golden]$ classes, quadratic-form
enumeration) because a test may not import a script.

Conditions declared by the corpus: v12 sums over the primes $p\leq10^6$ at six
scales; v27 checks $n\leq600$ against $p\leq20000$ with $p\nmid n$ and the
identity at $N=10^6$; v28/v30 work from the committed order table of the primes
$7\leq p\leq10^6$; v33 sums over the grid $10^3\ldots10^9$ and fits each layer
over the decades $10^4\ldots10^8$. The five computations take ~7 s together
(v30's tail model is the expensive one at ~5 s), so none is marked ``slow``.
"""

from __future__ import annotations

import functools
import json
import math
import pickle
import re
from fractions import Fraction

import numpy as np

from oddzeta.harness import REPO_ROOT, assert_half_last_digit, read_tex

DATOS = REPO_ROOT / "tests" / "fixtures" / "datos"

#: v12's symbols in the script's order — the manuscript lists their figures in
#: the same order ("0.993, 0.998 and 1.000").
SYMBOLS = ("nivel 80", "nivel 135", "F20")

#: v27's declared scope (03-mechanisms:1398), asserted against the text below.
N_MAX, P_MAX = 600, 20000


def _claim(chapter: str, pattern: str, note: str) -> re.Match[str]:
    """The manuscript text behind a claim (fails loudly if it is gone)."""
    m = re.search(pattern, read_tex(chapter))
    assert m is not None, f"{note} is no longer in {chapter}"
    return m


# ---------------------------------------------------------------------------
# Ports of the removed hipotesis/pruebas/comun.py — no script may be imported by a test.
# ---------------------------------------------------------------------------
def _criba(L: int) -> bytearray:
    sv = bytearray([1]) * (L + 1)
    sv[0] = sv[1] = 0
    for i in range(2, int(L**0.5) + 1):
        if sv[i]:
            sv[i * i :: i] = bytearray(len(sv[i * i :: i]))
    return sv


def _primos(L: int, desde: int = 7) -> list[int]:
    sv = _criba(L)
    return [p for p in range(desde, L + 1) if sv[p]]


def _factores(n: int) -> list[int]:
    fs = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            fs.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        fs.append(n)
    return fs


def _mul(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    x1, y1 = a
    x2, y2 = b
    return ((x1 * x2 + y1 * y2) % p, (x1 * y2 + x2 * y1 + y1 * y2) % p)


def _pw(a: tuple[int, int], n: int, p: int) -> tuple[int, int]:
    r = (1, 0)
    while n:
        if n & 1:
            r = _mul(r, a, p)
        a = _mul(a, a, p)
        n >>= 1
    return r


def _partido(p: int) -> bool:
    return p % 5 in (1, 4)


def _n_p(p: int) -> int:
    return p - 1 if _partido(p) else 2 * (p + 1)


def _orden(p: int) -> tuple[int, int]:
    """(N_p, order of phi in (Z[phi]/p)*)."""
    N = _n_p(p)
    o = N
    for q in _factores(N):
        while o % q == 0 and _pw((0, 1), o // q, p) == (1, 0):
            o //= q
    return N, o


def _indice(p: int) -> int:
    N, o = _orden(p)
    return N // o


def _sqrtmod(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r


def _raiz_phi(p: int) -> int:
    return (1 + _sqrtmod(5, p)) * pow(2, p - 2, p) % p


def _leg(a: int, p: int) -> int:
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def _orden_mult(x: int, p: int, N: int) -> int:
    o = N
    for q in _factores(N):
        while o % q == 0 and pow(x, o // q, p) == 1:
            o //= q
    return o


def _representados(formas: list[tuple[int, int, int]], L: int, disc: int) -> set[int]:
    """The norms n < L represented by the forms of discriminant ``disc``."""
    R: set[int] = set()
    D = -disc
    for (A, B, C) in formas:
        ymax = int(math.sqrt(4 * A * L / D)) + 2
        for y in range(0, ymax):
            xr = int(math.sqrt(L / A)) + abs(B * y) // (2 * A) + 2
            for x in range(-xr, xr + 1):
                n = A * x * x + B * x * y + C * y * y
                if 0 < n < L:
                    R.add(n)
    return R


def _tot(n: int) -> int:
    r, m, q = n, n, 2
    while q * q <= m:
        if m % q == 0:
            while m % q == 0:
                m //= q
            r -= r // q
        q += 1
    if m > 1:
        r -= r // m
    return r


def _factores_exp(n: int) -> dict[int, int]:
    f: dict[int, int] = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            f[q] = f.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def _divisores(n: int) -> list[int]:
    d = [1]
    for q, e in _factores_exp(n).items():
        d = [x * q**k for x in d for k in range(e + 1)]
    return sorted(d)


# ---------------------------------------------------------------------------
# v12_pitagoras_raiz_X.py — the Schur-orthogonality ratio and the inequality.
# ---------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def _v12_energy() -> dict[str, tuple[float, float]]:
    """{symbol: (sum|a_p|^2 log p / X at X=10^6, worst S(X)^2/E(X) over scales)}."""
    L = 10**6
    P = _primos(L, 2)
    R1 = _representados([(1, 0, 20)], L + 1, -80)
    R2 = _representados([(4, 0, 5)], L + 1, -80)
    Rg = _representados([(1, 1, 34), (5, 5, 8)], L + 1, -135)

    def af(p: int) -> int:
        if p == 2:
            return 0
        if p == 5:
            return -1
        return 2 if p in R1 else (-2 if p in R2 else 0)

    def ag(p: int) -> int:
        if p == 3:
            return 0
        if p == 5:
            return 1
        if p == 2:
            return -1
        if _leg(-15, p) != 1:
            return 0
        return 2 if p in Rg else -1

    def aF(p: int) -> int:
        if p == 5 or p % 5 != 1 or p < 7:
            return 0
        return 4 if _indice(p) % 5 == 0 else -1

    marcas = [10**k for k in (3, 4, 5)] + [2 * 10**5, 5 * 10**5, 10**6]
    out: dict[str, tuple[float, float]] = {}
    for nombre, a in zip(SYMBOLS, (af, ag, aF)):
        S = E = E1 = 0.0
        j = 0
        filas: list[tuple[int, float, float, float]] = []
        for p in P:
            v = a(p)
            lp = math.log(p)
            S += v * lp
            E += v * v * lp * lp
            E1 += v * v * lp
            while j < len(marcas) and p >= marcas[j] - 1:
                filas.append((marcas[j], S, E, E1))
                j += 1
        if len(filas) < len(marcas):
            filas.append((marcas[-1], S, E, E1))
        out[nombre] = (filas[-1][3] / filas[-1][0], max(f[1] ** 2 / f[2] for f in filas))
    return out


def test_pythagoras_energy_ratio_converges_to_one() -> None:
    r"""``04-bridges:1302`` — the three ratios "measured ... up to $10^6$"."""
    figures = _claim(
        "04-bridges.tex",
        r"measured \$([\d.]+)\$, \$([\d.]+)\$ and \$([\d.]+)\$ up to \$10\^6\$",
        "the three Schur-orthogonality ratios",
    ).groups()
    energy = _v12_energy()
    for symbol, figure in zip(SYMBOLS, figures):
        assert_half_last_digit(
            energy[symbol][0], figure, f"04-bridges:1302 {symbol} (sum|a_p|^2 log p / X)"
        )


def test_pythagoras_inequality_holds_at_every_measured_scale() -> None:
    r"""``04-bridges:1303`` — $\Sigma(X)^2<\mathcal E(X)$ at every scale."""
    _claim(
        "04-bridges.tex",
        r"\\Sigma\(X\)\^2<\\mathcal E\(X\)\$ at every scale measured",
        "the Pythagoras inequality",
    )
    for symbol, (_, worst) in _v12_energy().items():
        assert worst < 1.0, (
            f"{symbol}: the largest S(X)^2/E(X) over the six scales is {worst:.6f}, "
            "not below 1"
        )


# ---------------------------------------------------------------------------
# v27_reloj_ciclotomico.py — the clock census and the Mertens identity.
# ---------------------------------------------------------------------------
def _moebius_sieve(N: int) -> np.ndarray:
    mu = np.ones(N + 1, dtype=np.int64)
    mu[0] = 0
    es = np.ones(N + 1, bool)
    es[:2] = False
    for p in range(2, N + 1):
        if es[p]:
            es[2 * p :: p] = False
            mu[p :: p] *= -1
            if p * p <= N:
                mu[p * p :: p * p] = 0
    return mu


def _mu(n: int) -> int:
    r, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            r = -r
        p += 1
    return -r if n > 1 else r


def _cyclotomic_norms() -> list[int]:
    """N(Phi_n(phi)) for n <= N_MAX, by the multiplicative recursion of the script."""
    L = [2, 1]
    for _ in range(N_MAX + 2):
        L.append(L[-1] + L[-2])
    Npow = [0] + [(-1) ** d + 1 - L[d] for d in range(1, N_MAX + 1)]
    norms = [0]
    for n in range(1, N_MAX + 1):
        v = Fraction(1)
        for d in range(1, n + 1):
            if n % d == 0 and _mu(n // d):
                v *= Fraction(Npow[d]) ** _mu(n // d)
        assert v.denominator == 1, f"N(Phi_{n}(phi)) is not an integer"
        norms.append(int(v))
    return norms


@functools.lru_cache(maxsize=None)
def _v27_census() -> dict[str, object]:
    """The p-adic sweep of v27: pairs, primes with two clocks, failures, v5."""
    norms = _cyclotomic_norms()
    P = [p for p in _primos(P_MAX, 3) if p != 5]
    pares = dobles = fallos = 0
    for p in P:
        if _partido(p):
            r = _raiz_phi(p)
            relojes = {_orden_mult(r, p, p - 1), _orden_mult((1 - r) % p, p, p - 1)}
        else:
            relojes = {_orden(p)[1]}
        if len(relojes) == 2:
            dobles += 1
        for n in range(1, N_MAX + 1):
            if n % p == 0:
                continue
            pares += 1
            if (norms[n] % p == 0) != (n in relojes):
                fallos += 1
    v5 = []
    for n in (4, 20, 100, 500):
        x, k = norms[n], 0
        while x % 5 == 0:
            x //= 5
            k += 1
        v5.append(k)
    return {"primes": len(P), "pares": pares, "dobles": dobles, "fallos": fallos, "v5": v5}


@functools.lru_cache(maxsize=None)
def _v27_identity() -> float:
    """max |sum_{n<=N} err_n - sum_d eps_d M(N/d)| over the script's sample of N."""
    NM = 10**6
    phi = (1 + 5**0.5) / 2
    d_ = np.arange(1, NM + 1, dtype=float)
    eps = np.log1p(-phi ** (-d_)) + np.log(
        np.abs(1 - ((-1.0) ** np.arange(1, NM + 1)) * phi ** (-d_))
    )
    mu = _moebius_sieve(NM)
    err = np.zeros(NM + 1)
    for d in range(1, 60):
        err[d :: d] += eps[d - 1] * mu[1 : NM // d + 1]
    M = np.cumsum(mu).astype(float)
    A = np.cumsum(err)
    Ns = np.unique(np.logspace(2, 6, 300).astype(int))
    return float(max(abs(A[N] - sum(eps[d - 1] * M[N // d] for d in range(1, 60))) for N in Ns[::10]))


def test_cyclotomic_clock_scope_matches_the_manuscript() -> None:
    r"""``03-mechanisms:1398-1399`` — $1\,355\,192$ pairs, $752$ of $2260$."""
    m = _claim(
        "03-mechanisms.tex",
        r"\(\$(\d+(?:\\\,\d+)*)\$ pairs,\s+\$(\d+)\$ of the \$(\d+)\$ primes",
        "the scope of (ii)",
    )
    declared_pairs = int(m.group(1).replace(r"\,", ""))
    declared_doubles, declared_primes = int(m.group(2)), int(m.group(3))
    census = _v27_census()
    assert census["pares"] == declared_pairs, (
        f"the sweep covers {census['pares']} pairs, the manuscript says {declared_pairs}"
    )
    assert census["dobles"] == declared_doubles, (
        f"{census['dobles']} primes have two clocks, the manuscript says {declared_doubles}"
    )
    assert census["primes"] == declared_primes, (
        f"the sweep covers {census['primes']} primes, the manuscript says {declared_primes}"
    )


def test_p_adic_clock_equivalence_holds_on_every_pair() -> None:
    r"""(ii) over the declared scope — $p\mid N(\Phi_n(\varphi))$ iff $n$ is a clock."""
    scope = _claim(
        "03-mechanisms.tex",
        r"\(ii\) for \$n\\leq(\d+)\$ and \$p\\leq(\d+)\$, \$p\\nmid n\$",
        "the scope of (ii)",
    )
    assert (int(scope.group(1)), int(scope.group(2))) == (N_MAX, P_MAX), (
        "the manuscript moved the scope of (ii)"
    )
    census = _v27_census()
    assert census["fallos"] == 0, (
        f"{census['fallos']} of {census['pares']} pairs contradict the clock equivalence"
    )


def test_clock_mertens_identity_holds_to_the_manuscript_order() -> None:
    r"""``03-mechanisms:1399`` — (vi) at $N=10^6$ to $3.6\cdot10^{-12}$."""
    m = _claim(
        "03-mechanisms.tex",
        r"up to \$N=10\^6\$ to \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the size of the clock identity",
    )
    figure = float(f"{m.group(1)}e{m.group(2)}")
    residual = _v27_identity()
    # The identity is exact, so the residual is float noise: v27 prints 3.8e-12,
    # the manuscript 3.6e-12, and re-samplings of the same sum land between
    # 2.0e-12 and 6.2e-12. The assertion therefore pins the decade the
    # manuscript claims — a hundred times tighter than the script's own 1e-8.
    assert residual < 10 * figure, (
        f"the clock identity leaves {residual:.3e} at N=1e6, outside the decade "
        f"of the manuscript's {figure:.1e}"
    )


def test_five_valuation_of_the_cyclotomic_norms() -> None:
    r"""``03-mechanisms:1453`` — $v_5$ of $N(\Phi_{4\cdot5^k}(\golden))$ is $1,2,2,2$."""
    declared = [
        int(v)
        for v in _claim(
            "03-mechanisms.tex",
            r"is \$([\d,]+)\$ for \$k=0,1,2,3\$",
            "the five-valuation sequence",
        )
        .group(1)
        .split(",")
    ]
    census = _v27_census()
    assert census["v5"] == declared, (
        f"the norms of levels 4, 20, 100, 500 have 5-valuations {census['v5']}, "
        f"the manuscript says {declared}"
    )


# ---------------------------------------------------------------------------
# v28_hiperbola_reloj_tamano.py — the clock index against the hyperbola.
# ---------------------------------------------------------------------------
def _load_orders() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    with open(DATOS / "ordenes_1000000.pkl", "rb") as h:
        T = pickle.load(h)
    p = np.array([t[0] for t in T])
    Np = np.array([t[1] for t in T])
    fl = np.array([t[2] for t in T])
    return p, Np, fl, Np // fl


@functools.lru_cache(maxsize=None)
def _v28_metrics() -> dict[str, object]:
    p, Np, fl, ind = _load_orders()
    phi = (1 + 5**0.5) / 2
    lphi = math.log(phi)
    X = 10**6
    s = p <= X
    r2 = X**0.75
    y34 = int(2 * (X + 1) / r2)
    B = sum((m + 1) * lphi + 4 * phi ** (-(m + 1)) for m in range(1, y34 + 1))
    return {
        "count": len(p),
        "min_prime": int(p.min()),
        "max_prime": int(p.max()),
        "hyperbola": bool(np.all(ind * fl == Np) and np.all(Np <= 2 * (p + 1))),
        "mass_above": float(np.log(p[s & (ind > r2)]).sum()),
        "b34": B / X**0.5,
    }


def test_clock_index_hyperbola_holds_for_all_seven_primes() -> None:
    r"""``03-mechanisms:1671`` — the $78\,495$ primes, $N_p\leq2(p+1)$ in all."""
    count = int(
        _claim("03-mechanisms.tex", r"Over the \$(\d+(?:\\\,\d+)*)\$ primes", "the prime count")
        .group(1)
        .replace(r"\,", "")
    )
    _claim("03-mechanisms.tex", r"\$N_p\\leq2\(p\+1\)\$", "the hyperbola bound")
    m28 = _v28_metrics()
    assert m28["count"] == count, (
        f"the table holds {m28['count']} primes, the manuscript says {count}"
    )
    assert (m28["min_prime"], m28["max_prime"]) == (7, 10**6 - 17), (
        "the declared range 7 <= p <= 10^6 changed"
    )
    assert m28["hyperbola"], "some clock index sits above the hyperbola 2(p+1)"


def test_tower_bound_covers_the_large_index_mass() -> None:
    r"""``03-mechanisms:1672-1673`` — mass $0$ above $X^{3/4}$, bound $1.00\sqrt X$."""
    mass = float(
        _claim(
            "03-mechanisms.tex",
            r"have mass \$([\d.]+)\$ at \$X=10\^6\$",
            "the mass above X^{3/4}",
        ).group(1)
    )
    bound = _claim(
        "03-mechanisms.tex", r"bound \$([\d.]+)\\sqrt X\$", "the tower bound"
    ).group(1)
    m28 = _v28_metrics()
    assert m28["mass_above"] == mass, (
        f"the mass of the primes of index above X^3/4 is {m28['mass_above']}, "
        f"the manuscript says {mass}"
    )
    assert_half_last_digit(m28["b34"], bound, "03-mechanisms:1673 tower bound")


# ---------------------------------------------------------------------------
# v30_vertice_al_azar.py — the vertex model of the index tail.
# ---------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def _v30_metrics() -> dict[str, object]:
    p, _, _, ind = _load_orders()
    lp = np.log(p)
    js = np.unique(np.logspace(0, 4, 41).astype(int))
    Gm = np.zeros(len(js))
    P2 = P3 = 0.0
    with open(DATOS / "ordenes_1000000.pkl", "rb") as h:
        T = pickle.load(h)
    for (prime, N, f) in T:
        if _partido(prime):
            M = N // 2
            ds = _divisores(M)
            pr = np.array([_tot(M // i) / M for i in ds])
        else:
            M = prime + 1
            ds = [i for i in _divisores(M) if i % 2 == 1]
            pr = np.array([_tot(2 * M // i) / M for i in ds])
        ds_a = np.array(ds)
        tail = np.cumsum(pr[::-1])[::-1]
        pos = np.searchsorted(ds_a, js, side="right")
        Gm += math.log(prime) * np.where(pos < len(ds), tail[np.minimum(pos, len(ds) - 1)], 0.0)
        P2 += math.log(prime) * pr[ds_a % 2 == 0].sum()
        P3 += math.log(prime) * pr[ds_a % 3 == 0].sum()
    g = np.bincount(ind, weights=lp)
    G = np.cumsum(g[::-1])[::-1]
    Gr = np.array([G[j + 1] if j + 1 < len(G) else 0.0 for j in js])
    sel = (js >= 3) & (js <= 1000)
    ratios = (Gr / Gm)[sel]
    th = lp.sum()
    return {
        "worst": float(np.max(np.abs(1.0 - ratios))),
        # In the manuscript's reading: the two measured densities, then the two
        # the vertex model gives ("0.1237 and 0.1666 against 0.1243 and 0.1667").
        "densities": (
            float(lp[ind % 2 == 0].sum() / th),
            float(lp[ind % 3 == 0].sum() / th),
            float(P2 / th),
            float(P3 / th),
        ),
    }


def test_vertex_model_tracks_the_index_tail_within_eight_percent() -> None:
    r"""``04-bridges:1320`` — "to within $8\%$ for $3\leq j\leq1000$"."""
    pct = float(
        _claim(
            "04-bridges.tex",
            r"to within \$(\d+)\\%\$ for \$3\\leq j\\leq1000\$",
            "the tail tolerance and its range",
        ).group(1)
    )
    worst = _v30_metrics()["worst"]
    assert worst <= pct / 100, (
        f"the vertex model misses the measured mass by {100 * worst:.2f}% at some "
        f"j in [3,1000], the manuscript claims {pct:.0f}%"
    )


def test_layer_densities_match_the_manuscript_figures() -> None:
    r"""``04-bridges:1321`` — the densities $0.1237$/$0.1666$ against $0.1243$/$0.1667$."""
    figures = _claim(
        "04-bridges.tex",
        r"layer\s+densities \$([\d.]+)\$ and \$([\d.]+)\$ against \$([\d.]+)\$ and \$([\d.]+)\$",
        "the layer densities",
    ).groups()
    labels = ("capa 2 medida", "capa 3 medida", "capa 2 modelo", "capa 3 modelo")
    for label, value, figure in zip(labels, _v30_metrics()["densities"], figures):
        assert_half_last_digit(value, figure, f"04-bridges:1321 {label}")


# ---------------------------------------------------------------------------
# v33_capas_1e9.py — the layer families and their fluctuations.
# ---------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def _v33_metrics() -> dict[str, object]:
    with open(DATOS / "capas_hasta_1000000000.json") as h:
        c = json.load(h)
    with open(DATOS / "familias_hasta_1000000000.json") as h:
        f = json.load(h)
    Xs = np.array(c["Xs"], float)
    errs = {}
    for fam, q, i in (("135", 3, 3), ("F20", 5, 5)):
        T = np.array(f["res"][fam]["1"]["re"]) * np.sqrt(Xs)
        D = q * np.array(c["D"][str(i)])
        errs[fam] = float(np.max(np.abs(T - D) / np.maximum(1, np.abs(D))))
    w = Xs >= 1e4
    bs, ths = [], []
    for i in map(int, c["D"]):
        D = np.array(c["D"][str(i)])
        bs.append(np.sum(D[w] * Xs[w]) / np.sum(Xs[w] ** 2))
        rm, cen = [], []
        for k in range(4, 9):
            s = (Xs >= 10**k) & (Xs < 10 ** (k + 1))
            rm.append(np.sqrt(np.mean(D[s] ** 2)))
            cen.append(10 ** (k + 0.5))
        ths.append(np.polyfit(np.log(cen), np.log(rm), 1)[0])
    bs_a, ths_a = np.array(bs), np.array(ths)
    return {
        "grid_max": float(Xs.max()),
        "layers": sorted(int(k) for k in c["D"]),
        "errs": errs,
        "max_abs_b": float(np.max(np.abs(bs_a))),
        "theta_mean": float(ths_a.mean()),
        "theta_min": float(ths_a.min()),
        "theta_max": float(ths_a.max()),
    }


def test_layer_family_identities_hold_to_the_manuscript_precision() -> None:
    r"""``04-bridges:1322-1323`` — to $2\cdot10^{-10}$ and $6\cdot10^{-12}$."""
    m = _claim(
        "04-bridges.tex",
        r"to \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$ and \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the family identity errors",
    )
    figures = (f"{m.group(1)}e{m.group(2)}", f"{m.group(3)}e{m.group(4)}")
    up_to = 10 ** int(
        _claim("04-bridges.tex", r"in the sums up to \$10\^(\d+)\$", "the sum range").group(1)
    )
    metrics = _v33_metrics()
    assert metrics["grid_max"] == up_to, (
        f"the layer sums stop at {metrics['grid_max']:g}, the manuscript says {up_to:g}"
    )
    for family, figure in zip(("135", "F20"), figures):
        assert_half_last_digit(
            metrics["errs"][family], figure, f"04-bridges:1323 family {family}"
        )


def test_layer_fluctuations_cover_the_twenty_declared_layers() -> None:
    r"""``04-bridges:1485`` — the twenty layers $2\leq i\leq60$ measured."""
    m = _claim(
        "04-bridges.tex",
        r"(\w+) layers \$2\\leq i\\leq(\d+)\$ measured",
        "the declared layer range",
    )
    words = {"twenty": 20}
    declared, high = words[m.group(1)], int(m.group(2))
    layers = _v33_metrics()["layers"]
    assert len(layers) == declared, (
        f"the JSON carries {len(layers)} layers, the manuscript says {m.group(1)}"
    )
    assert min(layers) >= 2 and max(layers) <= high, (
        f"the layers run {min(layers)}..{max(layers)}, the manuscript declares 2..{high}"
    )


def test_layer_fluctuations_show_no_systematic_term() -> None:
    r"""``04-bridges:1485`` — "show no systematic term" (the script's $|b_i|<10^{-4}$)."""
    _claim("04-bridges.tex", r"measured show no systematic", "the systematic-term clause")
    worst = _v33_metrics()["max_abs_b"]
    assert worst < 1e-4, (
        f"the largest systematic layer coefficient is {worst:.2e}, above the "
        "script's 1e-4 threshold for 'no systematic term'"
    )


def test_layer_fluctuation_exponent_matches_the_manuscript() -> None:
    r"""``04-bridges:1486-1487`` — mean exponent $0.520$ (range $0.42$--$0.59$)."""
    mean = _claim("04-bridges.tex", r"mean exponent \$([\d.]+)\$", "the mean exponent").group(1)
    edges = _claim(
        "04-bridges.tex", r"\(range \$([\d.]+)\$--\$([\d.]+)\$\)", "the exponent range"
    ).groups()
    metrics = _v33_metrics()
    assert_half_last_digit(metrics["theta_mean"], mean, "04-bridges:1486 mean exponent")
    assert_half_last_digit(metrics["theta_min"], edges[0], "04-bridges:1487 lower edge")
    assert_half_last_digit(metrics["theta_max"], edges[1], "04-bridges:1487 upper edge")
