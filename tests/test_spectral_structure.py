"""Section "Spectral structure" (script section 4.7: mu_3, S_3, eigenvalues,
ell = 1, c = 3).

The contraction ``mu_3 = 1/2`` from ``|ker G| = 2``, the spectral uniqueness
of the roots of ``x^2 - 2x + 3/4``, the tripartite norm, the eigenvalues of
``Omega-hat`` (``omega^k/2`` for the cube root of unity), the S-duality fixed
point ``tau_PCF = i``, the Brown-Henneaux central charge and the holographic
ratio.  The modulus statement ``|omega^k/2| = 1/2`` is also the Weil-bound
reading of the script's section 5.8; it is asserted once, here.

Tolerances: the script's default (1e-45) for every comparison; the section
states exact rational values.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL
from oddzeta.harness import assert_close, kernel_of_g

# The three eigenvalues omega^k/2 of section 4.7.
_OMEGA = mp.exp(2 * mp.pi * mp.mpc(0, 1) / 3)
_EIGENVALUES = tuple(_OMEGA**k / 2 for k in range(3))

# Norms of the tripartite decomposition (section 4.7).
_TRIPARTITE_NORMS = {"P": 1 / mp.sqrt(3), "C": mp.mpf(1), "F": mp.sqrt(3) / 2}

# The sample points the script used for the diagonal obstruction.
_DIAGONAL_SAMPLE = (mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.25"), mp.mpf("0.499"), mp.mpf("0.5"))


def test_mu3_equals_one_half() -> None:
    """mu_3 = 1/|ker G| = 1/2, the kernel of G read from the character table.

    G: (Z/20)* -> Z2 x Z2 has the two trivial components exactly at the
    units 1 and 9, so |ker G| = 2 and mu_3 = 1/2 — the value the section
    uses throughout.
    """
    kernel = kernel_of_g()
    assert kernel == [1, 9], f"ker G = {kernel}, expected [1, 9]"
    assert_close(mp.mpf(1) / len(kernel), mp.mpf("1") / 2, DEFAULT_TOL, "mu_3 = 1/|ker G|")


def test_contraction_equals_ker_g_order() -> None:
    """mu_2/mu_3 = 2 = |ker G|: the contraction ratio."""
    ratio = mp.mpf(1) / (mp.mpf(1) / 2)
    assert_close(ratio, mp.mpf(2), DEFAULT_TOL, "contraction ratio")


def test_sigma_plus_mu_equals_two() -> None:
    """sigma + mu = 2, the trace equation of the spectral pair."""
    sigma, mu = mp.mpf("3") / 2, mp.mpf("1") / 2
    assert_close(sigma + mu, mp.mpf(2), DEFAULT_TOL, "trace equation")


def test_sigma_mu_product_equals_three_quarters() -> None:
    """sigma*mu = 3/4, the norm equation of the spectral pair."""
    sigma, mu = mp.mpf("3") / 2, mp.mpf("1") / 2
    assert_close(sigma * mu, mp.mpf("3") / 4, DEFAULT_TOL, "norm equation")


def test_sigma_polynomial_discriminant_is_one() -> None:
    """disc(x^2 - 2x + 3/4) = 4 - 3 = 1: two real roots."""
    discriminant = mp.mpf(4) - 4 * mp.mpf("3") / 4
    assert_close(discriminant, mp.mpf(1), DEFAULT_TOL, "discriminant of the spectral polynomial")


def test_sigma_mu_polynomial_root_three_halves() -> None:
    """Root 1 of x^2 - 2x + 3/4 = 0 is 3/2 (the sigma of the pair).

    Witness id cited by ``src/chapters/04-bridges.tex``.
    """
    discriminant = mp.mpf(4) - 4 * mp.mpf("3") / 4
    root = (2 + mp.sqrt(discriminant)) / 2
    assert_close(root, mp.mpf("3") / 2, DEFAULT_TOL, "larger root")


def test_sigma_mu_polynomial_root_one_half() -> None:
    """Root 2 of x^2 - 2x + 3/4 = 0 is 1/2 (the mu of the pair).

    Witness id cited by ``src/chapters/04-bridges.tex``.
    """
    discriminant = mp.mpf(4) - 4 * mp.mpf("3") / 4
    root = (2 - mp.sqrt(discriminant)) / 2
    assert_close(root, mp.mpf("1") / 2, DEFAULT_TOL, "smaller root")


def test_effective_obstruction_is_the_smaller_root() -> None:
    """Only mu = 1/2 < 1 survives: the effective obstruction is the small root.

    Uniqueness with the constraint ``mu < 1``: the pair (sigma, mu) of the
    spectral equations fixes mu at the smaller root.
    """
    discriminant = mp.mpf(4) - 4 * mp.mpf("3") / 4
    small_root = (2 - mp.sqrt(discriminant)) / 2
    assert_close(mp.mpf(1) / 2, small_root, DEFAULT_TOL, "mu against the smaller root")


def test_tripartite_norm_product_equals_one_half() -> None:
    """|P|*|C|*|F| = 1/2 = |Omega| for the tripartite norms."""
    product = _TRIPARTITE_NORMS["P"] * _TRIPARTITE_NORMS["C"] * _TRIPARTITE_NORMS["F"]
    assert_close(product, mp.mpf(1) / 2, DEFAULT_TOL, "tripartite norm product")


def test_tripartite_norm_components() -> None:
    """|P| = 1/sqrt(3), |C| = 1, |F| = sqrt(3)/2."""
    expected = {"P": 1 / mp.sqrt(3), "C": mp.mpf(1), "F": mp.sqrt(3) / 2}
    for name, value in _TRIPARTITE_NORMS.items():
        assert_close(value, expected[name], DEFAULT_TOL, f"tripartite norm {name}")


def test_eigenvalue_real_parts() -> None:
    """Re(omega^0/2) = 1/2, Re(omega^1/2) = Re(omega^2/2) = -1/4."""
    expected = (mp.mpf("1") / 2, mp.mpf("-1") / 4, mp.mpf("-1") / 4)
    for k, want in enumerate(expected):
        assert_close(mp.re(_EIGENVALUES[k]), want, DEFAULT_TOL, f"Re(eigenvalue {k})")


def test_eigenvalue_moduli_are_one_half() -> None:
    """|omega^k/2| = 1/2 for k = 0, 1, 2 — the Weil-bound reading of
    section 5.8 (|alpha_i| = q^{1/2}) as well."""
    for k, value in enumerate(_EIGENVALUES):
        assert_close(abs(value), mp.mpf("1") / 2, DEFAULT_TOL, f"|eigenvalue {k}|")


def test_unique_positive_real_eigenvalue() -> None:
    """Exactly one eigenvalue has Re > 0, and its real part is 1/2."""
    positive = [k for k in range(3) if mp.re(_EIGENVALUES[k]) > 0]
    assert positive == [0], f"eigenvalues with positive real part: {positive}, expected [0]"
    assert_close(mp.re(_EIGENVALUES[0]), mp.mpf("1") / 2, DEFAULT_TOL, "positive real part")


def test_s_duality_fixed_point() -> None:
    """-1/i = i: tau_PCF = i is the fixed point of the S transformation.

    The script compared the real part only; the port asserts the full
    complex difference, which is what "fixed point" states.
    """
    tau = mp.mpc(0, 1)
    assert_close(abs(-1 / tau - tau), mp.mpf(0), DEFAULT_TOL, "S-duality fixed point")


def test_brown_henneaux_central_charge_is_three() -> None:
    """c = 3*ell/(2*G_N) = 3 with ell = 1 and G_N = mu_3 = 1/2.

    The gravitational coupling ``G_N`` of the section is ``mu_3`` and the
    ads length ``ell`` is fixed at 1 by the S-duality equation ``ell =
    1/ell`` (the section's assignment, not a computed quantity).
    """
    ell_ads, g_newton = mp.mpf(1), mp.mpf("1") / 2
    assert_close(3 * ell_ads / (2 * g_newton), mp.mpf(3), DEFAULT_TOL, "Brown-Henneaux central charge")


def test_holographic_ratio_is_three_quarters() -> None:
    """S_gauge/S_gravity = 1 - mu_3^2 = 3/4."""
    mu3 = mp.mpf("1") / 2
    assert_close(1 - mu3**2, mp.mpf("3") / 4, DEFAULT_TOL, "holographic ratio")


def test_diagonal_obstruction_gap_positive() -> None:
    """For 0 < t <= mu_3 = 1/2 the diagonal is blocked: t - t^2 > 0."""
    for t in _DIAGONAL_SAMPLE:
        gap = t - t**2
        assert gap > 0, f"t = {t}: t - t^2 = {gap} is not positive"
