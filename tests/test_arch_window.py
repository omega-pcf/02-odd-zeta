"""arch_window.py behind the archimedean-window crossings of 04-bridges.

D7-446 (``appendix:446``) trivial fills ``GoldenArchimedeanWindow`` and
``GoldenArchimedeanHodge``: the committed run of
``hipotesis/pruebas/arch_window.py`` is the record of the computation, and
F10's rule holds throughout — nothing is recomputed, so a regenerated or
edited artifact fails the gate instead of drifting the paper.  The test
pins the artifact's digits and reconciles the figures 04-bridges prints
for them, together with the condition the sentence declares (the Galerkin
the crossings were measured on).

Sites covered (``src/chapters/04-bridges.tex``, the paragraph "The
archimedean form, explicitly"):

* ``04-bridges:1148`` — ``C_0 = -9.13493``;
* ``04-bridges:1151`` — without the pole the form is negative from
  support length ``0.453``;
* ``04-bridges:1153`` — the second eigenvalue of ``D`` exceeds ``|C_0|``
  up to support length ``1.647``, beyond the prime-free range
  ``[0, log 4]``, measured on a Galerkin basis of 30 Legendre
  polynomials in double precision (unchanged to three digits on bases
  of 24 to 80).

The rows of the artifact also carry the two statements of the window at
``S = log 4`` itself — ``lambda_2(D) > |C_0|`` (the Hodge criterion of
``GoldenArchimedeanHodge``, inclusive of the right end of the window) and
the minimum with the pole positive — which the manuscript asserts in the
wording above rather than as figures; both are asserted here.
"""

from __future__ import annotations

import math
import re

import pytest

from oddzeta.harness import assert_close, read_salidas, read_tex

GOLDEN_TOL = 1e-12

_BRIDGES = "04-bridges.tex"


def _first_float(text: str, pattern: str, note: str) -> float:
    match = re.search(pattern, text, re.MULTILINE)
    assert match is not None, f"{note}: pattern not found in the artifact: {pattern!r}"
    return float(match.group(1))


@pytest.mark.golden
def test_arch_window_crossings_are_pinned() -> None:
    """The two crossings of the archimedean form are pinned with their condition.

    INV-WIT-001 §A5 site ``04:1179`` (arch_window.py): the artifact's
    measurements, the article's own rounded figures recorded beside them,
    and the sentence of 04-bridges that now prints the measurements with
    the basis they were measured on.
    """
    arch = read_salidas("arch_window.txt")
    tex = read_tex(_BRIDGES)

    # --- the artifact's digits -------------------------------------------
    c0 = _first_float(arch, r"^C_0 = (-?[\d.]+)", "arch_window C_0")
    assert_close(c0, -9.13493, GOLDEN_TOL, "arch_window C_0")

    without_pole = _first_float(
        arch,
        r"sin el polo: C_0 \+ D deja de ser positiva en S = ([\d.]+)",
        "arch_window crossing without the pole",
    )
    assert_close(without_pole, 0.453, GOLDEN_TOL, "arch_window crossing without the pole")

    criterion = _first_float(
        arch,
        r"segundo autovalor de D = \|C_0\| en S = ([\d.]+)",
        "arch_window crossing of the Hodge criterion",
    )
    assert_close(criterion, 1.647, GOLDEN_TOL, "arch_window crossing of the Hodge criterion")

    log4 = _first_float(arch, r"log 4 = ([\d.]+)", "arch_window log 4")
    assert_close(log4, math.log(4), 5e-4, "arch_window log 4")

    with_pole = _first_float(
        arch,
        r"C_0 \+ D \+ polo, positiva hasta S = ([\d.]+)",
        "arch_window crossing with the pole",
    )
    assert_close(with_pole, 1.545, GOLDEN_TOL, "arch_window crossing with the pole")

    # the run's own reconciliation record: what the article printed
    assert "(articulo ~0.45)" in arch, "arch_window.txt lost its 0.45 record"
    assert "(articulo ~1.65)" in arch, "arch_window.txt lost its 1.65 record"
    assert round(without_pole, 2) == 0.45, without_pole
    assert round(criterion, 2) == 1.65, criterion

    # --- the two window statements the sentence carries -------------------
    # both crossings bracket the prime-free window [0, log 4], which is
    # what "beyond the prime-free range" asserts
    assert without_pole < log4 < criterion, (
        f"the crossings {without_pole} / {criterion} do not bracket log 4 = {log4}"
    )

    row = re.search(r"^\s+1\.386\s+([\d.]+)\s+(-?[\d.]+)\s+([+-][\d.]+)", arch, re.MULTILINE)
    assert row is not None, "arch_window.txt lost the row at S = log 4"
    lam2, lowest_without_pole, lowest_with_pole = (float(group) for group in row.groups())
    # GoldenArchimedeanHodge at S = log 4: lambda_2(D) exceeds |C_0|
    assert lam2 > -c0, f"the Hodge criterion fails at log 4: lambda_2(D) = {lam2} <= |C_0| = {-c0}"
    assert_close(lam2, 9.498, GOLDEN_TOL, "arch_window lambda_2(D) at log 4")
    # and the pole carries the form there: the minimum stays positive
    assert lowest_with_pole > 0, f"the form with the pole is negative at log 4: {lowest_with_pole}"
    assert_close(lowest_with_pole, 0.0068, GOLDEN_TOL, "arch_window minimum with the pole")
    assert lowest_without_pole < 0, f"the form without the pole is positive at log 4: {lowest_without_pole}"

    # --- the manuscript's figures and their declared condition -------------
    claim = re.search(
        r"negative from support length \$([\d.]+)\$; with it, the pole removes the ground mode of "
        r"\$D\$, and\s+positivity asks that the second eigenvalue of \$D\$ exceed \$\|C_0\|\$, "
        r"which holds up to support length\s+\$([\d.]+)\$, beyond the prime-free range "
        r"\$\[0,\\log4\]\$",
        tex,
    )
    assert claim is not None, "the arch_window.py crossings of 04-bridges.tex not found"
    assert claim.group(1) == f"{without_pole:g}", (
        f"04-bridges.tex says {claim.group(1)}, arch_window.txt records {without_pole:g}"
    )
    assert claim.group(2) == f"{criterion:g}", (
        f"04-bridges.tex says {claim.group(2)}, arch_window.txt records {criterion:g}"
    )

    # the condition the sentence declares: the basis the crossings were measured on
    condition = re.search(
        r"both crossings are measured on a Galerkin basis\s+"
        r"of \$30\$ Legendre polynomials in double precision, "
        r"unchanged to three digits on bases of \$24\$ to \$80\$",
        tex,
    )
    assert condition is not None, "04-bridges.tex no longer declares the basis of the crossings"

    # C_0 is printed by the same paragraph and agrees with the artifact
    assert "du=-9.13493$" in tex, "04-bridges.tex no longer prints the artifact's C_0"
