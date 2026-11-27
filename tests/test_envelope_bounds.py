"""`envelope.py` and `zeroside_check.py` behind the envelope statements.

Sites covered (statement line numbers as measured — snapshots, the convention
of `docs/numerical-port.md`):

* ``appendix:96`` — the table row "Envelope and fluctuation & Num &
  \\code{envelope.py}, \\code{tstar.py} & $\\gamma_n=E^{-1}(n-S(\\gamma_n))$,
  40 zeros." — the envelope of $L(s,\\chiv)$ evaluated at $n-S(\\gamma_n)$
  returns the $n$-th zero, over the 40 zeros the row declares.
* ``04-bridges:599-600`` — "the floor for $\\chiv$ is far larger at the same
  window ($\\lambda_{\\min}\\approx0.097$ at $L=1$, stable under basis
  refinement and confirmed from the zero side, \\code{weil\\_window\\_chi5.py},
  \\code{zeroside\\_check.py})" — the zero side of the Weil form reproduces the
  floor of the $L=1$ window.
* ``appendix:578`` — the sentence that names ``zeroside_check.py`` as "the
  minimum of the $L=1$ window".

Neither script is imported by another script and neither writes a committed
``salidas/*.txt``, so each test owns its computation. Both read the committed
input cache ``hipotesis/pruebas/zeros.txt`` — the 40 zeros of $L(s,\\chi_5)$
below $T=80$, byte-identical to ``chi5_zeros_T80.txt`` and committed in
``7b0c68f`` — which is the input both scripts declare.

Conditions declared by the corpus:

* ``envelope.py`` runs at ``mp.dps = 25`` (its own second line) and calibrates
  the offset so that $S$ has mean zero. The identity is exact, so the assertion
  is on the residual of the inversion: observed $1.3\\cdot10^{-24}$ at that
  precision, asserted below the declared $10^{-20}$. The script prints
  residuals for 7 of the 40 zeros; the test asserts all 40.
* ``zeroside_check.py`` evaluates the Weil form on both signs of the 40 zeros
  (tail omitted) for bases $J = 20, 40, 80$. With $J \\ge 40$ the truncated
  form has a null direction — the printed rows are $-2.1\\cdot10^{-17}$
  ($J=40$) and $-6.1\\cdot10^{-16}$ ($J=80$), i.e. zero — so the row that
  confirms the manuscript's figure is the $J = 20$ one.
"""

from __future__ import annotations

import re

import mpmath as mp
import numpy as np

from oddzeta.harness import REPO_ROOT, assert_printed_as_in_manuscript, read_tex

#: The committed cache both scripts read (40 zeros of L(s, chi_5), T < 80).
ZEROS_CACHE = REPO_ROOT / "hipotesis" / "pruebas" / "zeros.txt"


def _claim(chapter: str, pattern: str, note: str) -> re.Match[str]:
    """The manuscript text behind a claim (fails loudly if it is gone)."""
    m = re.search(pattern, read_tex(chapter))
    assert m is not None, f"{note} is no longer in {chapter}"
    return m


def _zero_tokens() -> list[str]:
    return ZEROS_CACHE.read_text().split()


def _inversion_residual(tokens: list[str]) -> mp.mpf:
    """max_n |Tsm(n - S(gamma_n)) - gamma_n| at envelope.py's own precision.

    ``Tsm`` is the inverse of ``Nsm(t) + c`` with the constant ``c`` calibrated
    so that ``S`` has mean zero, exactly as ``envelope.py`` does it — so the
    residual measures the round trip ``gamma_n -> n - S_n -> gamma_n``.
    """
    zeros = [mp.mpf(t) for t in tokens]
    with mp.workdps(25):  # envelope.py: mp.mp.dps=25
        th5 = lambda t: mp.im(mp.loggamma(mp.mpf(1) / 4 + 0.5j * t)) - (t / 2) * mp.log(mp.pi / 5)
        Nsm = lambda t: th5(t) / mp.pi + mp.mpf(1) / 2
        vals = [n + 1 - Nsm(g) for n, g in enumerate(zeros)]
        c = sum(vals) / len(vals)
        S = [v - c for v in vals]
        Tsm = lambda x: mp.findroot(
            lambda t: Nsm(t) + c - x,
            10.0 if x < 3 else float(2 * mp.pi * x / mp.log(5 * x)),
        )
        return max(abs(Tsm(i + 1 - s) - g) for i, (g, s) in enumerate(zip(zeros, S)))


def _zero_side_floor(L: float, J: int) -> float:
    """lambda_min of the Weil form over both signs of the committed zeros.

    The ``phihat`` of `weil_certificates/opcert.py` (the sine basis orthonormal
    on an interval of length ``L``, modes ``j = 1..J``), evaluated on
    ``[+gamma, -gamma]`` — the computation of ``zeroside_check.py``.
    """
    z = np.array([float(t) for t in _zero_tokens()])
    g = np.concatenate([z, -z])
    j = np.arange(1, J + 1)
    k = j * np.pi / L
    rr = g[:, None]
    den = k[None, :] ** 2 - rr ** 2
    den = np.where(np.abs(den) < 1e-12, 1e-12, den)
    I = k[None, :] * (1 - ((-1.0) ** j)[None, :] * np.exp(1j * rr * L)) / den
    F = np.sqrt(2 / L) * np.exp(-1j * rr * L / 2) * I
    M = np.real(F.conj().T @ F)
    return float(np.linalg.eigvalsh(M)[0])


def test_envelope_inverts_the_forty_declared_zeros() -> None:
    r"""``appendix:96`` — $\gamma_n=E^{-1}(n-S(\gamma_n))$ over the 40 zeros."""
    declared = int(
        _claim(
            "appendix.tex",
            r"\\gamma_n=E\^\{-1\}\(n-S\(\\gamma_n\)\)\$, (\d+) zeros",
            "the envelope row of the appendix",
        ).group(1)
    )
    below = int(
        _claim(
            "04-bridges.tex",
            r"zeros of \$L\(s,\\chiv\)\$ below \$(\d+)\$",
            "the 40-zero input declaration",
        ).group(1)
    )
    tokens = _zero_tokens()
    assert len(tokens) == declared, (
        f"zeros.txt holds {len(tokens)} zeros, the appendix row declares {declared}"
    )
    assert max(float(t) for t in tokens) < below, f"a zero sits above T={below}"

    residual = _inversion_residual(tokens)
    assert residual < mp.mpf("1e-20"), (
        f"the envelope inverse misses the {declared} zeros by {mp.nstr(residual, 3)} "
        "at mp.dps=25 (1.3e-24 when this test was written)"
    )


def test_zero_side_reproduces_the_l_one_floor() -> None:
    r"""``04-bridges:599-600`` — the zero side confirms $\lambda_{\min}\approx0.097$."""
    figure = _claim(
        "04-bridges.tex",
        r"\\lambda_\{\\min\}\\approx([\d.]+)\$ at\s+\$L=1\$",
        "the L=1 floor of the window paragraph",
    ).group(1)
    floor = _zero_side_floor(L=1.0, J=20)
    # The figure is marked approximate (the archimedean floor is 0.09718,
    # weil_window_chi5.py); the zero side computes 0.09799 — they agree to
    # 1.0%, inside the 5% the suite allows for an "$\\approx$" figure.
    assert_printed_as_in_manuscript(
        floor, figure, "04-bridges:599 zero-side floor at L=1, J=20"
    )
