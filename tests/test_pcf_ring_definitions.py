"""Section "Definitions: the PCF ring and torus" (script sections 2, 2.1, 3.6.1).

The golden ratio as the PCF ring: the defining relation, norm, trace and
powers of ``phi``, the Galois involution, the torus period, the self-dual
minimal polynomial, the field discriminant, and the self-measurement
identity ``z^2 = zy + y^2`` that the dimensional chain of section 3.6.1
derives from ``phi^2 = phi + 1``.

Tolerances: the script's default (``1e-45`` at 50 digits) unless a call
says otherwise.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL, PHI, PHI_BAR, T
from oddzeta.harness import assert_close

# Reference value the script compared T against (its section 2).
_T_REFERENCE = mp.mpf("3.0235430688555739168817063269892086903627584034175")


def test_phi_squared_equals_phi_plus_one() -> None:
    """phi is a root of x^2 - x - 1: the defining PCF relation."""
    assert_close(PHI**2, PHI + 1, DEFAULT_TOL, "defining PCF relation")


def test_phi_unit_norm_negative_one() -> None:
    """Norm of the fundamental unit: phi times its conjugate is -1.

    Witness id cited by ``src/chapters/02-foundations.tex``.
    """
    assert_close(PHI * PHI_BAR, mp.mpf(-1), DEFAULT_TOL, "norm of the fundamental unit")


def test_phi_trace_equals_one() -> None:
    """Tr(phi) = phi + phi_bar = 1."""
    assert_close(PHI + PHI_BAR, mp.mpf(1), DEFAULT_TOL, "trace of phi")


def test_phi_cubed_equals_two_phi_plus_one() -> None:
    """phi^3 = 2*phi + 1 (the ring relation read at degree 3)."""
    assert_close(PHI**3, 2 * PHI + 1, DEFAULT_TOL, "phi^3")


def test_phi_fifth_power_equals_five_phi_plus_three() -> None:
    """phi^5 = 5*phi + 3 (the ring relation read at degree 5)."""
    assert_close(PHI**5, 5 * PHI + 3, DEFAULT_TOL, "phi^5")


def test_galois_involution_is_identity() -> None:
    """-1/(-1/phi) = phi: the Galois involution squared is the identity."""
    assert_close(-1 / (-1 / PHI), PHI, DEFAULT_TOL, "Galois involution")


def test_torus_period_matches_reference_value() -> None:
    """T = 2*pi*log(phi) equals the reference value of the script."""
    assert_close(T, _T_REFERENCE, DEFAULT_TOL, "torus period T")


def test_minimal_polynomial_vanishes_at_conjugate() -> None:
    """p(-1/phi) = 0 for the self-dual minimal polynomial p(x) = x^2 - x - 1."""
    assert_close(PHI_BAR**2 - PHI_BAR - 1, mp.mpf(0), DEFAULT_TOL, "minimal polynomial at the conjugate")


def test_field_discriminant_is_five() -> None:
    """disc(Q(sqrt 5)) = (phi - phi_bar)^2 = 5."""
    assert_close((PHI - PHI_BAR) ** 2, mp.mpf(5), DEFAULT_TOL, "field discriminant")


def test_self_measurement_identity() -> None:
    """z = phi*y implies z^2 = z*y + y^2 for every sampled y (section 3.6.1).

    The geometric content of the golden ratio in E^3: the dimensional chain
    R -> C -> E^3.  The script checked five values of y; all five are kept
    as a single citable test, as the claim is one identity.
    """
    for y in (mp.mpf(1), mp.mpf("0.5"), mp.mpf("3.7"), mp.pi, mp.sqrt(2)):
        z = PHI * y
        assert_close(z**2, z * y + y**2, DEFAULT_TOL, f"self-measurement at y = {mp.nstr(y, 6)}")
