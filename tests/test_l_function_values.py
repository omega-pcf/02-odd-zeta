"""Sections "Fundamental formula", "Even zeta values" and "The pentagonal
source" (script sections 3.3, 3.4, 3.5).

``L(1, chi5)`` through its three derivations (digamma/class-number,
Gauss-Lerch, the torus period), the Bernoulli formula for the even values
``L(2k, chi5)``, and the pentagon: the four cosine identities, the Gauss
logarithmic sum, the digamma character sum and the Hurwitz representation.

Tolerances: the script's own at each check — 1e-14 where the digamma
reflection is the weaker side, 1e-44 for the Bernoulli and Hurwitz
comparisons, 1e-49/1e-50 for the logarithmic sums; default otherwise.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL, L_ONE_CHI5, PHI, T
from oddzeta.harness import assert_close, bernoulli_chi5, chi5, l_chi5

# Reference rational values of the generalised Bernoulli numbers B_{k, chi5}
# (script section 3.4).
_BERNOULLI_RATIONALS = {2: mp.mpf(4) / 5, 4: mp.mpf(-8), 6: mp.mpf(804) / 5, 8: mp.mpf(-5776)}

# The pentagonal cosine values the script asserted (section 3.5).
_COSINE_IDENTITIES = (
    (2, "1/phi", 1 / PHI),
    (3, "-1/phi", -1 / PHI),
    (4, "-phi", -PHI),
)


def test_l_one_chi5_digamma_value() -> None:
    """L(1, chi5) = 2*log(phi)/sqrt(5) through the digamma (class-number) formula.

    Witness id cited by ``src/chapters/03-mechanisms.tex``.  Script
    tolerance for this check: 1e-14 (the digamma reflection is the weaker
    of the two sides).
    """
    digamma_l_one = -(mp.mpf(1) / 5) * sum(chi5(a) * mp.digamma(mp.mpf(a) / 5) for a in (1, 2, 3, 4))
    assert_close(L_ONE_CHI5, digamma_l_one, mp.mpf("1e-14"), "class-number formula at s = 1")


def test_l_one_matches_t_over_pi_sqrt_five() -> None:
    """T/(pi*sqrt(5)) = 2*log(phi)/sqrt(5): the period bridge at s = 1."""
    assert_close(T / (mp.pi * mp.sqrt(5)), L_ONE_CHI5, DEFAULT_TOL, "period bridge")


def test_even_l_values_match_bernoulli_formula() -> None:
    """L(2k, chi5) through the generalised Bernoulli formula, k = 1..4.

    The closed form (-1)^(k+1)*sqrt(5)*(2*pi)^(2k)*B_{2k,chi5} /
    (2*(2k)!*5^(2k)) against the Hurwitz-zeta value.  Script tolerance:
    1e-44.
    """
    for k in (1, 2, 3, 4):
        b = bernoulli_chi5(2 * k)
        formula = (
            (-1) ** (k + 1)
            * mp.sqrt(5)
            * (2 * mp.pi) ** (2 * k)
            * b
            / (2 * mp.factorial(2 * k) * mp.mpf(5) ** (2 * k))
        )
        assert_close(formula, l_chi5(2 * k), mp.mpf("1e-44"), f"Bernoulli formula at 2k = {2 * k}")


def test_generalized_bernoulli_numbers_equal_rationals() -> None:
    """B_{2k, chi5} equals the reference rationals for 2k = 2, 4, 6, 8.

    Script tolerance: 1e-44.
    """
    for k, expected in _BERNOULLI_RATIONALS.items():
        assert_close(bernoulli_chi5(k), expected, mp.mpf("1e-44"), f"B_{{{k}, chi5}}")


def test_two_cos_pi_over_five_equals_phi() -> None:
    """Twice the cosine of pi/5 equals phi: the pentagon identity the manuscript cites.

    Witness id cited by ``src/chapters/03-mechanisms.tex``.
    """
    assert_close(2 * mp.cos(mp.pi / 5), PHI, DEFAULT_TOL, "pentagon identity")


def test_two_cos_multiples_of_pi_over_five() -> None:
    """2*cos(2*pi/5) = 1/phi, 2*cos(3*pi/5) = -1/phi, 2*cos(4*pi/5) = -phi."""
    for multiple, _name, expected in _COSINE_IDENTITIES:
        assert_close(
            2 * mp.cos(multiple * mp.pi / 5), expected, DEFAULT_TOL, f"pentagon identity at {multiple}*pi/5"
        )


def test_gauss_logarithmic_sum_equals_minus_two_log_phi() -> None:
    """sum chi5(a)*log(2*sin(pi*a/5)) = -2*log(phi) (Gauss' formula).

    Script tolerance: 1e-50.
    """
    gauss_log = sum(chi5(a) * mp.log(2 * mp.sin(mp.pi * mp.mpf(a) / 5)) for a in (1, 2, 3, 4))
    assert_close(gauss_log, -2 * mp.log(PHI), mp.mpf("1e-50"), "Gauss logarithmic sum")


def test_gauss_lerch_reproduces_l_one() -> None:
    """L(1, chi5) = -(sqrt(5)/5)*gauss_log = 2*log(phi)/sqrt(5)."""
    gauss_log = sum(chi5(a) * mp.log(2 * mp.sin(mp.pi * mp.mpf(a) / 5)) for a in (1, 2, 3, 4))
    assert_close(-(mp.sqrt(5) / 5) * gauss_log, L_ONE_CHI5, DEFAULT_TOL, "Gauss-Lerch derivation")


def test_digamma_character_sum_equals_two_sqrt_five_log_phi() -> None:
    """sum chi5(a)*psi(a/5) = -2*sqrt(5)*log(phi).

    The intermediate sum of the class-number derivation (the cited test
    above is the ratio it yields).  Script tolerance: 1e-49.
    """
    digamma_sum = sum(chi5(a) * mp.digamma(mp.mpf(a) / 5) for a in (1, 2, 3, 4))
    assert_close(digamma_sum, -2 * mp.sqrt(5) * mp.log(PHI), mp.mpf("1e-49"), "digamma character sum")


def test_hurwitz_definition_matches_character_sum() -> None:
    """L(s, chi5) as the explicit Hurwitz difference equals the character sum.

    The script's identity check at s = 3, 5, 7, 9 (its section 3.5): the
    character signs (+1, -1, -1, +1) reproduce the four-term difference the
    harness defines.  Script tolerance: 1e-44.
    """
    for k in (1, 2, 3, 4):
        s = 2 * k + 1
        direct = sum(chi5(a) * mp.hurwitz(s, mp.mpf(a) / 5) for a in (1, 2, 3, 4)) / mp.mpf(5) ** s
        assert_close(l_chi5(s), direct, mp.mpf("1e-44"), f"Hurwitz form of L(s, chi5) at s = {s}")
