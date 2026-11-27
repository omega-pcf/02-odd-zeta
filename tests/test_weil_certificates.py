"""The ``weil_certificates`` family behind the window theorems of section 6.

Sites covered (statement line numbers as measured — snapshots, the convention
of ``docs/numerical-port.md``):

* ``04-bridges:493`` — thm:second-window: $Q(f)\\ge0.0445\\,\\|f\\|^2$,
  computed in interval arithmetic from the certificate
  ``weil_certificates/cert_L1.0.json``, replay ``verify_iv.py``.
* ``04-bridges:506-511`` — the certificate: a linear programme gives $41$
  rational pairs with $\\lambda_i\\in[1,16]$ and Lipschitz constant
  $M_T=11.0$ (the committed artefact ``cert_L1.0.json``, written by the
  orphan ``verify_cert.py`` from ``cert.py``'s optimum).
* ``04-bridges:514-517`` — the interval bound: $M=67.92$, grid
  $h=\\tfrac1{100}$ over $[0,600]$, minimum $\\ge0.04458$, tail
  $\\ge0.04999$; the earlier double-precision replay (``verify_rig.py``)
  gave $0.0431$.
* ``04-bridges:521-524`` — thm:third-window: $Q\\ge0.0027$ at $L\\le1.3$,
  margins $0.0077$ ($L\\le1.2$) and $0.0261$ ($L\\le1.1$), computed with
  validated numerics (``op_rig_validated.py``).
* ``04-bridges:541-543`` — the validated computation at $L=1.3$: $t=2$,
  $J=800$, $h=2.5\\cdot10^{-4}$, $\\lambda_J\\le1.993719$,
  $\\eta_J=3.45\\cdot10^{-3}$, quadrature errors below $2.5\\cdot10^{-5}$,
  margin $0.00277$, $R=88$, Cholesky bound below $1.5\\cdot10^{-10}$;
  margins $0.0077$ and $0.0261$ at $L=1.2$ and $1.1$.
* ``04-bridges:547-555`` — rmk:rigour: partial sums bound $W$ from below
  (``rigW.py``), $\\psi(\\tfrac14)=-\\gamma_E-\\frac\\pi2-3\\log2$, an
  explicit margin of $10^{-9}$ per evaluated quantity, the grid stays at
  least $2.8\\cdot10^{-6}$ from every $k_j$, ``verify_iv.py`` gives $0.0445$,
  and the validated margins $0.0261$, $0.0077$, $0.0027$ at $L=1.1,1.2,1.3$.
* ``04-bridges:569-577`` — the sign of the Frobenius at 2: $a_2=+0.980$,
  the replaced-sign optimum $-0.573$ (``cert.py``), and the certificate
  reaching $L=1.08$ with margin $0.013$ (``cert.py``).
* ``appendix:41-42, 577-578`` — the census rows naming ``verify_iv.py``,
  ``op_rig_validated.py``, ``cert.py``, ``rigW.py``, ``opcert_rig.py``.
* ``04-bridges:379-381`` — the normalisation of the explicit formula: the
  $40$ zeros of height $\\le80$ (first $\\gamma=6.6484533447$) and Gaussian
  $g$ make both sides agree to $10^{-18}$ (``verify_weil_chi5.py``).
* ``04-bridges:426-433`` with ``appendix:93`` — prop:semilocal: the
  archimedean threshold $L_c=0.9251$, the floor $0.097$ at $L=1$,
  $5.3\\cdot10^{-3}$ at $1.4$, $\\sim10^{-6}$ at $2$, and the counterfactual
  $\\chi_5(2)=+1$ failing from $L\\approx0.9$ (``weil_window_chi5.py``).
* ``04-bridges:439-454`` with ``appendix:575`` — thm:first-window: the
  constants $\\kappa=-3.76274\\ldots$, $L^*=0.744725\\ldots$, the margin
  $m=0.0841$ at $L=\\log2$, the integral identity behind $\\kappa$ and
  $\\psi(\\tfrac12)=-\\gamma_E-2\\log2$ (``weil_window_rigorous_check.py``).

Conditions declared by the corpus:

* ``cert.py``'s LP runs at the script's own parameters (``lam_max=16``,
  ``m=200``, ``R=600``, the 12000+6000-point grid, ``method="highs"``);
  the flip test uses the script's own replacement set
  $n\\in\\{2,8,32,128\\}$ at $L=1$ (only $n=2$ enters the ansatz there).
* ``rigW.py``'s bounds are evaluated at the six radii its ``__main__``
  checks ($0,1,5,20,100,600$), $K=4000+60y$ terms, the explicit margin
  $10^{-9}$ subtracted.
* ``verify_rig.py`` replays the certificate on its coarse $W$ grid at
  $h=2\\cdot10^{-4}$ over $[0,600]$ with $\\mathtt{SAFE\\_T}=10^{-9}$ (the
  script's own constants).
* ``verify_iv.py`` replays in ball arithmetic (python-flint, precision 128 —
  the script uses ``mpmath.iv`` at ``dps=30``; both round outward, and the
  ball run reproduces the committed output's 13 digits) over $h=\\tfrac1{100}$
  on $[0,600]$ with $K=60$ terms and the $K=6000$ tail of the committed run.
* ``op_rig_validated.py`` runs at the three configurations of its committed
  output ``op_rig_validated_output.json`` ($t=2$; the $L=1.3$ line matches
  the parameters printed at 04-bridges:541, asserted there).
* ``opcert_rig.py`` runs at the two configurations of its ``__main__``
  ($t=2$, $J=400$, $h=5\\cdot10^{-4}$ at $L=1.1$ and $1.2$); its rigorous
  primal subtracts ``rigW``'s coarse $W$ bound and an explicit $10^{-9}J$
  float margin, so it certifies a slightly weaker margin than the validated
  replay of the theorem it backs.

Reconciliation of a figure read out of the manuscript: certified lower
bounds are printed truncated (``assert_lower_bound_figure``), upper bounds
printed rounded up (``assert_upper_bound_figure``), a second computation of
one figure agrees to one unit of its last digit
(``assert_within_last_digit``), and plain values use half of the last
printed digit (``assert_half_last_digit``). Every figure in this module is
parsed from the ``.tex`` — never typed.

No test imports a script: the LP, the $W$ bounds, the replays and the
operator runs are owned by this module (the P1/P2 pattern).
"""

from __future__ import annotations

import functools
import json
import re
from fractions import Fraction

import mpmath as mp
import numpy as np
import pytest
from flint import arb, ctx
from scipy.optimize import linprog
from scipy.special import digamma as scipy_digamma

from oddzeta.harness import (
    REPO_ROOT,
    assert_close,
    assert_half_last_digit,
    assert_lower_bound_figure,
    assert_upper_bound_figure,
    assert_within_last_digit,
    chi5,
    read_tex,
)

FAMILY_DIR = REPO_ROOT / "tests" / "fixtures" / "weil_certificates"
CERT_PATH = FAMILY_DIR / "cert_L1.0.json"
OP_RIG_OUTPUT = FAMILY_DIR / "op_rig_validated_output.json"
VERIFY_IV_OUTPUT = FAMILY_DIR / "verify_iv_L1.0_output.txt"


def _claim(chapter: str, pattern: str, note: str) -> tuple[str, ...]:
    """The figure printed at a manuscript site — parsed, never typed."""
    m = re.search(pattern, read_tex(chapter))
    assert m is not None, f"the manuscript does not print {note} ({chapter}: {pattern})"
    return m.groups()


def _sci(mantissa: str, exponent: str) -> float:
    """A ``$2.5\\cdot10^{-4}$`` figure, parsed as mantissa and exponent."""
    return float(mantissa) * 10.0 ** int(exponent)


def _safe_margin() -> float:
    """The explicit per-evaluation margin rmk:rigour declares (04-bridges:554)."""
    (exponent,) = _claim(
        "04-bridges.tex",
        r"margin of \$10\^\{(-?\d+)\}\$",
        "the explicit margin of rmk:rigour (04-bridges:554)",
    )
    return 10.0 ** int(exponent)


@functools.lru_cache(maxsize=1)
def _c0() -> float:
    """$W(0) = \\log(5/\\pi) + \\psi(1/4)$ with Gauss's closed form (04-bridges:551)."""
    with mp.workdps(40):
        return float(mp.log(5 / mp.pi) + (-mp.euler - mp.pi / 2 - 3 * mp.log(2)))


def _w_lower_adaptive(r, safe: float) -> np.ndarray:
    """``rigW.py``'s W_lower: C0 + the partial sums to K = 4000+60y terms, minus the margin.

    The script's own per-point loop: the term count grows with y, so a
    point at r=600 sums 22000 terms while one at r=0 sums 4000.
    """
    r = np.atleast_1d(np.asarray(r, dtype=float))
    y = r / 2
    out = np.empty_like(r)
    c0 = _c0()
    for i, yy in enumerate(y):
        K = int(4000 + 60 * yy)
        k = np.arange(K, dtype=float) + 0.25
        out[i] = c0 + np.sum(yy * yy / (k * (k * k + yy * yy)))
    return out - safe


def _w_lower_k400(r, safe: float) -> np.ndarray:
    """``op_rig_validated.py``'s own W: K=400 partial sums plus the integral tail."""
    r = np.atleast_1d(np.asarray(r, dtype=float))
    y = r / 2
    u = np.arange(400) + 0.25
    s = _c0() + np.sum((y[:, None] ** 2) / (u[None, :] * (u[None, :] ** 2 + y[:, None] ** 2)), axis=1)
    return s + 0.5 * np.log1p(y * y / (400 + 0.25) ** 2) - safe


def _w_exact(r: float) -> float:
    """$W(r) = \\log(5/\\pi) + \\mathrm{Re}\\,\\psi(1/4 + ir/2)$ at dps=40."""
    with mp.workdps(40):
        return float(mp.log(5 / mp.pi) + mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, r / 2))))


def _certificate() -> dict:
    return json.loads(CERT_PATH.read_text(encoding="utf-8"))


def _lp_prime_powers() -> dict[int, float]:
    """``lp.py``'s A: $a_n = -2\\log p\\,\\chi_5(n)/\\sqrt n$ over the prime
    powers $n<400$ with $\\chi_5(n)\\ne0$ (the arithmetic rewritten here,
    not imported)."""
    A: dict[int, float] = {}
    for n in range(2, 400):
        p = 2
        while p * p <= n and n % p:
            p += 1
        if p * p > n:
            p = n
        m = n
        while m % p == 0:
            m //= p
        if m == 1 and chi5(n) != 0:
            A[n] = -2.0 * np.log(p) * chi5(n) / np.sqrt(n)
    return A


def _W_lp(r) -> np.ndarray:
    """The LP's bound on W: $\\log(5/\\pi) + \\mathrm{Re}\\,\\psi(1/4+ir/2)$ (lp.py)."""
    return np.log(5.0 / np.pi) + np.real(scipy_digamma(0.25 + 0.5j * np.asarray(r, dtype=complex)))


def _lp_margin(L: float, A: dict[int, float], lam_max: float = 16.0, m: int = 200, R: float = 600.0) -> float:
    """``cert.py``'s LP: the best margin t over the certificate ansatz."""
    act = {n: a for n, a in A.items() if np.log(n) < L}

    def PL(r):
        return sum(a * np.cos(r * np.log(n)) for n, a in act.items())

    sumPL = sum(abs(a) for a in act.values())
    lams = np.linspace(L, lam_max, m)
    r = np.concatenate([np.linspace(0, 60, 12000), np.linspace(60, R, 6000)])
    C = np.cos(np.outer(r, lams))
    nv = 2 * m + 1
    c = np.zeros(nv)
    c[-1] = -1.0
    Aub = np.vstack(
        [np.hstack([-C, C, np.ones((len(r), 1))]), np.concatenate([np.ones(2 * m), [0.0]])]
    )
    Bmax = _W_lp(np.float64(R)) - sumPL - 0.05
    bub = np.append(_W_lp(r) + PL(r), Bmax)
    res = linprog(
        c,
        A_ub=Aub,
        b_ub=bub,
        bounds=[(0.0, None)] * (2 * m) + [(None, 10.0)],
        method="highs",
    )
    assert res.success, f"the LP at L={L} failed: {res.message}"
    return -float(res.fun)


def _phihat(r, L: float, J: int) -> np.ndarray:
    """The sine-basis transform of opcert.py / op_rig_validated.py."""
    j = np.arange(1, J + 1)
    k = j * np.pi / L
    rr = np.asarray(r)[:, None]
    den = k[None, :] ** 2 - rr**2
    den = np.where(np.abs(den) < 1e-12, 1e-12, den)
    return (
        np.sqrt(2 / L)
        * np.exp(-1j * rr * L / 2)
        * k[None, :]
        * (1 - ((-1.0) ** j)[None, :] * np.exp(1j * rr * L))
        / den
    )


def _op_rig_run(L: float, t: float, J: int, h: float, safe: float, chunk: int = 4000) -> dict:
    """``op_rig_validated.py``'s validated run of the operator-form window.

    W comes from the script's own K=400 partial sums plus the integral
    tail and the explicit margin; G is accumulated on the active cells'
    midpoints; the top eigenvalue is bounded by the script's verified
    Cholesky estimate and every rounding error enters the margin.
    """
    A = _lp_prime_powers()
    act = {n: a for n, a in A.items() if np.log(n) < L}
    S = sum(abs(a) for a in act.values())
    M = sum(abs(a) * np.log(n) for n, a in act.items())
    R = 0.5
    while _w_lower_k400(np.array([R]), safe)[0] < t + S:
        R *= 1.05
    G = np.zeros((J, J))
    eta = 0.0
    intN = 0.0
    ncell = 0
    r0 = 0.0
    while r0 < R:
        rk = np.arange(r0, min(R, r0 + chunk * h), h)
        rm = rk + h / 2
        Wk = _w_lower_k400(rk, safe)
        low = Wk + sum(a * np.cos(rk * np.log(n)) for n, a in act.items()) - M * h - safe
        N = np.clip(t - low, 0, None)
        if N.max() > 0:
            idx = N > 0
            F = _phihat(rm[idx], L, J)
            w = N[idx] * h / np.pi
            G += np.real((F.conj().T * w) @ F)
            eta += np.sum(w * np.clip(L - np.sum(np.abs(F) ** 2, 1), 0, None))
            intN += np.sum(w)
            ncell += int(idx.sum())
        r0 = rk[-1] + h
    u = 2.0**-53

    def gam(m: int) -> float:
        return (m * u) / (1 - m * u)

    Gs = (G + G.T) / 2
    lam_t = np.linalg.eigvalsh(Gs)[-1]
    mu = lam_t + 1e-8
    Acm = mu * np.eye(J) - Gs
    np.linalg.cholesky(Acm)  # the script checks the factorisation completes
    chol_bound = gam(J + 1) * (1 + gam(J + 1)) * np.trace(Acm) + u * np.max(np.abs(np.diag(Acm)))
    lam_up = mu + chol_bound
    e_G = J * (intN * h * h * L**3 / 24)
    e_eta = intN * h * h * (J * L**3) / 24
    e_acc = J * gam(ncell + 2 * J) * intN * L * 1.01
    e_eval = J * 2 * safe * intN * L
    e_sym = np.max(np.abs(G - G.T)) * J
    margin = t - (lam_up + e_G + e_acc + e_eval + e_sym) - (eta + e_eta + gam(ncell) * intN * L)
    return {
        "margin": float(margin),
        "lam_t": float(lam_t),
        "lam_up": float(lam_up),
        "chol": float(chol_bound),
        "eta": float(eta),
        "e_G": float(e_G),
        "e_eta": float(e_eta),
        "R": float(R),
    }


def _opcert_rig_run(L: float, t: float, J: int, h: float, safe: float, chunk: int = 8000) -> dict:
    """``opcert_rig.py``'s rigorous primal optimum: rigW's coarse W grid,
    the explicit quadrature and float error terms, midpoint rule."""
    A = _lp_prime_powers()
    act = {n: a for n, a in A.items() if np.log(n) < L}
    S = sum(abs(a) for a in act.values())
    M = sum(abs(a) * np.log(n) for n, a in act.items())
    R = 0.5
    while _w_lower_adaptive(np.array([R]), safe)[0] < t + S:
        R *= 1.05
    coarse = np.unique(
        np.concatenate(
            [
                np.arange(0, 5, 2e-4),
                np.arange(5, min(R, 50), 2e-3),
                np.arange(50, R + 0.02, 0.02) if R > 50 else np.array([]),
            ]
        )
    )
    Wc = _w_lower_adaptive(coarse, safe)
    G = np.zeros((J, J), complex)
    eta = 0.0
    intN = 0.0
    r0 = 0.0
    while r0 < R:
        rk = np.arange(r0, min(R, r0 + chunk * h), h)
        rm = rk + h / 2
        Wk = Wc[np.searchsorted(coarse, rk, side="right") - 1]
        low = Wk + sum(a * np.cos(rk * np.log(n)) for n, a in act.items()) - M * h - safe
        N = np.clip(t - low, 0, None)
        if N.max() > 0:
            idx = N > 0  # active cells only: w = 0 elsewhere contributes nothing
            F = _phihat(rm[idx], L, J)
            w = N[idx] * h / np.pi
            G += (F.conj().T * w) @ F
            eta += np.sum(w * np.clip(L - np.sum(np.abs(F) ** 2, 1), 0, None))
            intN += np.sum(w)
        r0 = rk[-1] + h
    lamJ = np.linalg.eigvalsh(np.real(G))[-1]
    e_G = J * (intN * h * h * L**3 / 24)
    e_eta = intN * h * h * (2 * J * (L / 2) ** 2 * L) / 24
    e_float = safe * J
    margin = t - (lamJ + e_G + e_float) - (eta + e_eta)
    return {"margin": float(margin), "lamJ": float(lamJ), "eta": float(eta), "R": float(R)}


def _verify_iv_replay(cert: dict, h_den: int, R: int, kterms: int) -> dict:
    """``verify_iv.py``'s replay of the certificate in ball arithmetic.

    Same bounds as the script's ``mpmath.iv`` run — K=60 series terms with
    the integral tail, the midpoint grid of step 1/h_den over [0, R], the
    loss M h^2/8, the tail at ``kterms`` terms — with python-flint's
    outward-rounded balls instead of interval mpf's.
    """
    lam = [Fraction(x) for x in cert["lam"]]
    b = [Fraction(x) for x in cert["b"]]
    primes = {int(p): Fraction(v) for p, v in cert["primes"].items()}
    old_prec = ctx.prec
    ctx.prec = 128
    try:
        C0 = (arb(5) / arb.pi()).log() + (-arb.const_euler() - arb.pi() / 2 - 3 * arb(2).log())
        a2 = arb(2).sqrt() * arb(2).log()

        def fr(c: Fraction) -> arb:
            return arb(c.numerator) / c.denominator

        M2 = a2 * arb(2).log() ** 2 + sum(abs(fr(c)) * fr(l) ** 2 for c, l in zip(b, lam))
        MW = (64 + (arb(5) / 4) ** -3 + ((arb(5) / 4) ** -2) / 2) / 2
        M = MW + M2
        x = arb(1) / 4
        K = 60
        h = arb(1) / h_den
        loss = (M * h * h / 8).upper()

        def W_low(r: arb) -> arb:
            y = r / 2
            s = C0
            for j in range(K):
                u = arb(j) + x
                s = s + y * y / (u * (u * u + y * y))
            U = arb(K) + x
            return s + (1 + y * y / (U * U)).log() / 2

        def T(r: arb) -> arb:
            return a2 * (r * arb(2).log()).cos() + sum(
                fr(c) * (fr(l) * r).cos() for c, l in zip(b, lam)
            )

        worst = None
        prev = (W_low(arb(0)) + T(arb(0))).lower()
        for k in range(R * h_den):
            nxt = (W_low(arb(k + 1) / h_den) + T(arb(k + 1) / h_den)).lower()
            low = (prev if prev < nxt else nxt) - loss
            if worst is None or low < worst:
                worst = low
            prev = nxt
        y = arb(R) / 2
        s = C0
        for j in range(kterms):
            u = arb(j) + x
            s = s + y * y / (u * (u * u + y * y))
        U = arb(kterms) + x
        W_tail = s + (1 + y * y / (U * U)).log() / 2
        tail = (W_tail - a2 - sum(abs(fr(c)) for c in b)).lower()
    finally:
        ctx.prec = old_prec
    return {"min": float(worst), "tail": float(tail), "M": float(M), "loss": float(loss)}


def _min_grid_distance(L: float, R: float, h: float) -> float:
    """The closest a cell midpoint of ``[0, R]`` gets to any $k_j = j\\pi/L$."""
    rm = np.arange(0.0, R, h) + h / 2
    j = np.arange(1, int(np.ceil(L * (R + h) / np.pi)) + 2)
    k = j * np.pi / L
    idx = np.searchsorted(k, rm)
    right = k[np.clip(idx, 0, len(k) - 1)]
    left = k[np.clip(idx - 1, 0, len(k) - 1)]
    return float(np.min(np.minimum(np.abs(rm - left), np.abs(rm - right))))


# --------------------------------------------------------------------------------------
# cert.py — the linear programme behind the certificate (04-bridges:569-577, 506-511).
# --------------------------------------------------------------------------------------


@pytest.mark.slow
def test_cert_lp_reaches_l_one_point_zero_eight_with_margin() -> None:
    """04-bridges:577 — the certificate method reaches $L=1.08$ (margin $0.013$).

    Condition: ``cert.py``'s own LP at ``lam_max=16``, ``m=200``,
    ``R=600`` on the 12000+6000-point grid, ``method="highs"``; the level
    and the margin are parsed from the sentence that names the script.
    """
    L_str, margin_str, cite = _claim(
        "04-bridges.tex",
        r"reaches \$L=([\d.]+)\$ \(margin \$([\d.]+)\$, \\code\{(cert\.py)\}\)",
        "the certificate's level and margin (04-bridges:577)",
    )
    assert cite == "cert.py"
    margin = _lp_margin(float(L_str), _lp_prime_powers())
    assert_lower_bound_figure(margin, margin_str, f"the LP margin at L={L_str} (04-bridges:577)")


@pytest.mark.slow
def test_cert_lp_flipped_frobenius_sign_gives_negative_optimum() -> None:
    """04-bridges:569-573 — replacing the sign of $a_2$ flips the optimum to $-0.573$.

    Condition: the same LP at $L=1$ with the script's own replacement set
    $n\\in\\{2,8,32,128\\}$ (the prime 2 and its odd powers, all with
    $\\chi_5=-1$; only $n=2$ enters the ansatz at $L=1$); the sign
    $a_2=+0.980$ and the optimum are parsed from the remark that names
    ``cert.py``.
    """
    sign_str = _claim(
        "04-bridges.tex", r"\\sqrt2=\+([\d.]+)", "the sign of a_2 (04-bridges:571)"
    )[0]
    opt_str, cite = _claim(
        "04-bridges.tex",
        r"optimum\s*\$(-?[\d.]+)\$ \(\\code\{(cert\.py)\}\)",
        "the replaced-sign optimum (04-bridges:573)",
    )
    assert cite == "cert.py"
    A = _lp_prime_powers()
    assert_half_last_digit(A[2], sign_str, "a_2 (04-bridges:571)")
    flip = dict(A)
    for n in (2, 8, 32, 128):
        flip[n] = -flip[n]
    optimum = _lp_margin(1.0, flip)
    assert optimum < 0, "replacing the sign of a_2 must flip the optimum (04-bridges:573)"
    assert_half_last_digit(optimum, opt_str, "the replaced-sign optimum (04-bridges:573)")


def test_certificate_json_declares_the_manuscript_pairs_and_lipschitz() -> None:
    """04-bridges:506-511 — the certificate: $41$ rational pairs with
    $\\lambda_i\\in[1,16]$ and Lipschitz constant $M_T=11.0$.

    Condition: the committed artefact ``cert_L1.0.json`` (the certificate
    named at 04-bridges:493, written by the orphan ``verify_cert.py`` from
    ``cert.py``'s optimum); $M_T$ is recomputed from the artefact as
    $\\sum|a_n|\\log n + \\sum|b_i|\\lambda_i$ over its recorded pairs.
    """
    pairs_str = _claim(
        "04-bridges.tex", r"gives \$(\d+)\$ rational pairs", "the pair count (04-bridges:506)"
    )[0]
    lo_str, hi_str = _claim(
        "04-bridges.tex",
        r"\\lambda_i\\in\[([\d.]+),([\d.]+)\]",
        "the lambda range (04-bridges:507)",
    )
    mt_str = _claim(
        "04-bridges.tex", r"M_T=[^$]*=([\d.]+)\$", "the Lipschitz constant (04-bridges:511)"
    )[0]
    cert = _certificate()
    lam = [Fraction(x) for x in cert["lam"]]
    b = [Fraction(x) for x in cert["b"]]
    keep = [(l, c) for l, c in zip(lam, b) if c != 0 and float(l) >= cert["L"]]
    assert len(keep) == int(pairs_str), (
        f"the certificate holds {len(keep)} rational pairs, the manuscript says {pairs_str} "
        "(04-bridges:506)"
    )
    lo, hi = float(lo_str), float(hi_str)
    for l, _ in keep:
        assert lo <= float(l) <= hi, f"lambda {float(l)} outside [{lo}, {hi}] (04-bridges:507)"
    primes = {int(p): Fraction(v) for p, v in cert["primes"].items()}
    with mp.workdps(40):
        mt = sum(abs(float(v)) * float(mp.log(p)) for p, v in primes.items())
    mt += sum(abs(float(c)) * float(l) for l, c in keep)
    assert_half_last_digit(mt, mt_str, "M_T recomputed from the certificate (04-bridges:511)")


# --------------------------------------------------------------------------------------
# rigW.py — the rigorous lower bound for W (04-bridges:547-555, appendix:577).
# --------------------------------------------------------------------------------------


def test_rig_w_bounds_the_archimedean_weight_below() -> None:
    """04-bridges:551-555 — the partial sums bound $W$ from below with the
    declared margin $10^{-9}$, monotonically (rmk:rigour names ``rigW.py``).

    Condition: the six radii ``rigW.py``'s ``__main__`` checks
    ($0,1,5,20,100,600$), $K=4000+60y$ terms, the declared margin
    subtracted; $W$ itself is $\\log(5/\\pi)+\\mathrm{Re}\\,\\psi(1/4+ir/2)$
    at dps=40, and $\\psi(1/4)$ is the closed form the remark prints.
    """
    assert re.search(
        r"bounded below \(\\code\{rigW\.py\}\)", read_tex("04-bridges.tex")
    ), "rmk:rigour must cite rigW.py (04-bridges:552)"
    assert re.search(
        r"\\psi\(\\tfrac14\)=-\\gamma_E-\\frac\\pi2-3\\log2", read_tex("04-bridges.tex")
    ), "the manuscript must print Gauss's psi(1/4) (04-bridges:551)"
    safe = _safe_margin()
    radii = [0.0, 1.0, 5.0, 20.0, 100.0, 600.0]  # rigW.py's __main__
    lower = _w_lower_adaptive(np.array(radii), safe)
    exact = np.array([_w_exact(r) for r in radii])
    assert np.all(lower <= exact), (
        f"W_lower must not exceed W at the checked radii: {list(zip(radii, lower, exact))}"
    )
    gaps = exact - lower
    assert np.all(gaps >= safe), (
        f"the gap must cover the declared margin {safe} (04-bridges:554): {gaps}"
    )
    assert np.all(np.diff(lower) > 0), "W_lower must be strictly increasing (04-bridges:552)"
    # Gauss's digamma theorem as printed: psi(1/4) = -gamma_E - pi/2 - 3 log 2.
    with mp.workdps(40):
        closed = float(mp.log(5 / mp.pi) + (-mp.euler - mp.pi / 2 - 3 * mp.log(2)))
        direct = float(mp.log(5 / mp.pi) + mp.re(mp.digamma(mp.mpf(1) / 4)))
    assert_close(closed, direct, 1e-15, "the psi(1/4) closed form (04-bridges:551)")


# --------------------------------------------------------------------------------------
# op_rig_validated.py — the validated replay of the operator form (04-bridges:521-543, 555).
# --------------------------------------------------------------------------------------


def _third_window_figures() -> dict[str, str]:
    """The three validated margins, parsed once and cross-checked at every site."""
    m_str, lo_str, hi_str, l_str = _claim(
        "04-bridges.tex",
        r"the margins are \$([\d.]+)\$, \$([\d.]+)\$, \$([\d.]+)\$ at \$L=([\d.,]+)\$",
        "the three validated margins (04-bridges:555)",
    )
    figs = dict(zip(l_str.split(","), (m_str, lo_str, hi_str)))
    thm_level, thm_floor = _claim(
        "04-bridges.tex",
        r"length \$L\\le([\d.]+)\$,\s*\$Q\(f\)\\ge([\d.]+)",
        "thm:third-window's level and floor (04-bridges:521)",
    )
    (m12,) = _claim(
        "04-bridges.tex",
        r"\\le1\.2\$ the margin is \$([\d.]+)\$",
        "the L=1.2 margin (04-bridges:522)",
    )
    (m11,) = _claim(
        "04-bridges.tex",
        r"at \$L\\le1\.1\$,?\s*\$([\d.]+)\$",
        "the L=1.1 margin (04-bridges:523)",
    )
    assert (thm_floor, m12, m11) == (figs["1.3"], figs["1.2"], figs["1.1"]), (
        "the theorem and rmk:rigour must print the same margins: "
        f"{thm_floor, m12, m11} vs {figs}"
    )
    assert thm_level == "1.3"
    a11, a12, a13 = _claim(
        "appendix.tex",
        r"margins \$([\d.]+)\$, \$([\d.]+)\$, \$([\d.]+)\$",
        "the census's margins (appendix:42)",
    )
    assert (a11, a12, a13) == (figs["1.1"], figs["1.2"], figs["1.3"]), (
        f"appendix:42 must print the same margins: {(a11, a12, a13)} vs {figs}"
    )
    return figs


def test_operator_replay_validates_the_three_window_margins() -> None:
    """04-bridges:521-524, 555 and appendix:42 — the validated margins
    $0.0027$ ($L\\le1.3$), $0.0077$ ($L\\le1.2$), $0.0261$ ($L\\le1.1$),
    all positive.

    Condition: the three configurations of the committed run
    ``op_rig_validated_output.json`` ($t=2$; $J=800$, $h=2.5\\cdot10^{-4}$
    at $L=1.3$ as printed at 04-bridges:541 and asserted equal to the
    artefact here; $J=400$, $h=5\\cdot10^{-4}$ at $L=1.1,1.2$ as recorded
    there), each recomputed with the script's own validated budget.
    """
    figs = _third_window_figures()
    assert re.search(r"op\\_rig\\_validated\.py", read_tex("04-bridges.tex")), (
        "04-bridges must cite op_rig_validated.py (04-bridges:524)"
    )
    safe = _safe_margin()
    L_str, t_str, J_str, h_m, h_e = _claim(
        "04-bridges.tex",
        r"Computation at \$L=([\d.]+)\$, \$t=([\d.]+)\$, \$J=(\d+)\$, \$h=([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the L=1.3 configuration (04-bridges:541)",
    )
    runs = [json.loads(line) for line in OP_RIG_OUTPUT.read_text(encoding="utf-8").splitlines() if line.strip()]
    r13 = next(r for r in runs if r["L"] == float(L_str))
    assert (r13["t"], r13["J"], r13["h"]) == (float(t_str), int(J_str), _sci(h_m, h_e)), (
        f"the committed L={L_str} run must record t={t_str}, J={J_str}, "
        f"h={h_m}e{h_e} (04-bridges:541), got t={r13['t']}, J={r13['J']}, h={r13['h']}"
    )
    for run in runs:
        result = _op_rig_run(run["L"], run["t"], run["J"], run["h"], safe)
        assert result["margin"] > 0, (
            f"L={run['L']}: the validated margin must be positive (04-bridges:555)"
        )
        assert_lower_bound_figure(
            result["margin"], figs[str(run["L"])], f"validated margin at L={run['L']}"
        )


def test_operator_replay_error_budget_matches_the_manuscript() -> None:
    """04-bridges:541-543 and 555 — the $L=1.3$ computation's error budget.

    Condition: the configuration the sentence prints ($t=2$, $J=800$,
    $h=2.5\\cdot10^{-4}$) with the script's validated budget; the two
    thresholds (quadrature errors, Cholesky bound) are one-sided claims,
    the printed values are reconciled at their precision, and the grid
    distance is the closest midpoint of $[0,R]$ to any $k_j$.
    """
    L_str, t_str, J_str, h_m, h_e = _claim(
        "04-bridges.tex",
        r"Computation at \$L=([\d.]+)\$, \$t=([\d.]+)\$, \$J=(\d+)\$, \$h=([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the L=1.3 configuration (04-bridges:541)",
    )
    lam_str = _claim(
        "04-bridges.tex", r"\\lambda_J\\le([\d.]+)\$", "the eigenvalue bound (04-bridges:542)"
    )[0]
    eta_m, eta_e = _claim(
        "04-bridges.tex", r"\\eta_J=([\d.]+)\\cdot10\^\{(-?\d+)\}\$", "eta_J (04-bridges:542)"
    )
    err_m, err_e = _claim(
        "04-bridges.tex",
        r"and quadrature errors below \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the quadrature-error threshold (04-bridges:542)",
    )
    margin_str = _claim(
        "04-bridges.tex", r"hence the margin \$([\d.]+)\$", "the margin (04-bridges:542)"
    )[0]
    r_str = _claim("04-bridges.tex", r"; \$R=(\d+)\$", "R (04-bridges:542)")[0]
    chol_m, chol_e = _claim(
        "04-bridges.tex",
        r"\\cite\{higham02\}, below \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the Cholesky threshold (04-bridges:542)",
    )
    grid_m, grid_e = _claim(
        "04-bridges.tex",
        r"at least \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the grid threshold (04-bridges:555)",
    )
    safe = _safe_margin()
    result = _op_rig_run(float(L_str), float(t_str), int(J_str), _sci(h_m, h_e), safe)
    assert_upper_bound_figure(result["lam_t"], lam_str, "lambda_J (04-bridges:542)")
    assert_half_last_digit(result["eta"], f"{eta_m}e{eta_e}", "eta_J (04-bridges:542)")
    err = _sci(err_m, err_e)
    assert result["e_G"] <= err and result["e_eta"] <= err, (
        f"quadrature errors {result['e_G']}, {result['e_eta']} must stay below {err} "
        "(04-bridges:542)"
    )
    assert_lower_bound_figure(result["margin"], margin_str, "the margin (04-bridges:542)")
    assert_half_last_digit(result["R"], r_str, "R (04-bridges:542)")
    chol = _sci(chol_m, chol_e)
    assert result["chol"] <= chol, (
        f"the Cholesky bound {result['chol']} must stay below {chol} (04-bridges:542)"
    )
    dist = _min_grid_distance(float(L_str), result["R"], _sci(h_m, h_e))
    assert_lower_bound_figure(dist, f"{grid_m}e{grid_e}", "the grid distance (04-bridges:555)")


@pytest.mark.golden
def test_operator_replay_committed_output_is_pinned() -> None:
    """The committed ``op_rig_validated_output.json`` still backs the figures.

    Nothing is recomputed here: the three recorded margins, eigenvalue,
    eta, Cholesky bound and R are reconciled with the figures of
    04-bridges:541-543 and 555, and the artefact's exact internal identity
    ``lambda_upper = lambda_float + 1e-8 + chol_bound`` is pinned.
    """
    figs = _third_window_figures()
    L_str, t_str, J_str, h_m, h_e = _claim(
        "04-bridges.tex",
        r"Computation at \$L=([\d.]+)\$, \$t=([\d.]+)\$, \$J=(\d+)\$, \$h=([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the L=1.3 configuration (04-bridges:541)",
    )
    lam_str = _claim(
        "04-bridges.tex", r"\\lambda_J\\le([\d.]+)\$", "the eigenvalue bound (04-bridges:542)"
    )[0]
    eta_m, eta_e = _claim(
        "04-bridges.tex", r"\\eta_J=([\d.]+)\\cdot10\^\{(-?\d+)\}\$", "eta_J (04-bridges:542)"
    )
    margin13_str = _claim(
        "04-bridges.tex", r"hence the margin \$([\d.]+)\$", "the margin (04-bridges:542)"
    )[0]
    r_str = _claim("04-bridges.tex", r"; \$R=(\d+)\$", "R (04-bridges:542)")[0]
    chol_m, chol_e = _claim(
        "04-bridges.tex",
        r"\\cite\{higham02\}, below \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$",
        "the Cholesky threshold (04-bridges:542)",
    )
    runs = [json.loads(line) for line in OP_RIG_OUTPUT.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_L = {r["L"]: r for r in runs}
    assert set(by_L) == {1.3, 1.2, 1.1}, f"the artefact must record the three runs, got {sorted(by_L)}"
    r13 = by_L[float(L_str)]
    assert (r13["t"], r13["J"], r13["h"]) == (float(t_str), int(J_str), _sci(h_m, h_e)), (
        f"the L={L_str} line must record the configuration of 04-bridges:541"
    )
    chol = _sci(chol_m, chol_e)
    for L, fig in figs.items():
        run = by_L[float(L)]
        assert run["MARGIN"] > 0, f"L={L}: the recorded margin must be positive"
        assert_lower_bound_figure(run["MARGIN"], fig, f"recorded margin at L={L}")
        assert run["lambda_float"] <= float(lam_str), (
            f"L={L}: lambda_float {run['lambda_float']} must not exceed {lam_str} (04-bridges:542)"
        )
        assert run["chol_bound"] <= chol, (
            f"L={L}: chol_bound {run['chol_bound']} must not exceed {chol} (04-bridges:542)"
        )
        assert_half_last_digit(run["R"], r_str, f"recorded R at L={L} (04-bridges:542)")
        assert_close(
            run["lambda_upper"],
            run["lambda_float"] + 1e-8 + run["chol_bound"],
            1e-15,
            f"lambda_upper = mu + chol_bound at L={L} (op_rig_validated.py)",
        )
    assert_upper_bound_figure(r13["lambda_float"], lam_str, "recorded lambda_J (04-bridges:542)")
    assert_half_last_digit(r13["eta"], f"{eta_m}e{eta_e}", "recorded eta_J (04-bridges:542)")
    assert_lower_bound_figure(
        r13["MARGIN"], margin13_str, "recorded margin at L=1.3 (04-bridges:542)"
    )


# --------------------------------------------------------------------------------------
# opcert_rig.py — the rigorous primal (appendix:578, against the theorem's figures).
# --------------------------------------------------------------------------------------


def test_op_cert_rig_certifies_the_two_windows_rigorously() -> None:
    """appendix:578 — ``opcert_rig.py`` is a certificate of the two window
    theorems; its rigorous primal certifies the third-window margins.

    Condition: the two configurations of the script's ``__main__`` ($t=2$,
    $J=400$, $h=5\\cdot10^{-4}$ at $L=1.1$ and $1.2$); the primal subtracts
    ``rigW``'s coarse $W$ bound ($K=4000+60y$ with the declared $10^{-9}$
    margin) and an explicit $10^{-9}J$ float margin, so it lands strictly
    below the validated replay of the theorem it backs and agrees with its
    printed figure to one unit of the last digit.
    """
    assert re.search(
        r"\\code\{opcert\\_rig\.py\}", read_tex("appendix.tex")
    ), "appendix:578 must cite opcert_rig.py"
    fig_12 = _claim(
        "04-bridges.tex", r"\\le1\.2\$ the margin is \$([\d.]+)\$", "the L=1.2 margin (04-bridges:522)"
    )[0]
    fig_11 = _claim(
        "04-bridges.tex", r"at \$L\\le1\.1\$,?\s*\$([\d.]+)\$", "the L=1.1 margin (04-bridges:523)"
    )[0]
    safe = _safe_margin()
    for L, fig in [(1.1, fig_11), (1.2, fig_12)]:
        result = _opcert_rig_run(L, 2.0, 400, 5e-4, safe)
        assert result["margin"] > 0, (
            f"L={L}: the rigorous primal must certify the window (appendix:578)"
        )
        assert_within_last_digit(
            result["margin"], fig, f"the rigorous primal margin at L={L} (appendix:578)"
        )


# --------------------------------------------------------------------------------------
# verify_iv.py — the interval replay of the certificate (04-bridges:493, 514-516, 555).
# --------------------------------------------------------------------------------------


def test_verify_iv_replays_the_certificate_in_interval_arithmetic() -> None:
    """04-bridges:493, 514-516 and 555 — the interval replay: minimum
    $\\ge0.04458$, tail $\\ge0.04999$, $M=67.92$, and the theorem's floor
    $0.0445$.

    Condition: ball arithmetic (python-flint, precision 128 — the script
    uses ``mpmath.iv`` at ``dps=30``; both round outward and the ball run
    reproduces the committed output's 13 digits) over $h=\\tfrac1{100}$ on
    $[0,600]$ (both parsed from 04-bridges:515) with $K=60$ terms, the tail
    at the committed run's $K=6000$; the loss is $Mh^2/8$.
    """
    h_str, r_str = _claim(
        "04-bridges.tex",
        r"\$h=\\tfrac1\{(\d+)\}\$ over \$\[0,(\d+)\]\$",
        "the replay's grid (04-bridges:515)",
    )
    (min_str,) = _claim(
        "04-bridges.tex", r"minimum is \$\\ge([\d.]+)\$", "the minimum (04-bridges:516)"
    )
    (tail_str,) = _claim(
        "04-bridges.tex",
        r"\\sum\|b_i\|\\ge([\d.]+)\$",
        "the tail bound (04-bridges:516)",
    )
    thm_str = _claim(
        "04-bridges.tex",
        r"satisfies \$Q\(f\)\\ge([\d.]+)",
        "thm:second-window's floor (04-bridges:493)",
    )[0]
    (m_str,) = _claim(
        "04-bridges.tex", r"M=M_W\+M_2=([\d.]+)\$", "M (04-bridges:514)"
    )
    cite, gives_str = _claim(
        "04-bridges.tex",
        r"\(\\code\{(verify\\_iv\.py)\}\), which gives \$([\d.]+)\$",
        "verify_iv's figure (04-bridges:555)",
    )
    assert cite == r"verify\_iv.py"
    assert gives_str == thm_str, (
        f"04-bridges:555 and 04-bridges:493 must print the same floor, got {gives_str} vs {thm_str}"
    )
    h_den, R = int(h_str), int(r_str)
    result = _verify_iv_replay(_certificate(), h_den, R, kterms=6000)
    assert_lower_bound_figure(result["min"], min_str, "the replay's minimum (04-bridges:516)")
    assert_lower_bound_figure(result["min"], thm_str, "thm:second-window's floor (04-bridges:493)")
    assert_lower_bound_figure(result["tail"], tail_str, "the K=6000 tail (04-bridges:516)")
    assert_upper_bound_figure(result["M"], m_str, "M (04-bridges:514)")
    h = 1.0 / h_den
    assert_close(result["loss"], result["M"] * h * h / 8, 1e-15, "loss = M h^2/8 (04-bridges:515)")


@pytest.mark.golden
def test_verify_iv_committed_replay_is_pinned() -> None:
    """The committed ``verify_iv_L1.0_output.txt`` still backs the figures.

    Nothing is recomputed here: the six chunk minima, M, loss and the
    K=6000 tail are reconciled with the figures of 04-bridges:514-516, the
    loss with $Mh^2/8$ at the precision the file prints, and the chunks
    with the grid $h=\\tfrac1{100}$ over $[0,600]$ of 04-bridges:515.
    """
    h_str, r_str = _claim(
        "04-bridges.tex",
        r"\$h=\\tfrac1\{(\d+)\}\$ over \$\[0,(\d+)\]\$",
        "the replay's grid (04-bridges:515)",
    )
    (min_str,) = _claim(
        "04-bridges.tex", r"minimum is \$\\ge([\d.]+)\$", "the minimum (04-bridges:516)"
    )
    (tail_str,) = _claim(
        "04-bridges.tex", r"\\sum\|b_i\|\\ge([\d.]+)\$", "the tail bound (04-bridges:516)"
    )
    (m_str,) = _claim(
        "04-bridges.tex", r"M=M_W\+M_2=([\d.]+)\$", "M (04-bridges:514)"
    )
    h_den, R = int(h_str), int(r_str)
    lines = [
        json.loads(line)
        for line in VERIFY_IV_OUTPUT.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    chunks = [d for d in lines if "start" in d and d["stop"] - d["start"] == 10000]
    assert len(chunks) == 6, f"the artefact must record the six chunks of [0,{R}], got {len(chunks)}"
    assert [d["start"] for d in chunks] == [i * 10000 for i in range(6)], (
        "the chunks must tile the grid of 04-bridges:515"
    )
    assert 6 * 10000 == R * h_den, "the grid must be h=1/h_den over [0, R] (04-bridges:515)"
    mins = [float(d["min_lower"]) for d in chunks]
    assert min(mins) == mins[0], "the global minimum sits in the first chunk"
    assert_lower_bound_figure(min(mins), min_str, "the recorded minimum (04-bridges:516)")
    assert all(v >= float(min_str) for v in mins), (
        f"every chunk must respect the bound {min_str} (04-bridges:516): {mins}"
    )
    M = float(chunks[0]["M"])
    assert_upper_bound_figure(M, m_str, "the recorded M (04-bridges:514)")
    assert len({d["M"] for d in chunks}) == 1 and len({d["loss"] for d in chunks}) == 1, (
        "the six chunks must record one run's M and loss"
    )
    loss = float(chunks[0]["loss"])
    assert_close(loss, M * (1.0 / h_den) ** 2 / 8, 5e-10, "loss = M h^2/8 at the printed precision")
    tail_lines = [d for d in lines if "tail_K6000" in d]
    assert len(tail_lines) == 1, "the artefact must record one K=6000 tail"
    assert_lower_bound_figure(
        float(tail_lines[0]["tail_K6000"]), tail_str, "the recorded K=6000 tail (04-bridges:516)"
    )


# --------------------------------------------------------------------------------------
# verify_rig.py — the earlier double-precision replay (04-bridges:517, appendix:41).
# --------------------------------------------------------------------------------------


def test_verify_rig_certifies_the_pointwise_window_in_double_precision() -> None:
    """04-bridges:517 — the double-precision replay gave $0.0431$.

    Condition: ``verify_rig.py``'s own constants — the coarse $W$ grid of
    ``rigW`` (steps $2\\cdot10^{-4}$, $2\\cdot10^{-3}$, $0.02$), cells of
    $h=2\\cdot10^{-4}$ over $[0,600]$, $\\mathtt{SAFE\\_T}=10^{-9}$ — with
    the committed certificate ``cert_L1.0.json`` as input; the figure is
    printed twice, at 04-bridges:517 and in appendix:41.
    """
    cite, fig = _claim(
        "04-bridges.tex",
        r"replay \((\\code\{verify\\_rig\.py\})[^)]*\) gave \$([\d.]+)\$",
        "the double-precision replay's minimum (04-bridges:517)",
    )
    assert cite == r"\code{verify\_rig.py}"
    (fig_app,) = _claim(
        "appendix.tex",
        r"supersedes the double-precision \$([\d.]+)\$",
        "the superseded figure (appendix:41)",
    )
    assert fig == fig_app, f"04-bridges:517 and appendix:41 must print the same figure: {fig} vs {fig_app}"
    safe = _safe_margin()
    cert = _certificate()
    lam = np.array([float(Fraction(x)) for x in cert["lam"]])
    b = np.array([float(Fraction(x)) for x in cert["b"]])
    pr = {int(k): Fraction(v) for k, v in cert["primes"].items()}
    an = np.array([float(v) for v in pr.values()])
    ln = np.log(np.array(list(pr.keys()), dtype=float))
    R = 600.0
    coarse = np.unique(
        np.concatenate(
            [np.arange(0, 5, 2e-4), np.arange(5, 50, 2e-3), np.arange(50, R + 0.02, 0.02)]
        )
    )
    Wc = _w_lower_adaptive(coarse, safe)
    MT = np.sum(np.abs(an) * ln) + np.sum(np.abs(b) * lam)
    h = 2e-4
    worst = np.inf
    r0 = 0.0
    while r0 < R:
        rk = np.arange(r0, min(R, r0 + 20000 * h), h)
        T = (an[None, :] * np.cos(np.outer(rk, ln))).sum(1) + (
            b[None, :] * np.cos(np.outer(rk, lam))
        ).sum(1)
        idx = np.searchsorted(coarse, rk, side="right") - 1  # coarse point <= rk
        val = Wc[idx] + T - MT * h - safe
        worst = min(worst, float(val.min()))
        r0 = rk[-1] + h
    assert_lower_bound_figure(worst, fig, "the rigorous minimum (04-bridges:517)")

# --------------------------------------------------------------------------------------
# verify_weil_chi5.py, weil_window_chi5.py, weil_window_rigorous_check.py — the
# normalisation of the explicit formula, the semilocal window, the first-window constants.
# --------------------------------------------------------------------------------------

#: The committed cache of the 40 zeros of L(s, chi_5) below T = 80 (byte-identical
#: to chi5_zeros_T80.txt, committed in 7b0c68f) — the input ``verify_weil_chi5.py``
#: recomputes by sign changes; the suite reads it instead of re-running the scan.
CHI5_ZEROS_T80 = REPO_ROOT / "tests" / "fixtures" / "zeros.txt"

#: The sine basis and the grid ``weil_window_chi5.py`` declares (its ``J=24, M=3000``).
WINDOW_J = 24
WINDOW_M = 3000


def _window_coefficients() -> dict[int, float]:
    r"""$\Lambda(n)\chi_5(n)/\sqrt n$ for the prime powers $n < 200$ (the script's ``cn``)."""
    coefficients = {}
    for n in range(2, 200):
        x, p = n, None
        for candidate in range(2, n + 1):
            if x % candidate == 0:
                p = candidate
                while x % candidate == 0:
                    x //= candidate
                break
        if x != 1 or p is None:
            continue
        chi = [0, 1, -1, -1, 1][n % 5]
        if chi:
            coefficients[n] = np.log(p) * chi / np.sqrt(n)
    return coefficients


def _window_lambda(L: float, with_primes: bool = True, flip_two: bool = False) -> float:
    """Smallest eigenvalue of the Weil form on $[-L/2,L/2]$ (``weil_window_chi5.py``).

    The orthonormal sine basis of ``WINDOW_J`` modes on a uniform grid of
    ``WINDOW_M`` points, the archimedean term in the variable $u$ with its
    singular pieces combined, and the prime side interpolated on the same
    grid. ``flip_two`` replaces the Frobenius at 2 by the identity, the
    counterfactual of 04-bridges:432.
    """
    coefficients = _window_coefficients()
    x = np.linspace(-L / 2, L / 2, WINDOW_M)
    dx = x[1] - x[0]
    basis = np.array([np.sin(j * np.pi * (x + L / 2) / L) for j in range(1, WINDOW_J + 1)])
    basis /= np.sqrt((basis**2).sum(1) * dx)[:, None]
    u = np.arange(0, WINDOW_M) * dx
    uu = u[1:]
    wg = -2 * np.exp(-uu / 2) / (1 - np.exp(-2 * uu))
    w0 = 2 * np.exp(-2 * uu) / (1 - np.exp(-2 * uu))
    form = np.zeros((WINDOW_J, WINDOW_J))
    for a in range(WINDOW_J):
        for b in range(a, WINDOW_J):
            full = np.correlate(basis[a], basis[b], "full") * dx
            g = (full[WINDOW_M - 1 :] + full[:WINDOW_M][::-1]) / 2
            g0 = g[0]
            integrand = np.empty_like(u)
            integrand[0] = -1.5 * g0
            integrand[1:] = w0 * g0 + wg * g[1:]
            arch = np.trapezoid(integrand, u) - np.log(1 - np.exp(-2 * L)) * g0
            arch = g0 * (np.log(5 / np.pi) - 0.5772156649015329) + arch
            prime = 0.0
            if with_primes:
                for n, c in coefficients.items():
                    log_n = np.log(n)
                    if log_n < L:
                        if flip_two and n == 2:
                            c = abs(c)
                        prime += c * np.interp(log_n, u, g)
            form[a, b] = form[b, a] = arch - 2 * prime
    return float(np.linalg.eigvalsh(form)[0])


def _archimedean_threshold() -> float:
    """The $L$ where the archimedean-only form changes sign, by bisection."""
    lo, hi = 0.5, 1.2  # positive at 0.5, negative at 1.2 (the script's finding)
    for _ in range(18):
        mid = (lo + hi) / 2
        if _window_lambda(mid, with_primes=False) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def test_verify_weil_chi5_normalisation_agrees_to_ten_minus_18() -> None:
    r"""``04-bridges:379-381`` — the $40$ zeros (first $\gamma=6.6484533447$) and Gaussian $g$ give $10^{-18}$.

    Condition: ``verify_weil_chi5.py``'s own — ``mp.dps = 25``, the
    completed $\Lambda$ split at $\sigma=0.30,0.35,0.45$ (the widths its
    docstring declares), the prime side over the prime powers below $6000$
    split by $\chi_5$. The zeros are the committed cache the script's sign
    scan reproduces (count, height and first ordinate asserted below), so
    the scan's 138 s stay out of the suite.
    """
    count, height, first, exponent = _claim(
        "04-bridges.tex",
        r"with the\s+\$(\d+)\$ zeros of height \$\\le(\d+)\$ \(first \$\\gamma=([\d.]+)\$\)"
        r"[\s\S]*?both sides agree to \$10\^\{(-?\d+)\}\$",
        "the normalisation figures (04-bridges:380-381)",
    )
    tokens = CHI5_ZEROS_T80.read_text().split()
    assert len(tokens) == int(count), f"the cache holds {len(tokens)} zeros, the manuscript says {count}"
    assert max(float(t) for t in tokens) < int(height), f"a zero sits above T={height}"
    assert_half_last_digit(float(tokens[0]), first, "the first zero (04-bridges:380)")

    tolerance = mp.mpf(10) ** int(exponent)
    for sigma in ("0.30", "0.35", "0.45"):
        residual = _explicit_formula_residual(mp.mpf(sigma))
        assert residual < tolerance, (
            f"the explicit formula misses at sigma={sigma} by {mp.nstr(residual, 4)}, "
            f"the manuscript claims {tolerance}"
        )


def _explicit_formula_residual(sigma: mp.mpf) -> mp.mpf:
    """``|Z - (A - 2P)|`` of ``verify_weil_chi5.py`` for a Gaussian of width ``sigma``."""
    with mp.workdps(25):
        zeros = [mp.mpf(t) for t in CHI5_ZEROS_T80.read_text().split()]
        g = lambda u: mp.e ** (-u ** 2 / (2 * sigma ** 2))
        h = lambda r: sigma * mp.sqrt(2 * mp.pi) * mp.e ** (-sigma ** 2 * r ** 2 / 2)
        zero_side = 2 * sum(h(gamma) for gamma in zeros)
        arch = (
            mp.quad(
                lambda r: h(r) * (mp.log(5 / mp.pi) + mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2))),
                [-mp.inf, 0, mp.inf],
            )
            / (2 * mp.pi)
        )
        split = mp.mpf(0)
        inert = mp.mpf(0)
        for n in range(2, 6000):
            x, p = n, None
            for candidate in range(2, n + 1):
                if x % candidate == 0:
                    p = candidate
                    while x % candidate == 0:
                        x //= candidate
                    break
            if x != 1 or p is None:  # the prime powers only (the script's factorint)
                continue
            chi = [0, 1, -1, -1, 1][n % 5]
            if chi == 0:
                continue
            term = mp.log(p) / mp.sqrt(n) * g(mp.log(n))
            if chi == 1:
                split += term
            else:
                inert += term
        return abs(zero_side - (arch - 2 * (split - inert)))


def test_weil_window_chi5_threshold_and_floor() -> None:
    r"""``04-bridges:426-431`` with ``appendix:93`` — $L_c=0.9251$, $0.097$ at $1$, $5.3\cdot10^{-3}$ at $1.4$, $\sim10^{-6}$ at $2$.

    Condition: ``weil_window_chi5.py``'s own — ``J=24`` sine modes,
    ``M=3000`` points, the archimedean term with its singular pieces
    combined. The threshold is where the archimedean-only form changes
    sign (bisected to $3\cdot10^{-6}$), reconciled with the printed
    $L_c$ at half of its last digit; the three floors are the form with
    the primes. $\sim10^{-6}$ is an order-of-magnitude claim, asserted
    within half a decade (the computed value is $2.5\cdot10^{-6}$).
    """
    (l_c,) = _claim(
        "04-bridges.tex",
        r"archimedean positivity alone holds up to \$L_c=([\d.]+)\$ and fails beyond",
        "the archimedean threshold (04-bridges:428)",
    )
    floor, decay_mantissa, decay_exponent, tail_exponent = _claim(
        "04-bridges.tex",
        r"decays super-exponentially \(\$([\d.]+)\$ at \$L=1\$, \$([\d.]+)\\cdot10\^\{(-?\d+)\}\$"
        r" at \$1\.4\$,\s+\$\\sim10\^\{(-?\d+)\}\$ at \$2\$",
        "the floor figures (04-bridges:430)",
    )
    (l_c_appendix,) = _claim(
        "appendix.tex",
        r"Archimedean alone up to \$L=([\d.]+)\$",
        "the appendix row for the threshold (appendix:93)",
    )
    assert l_c == l_c_appendix, f"04-bridges:428 and appendix:93 disagree: {l_c} vs {l_c_appendix}"

    threshold = _archimedean_threshold()
    assert_half_last_digit(threshold, l_c, "the archimedean threshold (04-bridges:428)")

    at_one = _window_lambda(1.0)
    at_one_four = _window_lambda(1.4)
    at_two = _window_lambda(2.0)
    assert at_one > 0 and at_one_four > 0 and at_two > 0, (
        "the form with the primes must stay positive on every window the manuscript computes"
    )
    assert_half_last_digit(at_one, floor, "the L=1 floor (04-bridges:430)")
    assert_half_last_digit(
        at_one_four, f"{decay_mantissa}e{decay_exponent}", "the L=1.4 floor (04-bridges:430)"
    )
    decade = mp.mpf(10) ** int(tail_exponent)
    assert abs(mp.log10(at_two) - int(tail_exponent)) <= mp.mpf("0.5"), (
        f"the L=2 floor {at_two} is not of order {mp.nstr(decade, 3)} (half a decade)"
    )


def test_weil_window_chi5_counterfactual_fails_from_the_printed_threshold() -> None:
    r"""``04-bridges:432-433`` with ``appendix:93`` — with $\chi_5(2)=+1$ positivity fails from $L\approx0.9$.

    Condition: the same ``J=24``/``M=3000`` window with the Frobenius at 2
    replaced by the identity. ``weil_window_chi5.py`` scans
    $L=0.6,0.7,0.8,0.9,\ldots$ and reports the first failure, so the
    figure is the grid point where the sign flips: positive one step
    below it, negative at it (the bisection puts the crossing at
    $0.840$).
    """
    (figure,) = _claim(
        "04-bridges.tex",
        r"positivity fails from \$L\\approx([\d.]+)\$",
        "the counterfactual threshold (04-bridges:433)",
    )
    (figure_appendix,) = _claim(
        "appendix.tex",
        r"it fails from \$L\\approx([\d.]+)\$",
        "the appendix row for the counterfactual (appendix:93)",
    )
    assert figure == figure_appendix, f"04-bridges:433 and appendix:93 disagree: {figure} vs {figure_appendix}"

    at_figure = _window_lambda(float(figure), flip_two=True)
    below = _window_lambda(float(figure) - 0.1, flip_two=True)
    assert at_figure < 0, f"the counterfactual form is still positive at L={figure}: {at_figure}"
    assert below > 0, f"the counterfactual form is already negative at L={float(figure) - 0.1}: {below}"


def test_weil_window_rigorous_check_constants() -> None:
    r"""``04-bridges:440,443,450,466`` — $\kappa=-3.76274\ldots$, $L^*=0.744725\ldots$, $m=0.0841$ at $\log2$.

    Condition: ``weil_window_rigorous_check.py``'s own — ``mp.dps = 30``,
    $\kappa$ in its two writings ($\log5-\log\pi-\gamma_E-\pi/2-3\log2$
    and $\log(5/\pi)+\psi(1/4)$), $L^*$ as the root of $\kappa+K(L/2)=0$,
    the margin at $L=\log2$, and the integral identity behind $\kappa$.
    The printed $\kappa$ is truncated (``\ldots``), reconciled at one unit
    of its last digit.
    """
    (kappa_figure,) = _claim(
        "04-bridges.tex",
        r"\\kappa=[^=]*=(-?[\d.]+)\\ldots",
        "kappa (04-bridges:440)",
    )
    (l_star_figure,) = _claim(
        "04-bridges.tex",
        r"L\^\*=([\d.]+)\\ldots",
        "L* (04-bridges:443)",
    )
    (margin_figure,) = _claim(
        "04-bridges.tex",
        r"At \$L=\\log2\$, \$m=([\d.]+)\$",
        "the margin at L = log2 (04-bridges:450)",
    )
    _claim(
        "04-bridges.tex",
        r"\\psi\(1\)-\\psi\(\\frac14\)=\\frac\\pi2\+3\\log2",
        "the integral identity behind kappa (04-bridges:466)",
    )
    _claim(
        "04-bridges.tex",
        r"\\psi\(\\tfrac12\)=-\\gamma_E-2\\log2",
        "the digamma value at 1/2 (04-bridges:453)",
    )

    with mp.workdps(30):
        kappa = mp.log(5) - mp.log(mp.pi) - mp.euler - mp.pi / 2 - 3 * mp.log(2)
        assert_close(kappa, mp.log(5 / mp.pi) + mp.digamma(mp.mpf(1) / 4), mp.mpf("1e-28"), "kappa, two writings")
        assert_within_last_digit(float(kappa), kappa_figure, "kappa (04-bridges:440)")

        k = lambda d: 2 * (mp.atanh(mp.e ** (-d / 2)) + mp.atan(mp.e ** (-d / 2)))
        bound = lambda L: kappa + k(L / 2)
        l_star = mp.findroot(bound, 0.75)
        assert_half_last_digit(float(l_star), l_star_figure, "L* (04-bridges:443)")
        assert_close(bound(l_star), 0, mp.mpf("1e-28"), "kappa + K(L*/2) = 0")

        margin = bound(mp.log(2))
        assert_half_last_digit(float(margin), margin_figure, "the margin at L = log2 (04-bridges:450)")

        identity = mp.quad(
            lambda u: 2 * (mp.e ** (-u / 2) - mp.e ** (-2 * u)) / (1 - mp.e ** (-2 * u)), [0, 1, mp.inf]
        )
        assert_close(identity, mp.pi / 2 + 3 * mp.log(2), mp.mpf("1e-25"), "the integral identity (04-bridges:466)")
        assert_close(mp.digamma(mp.mpf(1) / 2), -mp.euler - 2 * mp.log(2), mp.mpf("1e-29"), "psi(1/2)")


def test_first_window_margin_stays_nonnegative_up_to_l_star() -> None:
    r"""``04-bridges:446-450`` — $m(L)\ge0$ for every $L\le L^*$, the claim of thm:first-window.

    Condition: the theorem's own definition —
    $m(L)=\min(\kappa+K(L/2),\ \kappa+\tfrac12(K(L-\log2)+K(L))-\tfrac{\log2}{\sqrt2})$,
    the second term only for $L>\log2$, evaluated on a grid up to the
    root $L^*$ the check above reproduces.
    """
    (l_star_figure,) = _claim(
        "04-bridges.tex",
        r"L\^\*=([\d.]+)\\ldots",
        "L* (04-bridges:443)",
    )
    with mp.workdps(30):
        kappa = mp.log(5) - mp.log(mp.pi) - mp.euler - mp.pi / 2 - 3 * mp.log(2)
        k = lambda d: 2 * (mp.atanh(mp.e ** (-d / 2)) + mp.atan(mp.e ** (-d / 2)))
        l_star = mp.findroot(lambda L: kappa + k(L / 2), 0.75)
        log_two = mp.log(2)
        margins = []
        for i in range(41):
            L = l_star * i / 40
            if L == 0:
                continue
            first = kappa + k(L / 2)
            second = kappa + (k(L - log_two) + k(L)) / 2 - log_two / mp.sqrt(2)
            margins.append(min(first, second) if L > log_two else first)
        worst = min(margins)
        assert worst >= 0, f"the margin turns negative below L*: {mp.nstr(worst, 6)}"
        assert abs(float(l_star) - float(l_star_figure)) < 1e-5, (
            "the grid must reach the printed L* for the claim to be tested there"
        )

