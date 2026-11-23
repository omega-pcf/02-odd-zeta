"""Section "Polylogarithmic circuit: F1 to transcendence" (script section 5.9).

The Galois traces of the fifth root of unity, the Gauss sum, the polylog
representation of ``L(s, chi5)``, Baker's reduction at ``s = 1``, the units
of ``(Z/20)*`` (closed under multiplication, destroyed by addition) and the
Fourier projection of ``chi5``.

Tolerances: the script's — 1e-30 where the polylog series is the weaker
side, 1e-44 for the Gauss sum, Baker's ratio and the Fourier projection.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL, L_ONE_CHI5, PHI
from oddzeta.harness import UNITS_MOD_20, assert_close, chi5, l_chi5

# omega_5 = e^{2*pi*i/5}.
_OMEGA_5 = mp.exp(2 * mp.pi * mp.mpc(0, 1) / 5)

# The values of chi5 on 1..20 as the script's Fourier check sampled them.
_FOURIER_SAMPLE = range(1, 21)


def test_fifth_root_galois_traces() -> None:
    """omega_5 + omega_5^4 = (sqrt(5)-1)/2 = 1/phi and
    omega_5^2 + omega_5^3 = -(sqrt(5)+1)/2 = -phi."""
    assert_close(mp.re(_OMEGA_5 + _OMEGA_5**4), (mp.sqrt(5) - 1) / 2, DEFAULT_TOL, "trace at 1 and 4")
    assert_close(mp.re(_OMEGA_5**2 + _OMEGA_5**3), -(mp.sqrt(5) + 1) / 2, DEFAULT_TOL, "trace at 2 and 3")


def test_gauss_sum_equals_sqrt_five() -> None:
    """tau(chi5) = sum chi5(a)*omega_5^a = sqrt(5).

    Script tolerance: 1e-44.
    """
    gauss_sum = sum(chi5(a) * _OMEGA_5**a for a in range(1, 5))
    assert_close(mp.re(gauss_sum), mp.sqrt(5), mp.mpf("1e-44"), "Gauss sum")


def test_polylog_representation_matches_hurwitz() -> None:
    """L(s, chi5) = (1/sqrt(5)) * sum chi5(a)*Li_s(omega_5^a) at s = 3, 5, 7, 9, 11.

    Two independent representations of the same L-value.  Script tolerance:
    1e-30 (the polylog series is the weaker side).
    """
    for s in (3, 5, 7, 9, 11):
        polylog_l = sum(chi5(a) * mp.polylog(s, _OMEGA_5**a) for a in range(1, 5)) / mp.sqrt(5)
        assert_close(mp.re(polylog_l), l_chi5(s), mp.mpf("1e-30"), f"polylog vs Hurwitz at s = {s}")


def test_baker_ratio_equals_phi_squared() -> None:
    """|1-omega_5^2|^2 / |1-omega_5|^2 = phi^2 (Baker's reduction at s = 1).

    Script tolerance: 1e-44.
    """
    ratio = abs(1 - _OMEGA_5**2) ** 2 / abs(1 - _OMEGA_5) ** 2
    assert_close(ratio, PHI**2, mp.mpf("1e-44"), "Baker ratio")


def test_l_one_from_polylog_matches_closed_form() -> None:
    """L(1, chi5) = -(1/sqrt(5)) * sum chi5(a)*log(1-omega_5^a) = 2log(phi)/sqrt(5).

    Script tolerance: 1e-44.
    """
    from_polylog = -sum(chi5(a) * mp.log(1 - _OMEGA_5**a) for a in range(1, 5)) / mp.sqrt(5)
    assert_close(mp.re(from_polylog), L_ONE_CHI5, mp.mpf("1e-44"), "L(1, chi5) from the polylog")


def test_units_are_closed_under_multiplication() -> None:
    """(Z/20)* is closed under multiplication."""
    units = set(UNITS_MOD_20)
    for a in UNITS_MOD_20:
        for b in UNITS_MOD_20:
            assert (a * b) % 20 in units, f"{a}*{b} mod 20 = {(a * b) % 20} leaves the units"


def test_units_are_destroyed_under_addition() -> None:
    """No sum of two units is a unit (a + b not in (Z/20)* for every pair).

    The additive destruction the manuscript reads as decidability (Tarski).
    """
    units = set(UNITS_MOD_20)
    for a in UNITS_MOD_20:
        for b in UNITS_MOD_20:
            assert (a + b) % 20 not in units, f"{a}+{b} mod 20 = {(a + b) % 20} is still a unit"


def test_fourier_projection_identity() -> None:
    """cos(2*pi*n/5) - cos(4*pi*n/5) = (sqrt(5)/2)*chi5(n) for n = 1..20, 5 not dividing n.

    Script tolerance: 1e-44.
    """
    for n in _FOURIER_SAMPLE:
        if n % 5 == 0:
            continue
        lhs = mp.cos(2 * mp.pi * mp.mpf(n) / 5) - mp.cos(4 * mp.pi * mp.mpf(n) / 5)
        rhs = mp.sqrt(5) / 2 * chi5(n)
        assert_close(lhs, rhs, mp.mpf("1e-44"), f"Fourier projection at n = {n}")
