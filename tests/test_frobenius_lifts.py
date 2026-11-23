"""Section "Frobenius lifts and splitting criterion" (script section 2.2).

The lift ``psi_p(phi) = F_p*phi + F_{p-1} = phi^p`` at the first primes, the
Kronecker symbol ``chi5`` as the splitting type in Z[phi], and the Fibonacci
splitting criterion ``chi5(p) = F_p mod p``.

The criterion appears three times in the script — as section 2.2's sweep over
``p < 60``, as the Lambda-ring congruence of the categorical section, and as
Borger criterion 3 of the F1-descent block (an explicit prime list).  One
test now covers all three sites: its range ``[3, 60)`` contains both
explicit lists and asserts the same congruence the script asserted there.
"""

from __future__ import annotations

import sympy

from oddzeta.constants import DEFAULT_TOL, PHI
from oddzeta.harness import assert_close, chi5, fib

# Splitting types of the first eleven primes, chi5 in {+1 split, -1 inert, 0 ramified}.
_CHI5_BY_PRIME = {2: -1, 3: -1, 5: 0, 7: -1, 11: 1, 13: -1, 17: -1, 19: 1, 23: -1, 29: 1, 31: 1}
_SPLITTING_LABEL = {1: "split", -1: "inert", 0: "ramified"}

_SPLIT_PRIMES = (11, 19, 29)  # F_{p-1} = 0 mod p
_INERT_PRIMES = (3, 7, 13)  # F_{p+1} = 0 mod p


def test_frobenius_lift_reproduces_phi_power() -> None:
    """psi_p(phi) = F_p*phi + F_{p-1} = phi^p for the first nine primes.

    The lift is purely multiplicative: the Fibonacci pair evaluated at phi
    reproduces the p-th power.
    """
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        assert_close(fib(p) * PHI + fib(p - 1), PHI**p, DEFAULT_TOL, f"Frobenius lift at p = {p}")


def test_chi5_matches_the_prime_decomposition() -> None:
    """chi5(p) gives the splitting type of p in Z[phi]: only 5 ramifies.

    disc = 5, so p = 5 is the unique ramified prime and chi5(p) = +1/-1
    selects split/inert.
    """
    for p, expected in _CHI5_BY_PRIME.items():
        got = chi5(p)
        assert got == expected, (
            f"p = {p}: chi5 = {got:+d}, expected {expected:+d} ({_SPLITTING_LABEL[expected]})"
        )


def test_fibonacci_congruence_matches_chi5() -> None:
    """chi5(p) = F_p mod p for every prime 3 <= p < 60 (p != 5).

    The Fibonacci splitting criterion, which the manuscript also reads as
    the Lambda-ring congruence F_p = phi^p mod p and as Borger criterion 3
    of the F1-descent data.
    """
    for p in sympy.primerange(3, 60):
        if p == 5:
            continue
        assert fib(p) % p == chi5(p) % p, (
            f"p = {p}: F_p mod p = {fib(p) % p}, chi5(p) mod p = {chi5(p) % p}"
        )


def test_split_primes_have_f_p_minus_one_congruent_zero() -> None:
    """F_{p-1} = 0 mod p at the split primes 11, 19, 29."""
    for p in _SPLIT_PRIMES:
        assert fib(p - 1) % p == 0, f"p = {p} split but F_(p-1) mod p = {fib(p - 1) % p}"


def test_inert_primes_have_f_p_plus_one_congruent_zero() -> None:
    """F_{p+1} = 0 mod p at the inert primes 3, 7, 13."""
    for p in _INERT_PRIMES:
        assert fib(p + 1) % p == 0, f"p = {p} inert but F_(p+1) mod p = {fib(p + 1) % p}"
