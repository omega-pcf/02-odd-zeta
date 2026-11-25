"""Golden outputs behind the bare ``N`` marks of INV-WIT-001 §B (W6 Fase2).

INV-WIT-001 lists 69 sites that carry ``\\tier{N}`` without naming a test.
Re-audited against the tree of ``cfae72c``: 49 of them still carry the mark
(20 were retired when the tables lost their Tier column), and 25 of those 49
have backing — a committed output under ``hipotesis/pruebas/salidas`` (24) or
a test that already pins the numbers (1: ``03-mechanisms:2978`` cites
``test_even_l_values_match_bernoulli_formula``, which checks ``L(2k, chi5)``
for k = 1..4).  This file writes the tests for the 24 artifact-backed sites,
grouped into five families; the other 24 live sites are recorded in
INV-WIT-001 §B as ``no-test:<reason>`` and are NOT touched here (Fase2 rule 3).

F10's rule holds throughout: nothing is recomputed — the committed output is
the record of the run, so a regenerated or edited artifact fails the gate
instead of drifting the paper.  Each test pins the artifact's digits at
``GOLDEN_TOL`` and reconciles the figure the manuscript prints for the same
claim: equality against the artifact's own ``articulo:`` line (the author's
reconciliation record), or the precision the sentence claims.

Family → sites → test (line numbers of ``cfae72c``; a site is identified by
the tail of its sentence, as the contract asks):

* **fluctuation law** — ``04-bridges:851`` (testGeom.py), ``04-bridges:853``
  (testB1b.py), ``05-categorical:60`` →
  ``test_fluctuation_law_is_the_same_everywhere``
* **positivity arc** — ``04-bridges:886`` (dh.py), ``04-bridges:891``
  (mertens341.py), ``04-bridges:894`` (mobius.py), ``04-bridges:918``
  (blocks.py), ``04-bridges:922`` (fejer_check.py), ``04-bridges:942``
  (balance.py), ``04-bridges:947`` (fibres.py), ``04-bridges:950``
  (dedekind.py), ``04-bridges:956`` (offline.py) →
  ``test_additive_side_statistics_are_pinned``,
  ``test_fejer_window_is_pinned``, ``test_orbit_balance_is_pinned``,
  ``test_offline_minimum_stays_positive``
* **field form and residual scales** — ``04-bridges:1006`` (gram.py),
  ``04-bridges:1133`` (field_signature.py, "the measurements"),
  ``04-bridges:1137`` (field_signature.py), ``04-bridges:1288``
  (escala_ceros_bajos.py), ``04-bridges:1535`` (amplitud_clausula_ii.py) →
  ``test_intersection_form_signature_is_pinned``,
  ``test_field_signature_is_pinned``, ``test_residual_scales_are_pinned``
* **statistics of the closure** — ``04-bridges:1651`` (t1_index.py,
  t2_loo.py), ``04-bridges:1763`` (euler_link.py), ``04-bridges:1825``
  (zeroside.py) → ``test_angular_index_statistics_are_pinned``,
  ``test_euler_link_second_term_is_pinned``,
  ``test_zeroside_orbit_agrees_with_the_zeros``
* **mechanisms and chapter five** — ``03-mechanisms:2117`` (kisin.py),
  ``03-mechanisms:1051`` (teich.py), ``05-categorical:99``
  (law_resolution.py), ``05-categorical:593`` (fermat_quintic_points.py) →
  ``test_kisin_interpolation_is_pinned``,
  ``test_delta_p_tower_ratios_are_pinned``,
  ``test_zero_side_correction_matches_the_manuscript``,
  ``test_fermat_quintic_point_counts_are_pinned``
"""

from __future__ import annotations

import re

import pytest

from oddzeta.harness import assert_close, read_salidas, read_tex

GOLDEN_TOL = 1e-12

_BRIDGES = "04-bridges.tex"
_MECHANISMS = "03-mechanisms.tex"
_CATEGORICAL = "05-categorical.tex"


def assert_printed_as_in_manuscript(value: float, printed: float, note: str) -> None:
    """The artifact value must round to the manuscript's figure.

    Same margin as ``test_golden_observations``: half of the last significant
    digit the manuscript prints (5% of the value), which is the precision the
    sentence claims.
    """
    assert abs(value - printed) <= 0.05 * abs(printed) + GOLDEN_TOL, (
        f"{note}: artifact {value} does not round to the manuscript's {printed} "
        f"(margin {0.05 * abs(printed) + GOLDEN_TOL})"
    )


def _first_float(text: str, pattern: str, note: str) -> float:
    match = re.search(pattern, text, re.MULTILINE)
    assert match is not None, f"{note}: pattern not found in the artifact: {pattern!r}"
    return float(match.group(1))


# ---------------------------------------------------------------------------
# Family: the law of the fluctuation — INV-WIT-001 §B sites
#   04-bridges:851 ("standard deviation ≈0.62, skewness ≈-0.33, kurtosis
#   ≈-0.55, with Kolmogorov--Smirnov p-values between 0.14 and 0.69"
#   \texttt{testGeom.py} \tier{N}),
#   04-bridges:853 ("requires log p to precision ≈1/T" \texttt{testB1b.py} \tier{N}),
#   05-categorical:60 ("its law is the same along the line, at random points
#   of the torus and on the zeros" \tier{N}).
# ---------------------------------------------------------------------------

_GEOM_ROW = re.compile(
    r"^\(([a-d])\) (.+?)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*(\d+\.\d+)?\s*$", re.M
)
_GEOM_TORUS = re.compile(
    r"^ley del toro \(20000 puntos\):\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)", re.M
)
_GEOM_ARTICULO = re.compile(
    r"desv\. ~(-?[\d.]+), sesgo ~(-?[\d.]+), curtosis ~(-?[\d.]+); "
    r"KS entre ([\d.]+) y ([\d.]+)"
)
_B1B_ROW = re.compile(r"^\s+(\d+)\s+([\d.]+e[-+]?\d+)\s+([\d.]+)\s*$", re.M)


def _fluctuation_rows() -> dict[str, tuple[float, float, float, float | None]]:
    """The four samples of testGeom.txt: (desv, sesgo, curtosis, KS p)."""
    text = read_salidas("testGeom.txt")
    rows = {}
    for match in _GEOM_ROW.finditer(text):
        label, _name, desv, sesgo, curtosis, ks = match.groups()
        rows[label] = (float(desv), float(sesgo), float(curtosis), float(ks) if ks else None)
    assert sorted(rows) == ["a", "b", "c", "d"], f"testGeom samples changed: {sorted(rows)}"
    torus = _GEOM_TORUS.search(text)
    assert torus is not None, "testGeom torus-law row not found"
    rows["torus"] = tuple(float(v) for v in torus.groups())  # type: ignore[assignment]
    return rows


@pytest.mark.golden
def test_fluctuation_law_is_the_same_everywhere() -> None:
    """testGeom.py and testB1b.py pin the four samples of ONE law.

    INV-WIT-001 §B sites covered: ``04-bridges:851`` (Kolmogorov–Smirnov
    p-values between 0.14 and 0.69, sd ≈0.62, skew ≈-0.33, kurtosis ≈-0.55),
    ``04-bridges:853`` (log p to precision ≈1/T) and ``05-categorical:60``
    (the law is the same on the line, at random points of the torus and on
    the zeros).

    The golden numbers are the committed run's rows; the manuscript's figures
    are reconciled against the artifact's own ``articulo:`` line, which is the
    record of what the run was compared with.  ``05-categorical:60`` is the
    real numerical content of the claim: a Kolmogorov–Smirnov p-value that is
    not significant does not reject "same distribution".
    """
    geom = read_salidas("testGeom.txt")
    rows = _fluctuation_rows()

    expected = {
        "a": (0.613, -0.374, -0.524, None),
        "b": (0.606, -0.337, -0.576, 0.99),
        "c": (0.604, -0.317, -0.558, 0.16),
        "d": (0.605, -0.405, -0.309, 0.64),
        "torus": (0.623, -0.318, -0.585, None),
    }
    for label, want in expected.items():
        got = rows[label]
        for index, (value, target) in enumerate(zip(got[:3], want[:3], strict=True)):
            assert_close(value, target, GOLDEN_TOL, f"testGeom {label} component {index}")
        if want[3] is not None:
            assert_close(got[3], want[3], GOLDEN_TOL, f"testGeom {label} KS p-value")

    # 05-categorical:60 — the three surrogate samples are not rejected
    # against the true line, so one law stands for all of them.
    for label in ("b", "c", "d"):
        p_value = rows[label][3]
        assert p_value is not None and p_value >= 0.05, (
            f"the sample {label!r} is rejected against the true line at p = {p_value}: "
            "05-categorical:60's 'the law is the same' would not hold"
        )

    # 04-bridges:851 — the printed figures are the artifact's reconciliation.
    tex = read_tex(_BRIDGES)
    claim = re.search(
        r"standard deviation \$\\approx(-?[\d.]+)\$, skewness \$\\approx(-?[\d.]+)\$, "
        r"kurtosis \$\\approx(-?[\d.]+)\$, with\s+Kolmogorov--Smirnov \$p\$-values "
        r"between \$([\d.]+)\$ and \$([\d.]+)\$",
        tex,
    )
    assert claim is not None, "the fluctuation figures of 04-bridges.tex not found"
    article = _GEOM_ARTICULO.search(geom)
    assert article is not None, "the articulo line of testGeom.txt not found"
    for printed, recorded in zip(claim.groups(), article.groups(), strict=True):
        assert_close(float(printed), float(recorded), GOLDEN_TOL, "testGeom manuscript figure")

    # 04-bridges:853 — the precision the artifact measures is ~1/T.
    b1b = read_salidas("testB1b.txt")
    assert re.search(r"to precision \$\\approx1/T\$", tex), (
        "04-bridges.tex no longer asks for log p to precision ~1/T"
    )
    assert "precision de log p ~1/T" in b1b, "testB1b.txt lost its articulo line"
    deviations = {int(m.group(1)): float(m.group(3)) for m in _B1B_ROW.finditer(b1b)}
    assert sorted(deviations) == [25, 50, 100, 200, 400, 800], sorted(deviations)
    expected_eps_t = {25: 1.804, 50: 2.105, 100: 2.301, 200: 2.286, 400: 2.537, 800: 2.397}
    for height, want in expected_eps_t.items():
        assert_close(deviations[height], want, GOLDEN_TOL, f"testB1b eps*T at T = {height}")
    # eps*T bounded over two decades  <=>  eps ~ 1/T: the claim's content.
    assert min(deviations.values()) > 1.5 and max(deviations.values()) < 3.0, (
        f"eps*T is not the constant the manuscript's ~1/T claims: {deviations}"
    )
    assert_close(_first_float(b1b, r"desviacion de F:\s*([\d.]+)", "testB1b deviation"), 0.621, GOLDEN_TOL, "testB1b deviation of F")


# <<<APPEND>>>
