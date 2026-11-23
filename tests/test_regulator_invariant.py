"""Sections "Applications" and "The unifying invariant R = log(phi)" (script
sections 4 and 4.3, Props A, B, C).

Prop A unifies the three readings of the period through the regulator
``R = log(phi)``; Prop B separates the regulator from the L-value; Prop C is
the pentagon dictating ``chi5``.  The application block also carries the
entropy bridge ``S_BH/k_B = log 2``, the Dedekind eta value at ``tau = i``
(checked against its infinite product), the map ``G`` and the self-duality
of ``chi5``.

Tolerances: the script's own — 1e-48 wherever the Mersenne exponent is
involved, 1e-30 for the eta product, 1e-44/1e-45 for Prop C; default
otherwise.  Duplicates are owned once: ``lambda_log*R = log 2`` was stated
twice (Prop A (iii) and Prop B) with the same tolerance, and the two forms
of the bridge (through ``R`` and through ``(sqrt5/2)*L(1,chi5)``) are two
tests because the script asserted both expressions separately.
"""

from __future__ import annotations

import mpmath as mp
import sympy

from oddzeta.constants import DEFAULT_TOL, LAMBDA_LOG, L_ONE_CHI5, PHI, R_REGULATOR, T
from oddzeta.harness import assert_close, chi4, chi5

# tau_PCF = i and the values the script derived from it (its section 4).
_ETA_I = mp.gamma(mp.mpf(1) / 4) / (2 * mp.pi ** (mp.mpf(3) / 4))


def test_mersenne_bridge_s_bh_is_log_two() -> None:
    """S_BH/k_B = lambda_log*(sqrt(5)/2)*L(1, chi5) = log 2.

    Script tolerance: 1e-48.
    """
    bridge = LAMBDA_LOG * mp.sqrt(5) / 2 * L_ONE_CHI5
    assert_close(bridge, mp.log(2), mp.mpf("1e-48"), "entropy bridge")


def test_eta_i_matches_infinite_product() -> None:
    """|eta(i)| = Gamma(1/4)/(2*pi^(3/4)) equals its infinite product.

    The bridge of the manuscript at ``tau_PCF = i``; the product
    ``exp(-pi/12) * prod (1 - exp(-2*pi*n))`` runs to n = 199 as in the
    script.  Script tolerance: 1e-30.
    """
    eta_product = mp.exp(-mp.pi / 12)
    for n in range(1, 200):
        eta_product *= 1 - mp.exp(-2 * mp.pi * mp.mpf(n))
    assert_close(abs(_ETA_I), eta_product, mp.mpf("1e-30"), "Dedekind eta at tau = i")


def test_character_map_takes_values_in_z2() -> None:
    """G(p mod 20) = (chi4(p), chi5(p)) maps the units onto {-1, +1}^2.

    For every prime 3 <= p < 50 outside {2, 5} both components are defined
    and nonzero, which is what makes the image ``Z2 x Z2``.  (The script's
    membership test could not fail: every value of a Kronecker symbol lies
    in {-1, 0, 1}; the port asserts the non-vanishing on the units, the
    content of the map's codomain.)
    """
    for p in sympy.primerange(3, 50):
        if p in (2, 5):
            continue
        for name, value in (("chi4", chi4(p)), ("chi5", chi5(p))):
            assert value in (-1, 1), f"p = {p}: {name}(p) = {value}, expected +/-1 on the units"


def test_chi5_is_self_dual() -> None:
    """chi5(p)^2 = 1 for every prime 3 <= p < 100 (p != 5): exponent 2."""
    for p in sympy.primerange(3, 100):
        if p == 5:
            continue
        assert chi5(p) ** 2 == 1, f"p = {p}: chi5(p)^2 = {chi5(p) ** 2}"


def test_torus_period_is_two_pi_regulator() -> None:
    """Prop A (i): T = 2*pi*R with R = log(phi)."""
    assert_close(T, 2 * mp.pi * R_REGULATOR, DEFAULT_TOL, "period through the regulator")


def test_l_one_is_two_regulator_over_sqrt_five() -> None:
    """Prop A (ii): L(1, chi5) = 2*R/sqrt(5)."""
    assert_close(L_ONE_CHI5, 2 * R_REGULATOR / mp.sqrt(5), DEFAULT_TOL, "L(1, chi5) through the regulator")


def test_regulator_times_mersenne_exponent_is_log_two() -> None:
    """Prop A (iii) = Prop B: lambda_log*R = log 2 (the regulator reading).

    Stated twice by the script with the same tolerance, 1e-48, and owned
    here once.
    """
    assert_close(LAMBDA_LOG * R_REGULATOR, mp.log(2), mp.mpf("1e-48"), "regulator reading of the bridge")


def test_regulator_form_of_bridge_equals_l_one_form() -> None:
    """Prop B: lambda_log*R = lambda_log*(sqrt(5)/2)*L(1, chi5).

    The regulator and the L-value are related but distinct, and the bridge
    reads through either.  Script tolerance: 1e-48.
    """
    assert_close(
        LAMBDA_LOG * R_REGULATOR,
        LAMBDA_LOG * mp.sqrt(5) / 2 * L_ONE_CHI5,
        mp.mpf("1e-48"),
        "bridge through R vs through L(1, chi5)",
    )


def test_torus_period_consistency_with_l_one() -> None:
    """Consistency of Prop A: T/(2*pi) = R = (sqrt(5)/2)*L(1, chi5)."""
    assert_close(T / (2 * mp.pi), mp.sqrt(5) / 2 * L_ONE_CHI5, DEFAULT_TOL, "consistency of the three readings")


def test_regulator_equals_sqrt_five_halves_l_one() -> None:
    """R = (sqrt(5)/2)*L(1, chi5): the regulator against the L-value."""
    assert_close(R_REGULATOR, mp.sqrt(5) / 2 * L_ONE_CHI5, DEFAULT_TOL, "regulator vs L-value")


def test_pentagon_cosine_determines_chi5() -> None:
    """Prop C: chi5(a) = log|2*cos(a*pi/5)|/log(phi), equivalently
    |2*cos(a*pi/5)| = phi^{chi5(a)}, for a = 1..4.

    The pentagon dictates the character.  Script tolerances: 1e-44 for the
    logarithmic form, 1e-45 for the power form.
    """
    for a in (1, 2, 3, 4):
        cosine = abs(2 * mp.cos(mp.pi * mp.mpf(a) / 5))
        character = mp.mpf(chi5(a))
        assert_close(mp.log(cosine) / mp.log(PHI), character, mp.mpf("1e-44"), f"Prop C logarithmic form at a = {a}")
        assert_close(cosine, PHI ** int(character), mp.mpf("1e-45"), f"Prop C power form at a = {a}")


def test_pentagonal_cosine_log_sum() -> None:
    """Prop C summed: sum chi5(a)*log|2*cos(a*pi/5)| = 4*log(phi).

    Script tolerance: 1e-44.
    """
    cosine_log_sum = sum(chi5(a) * mp.log(abs(2 * mp.cos(mp.pi * mp.mpf(a) / 5))) for a in (1, 2, 3, 4))
    assert_close(cosine_log_sum, 4 * mp.log(PHI), mp.mpf("1e-44"), "Prop C summed over the pentagon")
