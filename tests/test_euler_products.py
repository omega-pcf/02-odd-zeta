"""Sections "Prime decomposition and local Euler factors" and the Dirichlet
factorisation (script sections 3.1 and 3.2).

Both sections compare the same two quantities — the Euler product of
``zeta_K`` over the primes up to 500 and the analytic value
``zeta(s)*L(s, chi5)`` — with the script's per-``s`` tolerances.  The port
owns the comparison once, keeping the STRICTEST tolerance the script used
at each ``s`` (section 3.1 for s = 2..5; section 3.2's 1e-5 for the values
it alone covers).
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.harness import assert_close, euler_product_qsqrt5, l_chi5

# Per-s tolerances inherited from the script: section 3.1 for s = 2..5,
# section 3.2 (its stated 1e-5 for every s it checks) for s = 6, 7, 9, 11.
_TOLERANCE_BY_S = {
    2: mp.mpf("5e-4"),
    3: mp.mpf("5e-7"),
    4: mp.mpf("5e-10"),
    5: mp.mpf("1e-12"),
    6: mp.mpf("1e-5"),
    7: mp.mpf("1e-5"),
    9: mp.mpf("1e-5"),
    11: mp.mpf("1e-5"),
}


def test_euler_product_matches_zeta_times_l() -> None:
    """E(S)(s) over p <= 500 converges to zeta(s)*L(s, chi5) at every s checked.

    The Dirichlet factorisation of the manuscript,
    ``zeta_{Q(sqrt 5)}(s) = zeta(s)*L(s, chi5)``, read from the two sides:
    the finite Euler product against the analytic factorisation, for
    s = 2, 3, 4, 5 (script section 3.1) and s = 6, 7, 9, 11 (section 3.2).
    The truncation error at 500 primes is what the tolerance admits.
    """
    for s, tol in _TOLERANCE_BY_S.items():
        analytic = mp.zeta(s) * l_chi5(s)
        product = euler_product_qsqrt5(s, primes_upto=500)
        assert_close(product, analytic, tol, f"Euler product of zeta_K at s = {s}")
