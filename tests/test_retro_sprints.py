r"""The sixteen ``retro*.py`` sprint scripts behind the retro statements of the corpus.

Sites covered (statement line numbers as measured — snapshots, the convention
of ``docs/numerical-port.md``):

* ``04-bridges:1079`` — ``retro101.py``: the free orbit of the
  Davenport--Heilbronn zeros at $\gamma=85.70$, $\delta=0.3085$
  ($1/\delta=3.24$), index $0$ up to window $2$ and one even plus one odd
  negative direction from window $3$ over the zeros below height $100$, and
  two of each with the second orbit at height $114.16$.
* ``04-bridges:1925`` — ``retro102.py``: $|t_k|/t_0$ grows like $7^{0.326k}$
  against the real part $0.8085$ of the first zero off the line, while
  without the two free orbits $|t_k|\le t_0$ for every $k\le60$.
* ``03-mechanisms:3546`` (prop:level-operators) — ``retro104.py``: a level
  operator keeps whole fibres (multiplicity six), colour and orientation
  commute with it and separate the joint index, the deck step conjugates them
  by $\zeta_3^{\pm1}$ and $-1$, the words $Y^aD^b$ span $M_6(\C)$, and the
  colour operator is normal and not self-adjoint.
* ``03-mechanisms:3595`` and ``04-bridges:168-176`` — ``retro105.py``: the
  $240$ zeros of $L(s,\chiv)$ and the $156$ of $\zeta$ below height $330$
  have no spacing below $0.1$ (smallest $0.231$ and $0.372$), the union has
  $11$ spacings below $0.1$ out of $388$ with smallest $0.017$ and no shared
  ordinate, the two- and six-sector fractions are $0.047$ and $0.079$ against
  the GUE $10^{-3}$, the commutants of $D$ and of $\{D,Y\}$ have dimension
  six and one, and the antiunitary symmetry forces doublets.
* ``03-mechanisms:3491`` — ``retro109.py``: Wall's law for the primes below
  $400$ and the fixed points $|\det(M^n-I)|$ enumerated for $n\le8$.
* ``03-mechanisms:1490`` — ``retro119.py``: over the primes $7\le p<6000$
  the criterion of prop:class-angular (iv) holds at every prime; $185$ split
  and $197$ inert meet its condition, $42$ and $52$ of them have $e_p$ prime
  to $3$.
* ``04-bridges:1509`` — ``retro67.py``: in the window $e^L=10^3$ removing
  any one of $108$ of the $127$ levels breaks the positivity, and a single
  prime ideal changes sign below $\log N\approx0.38\,L$ whatever its level.
* ``03-mechanisms:1402`` — ``retro69.py``: the clock mass over its main term
  is $1.0038$, $1.0018$, $1.0008$, $1.0006$ at $N=100$, $500$, $1000$,
  $2000$.
* ``03-mechanisms:1627`` — ``retro78.py``: $39\,234$ prime ideals of norm
  $p\equiv1\pmod5$ below $10^6$, class frequencies $0.2003$, $0.3999$,
  $0.3999$, the identification unambiguous at every one, and the two
  exchanged parts of the prime side coinciding.
* ``04-bridges:1725`` (the ``\code{retro81.py}--\code{retro87.py}`` range,
  whose "whole statement" is prop:index-degeneracy) — ``retro81.py``: the
  spectrum at $N=5^k$ is simple, fills half the circle with $e=2\cdot5^k$,
  and $p=e\,m+\chiv(p)$ at the primes.
* ``04-bridges:1721-1725`` — ``retro87.py``: the completion of the square is
  checked on $115$ elements (units and congruent to $1$ modulo $5$ and $25$)
  and every step of the chain holds for $k\le7$.
* ``04-bridges:1746`` — ``retro88.py``: at split primes the operator of the
  torus is the scaling of $\mathbb F_p$ by $\golden^2$ with the delta at $0$
  as the extra state, and at $5^k$ the shift by $5^{v+1}$ preserves the layer
  $v_5(j)=v$ and its occupation, one state left over.
* ``04-bridges:1751`` — ``retro89.py``: $|\tr U_N^n|^2$ is the number of
  fixed points of $M^{2n}$ on $(\Z/N)^2$ for odd $N$.
* ``04-bridges:1079`` — ``retro93.py``: with two zeros of $L(s,\chiv)$
  replaced by a quadruple the index is $0$ or $2$ on every window tried,
  never $1$.
* ``03-mechanisms:1528`` — ``retro94.py``: at every level $n\le420$ the
  inert primes carry between $0.066$ and $0.084$ of the accumulated mass and
  the kernel between $0.47$ and $0.56$.
* ``04-bridges:907`` — ``retro99.py``: the Davenport--Heilbronn zeros off the
  line at $0.8085+85.699i$ and $0.6508+114.163i$ are free orbits.

None of the sixteen was imported by a script of the removed ``hipotesis/pruebas/`` (four
of them ``exec`` another's source by path, which a test may not do), none
writes a committed ``salidas/*.txt``, and no script may be imported from here:
every test owns the code that produces its numbers. The inputs are the
committed ``tests/fixtures/dh_zeros.json`` and ``chi5_zeros.json``; the
window quadratic form of ``retro67.py`` (which retro69/78/93 ``exec``) and the
Weil representation of ``retro81/83/86`` (which retro87/88/89 ``exec``) are
ported below. ``retro94.py`` imports ``flint`` and its level factorisations
run past what a pure-Python factorisation can do (33--86 digit cofactors), so
``python-flint`` is a dev dependency of the project.

Conditions declared by the corpus: retro101 sums the zero side below height
$100$ (one orbit) and $130$ (two) over the windows $L=0.5\ldots6$ and
$1\ldots8$; retro102 uses the triangles $g_a$ at $u=k\log7$, $k\le60$, with
the fit over the last twenty steps; retro67 builds the cell base at $N=48$
over the ideals up to $X=10^3$; retro78/93 build it at $N=48$ (retro93 at
$N=64$) over the ideals up to $e^L$; retro87's chain runs $2\le k\le7$,
$v<k$, $m'=1\ldots14$; retro94 runs the levels $3\le n\le420$ and reads its
checkpoints at $n=60,120,\ldots,420$. The heavy computations (retro67,
retro78, retro93, retro94, and retro101's widest windows and retro105's
seeded ensembles) carry the ``slow`` mark.
"""

from __future__ import annotations

import functools
import itertools
import json
import math
import random
import re
from collections import defaultdict

import mpmath as mp
import numpy as np
import pytest
from flint import fmpz
from scipy.integrate import quad
from scipy.special import psi as cpsi
from sympy import divisors, isprime, legendre_symbol, mobius, n_order, nthroot_mod, primerange, sqrt_mod

from oddzeta.harness import REPO_ROOT, assert_half_last_digit, assert_printed_as_in_manuscript, read_tex

#: Where the numerical scripts and their committed inputs live.
PRUEBAS = REPO_ROOT / "tests" / "fixtures"

#: The manuscript figures spelled out rather than written as digits.
NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
}


def _claim(chapter: str, pattern: str, note: str) -> re.Match[str]:
    """The manuscript text behind a claim (fails loudly if it is gone)."""
    m = re.search(pattern, read_tex(chapter))
    assert m is not None, f"{note} is no longer in {chapter}"
    return m


def _figure(match: re.Match[str], group: int = 1) -> float:
    """A parsed figure: a digit run, or the word the sentence spells out."""
    token = match.group(group)
    return float(NUMBER_WORDS.get(token, token))


def _chi5p(p: int) -> int:
    """The character chi_5 of the splitting type (the script's dict)."""
    return {1: 1, 4: 1, 2: -1, 3: -1}[p % 5]


def _dh_zeros() -> tuple[np.ndarray, list]:
    """The committed Davenport--Heilbronn zeros: on the line, and off it."""
    data = json.loads((PRUEBAS / "dh_zeros.json").read_text(encoding="utf-8"))
    return np.array(data["line"]), data["off"]


# ===========================================================================
# retro101.py — 04-bridges:1079
# ===========================================================================
def _fr(x: np.ndarray, D: float, r) -> np.ndarray:
    """The step transform e(r x) 2 sin(r D/2)/r (retro101's ``fr``)."""
    return np.exp(1j * r * x) * (2 * np.sin(r * D / 2) / r)


def _zero_side_form(line: np.ndarray, orbits, L: float, N: int, T: float):
    """W(f) on the N cells of [-L/2, L/2], truncated at |gamma| < T."""
    D = L / N
    x = -L / 2 + (np.arange(N) + 0.5) * D
    M = np.zeros((N, N))
    for g in line[line < T]:
        v = _fr(x, D, g)
        M += 2 * np.real(np.outer(v, np.conj(v)))
    for b, g in orbits:
        d = b - 0.5
        for r in (g + 1j * d, g - 1j * d, -g + 1j * d, -g - 1j * d):
            M += np.real(np.outer(_fr(x, D, r), _fr(x, D, -r)))
    return (M + M.T) / 2, D


def _parity_negative_index(M: np.ndarray, D: float) -> tuple[int, int]:
    """(even, odd) negative directions of W on the two parity subspaces."""
    N = len(M)
    J = np.eye(N)[::-1]
    Ue = (np.eye(N) + J)[:, : N // 2] / math.sqrt(2)
    Uo = (np.eye(N) - J)[:, : N // 2] / math.sqrt(2)
    tol = 1e-9 * np.abs(M).max()
    return (
        int((np.linalg.eigvalsh(Ue.T @ M @ Ue) < -tol).sum()),
        int((np.linalg.eigvalsh(Uo.T @ M @ Uo) < -tol).sum()),
    )


def test_retro101_free_orbit_is_where_the_manuscript_places_it() -> None:
    r"""``04-bridges:1079`` — $\gamma=85.70$, $\delta=0.3085$,
    $1/\delta=3.24$, second orbit at height $114.16$ (the two zeros off the
    line of ``dh_zeros.json``)."""
    _, off = _dh_zeros()
    m = _claim(
        "04-bridges.tex",
        r"free orbit at \$\\gamma=([\d.]+)\$, \$\\delta=([\d.]+)\$",
        "the free orbit of the sentence",
    )
    delta = off[0][0] - 0.5
    assert_half_last_digit(off[0][1], m.group(1), "04-bridges:1079 gamma")
    assert_half_last_digit(delta, m.group(2), "04-bridges:1079 delta")
    inv = _claim("04-bridges.tex", r"against \$1/\\delta=([\d.]+)\$", "the reciprocal of delta")
    assert_half_last_digit(1.0 / delta, inv.group(1), "04-bridges:1079 1/delta")
    h = _claim("04-bridges.tex", r"second orbit, at height \$([\d.]+)\$", "the second orbit")
    assert_half_last_digit(off[1][1], h.group(1), "04-bridges:1079 second-orbit height")


def test_retro101_index_is_zero_up_to_the_stated_window_and_one_each_from_the_next() -> None:
    """``04-bridges:1079`` — index $0$ up to window $2$ and one even plus one
    odd negative direction from window $3$, for the zeros below height
    $100$; the control without the orbit stays at $0$."""
    tex = read_tex("04-bridges.tex")
    m = re.search(
        r"index \$0\$ up to window \$(\d+)\$ and one even and\s*one odd negative direction from window \$(\d+)\$",
        tex,
    )
    assert m is not None, "04-bridges:1079 index sentence is gone"
    flat_until, split_from = int(m.group(1)), int(m.group(2))
    height = int(
        _claim(
            "04-bridges.tex",
            r"Heilbronn sequence of \\cref\{ssec:two-sides\} below height \$(\d+)\$",
            "the height cutoff of the sentence",
        ).group(1)
    )

    line, off = _dh_zeros()
    g1 = off[0][1]
    rows = []
    for L in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0):
        N = 2 * int(math.ceil(L * g1 / 0.35 / 2))
        M, D = _zero_side_form(line, [tuple(off[0])], L, N, T=float(height))
        rows.append((L, *_parity_negative_index(M, D)))
    assert all(e == 0 and o == 0 for L, e, o in rows if L <= flat_until), rows
    assert all(e == 1 and o == 1 for L, e, o in rows if L >= split_from), rows
    for L in (2.0, 6.0):  # the script's control: the same zeros, no orbit
        N = 2 * int(math.ceil(L * g1 / 0.35 / 2))
        M, D = _zero_side_form(line, [], L, N, T=float(height))
        assert _parity_negative_index(M, D) == (0, 0), f"control at L={L}"


def test_retro101_the_second_orbit_raises_the_index_to_two_per_parity() -> None:
    """``04-bridges:1079`` — with the second orbit (height $114.16$) the
    truncated zero side has two of each: one negative direction per parity
    per free orbit, and the widest windows reach both."""
    line, off = _dh_zeros()
    orbits = [tuple(z) for z in off]
    rows = []
    for L in (1.0, 2.0, 4.0, 6.0, 8.0):
        N = 2 * int(math.ceil(L * off[1][1] / 0.35 / 2))
        M, D = _zero_side_form(line, orbits, L, N, T=130.0)
        rows.append((L, *_parity_negative_index(M, D)))
    per_orbit = len(orbits)
    assert per_orbit == 2, "the corpus speaks of two free orbits"
    assert all(e <= per_orbit and o <= per_orbit for _, e, o in rows), rows
    assert (rows[-1][1], rows[-1][2]) == (per_orbit, per_orbit), rows


# ===========================================================================
# retro102.py — 04-bridges:1925
# ===========================================================================
def _triangle_transform(a: float, x) -> np.ndarray:
    """ghat of the triangle (1-|x|/a)^+ — np.sinc(y) = sin(pi y)/(pi y)."""
    return a * (np.sinc(a * np.asarray(x) / (2 * np.pi))) ** 2


def _dh_autocorrelation(a: float, u: float, line: np.ndarray, off, *, orbits: bool = True, T: float = 130.0) -> float:
    """t(u) = W(g, tau_u g) for the triangle of width a over the DH zeros."""
    s = sum(2 * _triangle_transform(a, gm) ** 2 * math.cos(gm * u) for gm in line[line < T])
    if orbits:
        for b, gm in off:
            d = b - 0.5
            for gg in (gm + 1j * d, gm - 1j * d, -gm + 1j * d, -gm - 1j * d):
                s += (_triangle_transform(a, gg) ** 2 * np.exp(1j * gg * u)).real
    return float(s)


def test_retro102_growth_rate_is_the_real_part_of_the_first_off_line_zero() -> None:
    r"""``04-bridges:1925`` — $|t_k|/t_0$ grows like $7^{0.326k}$, against the
    real part $0.8085$ of the first zero off the line, at the prime $p=7$
    over the heights $k\le60$."""
    slope_txt = _claim("04-bridges.tex", r"grows like\s*\$7\^\{([\d.]+)k\}\$", "the growth rate").group(1)
    real_txt = _claim(
        "04-bridges.tex", r"real part \$([\d.]+)\$ of its first zero off the line", "the real part"
    ).group(1)
    height = int(_claim("04-bridges.tex", r"Davenport--Heilbronn zeros below height \$(\d+)\$", "the height").group(1))
    prime = int(_claim("04-bridges.tex", r"triangles \$g_a\$ and \$p=(\d+)\$", "the translation prime").group(1))
    kmax = int(_claim("04-bridges.tex", r"for every \$k\\le(\d+)\$", "the number of steps").group(1))

    line, off = _dh_zeros()
    assert_half_last_digit(off[0][0], real_txt, "04-bridges:1925 real part of the first off-line zero")

    log_p = math.log(prime)
    a = 0.05
    ks = np.arange(1, kmax + 1)
    r = np.array([abs(_dh_autocorrelation(a, k * log_p, line, off, T=float(height))) for k in ks])
    t0 = abs(_dh_autocorrelation(a, 0.0, line, off, T=float(height)))
    assert len(ks[r > 10 * t0]) > 5, "the quoted growth is only defined once |t_k| outruns 10 t_0"
    slope = float(np.polyfit(ks[-20:] * log_p, np.log(np.maximum(r[-20:], 1e-300)), 1)[0])
    assert_half_last_digit(slope, slope_txt, "04-bridges:1925 growth rate")


def test_retro102_without_the_free_orbits_w4_holds_at_every_stated_step() -> None:
    r"""``04-bridges:1925`` — without the two free orbits $|t_k|\le t_0$ for
    every $k\le60$ (Cauchy--Schwarz on the positive form), at the four widths
    the script sweeps."""
    kmax = int(_claim("04-bridges.tex", r"for every \$k\\le(\d+)\$", "the number of steps").group(1))
    prime = int(_claim("04-bridges.tex", r"triangles \$g_a\$ and \$p=(\d+)\$", "the translation prime").group(1))
    line, off = _dh_zeros()
    log_p = math.log(prime)
    for a in (0.05, 0.1, 0.2, 0.4):
        t0 = _dh_autocorrelation(a, 0.0, line, off, orbits=False, T=130.0)
        ratios = [_dh_autocorrelation(a, k * log_p, line, off, orbits=False, T=130.0) / t0 for k in range(1, kmax + 1)]
        assert all(abs(x) <= 1 + 1e-12 for x in ratios), f"width {a}: |t_k| > t_0 without the free orbit"


# ===========================================================================
# retro104.py — 03-mechanisms:3546 (prop:level-operators)
# ===========================================================================
def _joint_index_model() -> dict:
    """The finite model of prop:level-operators: J = levels x Z/3 x Z/2."""
    z3 = np.exp(2j * np.pi / 3)
    fib = [(k, e) for k in range(3) for e in range(2)]
    idx = {p: i for i, p in enumerate(fib)}
    Dm = np.zeros((6, 6), complex)
    for (k, e) in fib:
        Dm[idx[((k + 1) % 3, (e + 1) % 2)], idx[(k, e)]] = 1
    C = np.diag([z3**k / 2 for k, e in fib])
    W = np.diag([(-1) ** e for k, e in fib]).astype(complex)
    levels = 5
    I_F, I_L = np.eye(6), np.eye(levels)
    H = np.kron(np.diag(np.arange(1, levels + 1).astype(float)), I_F)
    return dict(z3=z3, Dm=Dm, C=C, W=W, levels=levels, H=H, D=np.kron(I_L, Dm),
                CC=np.kron(I_L, C), WW=np.kron(I_L, W))


def test_retro104_the_level_operator_keeps_the_stated_multiplicity() -> None:
    r"""``03-mechanisms:3546`` (iv) — every eigenspace of a level operator
    contains whole fibres: dimension six (the size of $M_6(\C)$, the algebra
    the words span), and every function of $H$ the model builds is constant on
    a fibre and commutes with the deck step."""
    six = int(_figure(_claim("03-mechanisms.tex", r"words span \$M_(\d+)\(\\C\)\$", "the full matrix algebra")))
    assert _figure(_claim("03-mechanisms.tex", r"has eigenspaces of dimension (\w+)", "the multiplicity of H")) == six
    model = _joint_index_model()
    H = model["H"]
    for f in (np.exp, np.sin, lambda x: x**3 - 2 * x, lambda x: 1 / (1 + x * x)):
        ev, V = np.linalg.eigh(H)
        fH = V @ np.diag(f(ev)) @ V.conj().T
        blocks = [fH[6 * i : 6 * i + 6, 6 * i : 6 * i + 6] for i in range(model["levels"])]
        assert all(np.allclose(b, b[0, 0] * np.eye(6)) for b in blocks), "f(H) is not constant on a fibre"
        assert np.allclose(model["D"] @ fH, fH @ model["D"]), "f(H) does not commute with the deck step"
    w = np.linalg.eigvalsh(H)
    for x in np.unique(np.round(w, 9)):
        assert int(np.sum(np.isclose(w, x))) == six, "an eigenspace of H does not contain whole fibres"


def test_retro104_colour_and_orientation_commute_and_separate_the_joint_index() -> None:
    r"""``03-mechanisms:3546`` (iv) — colour and orientation commute with each
    other and with $H$, and the three together separate $\mathcal J$ (five
    levels times the six points of the fibre)."""
    model = _joint_index_model()
    H, C, W = model["H"], model["CC"], model["WW"]
    for A, B in itertools.combinations((H, C, W), 2):
        assert np.allclose(A @ B, B @ A), "the ternary does not commute"
    joint = {
        (round(H[i, i].real, 9), round(C[i, i].real, 9), round(C[i, i].imag, 9), round(W[i, i].real, 9))
        for i in range(6 * model["levels"])
    }
    assert len(joint) == 6 * model["levels"], "the ternary does not separate the joint index"


def test_retro104_the_deck_step_conjugates_colour_and_orientation() -> None:
    r"""``03-mechanisms:3546`` (iv) — $D\OmH D^{-1}=\zeta_3^{-1}\OmH$ and
    $DWD^{-1}=-W$: neither colour nor orientation commutes with $D$."""
    model = _joint_index_model()
    Dm, C, W, z3, Di = model["Dm"], model["C"], model["W"], model["z3"], np.linalg.inv(model["Dm"])
    assert not np.allclose(Dm @ C @ Di, C), "D commutes with the colour operator"
    assert np.allclose(Dm @ C @ Di, z3**-1 * C) or np.allclose(Dm @ C @ Di, z3 * C), (
        "D C D^-1 is not zeta_3^{+-1} C"
    )
    assert np.allclose(Dm @ W @ Di, -W), "D W D^-1 is not -W"


def test_retro104_the_weyl_pair_spans_the_full_matrix_algebra() -> None:
    r"""``03-mechanisms:3546`` (iv) — $Y=2\OmH W$ and $D$ satisfy
    $DY=\zeta_6 YD$ with $\zeta_6$ primitive, and the words $Y^aD^b$ span the
    full matrix algebra of the fibre ($6\times6=36$ dimensions)."""
    six = int(_figure(_claim("03-mechanisms.tex", r"words span \$M_(\d+)\(\\C\)\$", "the full matrix algebra")))
    model = _joint_index_model()
    Dm, Di = model["Dm"], np.linalg.inv(model["Dm"])
    Y = (2 * model["C"]) @ model["W"]
    z6 = np.exp(2j * np.pi / 6)
    rel = [c for c in (z6**j for j in range(six)) if np.allclose(Dm @ Y @ Di, c * Y)]
    assert len(rel) == 1 and not np.isclose(rel[0], 1), "DYD^-1 is not a primitive sixth root times Y"
    words = [np.linalg.matrix_power(Y, a) @ np.linalg.matrix_power(Dm, b) for a in range(six) for b in range(six)]
    assert np.linalg.matrix_rank(np.array([w.ravel() for w in words])) == six * six, (
        "the words Y^a D^b do not span the full matrix algebra"
    )


def test_retro104_colour_is_normal_and_not_self_adjont() -> None:
    r"""``03-mechanisms:3546`` (iv) — $\tfrac12\operatorname{diag}(1,\zeta_3,
    \zeta_3^2)$ is normal and not self-adjoint, i.e. its eigenvalues are not
    real."""
    _claim(
        "03-mechanisms.tex",
        r"is\s+normal and not self-adjoint",
        "the colour operator of the proposition",
    )
    C = _joint_index_model()["C"]
    assert np.allclose(C @ C.conj().T, C.conj().T @ C), "the colour operator is not normal"
    assert not np.allclose(C, C.conj().T), "the colour operator is self-adjoint"
    assert not np.allclose(C.imag, 0), "the eigenvalues of the colour operator are real"


# ===========================================================================
# retro105.py — 03-mechanisms:3595, 04-bridges:168-176
# ===========================================================================
def _gue(rng: np.random.Generator, n: int) -> np.ndarray:
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (a + a.conj().T) / 2


def _unfolded_small(ev: np.ndarray, a: float = 0.1, frac=(0.25, 0.75)) -> tuple[float, float]:
    """Fraction of unfolded spacings below ``a`` in the middle of the spectrum."""
    ev = np.sort(ev)
    n = len(ev)
    s = np.diff(ev[int(frac[0] * n) : int(frac[1] * n)])
    s = s / s.mean()
    return float(np.mean(s < a)), float(s.min())


def _kramers_doublet(rng: np.random.Generator, n: int = 40) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """One quaternionic self-dual sample (H, T, v): the Kramers block of section A.

    The test vector ``v`` is drawn here so that the stream section B reads is
    retro105's own, draw for draw.
    """
    A = _gue(rng, n)
    B = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    B = B - B.T
    H = np.block([[A, B], [-B.conj(), A.conj()]])
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    v = rng.normal(size=2 * n) + 1j * rng.normal(size=2 * n)
    return H, J, v


def _sector_sweep() -> list[tuple[str, int, float, float]]:
    """GUE against the same ensemble conditioned on Z/2 and on mu_6.

    retro105's own stream (``default_rng(105)``, the five Kramers samples of
    section A consumed first), so the fractions are the ones the script prints.
    """
    rng = np.random.default_rng(105)
    for _ in range(5):
        _kramers_doublet(rng)
    rows, N = [], 720
    for name, m in (("GUE", 1), ("Z/2", 2), ("mu_6", 6)):
        fr, mins = [], []
        for _ in range(12):
            ev = np.concatenate([np.linalg.eigvalsh(_gue(rng, N // m)) for _ in range(m)])
            f, mn = _unfolded_small(ev)
            fr.append(f)
            mins.append(mn)
        rows.append((name, m, float(np.mean(fr)), float(np.min(mins))))
    return rows


def _counting_zeta(t: float) -> float:
    return t / (2 * math.pi) * math.log(t / (2 * math.pi * math.e)) + 7 / 8


def _counting_chi(t: float) -> float:
    return t / (2 * math.pi) * math.log(5 * t / (2 * math.pi * math.e))


def _small_spacings(seq, N_, a: float = 0.1, tmin: float = 20.0) -> tuple[int, int, float]:
    """(spacings below ``a``, number of spacings, smallest spacing), unfolded."""
    x = np.array([N_(t) for t in seq if t > tmin])
    s = np.diff(x)
    return int(np.sum(s < a)), len(s), float(s.min())


@functools.lru_cache(maxsize=None)
def _zeta_zeros_upto(T: float) -> tuple[float, ...]:
    out, n = [], 1
    while True:
        g = float(mp.im(mp.zetazero(n)))
        if g > T:
            return tuple(out)
        out.append(g)
        n += 1


def _omega_characters() -> tuple[dict, dict, float]:
    """The Teichmuller characters mod 5 and kappa of the DH series."""
    I = mp.mpc(0, 1)
    om = {0: 0, 1: 1, 2: I, 4: -1, 3: -I}
    omb = {k: mp.conj(v) for k, v in om.items()}
    kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    return om, omb, float(kap)


def _weil_conjugation() -> dict:
    """The deck step D, colour C and orientation W of the fibre (retro104's)."""
    return _joint_index_model()


def _commutant_dimension(gens: list[np.ndarray]) -> int:
    """dim of the commutant of the algebra generated by ``gens``."""
    n = gens[0].shape[0]
    rows = [np.kron(np.eye(n), g) - np.kron(g.T, np.eye(n)) for g in gens]
    M = np.vstack(rows)
    return n * n - np.linalg.matrix_rank(M, tol=1e-9)


@pytest.mark.slow
def test_retro105_the_two_factors_have_the_counts_and_spacings_of_the_manuscript() -> None:
    r"""``04-bridges:168`` — the $240$ zeros of $L(s,\chiv)$ and the $156$ of
    $\zeta$ below height $330$: no spacing below $0.1$, the smallest are
    $0.231$ and $0.372$ (in that order, the two factors as named)."""
    census = _claim(
        "04-bridges.tex",
        r"the\s*\$(\d+)\$ zeros of \$L\(s,\\chiv\)\$ and the \$(\d+)\$ zeros of \$\\zeta\$ "
        r"below height \$(\d+)\$",
        "the zero census of the two factors",
    )
    n_l, n_z, height = (int(census.group(i)) for i in (1, 2, 3))
    m = _claim(
        "04-bridges.tex",
        r"have no spacing below \$([\d.]+)\$: the smallest are\s*\$([\d.]+)\$ and \$([\d.]+)\$",
        "the smallest spacings",
    )
    a, small_l, small_z = float(m.group(1)), m.group(2), m.group(3)

    chi = json.loads((PRUEBAS / "chi5_zeros.json").read_text(encoding="utf-8"))
    # The corpus reads zeta up to the top of the committed L set (retro105's
    # own T), which sits below the height the sentence states.
    zeta = _zeta_zeros_upto(chi[-1])
    assert len(zeta) == n_z, f"{len(zeta)} zeta zeros, the manuscript says {n_z}"
    assert len(chi) == n_l, f"{len(chi)} L(s,chi5) zeros, the manuscript says {n_l}"
    assert chi[-1] <= height, "the committed L zeros run past the stated height"

    below_l, _, min_l = _small_spacings(chi, _counting_chi, a)
    below_z, _, min_z = _small_spacings(zeta, _counting_zeta, a)
    assert below_l == 0 and below_z == 0, f"a spacing below {a}: L {below_l}, zeta {below_z}"
    assert min_l > a and min_z > a, "the smallest spacing is not above the threshold"
    assert_half_last_digit(min_l, small_l, "04-bridges:168 smallest L spacing")
    assert_half_last_digit(min_z, small_z, "04-bridges:168 smallest zeta spacing")


@pytest.mark.slow
def test_retro105_the_union_of_the_two_sectors_shows_the_small_spacings() -> None:
    r"""``04-bridges:174-176`` — the zeros of $\zeta_K=\zeta\cdot L(s,\chiv)$
    have $11$ spacings below $0.1$ out of $388$, the smallest $0.017$, and no
    ordinate is shared by the two factors in this range."""
    m = _claim(
        "04-bridges.tex",
        r"have \$(\d+)\$\s*spacings below \$([\d.]+)\$ out of \$(\d+)\$, the smallest \$([\d.]+)\$, "
        r"and no ordinate is shared",
        "the union spacings",
    )
    n_small, a, n_total, smallest = m.group(1), float(m.group(2)), int(m.group(3)), m.group(4)

    chi = json.loads((PRUEBAS / "chi5_zeros.json").read_text(encoding="utf-8"))
    zeta = _zeta_zeros_upto(chi[-1])
    merged = sorted(list(zeta) + chi)
    below, total, min_sp = _small_spacings(merged, lambda t: _counting_zeta(t) + _counting_chi(t), a)
    assert below == int(n_small), f"{below} spacings below {a}, the manuscript says {n_small}"
    assert total == n_total, f"{total} spacings, the manuscript says {n_total}"
    assert_half_last_digit(min_sp, smallest, "04-bridges:174 smallest union spacing")
    dmin = min(abs(z - c) for z in zeta for c in chi)
    assert dmin > 1e-6, f"a zero of zeta and one of L(chi5) share an ordinate within {dmin}"


@pytest.mark.slow
def test_retro105_sector_fractions_match_the_manuscript() -> None:
    """``04-bridges:171-173`` — the expected fraction of small spacings is
    about $10^{-3}$ for the GUE, $0.047$ for two independent sectors and
    $0.079$ for six (the seeded ensemble of the script)."""
    gue_txt = _claim("04-bridges.tex", r"ensemble the expected fraction of such spacings is about \$10\^\{(-\d+)\}\$",
                     "the GUE expectation").group(1)
    m = _claim(
        "04-bridges.tex",
        r"for two\s*independent sectors it is about \$([\d.]+)\$, and for six about \$([\d.]+)\$",
        "the sector fractions",
    )
    rows = _sector_sweep()
    gue, two, six = (r[2] for r in rows)
    gue_exp = 32 / math.pi**2 * 0.1**3 / 3
    assert 0.5 <= gue_exp / 10.0 ** int(gue_txt) < 1.5, f"{gue_exp} does not round to 10^{gue_txt}"
    assert_half_last_digit(two, m.group(1), "04-bridges:171 two-sector fraction")
    assert_half_last_digit(six, m.group(2), "04-bridges:171 six-sector fraction")
    assert gue < two < six, "the loss of repulsion does not grow with the number of sectors"


def test_retro105_commutants_have_the_dimensions_the_manuscript_states() -> None:
    r"""``03-mechanisms:3584-3585`` — the commutant of the deck step has
    dimension six (one sector per character of $\mu_6$) and the commutant of
    the pair $D,Y$ is the scalars (dimension one)."""
    six = int(_figure(_claim("03-mechanisms.tex", r"commutant of the deck\s+step of \S+ has dimension (\w+)",
                             "the commutant of D")))
    model = _weil_conjugation()
    Y = (2 * model["C"]) @ model["W"]
    assert _commutant_dimension([model["Dm"]]) == six, "the commutant of D is not six-dimensional"
    assert _commutant_dimension([model["Dm"], Y]) == 1, "the pair D, Y does have a non-scalar commutant"


def test_retro105_antiunitary_symmetry_forces_doublets() -> None:
    """``03-mechanisms:3577-3579`` (prop:symmetry-spectrum ii) — an
    antiunitary $T=UK$ with $T^2=-1$ commuting with $H$ forces every
    eigenvalue to have even multiplicity and fixes no ray: the Kramers
    sample of the script splits into exact doublets."""
    _claim("03-mechanisms.tex", r"then \$T\$ fixes no ray", "the antiunitary clause")
    rng = np.random.default_rng(105)
    H, J, v = _kramers_doublet(rng)
    assert np.allclose(J @ J.conj(), -np.eye(80)), "T^2 is not -1"
    assert np.allclose(J @ H.conj(), H @ J), "T does not commute with H"
    w = np.linalg.eigvalsh(H)
    assert np.allclose(w[0::2], w[1::2], atol=1e-8), "an eigenvalue is not a Kramers doublet"
    assert abs(np.vdot(v, J @ v.conj())) < 1e-9 * np.linalg.norm(v) ** 2, "T fixes a ray"


# ===========================================================================
# retro109.py — 03-mechanisms:3491
# ===========================================================================
def _mpow(n: int, mod: int | None = None) -> tuple[int, int, int, int]:
    """M^n for M = [[0,1],[1,1]], reduced mod ``mod`` when given (retro109's)."""
    a, b, c, d = 1, 0, 0, 1
    x = (0, 1, 1, 1)
    for _ in range(n):
        a, b, c, d = (a * x[0] + b * x[2], a * x[1] + b * x[3], c * x[0] + d * x[2], c * x[1] + d * x[3])
        if mod:
            a, b, c, d = a % mod, b % mod, c % mod, d % mod
    return a, b, c, d


def _lucas(n: int) -> int:
    L = [2, 1]
    for _ in range(2, n + 1):
        L.append(L[-1] + L[-2])
    return L[n]


def _clocks(p: int) -> list[int]:
    """The clock orders of phi at p: two in F_p if p splits, one in F_p^2."""
    if p % 5 in (1, 4):
        r = sqrt_mod(5, p)
        inv2 = pow(2, -1, p)
        out = []
        for t in ((1 + r) * inv2 % p, (1 - r) * inv2 % p):
            k, x = 1, t
            while x != 1:
                x = x * t % p
                k += 1
            out.append(k)
        return out
    k, x = 1, (0, 1)
    while x != (1, 0):
        u, v = x
        x = (v % p, (u + v) % p)
        k += 1
    return [k]


def test_retro109_wall_law_holds_for_every_prime_below_the_stated_bound() -> None:
    """``03-mechanisms:3491`` (ii) — the period of $M$ on the $p$-torsion is
    the lcm of the clocks over $p$ (Wall's law) and $p$ divides
    $|N(\varphi^{e}-1)|$, for every prime below $400$ other than the
    ramified $5$."""
    bound = int(_claim("03-mechanisms.tex", r"by \\code\{retro109\.py\} for the primes below \$(\d+)\$",
                       "the prime bound").group(1))
    for p in primerange(2, bound):
        if p == 5:
            continue
        clocks = _clocks(p)
        e = 1
        while _mpow(e, p) != (1, 0, 0, 1):
            e += 1
        expected = math.lcm(*clocks) if len(clocks) > 1 else clocks[0]
        assert e == expected, f"p={p}: period {e} != lcm of the clocks {expected}"
        assert abs(_lucas(e) - 1 - (-1) ** e) % p == 0, f"p={p} does not divide N(phi^e - 1)"


def test_retro109_fixed_points_equal_the_determinant_up_to_the_stated_height() -> None:
    r"""``03-mechanisms:3489-3491`` (i) — the kernel of $M^n-I$ on the torus
    has $|\det(M^n-I)|=|L_n-1-(-1)^n|$ points, enumerated for $n\le8$."""
    nmax = int(_claim("03-mechanisms.tex", r"by\s+enumeration for \$n\\le(\d+)\$", "the enumeration height").group(1))
    for n in range(1, nmax + 1):
        a, b, c, d = _mpow(n)
        det = abs((a - 1) * (d - 1) - b * c)
        assert det == abs(_lucas(n) - 1 - (-1) ** n), f"n={n}: the determinant is not N(phi^n - 1)"
        cnt = sum(
            1
            for x in range(det)
            for y in range(det)
            if ((a - 1) * x + b * y) % det == 0 and (c * x + (d - 1) * y) % det == 0
        )
        assert cnt == det, f"n={n}: {cnt} fixed points, the determinant says {det}"


# ===========================================================================
# retro119.py — 03-mechanisms:1490 (prop:class-angular (iv))
# ===========================================================================
def _mulq(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    """(a0+a1 w)(b0+b1 w) over Z/p with w^2 = w+1."""
    a0, a1 = a
    b0, b1 = b
    return ((a0 * b0 + a1 * b1) % p, (a0 * b1 + a1 * b0 + a1 * b1) % p)


def _powq(a: tuple[int, int], n: int, p: int) -> tuple[int, int]:
    r = (1, 0)
    while n:
        if n & 1:
            r = _mulq(r, a, p)
        a = _mulq(a, a, p)
        n >>= 1
    return r


def _omega_order(p: int, N: int) -> int:
    """Order of w in (Z[w]/p)^x, given w^N = 1."""
    e = N
    for q in factorint_local(N):
        while e % q == 0 and _powq((0, 1), e // q, p) == (1, 0):
            e //= q
    return e


def factorint_local(n: int) -> list[int]:
    """The distinct prime factors of ``n`` (small n: trial division)."""
    return sorted(_factor_counts(n))


def _factor_counts(n: int) -> dict[int, int]:
    """Prime -> exponent for ``n`` (small n: trial division, no sympy call)."""
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


@functools.lru_cache(maxsize=None)
def _clock_three_data(lo: int, hi: int) -> tuple[int, dict]:
    r"""(criterion failures, [(split_total, inert_total, split_coprime, inert_coprime)]).

    Ports retro119's sweep: for every prime in [lo, hi) the criterion of
    prop:class-angular (iv) — with $N_p=3^km$, $3\nmid m$, $3\mid e_p$ iff
    $\varphi^m\not\equiv1$ — and the tally of the primes whose class admits a
    factor 3 (necessary condition of (iv)).
    """
    bad = 0
    occ = {"split": [0, 0], "inert": [0, 0]}
    for p in primerange(lo, hi):
        split = p % 5 in (1, 4)
        N = p - 1 if split else 2 * (p + 1)
        assert _powq((0, 1), N, p) == (1, 0), f"p={p}: phi^N_p is not 1"
        e = _omega_order(p, N)
        m, k = N, 0
        while m % 3 == 0:
            m //= 3
            k += 1
        crit = _powq((0, 1), m, p) != (1, 0)
        if crit != (e % 3 == 0):
            bad += 1
        nec = (p % 3 == 1) if split else (p % 3 == 2)
        if e % 3 == 0:
            assert nec, f"p={p}: 3 | e_p but the necessary condition fails"
        if nec:
            occ["split" if split else "inert"][int(e % 3 == 0)] += 1
    return bad, occ


def test_retro119_the_three_criterion_holds_at_every_prime_of_the_stated_range() -> None:
    r"""``03-mechanisms:1490`` — over the primes $7\le p<6000$ (iv) holds at
    every prime: $3\mid e_p$ iff $\varphi^m\not\equiv1$, and the necessary
    condition on $p\bmod3$ is never violated."""
    m = _claim("03-mechanisms.tex", r"over the\s*primes \$(\d+)\\le p<(\d+)\$", "the prime range")
    lo, hi = int(m.group(1)), int(m.group(2))
    bad, _ = _clock_three_data(lo, hi)
    assert bad == 0, f"{bad} primes violate the criterion of (iv)"


def test_retro119_counts_of_primes_meeting_the_condition_match_the_manuscript() -> None:
    """``03-mechanisms:1488-1490`` — of the primes that meet the condition of
    (iv) $185$ split and $197$ inert, and $42$ and $52$ of them have $e_p$
    prime to $3$."""
    m = _claim(
        "03-mechanisms.tex",
        r"condition of \(iv\) \$(\d+)\$ split and \$(\d+)\$ inert, \$(\d+)\$ and \$(\d+)\$ of them have",
        "the tallies of the sentence",
    )
    rng = _claim("03-mechanisms.tex", r"over the\s*primes \$(\d+)\\le p<(\d+)\$", "the prime range")
    _, occ = _clock_three_data(int(rng.group(1)), int(rng.group(2)))
    assert len(occ["split"]) == 2 and occ["split"][0] + occ["split"][1] == int(m.group(1)), occ
    assert occ["inert"][0] + occ["inert"][1] == int(m.group(2)), occ
    assert occ["split"][0] == int(m.group(3)), occ
    assert occ["inert"][0] == int(m.group(4)), occ


# ===========================================================================
# The window quadratic form of retro67.py (exec'd by retro69/78/93)
# ===========================================================================
def _repsi(r) -> float:
    return float(np.real(cpsi(0.25 + 0.5j * r)))


def _inert_order(p: int) -> int:
    """Order of w in (Z[w]/p)^x for an inert prime (m = 2(p+1))."""
    m = 2 * (p + 1)
    o = m
    for q in factorint_local(m):
        while o % q == 0 and _powq((0, 1), o // q, p) == (1, 0):
            o //= q
    return o


@functools.lru_cache(maxsize=None)
def _ideals_upto(X: int) -> tuple:
    """The ideals of K = Q(phi) of norm <= X as (norm, level) pairs."""
    out = [(4, "2"), (5, "5")]  # 2 inert (norm 4) and sqrt5 ramified: outside the clock
    for p in primerange(3, X + 1):
        if p == 5:
            continue
        if _chi5p(p) == 1:
            inv2 = pow(2, -1, p)
            for s in sqrt_mod(5, p, all_roots=True):
                out.append((p, n_order((1 + s) * inv2 % p, p)))
        elif p * p <= X:
            out.append((p * p, _inert_order(p)))
    return tuple(out)


@functools.lru_cache(maxsize=None)
def _build(L: float, N: int) -> dict:
    """The cell base of retro67's window: steps, the pole, Psi and Pform."""
    D = L / N
    x = -L / 2 + (np.arange(N) + 0.5) * D
    d = x[:, None] - x[None, :]

    def T(v):
        return np.maximum(0.0, D - np.abs(v))

    G0 = D * np.eye(N)
    vp = np.array([(math.exp((xj + D / 2) / 2) - math.exp((xj - D / 2) / 2)) * 2 for xj in x])
    vm = np.array([-(math.exp(-(xj + D / 2) / 2) - math.exp(-(xj - D / 2) / 2)) * 2 for xj in x])
    Pole = np.outer(vp, vm) + np.outer(vm, vp)

    def f(r, m=0):
        return D * D * (np.sinc(r * D / (2 * math.pi))) ** 2 * _repsi(r) * math.cos(m * D * r)

    def lowm(m, R=1e5):
        step = math.pi / ((m + 1) * D)
        s, a = 0.0, 0.0
        while a < R:
            b = min(a + step, R)
            s += quad(f, a, b, args=(m,), epsabs=1e-14, epsrel=1e-12)[0]
            a = b
        return s + {0: 1.0, 1: -0.5}.get(m, 0.0) * 2 * (math.log(R / 2) + 1) / R

    def qawf(m):
        return quad(lambda r: f(r), 0, np.inf, weight="cos", wvar=m * D, limlst=400)[0]

    psim = [(lowm(m) if m <= 4 else qawf(m)) / math.pi for m in range(N)]
    Psi1 = np.array([[psim[abs(i - j)] for j in range(N)] for i in range(N)])

    def Pform(lst):
        M = np.zeros((N, N))
        for Nrm in lst:
            Nk = Nrm
            while math.log(Nk) < L:
                w = math.log(Nrm) / math.sqrt(Nk)
                u = math.log(Nk)
                M += w * (T(u - d) + T(-u - d))
                Nk *= Nrm
        return M

    return dict(x=x, D=D, G0=G0, Pole=Pole, Psi1=Psi1, Pform=Pform, T=T)


def _window_form(X: int, N: int = 48) -> tuple[dict, np.ndarray, dict, dict]:
    """(base, A, level forms, W) of the window e^L = X: A - sum_n P_n."""
    L = math.log(X)
    B = _build(L, N)
    A = B["Pole"] + (math.log(5) - 2 * math.log(math.pi)) * B["G0"] + 2 * B["Psi1"]
    groups = defaultdict(list)
    for Nrm, lev in _ideals_upto(X):
        groups[lev].append(Nrm)
    Pn = {lev: B["Pform"](v) for lev, v in groups.items()}
    W = A - sum(Pn.values())
    return B, A, Pn, W


def _window_of_the_sentence() -> int:
    """``e^L=10^3`` of 04-bridges:1508, as the level bound X of the window."""
    m = _claim("04-bridges.tex", r"in the window \$e\^L=(\d+)\^(\d+)\$", "the window")
    return int(m.group(1)) ** int(m.group(2))


@pytest.mark.slow
def test_retro67_removing_any_one_of_the_stated_levels_breaks_the_positivity() -> None:
    """``04-bridges:1508-1509`` — in the window $e^L=10^3$ the window form is
    positive, but removing any one of $108$ of the $127$ levels makes it
    indefinite (the other $19$ levels are dispensable)."""
    X = _window_of_the_sentence()
    m = _claim(
        "04-bridges.tex",
        r"removing any one of \$(\d+)\$ of the \$(\d+)\$ levels breaks it",
        "the leave-one-out tally",
    )
    n_breaking, n_levels = int(m.group(1)), int(m.group(2))

    _, _, Pn, W = _window_form(X)
    lam = np.linalg.eigvalsh(W)
    assert lam[0] > -1e-8 * abs(lam[-1]), f"the window form is already indefinite: {lam[0]}"
    assert len(Pn) == n_levels, f"{len(Pn)} levels in the window, the manuscript says {n_levels}"
    loo = [float(np.linalg.eigvalsh(W + M)[0]) for M in Pn.values()]
    assert sum(1 for v in loo if v < 0) == n_breaking, (
        f"{sum(1 for v in loo if v < 0)} of {len(loo)} levels break the positivity, "
        f"the manuscript says {n_breaking}"
    )


@pytest.mark.slow
def test_retro67_a_single_ideal_changes_sign_at_the_stated_fraction_of_the_window() -> None:
    r"""``04-bridges:1509`` — along the direction of the pole a single prime
    ideal contributes with the sign of its size: negative below
    $\log N\approx0.38\,L$ and positive above, whatever its level — one
    crossing, at the stated fraction, for every level of the window."""
    X = _window_of_the_sentence()
    frac_txt = _claim(
        "04-bridges.tex", r"negative below\s+\$\\log N\\approx([\d.]+)\\,L\$ and positive above", "the threshold"
    ).group(1)

    B, A, _, W = _window_form(X)
    L = math.log(X)
    ev, V = np.linalg.eigh(A)
    w1 = V[:, 0]
    D, xx = B["D"], B["x"]
    dd = xx[:, None] - xx[None, :]
    T = B["T"]

    def contribution(u: float) -> float:
        return float(-w1 @ (T(u - dd) + T(-u - dd)) @ w1)

    us = np.linspace(0.01, L, 2000)
    cs = [contribution(u) for u in us]
    crossings = [us[i] for i in range(len(us) - 1) if cs[i] * cs[i + 1] < 0]
    assert len(crossings) == 1, f"{len(crossings)} sign changes in the window"
    above = [us[i] for i, v in enumerate(cs) if v < 0 and us[i] > crossings[0]]
    assert not above, f"negative again above the crossing at u*={crossings[0]}: {above[:5]}"
    assert_printed_as_in_manuscript(crossings[0] / L, frac_txt, "04-bridges:1509 u*/L")
    # The pole direction of A is the negative one, and the window form is
    # positive there once every level contributes.
    assert ev[0] < 0, "A has no negative direction to speak of"
    assert float(w1 @ W @ w1) > 0, "the window form is negative along the pole direction"


# ===========================================================================
# retro69.py — 03-mechanisms:1402
# ===========================================================================
def _Q_value(n: int) -> int:
    """Q(n) = prod_{d|n} |N(phi^d-1)|^{mu(n/d)} (retro69's ``Q``)."""
    L = [2, 1]
    for _ in range(2, n + 1):
        L.append(L[-1] + L[-2])
    Npow = {d: abs((-1) ** d - L[d] + 1) for d in range(1, n + 1)}
    num = den = 1
    for d in divisors(n):
        m = mobius(n // d)
        if m == 1:
            num *= Npow[d]
        elif m == -1:
            den *= Npow[d]
    assert num % den == 0, f"Q({n}) is not an integer"
    return num // den


def test_retro69_clock_mass_over_its_main_term_matches_the_manuscript() -> None:
    r"""``03-mechanisms:1400-1402`` (vii) — the mass of the clock up to the
    level $N$, over $(3/\pi^2)\log\varphi\,N^2$, is $1.0038$, $1.0018$,
    $1.0008$ and $1.0006$ at $N=100$, $500$, $1000$, $2000$."""
    m = _claim(
        "03-mechanisms.tex",
        r"whose ratio to the main term is\s*\$([\d.]+)\$, \$([\d.]+)\$, \$([\d.]+)\$ and \$([\d.]+)\$ "
        r"at \$N=(\d+)\$, \$(\d+)\$, \$(\d+)\$ and \$(\d+)\$",
        "the four ratios",
    )
    printed = [m.group(i) for i in (1, 2, 3, 4)]
    levels = [int(m.group(i)) for i in (5, 6, 7, 8)]

    log_phi = math.log((1 + 5**0.5) / 2)
    mass, ratios, next_level = 0.0, {}, 1
    for n in range(1, max(levels) + 1):
        if n >= 3:
            q = _Q_value(n)
            mass += math.log(q) if q > 1 else 0.0
        if n in levels:
            ratios[n] = mass / (3 / math.pi**2 * log_phi * n * n)
    assert sorted(ratios) == sorted(levels), "the sentence's levels are not the ones checked"
    for n, txt in zip(levels, printed):
        assert_half_last_digit(ratios[n], txt, f"03-mechanisms:1402 clock mass at N={n}")


# ===========================================================================
# retro78.py — 03-mechanisms:1627
# ===========================================================================
def _zeta5_from_phi(p: int, r: int):
    """The primitive 5th root of unity with z + 1/z = r - 1 (the one phi fixes)."""
    for z in nthroot_mod(1, 5, p, all_roots=True):
        if z != 1 and (z + pow(z, -1, p)) % p == (r - 1) % p:
            return z
    return None


@functools.lru_cache(maxsize=None)
def _prime_ideal_classes(X: int) -> tuple[dict, int, int]:
    """The classes {1}, {zeta^+-1}, {zeta^+-2} of the ideals over p=1 mod 5.

    Returns (parts, checked, ambiguous): ``checked`` counts the ideals whose
    identification the quintic symbol of phi fixes, ``ambiguous`` those it
    fails to fix (the corpus says zero).
    """
    parts = defaultdict(list)
    ambig = checked = 0
    for p in primerange(11, X + 1):
        if p % 5 != 1:
            continue
        inv2 = pow(2, -1, p)
        for s in sqrt_mod(5, p, all_roots=True):
            r = (1 + s) * inv2 % p
            z = _zeta5_from_phi(p, r)
            if z is None:
                ambig += 1
                continue
            checked += 1
            sym = pow(r, (p - 1) // 5, p)
            e = next(j for j in range(5) if pow(z, j, p) == sym)
            parts[min(e, 5 - e)].append(p)
    return dict(parts), checked, ambig


def test_retro78_ideal_count_and_class_frequencies_match_the_manuscript() -> None:
    r"""``03-mechanisms:1625-1627`` — over the $39\,234$ prime ideals of norm
    $p\equiv1\pmod5$ below $10^6$ the identification of $\mu_5$ is
    unambiguous at every one, and the classes have frequencies $0.2003$,
    $0.3999$, $0.3999$."""
    m = _claim(
        "03-mechanisms.tex",
        r"over the \$(\d+)\\,(\d+)\$ prime ideals of norm \$p\\equiv1\\pmod5\$ below \$10\^(\d+)\$",
        "the ideal census",
    )
    n_ideals = int(m.group(1) + m.group(2))
    X = 10 ** int(m.group(3))
    freq_txt = _claim(
        "03-mechanisms.tex",
        r"the classes have frequencies \$([\d.]+)\$, \$([\d.]+)\$, \$([\d.]+)\$",
        "the class frequencies",
    )
    _claim("03-mechanisms.tex", r"the identification is unambiguous at every one", "the unambiguity clause")

    parts, checked, ambig = _prime_ideal_classes(X)
    assert ambig == 0, f"{ambig} ideals the identification does not fix"
    assert checked == n_ideals, f"{checked} prime ideals, the manuscript says {n_ideals}"
    tot = sum(len(v) for v in parts.values())
    assert tot == n_ideals, "the classes do not partition the ideals"
    for k in (0, 1, 2):
        assert_half_last_digit(len(parts[k]) / tot, freq_txt.group(k + 1),
                               f"03-mechanisms:1627 frequency of class {k}")


@pytest.mark.slow
def test_retro78_the_two_exchanged_parts_of_the_prime_side_coincide() -> None:
    """``03-mechanisms:1627`` — the two exchanged parts of the prime side
    coincide: the Weil forms of {zeta^+-1} and {zeta^+-2} are equal, because
    conjugation maps one to the other (each $p$ contributes one ideal to each
   , or both to {1})."""
    _claim("03-mechanisms.tex", r"the two exchanged parts of the prime side coincide", "the coincidence clause")
    X = 10**6
    parts, _, _ = _prime_ideal_classes(X)
    B = _build(math.log(X), 48)
    F = {k: B["Pform"](v) for k, v in parts.items()}
    norm = lambda M: float(np.abs(np.linalg.eigvalsh(M)).max())
    assert norm(F[1] - F[2]) / norm(F[1]) == 0.0, "the two exchanged parts differ as Weil forms"
    pair = defaultdict(list)
    for k, v in parts.items():
        for p in v:
            pair[p].append(k)
    assert all(sorted(v) in ([1, 2], [0, 0]) for v in pair.values()), (
        "a prime contributes its two ideals to the wrong classes"
    )


# ===========================================================================
# The Weil representation of retro81/83/86 (exec'd by retro87/88/89)
# ===========================================================================
def _mm(g, h, N: int):
    """Matrix product mod N (retro81's ``mm``)."""
    return tuple(
        tuple(sum(g[i][k] * h[k][j] for k in range(2)) % N for j in range(2)) for i in range(2)
    )


I2 = ((1, 0), (0, 1))


def _order(g, N: int, proj: bool = False) -> int:
    h, n = g, 1
    while not (h == I2 or (proj and h == ((N - 1, 0), (0, N - 1)))):
        h = _mm(h, g, N)
        n += 1
    return n


def _weil(g, N: int) -> np.ndarray:
    """The unnormalised Weil kernel U[y,x] = N^{-1/2} e(...)."""
    (a, b), (c, d) = g
    assert math.gcd(b, N) == 1
    k = pow(2 * b, -1, N)
    x = np.arange(N)
    ph = (k * (a * x[None, :] ** 2 - 2 * np.outer(x, x) + d * x[:, None] ** 2)) % N
    return np.exp(2j * np.pi * ph / N) / math.sqrt(N)


def _gauss(k: int, N: int) -> complex:
    return sum(np.exp(2j * np.pi * ((k * x * x) % N) / N) for x in range(N))


def _wn(g, N: int) -> np.ndarray:
    """W(g): the Weil representation normalised to be multiplicative."""
    return math.sqrt(N) / _gauss(pow(2 * g[0][1], -1, N), N) * _weil(g, N)


def _rand_sl2(N: int, rng: random.Random, bunit: bool = True):
    """A random element of SL_2(Z/N) with a unit b-entry (retro83's sampler)."""
    while True:
        a, b, c = rng.randrange(N), rng.randrange(N), rng.randrange(N)
        if math.gcd(a, N) != 1 or (bunit and math.gcd(b, N) != 1):
            continue
        return ((a, b), (c, (1 + b * c) * pow(a, -1, N) % N))


def _prop_to(U: np.ndarray, V: np.ndarray):
    """Whether U = c V for a unimodular c (a projective relation)."""
    i = np.unravel_index(np.argmax(np.abs(V)), V.shape)
    c = U[i] / V[i]
    return abs(abs(c) - 1) < 1e-8 and np.allclose(U, c * V, atol=1e-8), c


def _uperiod(U: np.ndarray, maxn: int):
    """The projective period of U: the least n with U^n a unimodular scalar."""
    P = np.eye(len(U), dtype=complex)
    for n in range(1, maxn + 1):
        P = P @ U
        ok, c = _prop_to(P, np.eye(len(U)))
        if ok:
            return n, c
    return None, None


def _five_power_spectrum(N: int) -> dict:
    """The propagator U(B) at N: period, Hecke order and multiplicities."""
    B = ((1, 1), (1, 2))
    U = _wn(B, N)
    per, c = _uperiod(U, 4 * _order(B, N))
    ev = np.linalg.eigvals(U)
    lam = c ** (1.0 / per)
    k_ = np.round(np.angle(ev / lam) / (2 * np.pi) * per).astype(int) % per
    C = [
        ((x + y) % N, y % N)
        for x in range(N)
        for y in range(N)
        if ((x + y) * (x + 2 * y) - y * y) % N == 1
    ]
    mult = np.bincount(k_, minlength=per)
    return dict(per=per, mult=mult, hecke=len(C), oB=_order(B, N), oM=_order(((0, 1), (1, 1)), N), U=U, c=c, lam=lam)


def test_retro81_the_spectrum_at_five_powers_is_simple_with_the_stated_index() -> None:
    r"""``04-bridges:1689-1691`` (prop:index-degeneracy (iv), the statement
    the ``\code{retro81.py}--\code{retro87.py}`` range carries) — at $N=5^k$
    the spectrum is simple and fills half the circle with $e=2\cdot5^k$: each
    phase appears at most once, the occupied phases are half of them, and the
    period of $U$ is that $e$."""
    m = _claim(
        "04-bridges.tex",
        r"At \$N=5\^k\$ the spectrum is simple and fills half the circle: \$e=(\d+)\\cdot5\^k\$",
        "the index at 5^k",
    )
    e_coeff = int(m.group(1))
    for k in (1, 2, 3):
        N = 5**k
        r = _five_power_spectrum(N)
        e = e_coeff * N
        assert r["per"] == e, f"N=5^{k}: period {r['per']}, the manuscript says {e}"
        assert r["oB"] == e, f"N=5^{k}: order of M^2 is {r['oB']}, not {e}"
        assert r["hecke"] == e, f"N=5^{k}: the Hecke group has order {r['hecke']}"
        assert set(np.unique(r["mult"])) <= {0, 1}, "the spectrum is not simple"
        assert int(r["mult"].sum()) == N, "the multiplicities do not fill the dimension"
        assert int((r["mult"] > 0).sum()) * 2 == e, "the occupied phases are not half the circle"


def test_retro81_the_index_identity_holds_at_the_primes() -> None:
    r"""``04-bridges:1683-1686`` (prop:index-degeneracy (ii)-(iii)) — at a
    prime $p\ne5$ every $e$-th root but one has multiplicity
    $m=(p-\chiv(p))/e$, and $p=e\,m+\chiv(p)$."""
    mult_txt = _claim("04-bridges.tex", r"multiplicity \$m=\(p-\\chiv\(p\)\)/e\$", "the multiplicity")
    identity = _claim("04-bridges.tex", r"In both cases \$p=e\\,m\+\\chiv\(p\)\$", "the index identity")
    assert mult_txt is not None and identity is not None
    for p in (3, 7, 11, 19, 29, 31):
        chi = _chi5p(p)
        r = _five_power_spectrum(p)
        e, mult = r["per"], r["mult"]
        base = int(np.bincount(mult).argmax())
        assert base == (p - chi) // e, f"p={p}: multiplicity {base} != (p-chi5(p))/{e}"
        assert p == e * base + chi, f"p={p}: the index identity p = e m + chi5(p) fails"
        assert set(np.unique(mult).tolist()) <= {base - 1, base, base + 1}, (
            f"p={p}: a phase carries a multiplicity far from m={base}"
        )
        assert int((mult == base).sum()) == e - 1, f"p={p}: not every phase but one carries m={base}"


# ===========================================================================
# retro87.py — 04-bridges:1721-1725
# ===========================================================================
def _fib_fast(n: int) -> int:
    """F_n by fast doubling (the chain reaches n ~ 10^6, where a loop drags)."""
    def pair(k: int) -> tuple[int, int]:
        if k == 0:
            return (0, 1)
        a, b = pair(k >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (d, c + d) if k & 1 else (c, d)

    return pair(n)[0]


def _v5(x: int) -> tuple[int, int]:
    v = 0
    while x and x % 5 == 0:
        x //= 5
        v += 1
    return v, x


def _L5(x: int) -> int:
    return int(legendre_symbol(x % 5, 5))


def _G1(c: int, K: int) -> tuple[int, int]:
    """sum_{x mod 5^K} e(c x^2/5^K) = sign * 5^(e/2)."""
    N = 5**K
    c %= N
    if c == 0:
        return (1, 2 * K)
    v, u = _v5(c)
    return (_L5(u) ** (K - v), 2 * v + (K - v))


def _S2(A: int, Bc: int, C: int, K: int) -> tuple[int, int]:
    """The binary quadratic Gauss sum of retro86, exact as (sign, e/2)."""
    N = 5**K
    A, Bc, C = A % N, Bc % N, C % N
    if K == 0:
        return (1, 0)
    if A % 5 == 0 and Bc % 5 == 0 and C % 5 == 0:
        if (A, Bc, C) == (0, 0, 0):
            return (1, 4 * K)
        s, e = _S2(A // 5, Bc // 5, C // 5, K - 1)
        return (s, e + 4)
    if A % 5 == 0 and C % 5 != 0:
        A, C = C, A
    if A % 5 == 0:
        A, Bc, C = A, (2 * A + Bc) % N, (A + Bc + C) % N
        A, C = C, A
    inv = pow(4 * A, -1, N)
    s1, e1 = _G1(A, K)
    s2, e2 = _G1(C - Bc * Bc * inv, K)
    return (s1 * s2, e1 + e2)


def _ldt_trace(g, K: int, var: tuple) -> float:
    """The LDT formula for tr W(g): (a/5)^K 5^{-K} S(Q)."""
    N = 5**K
    (a, b), (c, d) = g
    ai, i2 = pow(a, -1, N), pow(2, -1, N)
    sb, sg, inv, sx = var
    beta, gamma = b * ai % N, c * ai % N
    A = sb * beta * i2 % N
    X = sx * (1 - (ai if inv else a)) % N
    Cc = sg * gamma * i2 % N
    s, e = _S2(A, X, Cc, K)
    return _L5(a) ** K * s * 5 ** (e / 2 - K)


def _true_trace(g, K: int) -> complex:
    """tr W(g) straight from the matrix (the diagonalisation of the corpus)."""
    N = 5**K
    if g[0][1] % 5:
        return complex(np.trace(_wn(g, N)))
    for h in (((1, 1), (0, 1)), ((1, 2), (0, 1)), ((2, 1), (1, 1)), ((1, 1), (1, 2))):
        hi = ((h[1][1] % N, -h[0][1] % N), (-h[1][0] % N, h[0][0] % N))
        g2 = _mm(hi, g, N)
        if g2[0][1] % 5:
            return complex(np.trace(_wn(h, N) @ _wn(g2, N)))
    raise ValueError("no unit entry to reduce to")


VARIANTS = list(itertools.product((1, -1), (1, -1), (0, 1), (1, -1)))


def _rand_g(K: int, rng: random.Random, cong: int = 0):
    N = 5**K
    while True:
        a = rng.randrange(N)
        b = rng.randrange(N)
        c = rng.randrange(N)
        if cong:
            a = (1 + 5**cong * a) % N
            b = 5**cong * b % N
            c = 5**cong * c % N
        if a % 5 == 0:
            continue
        return ((a, b), (c, (1 + b * c) * pow(a, -1, N) % N))


def _retro87_elements() -> list[tuple]:
    """The validation set of retro87: units, then 1 mod 5, then 1 mod 25."""
    rng = random.Random(87)
    return (
        [(_rand_g(K, rng), K) for K in (1, 2, 3) for _ in range(25)]
        + [(_rand_g(K, rng, 1), K) for K in (2, 3) for _ in range(25)]
        + [(_rand_g(3, rng, 2), 3) for _ in range(15)]
    )


@functools.lru_cache(maxsize=1)
def _retro87_variant() -> tuple:
    """The sign variant retro87 settles on: the first that reproduces every
    trace of the validation set against the diagonalisation (its ``good[0]``)."""
    elements = _retro87_elements()
    good = [
        var
        for var in VARIANTS
        if all(abs(_ldt_trace(g, K, var) - _true_trace(g, K)) < 1e-6 for g, K in elements)
    ]
    assert good, "no variant of the LDT formula reproduces the traces"
    return good[0]


def test_retro87_the_completion_of_the_square_is_checked_on_the_stated_elements() -> None:
    r"""``04-bridges:1721-1724`` — the completion of the square is checked on
    $115$ elements, units and congruent to $1$ modulo $5$ and $25$: the
    elements of the validation set at $k\ge2$ are that many, and the LDT
    formula reproduces their trace against the diagonalisation."""
    n_elems = int(_claim("04-bridges.tex", r"checked on \$(\d+)\$ elements, units and congruent to \$1\$",
                         "the element count").group(1))
    elements = _retro87_elements()
    checked = [(g, K) for g, K in elements if K >= 2]
    assert len(checked) == n_elems, f"{len(checked)} elements at k>=2, the manuscript says {n_elems}"

    var = _retro87_variant()
    for g, K in checked:
        assert abs(_ldt_trace(g, K, var) - _true_trace(g, K)) < 1e-6, f"the formula misses at k={K}"


def test_retro87_every_step_of_the_chain_holds_up_to_the_stated_k() -> None:
    r"""``04-bridges:1724-1725`` — every step of the chain holds for $k\le7$,
    for $g=B^{2m}$ with $m=5^v m'$: the three coefficients are divisible by
    $5^v$, $A/5^v$ is a unit, the second coefficient after completing the
    square has valuation exactly $1$ with $(A_1w'/5)=+1$, $(A_1/5)=\chiv(m')$
    because $F_{4m}/5^v\equiv3m'$, and the trace is $5^v\sqrt5\,\chiv(m')$."""
    kmax = int(_claim("04-bridges.tex", r"every\s*step of the chain for \$k\\le(\d+)\$", "the chain bound").group(1))
    B = ((1, 1), (1, 2))
    VAR = _retro87_variant()
    for K in range(2, kmax + 1):
        N = 5**K
        for v in range(1, K):
            for mp in (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14):
                m = 5**v * mp
                a, b, c, d = (_fib_fast(4 * m - 1) % N, _fib_fast(4 * m) % N,
                              _fib_fast(4 * m) % N, _fib_fast(4 * m + 1) % N)
                g = ((a, b), (c, d))
                assert (a - 1) % 5**v == 0 and (d - 1) % 5**v == 0, f"k={K} v={v} m'={mp}: g is not 1 mod 5^v"
                assert _v5(_fib_fast(4 * m))[0] == v, f"k={K} v={v} m'={mp}: v5(F_4m) != v"
                (A, X, Cc) = _chain_coefficients(g, K, VAR)
                assert A % 5**v == 0 and X % 5**v == 0 and Cc % 5**v == 0, f"k={K}: coefficients not divisible"
                assert (A // 5**v) % 5 != 0, f"k={K} v={v}: A/5^v is not a unit"
                assert _L5(A // 5**v) == _L5(mp), f"k={K} v={v} m'={mp}: (A1/5) != chi5(m')"
                assert (_fib_fast(4 * m) // 5**v) % 5 == 3 * mp % 5, f"k={K}: F_4m/5^v != 3m' (mod 5)"
                if K - v >= 2:
                    A1, X1, C1 = A // 5**v, X // 5**v, Cc // 5**v
                    M_ = 5 ** (K - v)
                    w = (C1 - X1 * X1 * pow(4 * A1, -1, M_)) % M_
                    vw, wu = _v5(w)
                    assert vw == 1, f"k={K} v={v}: the completed square has valuation {vw}, not 1"
                    assert _L5(A1) * _L5(wu) == 1, f"k={K} v={v}: (A1 w'/5) != +1"
                s, e = _S2(A, X, Cc, K)
                assert (_L5(a) ** K * s, e - 2 * K) == (_L5(mp), 2 * v + 1), (
                    f"k={K} v={v} m'={mp}: the trace is not 5^v sqrt5 chi5(m')"
                )


def _chain_coefficients(g, K: int, var: tuple) -> tuple[int, int, int]:
    N = 5**K
    (a, b), (c, d) = g
    ai, i2 = pow(a, -1, N), pow(2, -1, N)
    sb, sg, inv, sx = var
    beta, gamma = b * ai % N, c * ai % N
    return (sb * beta * i2 % N, sx * (1 - (ai if inv else a)) % N, sg * gamma * i2 % N)


# ===========================================================================
# retro88.py — 04-bridges:1746
# ===========================================================================
@pytest.mark.parametrize("p", [11, 19, 29, 31, 41, 59, 61])
def test_retro88_at_split_primes_the_operator_is_scaling_and_zero_is_the_extra_state(p: int) -> None:
    r"""``04-bridges:1743-1746`` — at a split prime, in the basis of the torus
    $U(M^2)$ is the scaling of $\mathbb F_p$ by $a=\golden^2$, and the extra
    state is the delta at the fixed point $0$; off it, $\beta$ conjugates the
    operator by a Dirichlet character of order $e$, permuting the $e$ phases
    that each carry multiplicity $m=(p-\chiv(p))/e$."""
    _claim("04-bridges.tex", r"the\s+extra state is the delta at the fixed point \$0\$", "the fixed point")
    _claim("04-bridges.tex", r"multiplicity \$m=\(p-\\chiv\(p\)\)/e\$", "the multiplicity")
    B = ((1, 1), (1, 2))
    r = next(x for x in range(p) if (x * x - x - 1) % p == 0)
    a = r * r % p
    ai = pow(a, -1, p)

    def left(l):
        return (1, (l - 1) % p)

    v1, v2 = left(a), left(ai)
    det = (v1[0] * v2[1] - v1[1] * v2[0]) % p
    s = pow(det, -1, p)
    h = ((v1[0] * s % p, v1[1] * s % p), (v2[0], v2[1]))
    hi = ((h[1][1], -h[0][1] % p), (-h[1][0] % p, h[0][0]))
    assert _mm(_mm(h, B, p), hi, p) == ((a, 0), (0, ai)), "h B h^-1 is not diag(a, 1/a)"

    H = _wn(h, p)
    D = H @ _wn(B, p) @ np.linalg.inv(H)
    eps = int(legendre_symbol(a, p))
    x = np.arange(p)
    D1 = np.zeros((p, p))
    D1[x, x * ai % p] = eps
    D2 = np.zeros((p, p))
    D2[x, x * a % p] = eps
    which = 1 if np.allclose(D, D1, atol=1e-7) else (2 if np.allclose(D, D2, atol=1e-7) else 0)
    assert which in (1, 2), f"p={p}: U(M^2) is not the scaling by a = phi^2"
    assert abs(D[0, 0] - 1) < 1e-7, "delta_0 is not the +1 state"
    assert np.allclose(D[0, 1:], 0, atol=1e-7) and np.allclose(D[1:, 0], 0, atol=1e-7), (
        "the fixed point is not an isolated state"
    )

    g0 = next(g for g in range(2, p) if len({pow(g, k, p) for k in range(p - 1)}) == p - 1)
    ind = {pow(g0, k, p): k for k in range(p - 1)}
    beta = np.diag([np.exp(2j * np.pi * ind[y] / (p - 1)) for y in range(1, p)])
    Dc = D[1:, 1:]
    z = np.exp(2j * np.pi * ind[a] / (p - 1))
    e = _order(B, p)
    assert (
        np.allclose(beta @ Dc @ np.linalg.inv(beta), z * Dc, atol=1e-7)
        or np.allclose(beta @ Dc @ np.linalg.inv(beta), np.conj(z) * Dc, atol=1e-7)
    ), f"p={p}: beta is not a Dirichlet character conjugating U to zeta U"
    assert abs(z**e - 1) < 1e-9 and all(abs(z**k - 1) > 1e-9 for k in range(1, e)), (
        f"p={p}: zeta does not have order e = {e}"
    )
    ev = np.linalg.eigvals(Dc)
    k_ = np.round(np.angle(ev) / (2 * np.pi) * e).astype(int) % e
    assert set(np.bincount(k_, minlength=e).tolist()) == {(p - 1) // e}, (
        f"p={p}: the phases do not all carry m = (p-chi5(p))/e"
    )


def _occupation(j: int, K: int) -> bool:
    """The occupation rule of the phases at N = 5^K (retro88's ``occ``)."""
    N = 5**K
    j %= 2 * N
    if j % N == 0:
        return j == 0
    while j % 5 == 0:
        j //= 5
    return _L5(j) == 1


@pytest.mark.parametrize("K", [1, 2, 3, 4, 5, 6])
def test_retro88_the_shift_preserves_the_layer_and_its_occupation(K: int) -> None:
    """``04-bridges:1746-1748`` — at $5^k$ the shift of the phases by
    $5^{v+1}$ preserves the layer $v_5(j)=v$ and its occupation, and one
    state is left over: outside the layers $j=0$ is occupied, $j=5^k$ is not,
    and the occupied phases are exactly $N$ of the $2N$ available."""
    _claim("04-bridges.tex", r"shift of the phases by \$5\^\{v\+1\}\$ preserves the layer \$v_5\(j\)=v\$",
           "the layer rule")
    N = 5**K
    e = 2 * N
    for v in range(K):
        layer = [j for j in range(e) if j % 5**v == 0 and j % 5 ** (v + 1) != 0]
        shift = 5 ** (v + 1)
        assert all(_occupation(j, K) == _occupation(j + shift, K) for j in layer), (
            f"K={K} v={v}: the shift by 5^{v+1} changes the occupation"
        )
        assert sum(_occupation(j, K) for j in layer) == 4 * 5 ** (K - v - 1), f"K={K} v={v}: wrong occupancy"
        assert len(layer) == 8 * 5 ** (K - v - 1), f"K={K} v={v}: wrong layer size"
    assert _occupation(0, K) and not _occupation(N, K), "the two multiples of 5^K are not as stated"
    assert sum(_occupation(j, K) for j in range(e)) == N, "the occupied phases are not one state left over"


# ===========================================================================
# retro89.py — 04-bridges:1751
# ===========================================================================
def _lucas_num(n: int) -> int:
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _Nm1(n: int) -> int:
    return _lucas_num(n) - 1 - (-1) ** n


def _fixed_points(n: int, N: int) -> int:
    g = ((1, 0), (0, 1))
    for _ in range(n):
        g = _mm(g, ((1, 1), (1, 2)), N)
    return sum(
        1
        for x in range(N)
        for y in range(N)
        if ((g[0][0] - 1) * x + g[0][1] * y) % N == 0 and (g[1][0] * x + (g[1][1] - 1) * y) % N == 0
    )


def _local_trace(n: int, p: int, k: int, c: int) -> float:
    """The local trace of U^n at p^k (retro89's ``local_trace``)."""
    N = p**k
    e = _order(((1, 1), (1, 2)), N)
    if p != 5:
        if n % e == 0:
            return float(p)
        return 1.0 if _chi5p(p) == 1 else float(-((-1) ** n))
    if n % 2:
        return 1.0
    m = n // 2
    if m % N == 0:
        return float(N)
    v = 0
    while m % 5 == 0:
        m //= 5
        v += 1
    return 5**v * math.sqrt(5) * _L5(m) * _L5(c)


RETRO89_N = (21, 33, 77, 35, 55, 231, 175)


def test_retro89_the_weil_representation_is_multiplicative() -> None:
    """``04-bridges:1681`` (prop:index-degeneracy) — $W_N$ is normalised to
    be multiplicative: $W_N(g)W_N(h)=W_N(gh)$ at every odd $N$ of the sweep."""
    _claim("04-bridges.tex", r"normalised to be\s*multiplicative", "the normalisation clause")
    rng = random.Random(89)
    for N in RETRO89_N:
        for _ in range(12):
            g, h = _rand_sl2(N, rng), _rand_sl2(N, rng)
            gh = _mm(g, h, N)
            if math.gcd(gh[0][1], N) != 1:
                continue
            assert np.allclose(_wn(g, N) @ _wn(h, N), _wn(gh, N), atol=1e-7), f"N={N}: W is not multiplicative"


@pytest.mark.parametrize("N", RETRO89_N)
def test_retro89_the_glued_trace_is_the_product_of_the_local_traces(N: int) -> None:
    """``04-bridges:1749-1751`` — for odd $N$ the trace of $U_N^n$ is the
    product of the local traces, twisted by the Legendre symbol at the
    ramified prime, for every $n$ below the period $e$."""
    _claim("04-bridges.tex", r"for odd \$N\$, \$W_N=\\bigotimes", "the gluing clause")
    f = _factor_counts(N)
    U = _wn(((1, 1), (1, 2)), N)
    e = _order(((1, 1), (1, 2)), N)
    P = np.eye(N, dtype=complex)
    for n in range(1, e):
        P = P @ U
        pred = math.prod(_local_trace(n, p, k, pow(N // p**k, -1, p**k)) for p, k in f.items())
        assert abs(np.trace(P) - pred) < 1e-6 * max(1, abs(pred)), f"N={N} n={n}: trace != product of locals"


@pytest.mark.parametrize("N", [n for n in RETRO89_N if n <= 80])
def test_retro89_the_squared_trace_counts_the_fixed_points(N: int) -> None:
    r"""``04-bridges:1751`` — $|\tr U_N^n|^2$ is the number of fixed points of
    $M^{2n}$ on $(\Z/N)^2$, for every $n$ below the period (the corpus's
    bound: the fixed points are enumerated, so $N$ stays small)."""
    _claim("04-bridges.tex", r"is the number of fixed points of \$M\^\{2n\}\$", "the fixed-point clause")
    U = _wn(((1, 1), (1, 2)), N)
    e = _order(((1, 1), (1, 2)), N)
    P = np.eye(N, dtype=complex)
    for n in range(1, e):
        P = P @ U
        tr = np.trace(P)
        assert abs(abs(tr) ** 2 - _fixed_points(n, N)) < 1e-6 * N, (
            f"N={N} n={n}: |tr|^2 = {abs(tr) ** 2}, #Fix = {_fixed_points(n, N)}"
        )


def test_retro89_the_glued_spectrum_is_the_convolution_of_the_local_ones() -> None:
    """``04-bridges:1749-1751`` — the spectrum of the glued operator is a
    convolution of the local ones: its multiplicities are non-negative
    integers summing to $N$ (the dimension of the glued space)."""
    _claim("04-bridges.tex", r"the trace of\s*\$U_N\^\{\\,n\}\$ is the product of the local traces",
           "the local traces clause")
    for N in RETRO89_N:
        e = _order(((1, 1), (1, 2)), N)
        z = np.exp(2j * np.pi / e)
        trs = [N]
        P = np.eye(N, dtype=complex)
        U = _wn(((1, 1), (1, 2)), N)
        for n in range(1, e):
            P = P @ U
            trs.append(np.trace(P))
        mult = [round((sum(trs[n] * z ** (-j * n) for n in range(e)) / e).real) for j in range(e)]
        assert all(x >= 0 for x in mult), f"N={N}: a negative multiplicity"
        assert sum(mult) == N, f"N={N}: the multiplicities sum to {sum(mult)}, not {N}"


# ===========================================================================
# retro93.py — 04-bridges:1079
# ===========================================================================
def _fhat_rows(x: np.ndarray, D: float, r) -> np.ndarray:
    return np.exp(1j * r * x) * (2 * np.sin(r * D / 2) / r)


@pytest.mark.slow
def test_retro93_the_index_is_zero_or_two_and_never_one() -> None:
    r"""``04-bridges:1079`` — in the form of $L(s,\chiv)$ with two zeros
    replaced by a quadruple the index is $0$ or $2$ on every window tried,
    never $1$: the two parity subspaces light up together."""
    m = _claim(
        "04-bridges.tex",
        r"the index is \$(\d+)\$ or \$(\d+)\$ on every window tried, never \$(\d+)\$",
        "the counterfactual index",
    )
    zero, two, one = (int(m.group(i)) for i in (1, 2, 3))
    N = 64

    chi = json.loads((PRUEBAS / "chi5_zeros.json").read_text(encoding="utf-8"))
    g1, g2 = chi[0], chi[1]
    ALL = _ideals_upto(10**6)
    rows = []
    for L in (3.0, 5.0, 8.0, 10.0, 12.0, math.log(10**6)):
        B = _build(L, N)
        x, D = B["x"], B["D"]
        W = (
            B["Pole"]
            + (math.log(5) - 2 * math.log(math.pi)) * B["G0"]
            + 2 * B["Psi1"]
            - B["Pform"]([n for n, _ in ALL if n <= math.exp(L) + 1e-9])
        )

        def zer(rs) -> np.ndarray:
            M = sum(np.outer(_fhat_rows(x, D, r), _fhat_rows(x, D, -r)) for r in rs)
            return np.real(M + M.T) / 2

        J = np.eye(N)[::-1]
        Ue = (np.eye(N) + J)[:, : N // 2] / math.sqrt(2)
        Uo = (np.eye(N) - J)[:, : N // 2] / math.sqrt(2)
        for d in (0.45, 0.2, 0.1):
            gq = (g1 + g2) / 2
            Wp = (
                W
                - zer([g1, -g1])
                - zer([g2, -g2])
                + zer([gq + 1j * d, -gq - 1j * d, gq - 1j * d, -gq + 1j * d])
            )
            tol = 1e-6 * D
            ne = int((np.linalg.eigvalsh(Ue.T @ Wp @ Ue) < -tol).sum())
            no = int((np.linalg.eigvalsh(Uo.T @ Wp @ Uo) < -tol).sum())
            rows.append((L, d, ne, no))
    assert all(ne == no for _, _, ne, no in rows), rows
    assert all(ne + no in (zero, two) for _, _, ne, no in rows), rows
    assert all(ne + no != one for _, _, ne, no in rows), rows
    assert any(ne + no == two for _, _, ne, no in rows), "the quadruple is never detected"


# ===========================================================================
# retro94.py — 03-mechanisms:1528
# ===========================================================================
FIBRES = {1: "K", 9: "K", 11: "S", 19: "S", 13: "I1", 17: "I1", 3: "I3", 7: "I3"}


@functools.lru_cache(maxsize=None)
def _clock_mass_fractions(NMAX: int) -> dict[int, dict[str, float]]:
    r"""Accumulated mass per fibre of G at the levels n = 60, 120, ..., NMAX.

    Ports retro94: $Q_n=|N(\Phi_n(\varphi))|$ by Mobius over
    $|N(\varphi^d-1)|=|(-1)^d-L_d+1|$, factored exactly (``flint``), the
    weight $v_p(Q_n)\log p$ assigned to the fibre of $p\bmod20$, the primes
    $2$, $5$ and those dividing $n$ going to ``others``.
    """
    L = [2, 1]
    for _ in range(2, NMAX + 2):
        L.append(L[-1] + L[-2])
    Npow = {d: abs((-1) ** d - L[d] + 1) for d in range(1, NMAX + 1)}
    factored: dict[int, list] = {}

    def factors(value: int) -> dict[int, int]:
        if value not in factored:
            factored[value] = [(int(p), int(e)) for p, e in fmpz(value).factor()] if value > 1 else []
        return dict(factored[value])

    out: dict[int, dict[str, float]] = {}
    acum: dict[str, float] = defaultdict(float)
    for n in range(3, NMAX + 1):
        num = den = 1
        for d in divisors(n):
            mu = mobius(n // d)
            if mu == 1:
                num *= Npow[d]
            elif mu == -1:
                den *= Npow[d]
        assert num % den == 0, f"Q({n}) is not an integer"
        q = num // den
        s = 0.0
        for p, e in factors(q).items():
            w = e * math.log(p)
            s += w
            if p in (2, 5) or n % p == 0:
                f = "others"
            else:
                f = FIBRES[p % 20]
            acum[f] += w
        assert abs(s - math.log(q)) < 1e-6 * max(1, s), f"the weights of level {n} do not add up to log Q_n"
        if n % 60 == 0:
            out[n] = dict(acum)
    return out


@pytest.mark.slow
def test_retro94_clock_mass_fractions_stay_inside_the_stated_ranges() -> None:
    r"""``03-mechanisms:1526-1528`` — at every level $n\le420$ (read at the
    checkpoints $60,120,\ldots,420$) the inert primes carry between $0.066$
    and $0.084$ of the accumulated mass and the kernel between $0.47$ and
    $0.56$, with no stable value."""
    nmax = int(_claim("03-mechanisms.tex", r"on every prime of every level \$n\\leq(\d+)\$", "the level bound").group(1))
    m = _claim(
        "03-mechanisms.tex",
        r"inert primes carry between \$([\d.]+)\$ and\s*\$([\d.]+)\$ of the mass "
        r"and the kernel between \$([\d.]+)\$ and\s*\$([\d.]+)\$",
        "the mass ranges",
    )
    lo_in, hi_in, lo_k, hi_k = (m.group(i) for i in (1, 2, 3, 4))

    fr = _clock_mass_fractions(nmax)
    inert, kernel = [], []
    for n, d in sorted(fr.items()):
        t = sum(d.values())
        inert.append((d.get("I1", 0) + d.get("I3", 0)) / t)
        kernel.append(d.get("K", 0) / t)
    assert min(inert) <= max(inert) and min(kernel) <= max(kernel)
    assert_half_last_digit(min(inert), lo_in, f"03-mechanisms:1528 lower inert mass at n={max(fr)}")
    assert_half_last_digit(max(inert), hi_in, f"03-mechanisms:1528 upper inert mass at n={max(fr)}")
    assert_half_last_digit(min(kernel), lo_k, f"03-mechanisms:1528 lower kernel mass at n={max(fr)}")
    assert_half_last_digit(max(kernel), hi_k, f"03-mechanisms:1528 upper kernel mass at n={max(fr)}")
    assert max(fr) == nmax, f"the sweep stops at n={max(fr)}, the manuscript says {nmax}"
    assert max(inert) - min(inert) > 1e-3 and max(kernel) - min(kernel) > 1e-2, (
        "the fractions have a stable value, the manuscript says they have none"
    )


# ===========================================================================
# retro99.py — 04-bridges:907
# ===========================================================================
def _dh_series() -> tuple[dict, dict, float]:
    I = mp.mpc(0, 1)
    om = {0: 0, 1: 1, 2: I, 4: -1, 3: -I}
    omb = {k: mp.conj(v) for k, v in om.items()}
    kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    return om, omb, kap


def _DH(s, om: dict, omb: dict, kap) -> mp.mpc:
    def L(s, c):
        return mp.dirichlet(s, [c[k] for k in range(5)])

    return (1 - mp.mpc(0, 1) * kap) / 2 * L(s, om) + (1 + mp.mpc(0, 1) * kap) / 2 * L(s, omb)


def test_retro99_the_off_line_zeros_are_where_the_manuscript_places_them() -> None:
    """``04-bridges:906-907`` — the zeros of the Davenport--Heilbronn
    function off the line are at $0.8085+85.699i$ and $0.6508+114.163i$."""
    m = _claim(
        "04-bridges.tex",
        r"its zeros off the line, at \$([\d.]+)\+([\d.]+)i\$ and \$([\d.]+)\+([\d.]+)i\$",
        "the two zeros off the line",
    )
    mp.mp.dps = 30
    om, omb, kap = _dh_series()
    for seed, (re_txt, im_txt) in (
        ((m.group(1), m.group(2)), (0.808, 85.699)),
        ((m.group(3), m.group(4)), (0.651, 114.163)),
    ):
        rho = mp.findroot(lambda s: _DH(s, om, omb, kap), mp.mpc(*seed))
        assert abs(_DH(rho, om, omb, kap)) < 1e-20, f"{rho} is not a zero"
        assert_half_last_digit(float(mp.re(rho)), seed[0], "04-bridges:907 real part")
        assert_half_last_digit(float(mp.im(rho)), seed[1], "04-bridges:907 ordinate")


def test_retro99_the_klein_orbit_of_the_zero_is_free() -> None:
    """``04-bridges:907`` — the zero off the line is a *free* orbit: its four
    Klein images are distinct zeros (no element of the group fixes it)."""
    _claim("04-bridges.tex", r"are free orbits\s*\(\\code\{retro99\.py\}\)", "the free-orbit clause")
    mp.mp.dps = 30
    om, omb, kap = _dh_series()
    rho = mp.findroot(lambda s: _DH(s, om, omb, kap), mp.mpc(0.808, 85.699))
    orb = {"id": rho, "conj": mp.conj(rho), "mate": 1 - mp.conj(rho), "conj.mate": 1 - rho}
    for name, z in orb.items():
        assert abs(_DH(z, om, omb, kap)) < 1e-18, f"the {name} image is not a zero"
    assert len({complex(z) for z in orb.values()}) == 4, "an element of the Klein group fixes the zero"
