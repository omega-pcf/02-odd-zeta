"""Generic helpers shared by the tests of the suite.

Contents
--------
* the characters ``chi5``, ``chi4``, ``chi4chi5`` and ``fib``;
* the Dirichlet L-values the manuscript writes ``L(s, chi)`` (Hurwitz-zeta
  definitions, exact at the working precision);
* the Euler products over ``Q(sqrt 5)`` (and the partial products of the
  colimit check);
* ``assert_close`` — the ONE tolerance assertion of the suite: a comparison
  inherits the script's tolerance and reports the difference on failure;
* ``assert_printed_as_in_manuscript`` and ``assert_half_last_digit`` — the two
  reconciliation margins for a figure read out of the manuscript text (5% of
  the value for a figure marked ``\approx``; half of the last digit printed
  otherwise);
* readers for the repository's committed text artifacts (the manuscript
  sources and the observation outputs under ``hipotesis/pruebas/salidas``).

No helper here asserts or prints: assertions live in the tests, and the
suite's contract is values, not stdout.
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp
import sympy

REPO_ROOT = Path(__file__).resolve().parents[3]

SALIDAS_DIR = REPO_ROOT / "hipotesis" / "pruebas" / "salidas"

# The golden pinning tolerance (the golden test modules define the same
# value locally; the manuscript-figure assert below needs it here too).
GOLDEN_TOL = 1e-12

# The units of (Z/20)*: the domain of the character map G = (chi4, chi5).
UNITS_MOD_20 = (1, 3, 7, 9, 11, 13, 17, 19)

# The manuscript sources a witness tag or a quoted number can sit in:
# main.tex plus every chapter it \input{}s.
TEX_SOURCES = [REPO_ROOT / "main.tex", *sorted((REPO_ROOT / "src" / "chapters").glob("*.tex"))]


def chi5(n: int) -> int:
    """Legendre/Kronecker symbol (5/n): +1 split, -1 inert, 0 ramified."""
    n %= 5
    if n == 0:
        return 0
    return 1 if n in (1, 4) else -1


def chi4(n: int) -> int:
    """Kronecker symbol (-4/n)."""
    n %= 4
    if n == 1:
        return 1
    if n == 3:
        return -1
    return 0


def chi4chi5(n: int) -> int:
    """Product character chi4 * chi5, of conductor 20."""
    return chi4(n) * chi5(n)


def fib(n: int) -> int:
    """n-th Fibonacci number, F_0 = 0, F_1 = 1."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def l_chi5(s) -> mp.mpf:
    """L(s, chi5) via the Hurwitz zeta — exact at the working precision."""
    return (
        mp.hurwitz(s, mp.mpf(1) / 5)
        - mp.hurwitz(s, mp.mpf(2) / 5)
        - mp.hurwitz(s, mp.mpf(3) / 5)
        + mp.hurwitz(s, mp.mpf(4) / 5)
    ) / mp.mpf(5) ** s


def l_chi4(s) -> mp.mpf:
    """L(s, chi4) via the Hurwitz zeta (conductor 4)."""
    return (mp.hurwitz(s, mp.mpf(1) / 4) - mp.hurwitz(s, mp.mpf(3) / 4)) / mp.mpf(4) ** s


def l_chi4chi5(s) -> mp.mpf:
    """L(s, chi4*chi5) via the Hurwitz zeta (conductor 20)."""
    total = mp.mpf(0)
    for a in range(1, 21):
        c = chi4chi5(a)
        if c != 0:
            total += c * mp.hurwitz(s, mp.mpf(a) / 20)
    return total / mp.mpf(20) ** s


def bernoulli_chi5(k: int) -> mp.mpf:
    """Generalised Bernoulli number B_{k, chi5}."""
    return sum(chi5(a) * mp.bernpoly(k, mp.mpf(a) / 5) for a in range(1, 6)) * mp.mpf(5) ** (k - 1)


def kernel_of_g() -> list[int]:
    """Units u with (chi4(u), chi5(u)) = (+1, +1): the kernel of G.

    The manuscript reads |ker G| = 2 from this table, and mu_3 = 1/|ker G|
    follows.
    """
    return [u for u in UNITS_MOD_20 if chi4(u) == 1 and chi5(u) == 1]


def euler_product_qsqrt5(s, primes_upto: int = 500) -> mp.mpf:
    """Euler product of zeta_{Q(sqrt 5)} over the primes p <= primes_upto."""
    prod = mp.mpf(1)
    for p in sympy.primerange(2, primes_upto):
        c = chi5(p)
        if c == 0:  # ramified (p = 5)
            prod *= (1 - mp.mpf(p) ** (-s)) ** (-1)
        elif c == 1:  # split
            prod *= (1 - mp.mpf(p) ** (-s)) ** (-2)
        else:  # inert (including p = 2)
            prod *= (1 - mp.mpf(p) ** (-2 * s)) ** (-1)
    return prod


def euler_partial(s, primes) -> mp.mpf:
    """Partial Euler product of zeta_K over an explicit list of primes."""
    prod = mp.mpf(1)
    for p in primes:
        c = chi5(p)
        if p == 5:  # ramified
            prod *= 1 / (1 - p ** (-s))
        elif c == 1:  # split
            prod *= 1 / (1 - p ** (-s)) ** 2
        else:  # inert
            prod *= 1 / (1 - p ** (-2 * s))
    return prod


def assert_close(computed, expected, tol, note: str = "") -> None:
    """Assert ``|computed - expected| < tol`` and report the difference.

    The single tolerance assertion of the suite (the script's ``check``
    helper, ported): ``tol`` is always the script's value for that check,
    stated literally by the caller, and the failure message carries both
    operands and the gap so a regression is read, not guessed.
    """
    diff = abs(mp.mpf(computed) - mp.mpf(expected))
    assert diff < tol, (
        f"{note or 'value mismatch'}: |{computed} - {expected}| = {diff} "
        f"is not below the tolerance {tol}"
    )


def assert_printed_as_in_manuscript(value: float, printed: str, note: str) -> None:
    """Assert a computed figure matches the figure the manuscript prints.

    The manuscript figures are reconciled at the precision those sentences
    claim: half of its last significant digit (5% of the value, the margin the
    golden tests use for a ``\\pm`` range). The caller passes the figure as the
    manuscript prints it (``"0.520"``, ``"1.1503"``), never a re-typed float.
    """
    expected = float(printed)
    tol = 0.05 * abs(expected) + GOLDEN_TOL
    assert abs(value - expected) <= tol, (
        f"{note}: |{value} - {expected}| = {abs(value - expected)} exceeds "
        f"{tol} (5% of the manuscript figure {printed})"
    )


def assert_half_last_digit(value: float, printed: str, note: str) -> None:
    """Assert a computed figure matches the figure the manuscript prints, at the
    precision the sentence claims: half of the last digit it printed.

    ``printed`` is the figure exactly as it appears in the ``.tex`` — a decimal
    (``"0.520"``) or a scientific literal (``"2e-10"``, the mantissa and
    exponent of ``$2\\cdot10^{-10}$`` joined by the caller). A figure the
    manuscript marks approximate (``$\\approx0.097$``) is reconciled with
    ``assert_printed_as_in_manuscript`` instead: there the last digit is not a
    claim and the suite allows 5% of the value.
    """
    mantissa, _, exponent = printed.partition("e")
    decimals = len(mantissa.split(".")[1]) if "." in mantissa else 0
    tol = 0.5 * 10.0 ** (int(exponent or 0) - decimals) + GOLDEN_TOL
    assert abs(value - float(printed)) <= tol, (
        f"{note}: |{value} - {float(printed)}| = {abs(value - float(printed))} exceeds "
        f"{tol} (half the last digit of the manuscript figure {printed})"
    )


def read_salidas(name: str) -> str:
    """Text of a committed observation output, e.g. ``castelnuovo.txt``."""
    path = SALIDAS_DIR / name
    return path.read_text(encoding="utf-8")


def read_tex(name: str) -> str:
    """Text of a manuscript source (chapter file name, e.g. ``04-bridges.tex``)."""
    for path in TEX_SOURCES:
        if path.name == name:
            return path.read_text(encoding="utf-8")
    raise AssertionError(f"no manuscript source named {name}; looked in {[p.name for p in TEX_SOURCES]}")
