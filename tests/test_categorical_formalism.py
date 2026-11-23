"""Section "Formalism: categorical framework" (script section 5).

Functoriality of the Frobenius lift, the Euler colimit, the co-determination
of the two branches from the same ``G``, the terminality of the spectral
point, the character group and the monoidal product of partial Euler
products.

Merges and drops, with their reason:

* functoriality is asserted once over the union of the script's prime pairs
  (section 5's five pairs keep their 1e-40, the F1-descent block's four
  additional pairs keep its 1e-30 — the tolerances are per pair, never
  loosened);
* the four Dedekind components of section 5 (``zeta_K = zeta * L(s, chi)``
  for Q, Q(sqrt 5), Q(i), Q(sqrt -5)) compared an expression with itself
  and are not ported as they stood: as written each check evaluates
  ``zeta(s)*L(s, chi)`` against the identical expression.  The
  non-trivial instance the manuscript claims, ``zeta_{Q(sqrt 5)} =
  zeta * L(s, chi5)``, is asserted by the Euler-product tests;
* the arithmetic-branch check ``zeta_K(3)/L(3, chi5) = zeta(3)`` used a
  ``zeta_K`` the script had itself defined as ``zeta(3)*L(3, chi5)``, so it
  divided its own product back out; the branch is covered by the
  odd-value and Euler-product tests instead.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL, PHI
from oddzeta.harness import assert_close, chi4, chi4chi5, chi5, euler_partial, kernel_of_g, l_chi5

# Functoriality psi_p o psi_q = psi_{pq}: the union of the script's pairs.
# Section 5 checked the first five at 1e-40; the F1-descent block checked
# its nine at 1e-30; a pair present in both keeps the stricter tolerance.
_FUNCTORIALITY_TOLERANCE = {
    (2, 3): mp.mpf("1e-40"),
    (3, 5): mp.mpf("1e-40"),
    (5, 7): mp.mpf("1e-40"),
    (2, 11): mp.mpf("1e-40"),
    (3, 13): mp.mpf("1e-40"),
    (2, 5): mp.mpf("1e-30"),
    (2, 7): mp.mpf("1e-30"),
    (3, 7): mp.mpf("1e-30"),
    (7, 11): mp.mpf("1e-30"),
}

# The 25 primes of the colimit check (script section 5).
_COLIMIT_PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
)


def test_frobenius_functoriality_adds_exponents() -> None:
    """(phi^p)^q = phi^(p*q) for the nine prime pairs of the script.

    Functoriality of the lift without addition: section 5 states it for
    five pairs at 1e-40, the F1-descent block (Borger criterion 2) for nine
    pairs at 1e-30; both are asserted here pair by pair, each at the
    tolerance of its own site.
    """
    for (p, q), tol in _FUNCTORIALITY_TOLERANCE.items():
        assert_close((PHI**p) ** q, PHI ** (p * q), tol, f"functoriality at ({p}, {q})")


def test_frobenius_identity_at_one() -> None:
    """psi_1 = id: phi^1 = phi."""
    assert_close(PHI**1, PHI, DEFAULT_TOL, "functorial identity")


def test_euler_colimit_converges_at_three() -> None:
    """The partial Euler product over 25 primes approximates zeta_K(3).

    The colimit of section 5: E(S)(3) -> zeta(3)*L(3, chi5) as S grows.
    Script tolerance for the 25-prime product: 1e-3.
    """
    zeta_k_three = mp.zeta(3) * l_chi5(3)
    assert_close(euler_partial(3, _COLIMIT_PRIMES), zeta_k_three, mp.mpf("1e-3"), "Euler colimit at s = 3")


def test_same_g_yields_both_branches() -> None:
    """Co-determination: the kernel of G gives mu_3 = 1/2 and the spectrum
    gives Re(omega^0/2) = 1/2 — the same value from both branches.

    ``|ker G| = 2`` is read from the character table (units 1 and 9), the
    eigenvalue from the cube root of unity.
    """
    mu3_from_g = mp.mpf(1) / len(kernel_of_g())
    eigenvalue_zero = mp.exp(2 * mp.pi * mp.mpc(0, 1) / 3) ** 0 / 2
    assert_close(mp.re(eigenvalue_zero), mu3_from_g, DEFAULT_TOL, "arithmetic vs spectral branch")


def test_terminal_spectral_solution_count() -> None:
    """Exactly one solution of sigma + mu = 2, sigma*mu = 3/4 has mu < 1."""
    roots = [(2 + 1) / 2, (2 - 1) / 2]  # the roots of x^2 - 2x + 3/4
    solutions = [(s, 2 - s) for s in roots if 2 - s < 1]
    assert len(solutions) == 1, f"solutions with mu < 1: {solutions}"


def test_terminal_spectral_solution_value() -> None:
    """The surviving solution is (sigma, mu) = (3/2, 1/2)."""
    roots = [(2 + 1) / 2, (2 - 1) / 2]
    solutions = [(s, 2 - s) for s in roots if 2 - s < 1]
    sigma, mu = solutions[0]
    assert_close(sigma, mp.mpf("3") / 2, DEFAULT_TOL, "terminal sigma")
    assert_close(mu, mp.mpf("1") / 2, DEFAULT_TOL, "terminal mu")


def test_character_group_is_exponent_two() -> None:
    """{1, chi4, chi5, chi4*chi5} is closed and of exponent 2 (Z2 x Z2).

    chi4^2 = 1, chi5^2 = 1, chi4*chi5 = chi4chi5 and (chi4*chi5)^2 = 1 at
    every prime of the script's sample (3, 7, 11, 13, 17, 19).
    """
    sample = (3, 7, 11, 13, 17, 19)
    for p in sample:
        assert chi4(p) ** 2 == 1, f"p = {p}: chi4(p)^2 = {chi4(p) ** 2}"
        assert chi5(p) ** 2 == 1, f"p = {p}: chi5(p)^2 = {chi5(p) ** 2}"
        assert chi4(p) * chi5(p) == chi4chi5(p), f"p = {p}: chi4*chi5 differs from chi4chi5"
        assert chi4chi5(p) ** 2 == 1, f"p = {p}: (chi4chi5)(p)^2 = {chi4chi5(p) ** 2}"


def test_partial_euler_products_multiply() -> None:
    """E(S1)(3)*E(S2)(3) = E(S1 u S2)(3): multiplicativity of the factors.

    Script tolerance: 1e-45.
    """
    for left, right in (((2, 3), (5, 7)), ((2, 3, 5), (7, 11, 13))):
        separate = euler_partial(3, left) * euler_partial(3, right)
        combined = euler_partial(3, left + right)
        assert_close(separate, combined, DEFAULT_TOL, f"E({list(left)})*E({list(right)})")
