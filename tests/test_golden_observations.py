"""Golden values of the four observations the manuscript cites by script name.

Each observation has a committed output under ``hipotesis/pruebas/salidas``
(the corpus the author's pass shipped); the tests here PIN those artifacts
against the golden numbers and reconcile them with the figures the
manuscript prints for the same script.  Nothing is recomputed: the heavy
scripts stay out of the suite (the artifact is the record of the run), so a
regenerated or edited output fails loudly instead of drifting the paper.

Two tolerances, both documented:

* ``GOLDEN_TOL`` (1e-12) pins a parsed value far below the four decimals
  the artifacts print — a golden comparison, not a rounding band: any change
  in the artifact's digits fails;
* ``assert_printed_as_in_manuscript`` allows half of the last digit the
  MANUSCRIPT prints (5% of the value), which is what "the paper rounds this
  run to 0.21 / 1.27 / 1.2e-4" means.

Reconciliation source: ``src/chapters/04-bridges.tex`` cites each script by
name beside its numbers (castelnuovo, corrected_operator, law_resolution,
circle_and_detect).
"""

from __future__ import annotations

import re

import pytest

from oddzeta.harness import SALIDAS_DIR, assert_close, read_salidas, read_tex

GOLDEN_TOL = 1e-12
_BRIDGES_TEX = "04-bridges.tex"


def assert_printed_as_in_manuscript(value: float, printed: float, note: str) -> None:
    """The artifact value must round to the manuscript's figure.

    ``printed`` is what the manuscript prints; the margin is half of its
    last significant digit (5% of the value), which is the precision the
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
# Observation 1: castelnuovo.txt — character and fibre bounds of |psi|/sqrt(x)
# ---------------------------------------------------------------------------

def _castelnuovo_values() -> dict[str, float]:
    text = read_salidas("castelnuovo.txt")
    return {
        "chi_4": _first_float(text, r"^chi_4\s*:.*?=\s*([\d.]+);", "castelnuovo chi_4"),
        "chi_5": _first_float(text, r"^chi_5\s*:.*?=\s*([\d.]+);", "castelnuovo chi_5"),
        "chi_20": _first_float(text, r"^chi_20\s*:.*?=\s*([\d.]+);", "castelnuovo chi_20"),
        "worst_fibre": _first_float(text, r"^peor fibra:\s*([\d.]+)", "castelnuovo worst fibre"),
    }


@pytest.mark.golden
def test_castelnuovo_golden_values() -> None:
    """The committed castelnuovo output pins 1.2674 / 1.2782 / 2.2127 / 0.7815."""
    values = _castelnuovo_values()
    expected = {"chi_4": 1.2674, "chi_5": 1.2782, "chi_20": 2.2127, "worst_fibre": 0.7815}
    for key, want in expected.items():
        assert_close(values[key], want, GOLDEN_TOL, f"castelnuovo {key}")


@pytest.mark.golden
def test_castelnuovo_matches_manuscript_claim() -> None:
    """The manuscript's bounds for the same run: below 1.27 / 1.28 / 2.22 and
    at most 0.79*sqrt(x) for the worst fibre."""
    values = _castelnuovo_values()
    text = read_tex(_BRIDGES_TEX)

    below = re.search(r"stays below \$([\d.]+)\$, \$([\d.]+)\$ and \$([\d.]+)\$", text)
    assert below is not None, "castelnuovo claim not found in 04-bridges.tex"
    for key, bound in zip(("chi_4", "chi_5", "chi_20"), map(float, below.groups()), strict=True):
        assert values[key] < bound, (
            f"castelnuovo {key} = {values[key]} does not stay below the manuscript's {bound}"
        )

    at_most = re.search(r"at most \$([\d.]+)\\sqrt", text)
    assert at_most is not None, "castelnuovo fibre bound not found in 04-bridges.tex"
    bound = float(at_most.group(1))
    assert values["worst_fibre"] <= bound, (
        f"worst fibre {values['worst_fibre']} exceeds the manuscript's at most {bound}"
    )


# ---------------------------------------------------------------------------
# Observation 2: corrected_operator.txt — T* and the exact envelope
# ---------------------------------------------------------------------------

def _corrected_operator_values() -> dict[str, float]:
    text = read_salidas("corrected_operator.txt")
    match = re.search(
        r"^n = 1\.\.1000:.*?envolvente exacta: media ([\d.]+), mediana ([\d.]+)",
        text,
        re.MULTILINE,
    )
    assert match is not None, "corrected_operator envelope row for n = 1..1000 not found"
    return {"envelope_mean": float(match.group(1)), "envelope_median": float(match.group(2))}


@pytest.mark.golden
def test_corrected_operator_golden_values() -> None:
    """The committed corrected_operator output pins the n = 1..1000 envelope
    mean 0.212 and median 0.186 (spacings)."""
    values = _corrected_operator_values()
    assert_close(values["envelope_mean"], 0.212, GOLDEN_TOL, "envelope mean")
    assert_close(values["envelope_median"], 0.186, GOLDEN_TOL, "envelope median")


@pytest.mark.golden
def test_corrected_operator_matches_manuscript_claim() -> None:
    """The manuscript prints the same run as 0.21 spacings with median 0.19."""
    values = _corrected_operator_values()
    text = read_tex(_BRIDGES_TEX)
    claim = re.search(r"it is \$([\d.]+)\$\s*spacings.*?median is \$([\d.]+)\$", text, re.DOTALL)
    assert claim is not None, "corrected_operator claim not found in 04-bridges.tex"
    assert_printed_as_in_manuscript(values["envelope_mean"], float(claim.group(1)), "envelope mean")
    assert_printed_as_in_manuscript(values["envelope_median"], float(claim.group(2)), "envelope median")


# ---------------------------------------------------------------------------
# Observation 3: law_resolution.txt — the law's windows
# ---------------------------------------------------------------------------

# The five window widths the law is resolved at (script and manuscript).
_DELTAS = (1e-2, 3e-3, 1e-3, 3e-4, 1e-4)


def _law_resolution_values():
    text = read_salidas("law_resolution.txt")
    block = re.search(
        r"ley por ventanas \(rejilla fija, promedio en la ventana\), X = 500:\n"
        r"\s*delta\s+[^\n]*\n\s*mediana\s+([^\n]*)",
        text,
    )
    assert block is not None, "law_resolution fixed-window block for X = 500 not found"
    medians = tuple(float(v) for v in block.group(1).split())

    article = re.search(
        r"^articulo: ([\d.]+), ([\d.]+), ([\d.]+), ([\d.]+), ([\d.]+); "
        r"sin correccion ([\d.]+); primo por primo ([\d.]+)",
        text,
        re.MULTILINE,
    )
    assert article is not None, "law_resolution reference row not found"
    reference = re.search(
        r"^X = 500: sin correccion mediana ([\d.]+) \(media [\d.]+\);"
        r"\s+primo por primo mediana ([\d.]+) \(media [\d.]+\)",
        text,
        re.MULTILINE,
    )
    assert reference is not None, "law_resolution reference line for X = 500 not found"
    return {
        "medians": medians,
        "article": tuple(float(v) for v in article.groups()[:5]),
        "uncorrected": float(article.group(6)),
        "prime_by_prime": float(article.group(7)),
        "uncorrected_median": float(reference.group(1)),
        "prime_by_prime_median": float(reference.group(2)),
    }


@pytest.mark.golden
def test_law_resolution_golden_values() -> None:
    """The committed law_resolution output pins the fixed-window medians
    0.194, 0.170, 0.089, 0.041, 0.025 at delta = 1e-2 .. 1e-4 (X = 500)."""
    medians = _law_resolution_values()["medians"]
    expected = (0.194, 0.170, 0.089, 0.041, 0.025)
    assert len(medians) == len(expected), f"expected {len(expected)} medians, artifact has {len(medians)}"
    for delta, got, want in zip(_DELTAS, medians, expected, strict=True):
        assert_close(got, want, GOLDEN_TOL, f"law_resolution median at delta = {delta:g}")


@pytest.mark.golden
def test_law_resolution_matches_manuscript_claim() -> None:
    """The manuscript's five figures for law_resolution.py (0.194, 0.170,
    0.089, 0.041 and 0.025 against 0.20 uncorrected and 0.021 prime by
    prime) are the fixed-window medians of the committed output, printed
    at the same precision."""
    values = _law_resolution_values()
    text = read_tex(_BRIDGES_TEX)

    start = text.find("the median error of the corrected operator")
    assert start != -1, "law_resolution claim not found in 04-bridges.tex"
    # Skip the window "(n = 100 to 3000)": its figure is a count, not a result.
    start = text.find(") is ", start)
    assert start != -1, "law_resolution claim has no result clause"
    start += len(") is ")
    end = text.find("prime by prime", start)
    assert end != -1, "law_resolution claim has no end in 04-bridges.tex"
    # Plain decimals inside the sentence: the delta figures are written as
    # $\delta=10^{-2}$ / $3\cdot10^{-3}$ and do not match this pattern.
    quoted = [float(v) for v in re.findall(r"\$([\d.]+)\$", text[start:end])]
    assert len(quoted) == 7, f"expected 7 figures in the law_resolution sentence, found {quoted}"

    for delta, got, want in zip(_DELTAS, values["medians"], quoted[:5], strict=True):
        assert_printed_as_in_manuscript(got, want, f"law_resolution median at delta = {delta:g}")
    assert_printed_as_in_manuscript(values["uncorrected_median"], quoted[5], "law_resolution uncorrected")
    assert_printed_as_in_manuscript(
        values["prime_by_prime_median"], quoted[6], "law_resolution prime by prime"
    )


# ---------------------------------------------------------------------------
# Observation 4: circle_and_detect.txt — Fejer minima and detectable delta
# ---------------------------------------------------------------------------

def _circle_and_detect_values():
    text = read_salidas("circle_and_detect.txt")
    minima = re.search(r"de ([\d.eE+-]+) \(zeta\) a ([\d.]+) \(chi_20\)", text)
    assert minima is not None, "circle_and_detect minima summary not found"
    thresholds = {}
    for gamma in (30, 100):
        match = re.search(rf"gamma ~ {gamma} \([^)]*\): delta >= ([\d.]+)", text)
        assert match is not None, f"circle_and_detect threshold at gamma = {gamma} not found"
        thresholds[gamma] = float(match.group(1))
    table = re.search(
        r"s_max =\s+120: gamma~30: ([\d.]+), gamma~100: ([\d.]+), "
        r"gamma~200: ([\d.]+), gamma~300: ([\d.]+)",
        text,
    )
    assert table is not None, "circle_and_detect s_max = 120 row not found"
    return {
        "min_zeta": float(minima.group(1)),
        "min_chi20": float(minima.group(2)),
        "thresholds": thresholds,
        "s_max_120": tuple(float(v) for v in table.groups()),
    }


@pytest.mark.golden
def test_circle_and_detect_golden_values() -> None:
    """The committed circle_and_detect output pins the detectable delta
    0.1010 (gamma = 30) and 0.3840 (gamma = 100), and the s_max = 120 row
    0.001 / 0.009 / 0.022 / 0.028."""
    values = _circle_and_detect_values()
    assert_close(values["thresholds"][30], 0.1010, GOLDEN_TOL, "delta threshold at gamma = 30")
    assert_close(values["thresholds"][100], 0.3840, GOLDEN_TOL, "delta threshold at gamma = 100")
    expected_row = (0.001, 0.009, 0.022, 0.028)
    assert len(values["s_max_120"]) == len(expected_row)
    for gamma, got, want in zip((30, 100, 200, 300), values["s_max_120"], expected_row, strict=True):
        assert_close(got, want, GOLDEN_TOL, f"threshold at gamma = {gamma} (s_max = 120)")


@pytest.mark.golden
def test_circle_and_detect_matches_manuscript_claim() -> None:
    """The manuscript prints the same run: minima from 1.2e-4 (zeta) to 0.032
    (chi_20), detection from delta >= 0.10 at gamma = 30 and >= 0.38 at
    gamma = 100, and the four thresholds 0.001 / 0.009 / 0.022 / 0.028 for
    k*log p <= 120."""
    values = _circle_and_detect_values()
    text = read_tex(_BRIDGES_TEX)

    minima = re.search(
        r"minima from \$([\d.]+)(?:\\cdot10\^\{(-?\d+)\})?\$ \(\$\\zeta\$\) "
        r"to \$([\d.]+)\$ \(\$\\chi_\{20\}\$\)",
        text,
    )
    assert minima is not None, "circle_and_detect minima claim not found in 04-bridges.tex"
    mantissa = float(minima.group(1))
    zeta_min = mantissa * 10 ** int(minima.group(2)) if minima.group(2) else mantissa
    assert_printed_as_in_manuscript(values["min_zeta"], zeta_min, "Fejer minimum at zeta")
    assert_printed_as_in_manuscript(values["min_chi20"], float(minima.group(3)), "Fejer minimum at chi_20")

    detection = re.search(
        r"\$\\delta\\ge([\d.]+)\$ at \$\\gamma=30\$ and \$\\delta\\ge([\d.]+)\$ at \$\\gamma=100\$",
        text,
    )
    assert detection is not None, "circle_and_detect detection claim not found in 04-bridges.tex"
    assert_printed_as_in_manuscript(values["thresholds"][30], float(detection.group(1)), "detection at gamma = 30")
    assert_printed_as_in_manuscript(values["thresholds"][100], float(detection.group(2)), "detection at gamma = 100")

    row = re.search(
        r"thresholds fall to \$([\d.]+)\$, \$([\d.]+)\$, \$([\d.]+)\$\s*and \$([\d.]+)\$",
        text,
    )
    assert row is not None, "circle_and_detect threshold row not found in 04-bridges.tex"
    for gamma, got, want in zip((30, 100, 200, 300), values["s_max_120"], map(float, row.groups()), strict=True):
        assert_printed_as_in_manuscript(got, want, f"threshold at gamma = {gamma} (s_max = 120)")


def test_observations_dir_is_the_committed_corpus() -> None:
    """The four observation outputs exist where the suite reads them."""
    for name in ("castelnuovo.txt", "corrected_operator.txt", "law_resolution.txt", "circle_and_detect.txt"):
        assert (SALIDAS_DIR / name).is_file(), f"missing observation output: {name}"
