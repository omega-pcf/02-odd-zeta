"""Section "Weil analogy: PCF over Z vs Weil over F_q" (script section 5.8).

The Riemann-Hilbert bound read on the PCF spectrum: the real parts of the
eigenvalues stay below ``mu_3``, the moduli are uniform (the squeeze to
``Re = 1/2``), and the character map is a homomorphism on all 64 pairs of
units.  The statements ``|omega^k/2| = 1/2`` and the uniqueness of the
positive real part are the same values the spectral section asserts; the
port owns them there, once, and this module keeps what section 5.8 adds.

The script's "exponent 2 of Z2 x Z2" check of this section was an
arithmetic identity (``(g + g) % 2 = 0`` holds for every integer) and is
not ported: it could not fail and asserts nothing about the group.  The
substantive exponent-2 statement lives in the character-group test of the
categorical module.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL
from oddzeta.harness import UNITS_MOD_20, assert_close, chi4, chi5

_OMEGA = mp.exp(2 * mp.pi * mp.mpc(0, 1) / 3)


def test_eigenvalue_real_parts_bounded_by_mu3() -> None:
    """Re(omega^k/2) <= mu_3 = 1/2 for k = 0, 1, 2 (the Weil upper bound).

    Script tolerance for the slack: 1e-50.
    """
    bound = mp.mpf("1") / 2 + mp.mpf("1e-50")
    for k in range(3):
        real_part = mp.re(_OMEGA**k / 2)
        assert real_part <= bound, f"k = {k}: Re(omega^k/2) = {real_part} exceeds 1/2"


def test_weil_uniformity_of_moduli() -> None:
    """All eigenvalue moduli agree (Weil uniformity): |omega^1/2| = |omega^0/2|."""
    assert_close(abs(_OMEGA**1 / 2), abs(_OMEGA**0 / 2), DEFAULT_TOL, "Weil uniformity")


def test_character_homomorphism_over_units() -> None:
    """chi4(ab) = chi4(a)*chi4(b) and chi5(ab) = chi5(a)*chi5(b) on all 64 pairs."""
    for a in UNITS_MOD_20:
        for b in UNITS_MOD_20:
            product = (a * b) % 20
            assert chi4(product) == chi4(a) * chi4(b), f"chi4 not multiplicative at ({a}, {b})"
            assert chi5(product) == chi5(a) * chi5(b), f"chi5 not multiplicative at ({a}, {b})"
