"""Sections "Odd values" and "Discussion: odd zeta values are not free" (script
sections 3.5 odd values and 6).

The odd values are read as ratios ``zeta(2k+1) = zeta_K(2k+1)/L(2k+1, chi5)``
with ``zeta_K`` taken from its Euler product — the non-tautological form of
the R_PCF determination, since the finite Euler product and the analytic
zeta are computed independently — and the even values as rational multiples
of ``pi^{2k}``.

Script tolerance for the ratios: 1e-5 (the truncation of the Euler product
at 500 primes), checked at k = 1..5 by section 3.5 and repeated at k = 1..4
by section 6; the port runs the union once.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL
from oddzeta.harness import assert_close, euler_product_qsqrt5, l_chi5

# The even values as powers of pi (script section 6), beyond the cited one.
_EVEN_ZETA_IDENTITIES = (
    (4, mp.pi**4 / 90),
    (6, mp.pi**6 / 945),
)


def test_zeta_two_pi_squared_over_six() -> None:
    """zeta(2) = pi^2/6: the even value as a rational multiple of pi.

    Witness id cited by ``src/chapters/02-foundations.tex``.
    """
    assert_close(mp.pi**2 / 6, mp.zeta(2), DEFAULT_TOL, "zeta(2)")


def test_even_zeta_values_match_pi_powers() -> None:
    """zeta(4) = pi^4/90 and zeta(6) = pi^6/945."""
    for s, expected in _EVEN_ZETA_IDENTITIES:
        assert_close(expected, mp.zeta(s), DEFAULT_TOL, f"zeta({s})")


def test_odd_zeta_values_from_euler_product() -> None:
    """zeta(2k+1) = E(500)(2k+1)/L(2k+1, chi5) for k = 1..5.

    The determination the manuscript claims: the Euler product of zeta_K
    divided by the character L-value reproduces the odd zeta value.  Script
    tolerance: 1e-5 (stated both as the odd-value check of section 3.5 and
    as the R_PCF determination of section 6, same comparison).
    """
    for k in (1, 2, 3, 4, 5):
        s = 2 * k + 1
        ratio = euler_product_qsqrt5(s, primes_upto=500) / l_chi5(s)
        assert_close(ratio, mp.zeta(s), mp.mpf("1e-5"), f"zeta({s}) from the Euler quotient")
