"""Contract between the manuscript's witness tags and the suite.

The manuscript marks a numerically verified claim with
``\\witness[\\testref{<id>}]{N}``, where ``<id>`` is a test of THIS suite: the
claim and its evidence are then the same string.  ``\\witness`` is the single
name of the mark since the F1-A unification: one macro, one optional argument,
and the placement of the call in the source -- not the class -- picks the
inline or the own-line rendering (contract §6.12 S7).  This module parses every
``\\testref{...}`` of main.tex and of the chapters it inputs, and pins the
contract:

* the cited set equals the pinned set exactly (a new citation lands together
  with its line here, and a dropped one cannot stay behind);
* every cited id exists in the suite as a node-id tail — the id is data, so
  it is read from a real ``--collect-only`` run, never from a docstring;
* every cited id is snake_case in English (the repository's naming
  standard), so a formula-style id cannot return.

The sixth mark carries two ids separated by `,` inside one bracket;
they are split here into the two citations they name.

A second rule of the same contract (docs/witness-contract.md §6.5) is
measured here too, because it needs data that lives outside TeX: no part
of a ``\\witness[...]`` bracket may equal the id of a record of
``citation.csl.json``, nor carry a ``\\cite`` token.  The tag
macros read the bracket as an arbitrary string -- a character-shape test
rejects valid internal ids and cannot recognise a key -- so this suite is
the only place where the citation-key rule is measured.
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys

import pytest

from oddzeta.harness import REPO_ROOT, TEX_SOURCES

_TESTREF = re.compile(r"\\testref\{([^}]*)\}")
_SNAKE_CASE = re.compile(r"^[a-z][a-z0-9_]*$")

# The witness ids the manuscript cites today: forty-five marks, fifty-seven
# citations, forty-one distinct ids -- eleven ids are cited by two of the marks
# (test_mersenne_bridge_phi_lambda_log_two among them).  W5a added the eleven
# ids of the nine N claims whose script has a test in this suite (INV-WIT-001
# B2); W6 Fase A converted the twenty-five tested bare N marks of INV-WIT-001
# B8 and added their sixteen ids here, in the same commit that cites them.  The
# final editorial layer closed five bare marks (four with the id whose
# docstring cites that line, one on the certified-orbit figures), again in the
# same commit that cites them.
PINNED_CITED_IDS = (
    "test_additive_side_statistics_are_pinned",
    "test_angular_index_statistics_are_pinned",
    "test_castelnuovo_golden_values",
    "test_castelnuovo_matches_manuscript_claim",
    "test_castelnuovo_window_maxima",
    "test_circle_and_detect_golden_values",
    "test_circle_and_detect_matches_manuscript_claim",
    "test_corrected_operator_golden_values",
    "test_corrected_operator_matches_manuscript_claim",
    "test_delta_p_tower_ratios_are_pinned",
    "test_euler_link_second_term_is_pinned",
    "test_even_l_values_match_bernoulli_formula",
    "test_fejer_window_is_pinned",
    "test_fermat_quintic_point_counts_are_pinned",
    "test_field_signature_is_pinned",
    "test_five_valuation_of_the_cyclotomic_norms",
    "test_fluctuation_law_is_the_same_everywhere",
    "test_intersection_form_signature_is_pinned",
    "test_kisin_interpolation_is_pinned",
    "test_l_one_chi5_digamma_value",
    "test_law_resolution_golden_values",
    "test_law_resolution_matches_manuscript_claim",
    "test_mersenne_bridge_phi_lambda_log_two",
    "test_mersenne_bridge_s_bh_is_log_two",
    "test_offline_minimum_stays_positive",
    "test_orbit_balance_is_pinned",
    "test_orbita_cert_bounds_hold_for_chi5_and_the_quintic_layer",
    "test_phi_unit_norm_negative_one",
    "test_pythagoras_inequality_holds_at_every_measured_scale",
    "test_regulator_form_of_bridge_equals_l_one_form",
    "test_residual_scales_are_pinned",
    "test_sigma_mu_polynomial_root_one_half",
    "test_sigma_mu_polynomial_root_three_halves",
    "test_tstar_agrees_with_the_zeta_zero_ordinates",
    "test_two_cos_pi_over_five_equals_phi",
    "test_w3_orbita_fits_the_first_zero_height",
    "test_x_sweep_fejer_weight_is_minimal_at_the_printed_cutoff",
    "test_x_sweep_plain_sum_error_grows_past_the_smallest_cutoff",
    "test_zero_side_correction_matches_the_manuscript",
    "test_zeroside_orbit_agrees_with_the_zeros",
    "test_zeta_two_pi_squared_over_six",
)


def cited_ids() -> list[str]:
    """Every id inside a \\testref{...} of the manuscript, split per id."""
    ids: list[str] = []
    for source in TEX_SOURCES:
        text = source.read_text(encoding="utf-8")
        for argument in _TESTREF.findall(text):
            # The argument is written with \_ so the macro can allow a line
            # break: undo that escape to recover the node id.
            for part in argument.split(","):
                ids.append(part.strip().replace(r"\_", "_"))
    return ids


_NODE_IDS: list[str] | None = None


def node_ids() -> list[str]:
    """All node ids of the suite (one collect-only run, cached per session)."""
    global _NODE_IDS
    if _NODE_IDS is None:
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", "-q", "tests/", "-p", "no:cacheprovider"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=300,
        )
        assert proc.returncode == 0, proc.stdout + proc.stderr
        _NODE_IDS = [line.strip() for line in proc.stdout.splitlines() if line.startswith("tests/") and "::" in line]
        assert _NODE_IDS, f"no node ids collected:\n{proc.stdout}"
    return _NODE_IDS


@pytest.mark.witness
def test_cited_ids_match_the_pinned_set() -> None:
    """The manuscript's citations and the pinned set are the same set."""
    cited = sorted(set(cited_ids()))
    pinned = sorted(PINNED_CITED_IDS)
    missing_from_suite_side = [i for i in pinned if i not in cited]
    missing_from_tex_side = [i for i in cited if i not in pinned]
    assert cited == pinned, (
        "the cited set drifted from the pinned set; add the citation and its "
        f"line here in the same commit.  in the tex but not pinned: {missing_from_tex_side}; "
        f"pinned but not cited: {missing_from_suite_side}"
    )


@pytest.mark.witness
def test_every_cited_id_resolves_to_a_test() -> None:
    """Each cited id is the tail of a collected node id of the suite."""
    ids = node_ids()
    for citation in sorted(set(cited_ids())):
        matches = [i for i in ids if i.rsplit("::", 1)[1].split("[", 1)[0] == citation]
        assert matches, f"the manuscript cites {citation!r}, which no test of the suite defines"


@pytest.mark.witness
def test_the_self_baked_verification_script_is_gone() -> None:
    """The ported script was folded into this suite and did not survive.

    F10's contract: ``tests/verify_odd_zeta_pcf_unified.py`` no longer
    exists, and no module of ``tests/`` or ``scripts/`` imports it — the
    computation lives in the claim tests, the shared numbers in
    ``oddzeta.constants`` / ``oddzeta.harness``.
    """
    leftover = REPO_ROOT / "tests" / "verify_odd_zeta_pcf_unified.py"
    assert not leftover.exists(), f"{leftover.relative_to(REPO_ROOT)} still exists: the port is not closed"

    offenders: list[str] = []
    for directory in ("tests", "scripts"):
        for path in sorted((REPO_ROOT / directory).rglob("*.py")):
            if "__pycache__" in path.parts:
                continue
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    names = [alias.name for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and node.module:
                    names = [node.module]
                else:
                    continue
                for name in names:
                    if "verify_odd_zeta_pcf_unified" in name:
                        offenders.append(f"{path.relative_to(REPO_ROOT)} imports {name}")
    assert not offenders, "the eliminated script is imported again: " + "; ".join(offenders)


@pytest.mark.witness
def test_cited_ids_are_snake_case() -> None:
    """Every cited id is snake_case in English (lowercase letters, digits, underscores)."""
    for citation in sorted(set(cited_ids())):
        assert _SNAKE_CASE.match(citation), f"cited id {citation!r} is not snake_case"


# --------------------------------------------------------------------------
# The citation-key rule of the tag grammar (docs/witness-contract.md §6.5).
#
# The macro reads a bracket as an arbitrary string, so it cannot know
# whether a part is one of OUR ids or one of the BIBLIOGRAPHY's keys; the
# key set exists only outside TeX, so the rule is measured here, in the
# suite (a check that needs external data runs outside the typesetting).
# --------------------------------------------------------------------------

_TAG_SITE = re.compile(r"\\witness\s*\[")
_TESTREF_WRAPPED = re.compile(r"^\\testref\{(.*)\}$", re.DOTALL)
_KEYS: set[str] | None = None


def citation_keys() -> set[str]:
    """The documented citation keys of this repository (the CSL ``id`` field)."""
    global _KEYS
    if _KEYS is None:
        records = json.loads((REPO_ROOT / "citation.csl.json").read_text(encoding="utf-8"))
        _KEYS = {record["id"] for record in records}
    return _KEYS


def _read_group(text: str, start: int) -> tuple[str, int] | None:
    """The balanced ``{...}`` group that opens at ``start``; else ``None``."""
    if start >= len(text) or text[start] != "{":
        return None
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1 : index], index + 1
    return None


def _read_optional(text: str, start: int) -> tuple[str, int] | None:
    """The ``[...]`` optional argument that opens at ``start``, braces aware."""
    if start >= len(text) or text[start] != "[":
        return None
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
        elif text[index] == "]" and depth == 0:
            return text[start + 1 : index], index + 1
    return None


def tag_arguments(text: str) -> list[tuple[int, str, str]]:
    """``(line, macro, argument)`` for every ``\\witness[...]`` of the manuscript.

    A ``%`` before the site on its line comments it out in TeX, so such a
    site is not part of the manuscript and is not read as one here.  The mark
    has one name and one optional argument since F1-A: the ids sit in the
    brackets, the class in the braces, and no second body form exists.
    """
    sites: list[tuple[int, str, str]] = []
    for match in _TAG_SITE.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        if "%" in text[line_start : match.start()]:
            continue
        line = text.count("\n", 0, match.start()) + 1
        parsed = _read_optional(text, match.end() - 1)
        if parsed is None:
            continue
        sites.append((line, "witness", parsed[0]))
    return sites


def split_on_top_level_commas(argument: str) -> list[str]:
    """Split on the commas that sit OUTSIDE ``\\testref{...}`` (brace count)."""
    parts: list[str] = []
    depth, current = 0, []
    for char in argument:
        if char == "," and depth == 0:
            parts.append("".join(current))
            current = []
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        current.append(char)
    parts.append("".join(current))
    return parts


def without_testref(part: str) -> str:
    """Drop an outer ``\\testref{...}`` wrapper and the surrounding spaces."""
    stripped = part.strip()
    wrapped = _TESTREF_WRAPPED.match(stripped)
    return (wrapped.group(1) if wrapped else stripped).strip()


def citation_offenders(text: str, keys: set[str], label: str) -> list[str]:
    """One ``file:line`` row per part of a bracket that holds a citation key.

    Equality against the loaded key set decides -- never a character
    heuristic: a part equal to the id of a record of ``citation.csl.json``,
    or one carrying the ``\\cite`` token, is a violation.
    """
    offenders: list[str] = []
    for line, macro, argument in tag_arguments(text):
        for part in split_on_top_level_commas(argument):
            part = without_testref(part)
            if part in keys:
                offenders.append(
                    f"{label}:{line} \\{macro}: the part {part!r} is the id of a "
                    f"record of citation.csl.json"
                )
            elif "\\cite" in part:
                # the report stops at the token, so the message stays readable
                clipped = part[: part.index("\\cite") + len("\\cite")]
                offenders.append(
                    f"{label}:{line} \\{macro}: the part {clipped!r} carries the "
                    f"\\cite token (an external source is an adjacent \\cite)"
                )
    return offenders


@pytest.mark.witness
def test_no_citation_key_sits_inside_a_tag() -> None:
    """No part of any tag bracket equals a citation key or carries ``\\cite``.

    The corpus is every ``\\witness[...]`` of the manuscript, split on the commas that sit outside ``\\testref{...}``;
    the keys are the ids of ``citation.csl.json``.  The tag macro accepts an
    arbitrary string now, so this test -- not the macro -- is the whole of
    the citation-key rule (contract §6.5).
    """
    keys = citation_keys()
    assert keys, "citation.csl.json declares no id: the key set is empty"
    offenders: list[str] = []
    sites = 0
    for source in TEX_SOURCES:
        text = source.read_text(encoding="utf-8")
        sites += len(tag_arguments(text))
        offenders.extend(citation_offenders(text, keys, source.name))
    assert sites > 0, "the extractor found no tag argument: the pattern or the corpus broke"
    assert not offenders, (
        "a citation key (or a \\cite token) sits inside a tag: an external "
        "source stays an adjacent \\cite, never fused into the mark: "
        + "; ".join(offenders)
    )


@pytest.mark.witness
def test_the_tag_lint_catches_a_synthetic_insertion() -> None:
    """The rule is not vacuous: a key inserted into a bracket fails the check.

    the prototype that motivated the lint caught three rows against this
    repository's key set -- a bare key in a mark, the same key in a second
    mark after a comma, and the ``\\cite`` token the macro still rejects at
    run time -- and none over the real manuscript.
    half is pinned here on a synthetic manuscript, so a weakened extractor
    is loud instead of silently green.
    """
    keys = citation_keys()
    assert {"riemann1859", "montgomery73"} <= keys, "the fixture keys left citation.csl.json"
    synthetic = (
        "\\witness[riemann1859]{P}\n"
        "\\witness[montgomery73, a_valid_internal_id]{P}\n"
        "\\witness[\\cite{riemann1859}]{N}\n"
        "\\witness[\\testref{a_valid_id, other_valid_id}]{N}\n"
        "\\witness[a_valid_id]{N}\n"
    )
    offenders = citation_offenders(synthetic, keys, "synthetic.tex")
    assert len(offenders) == 3, offenders
    assert offenders[0].startswith("synthetic.tex:1"), offenders[0]
    assert any("montgomery73" in row for row in offenders), offenders
    assert any("\\cite" in row for row in offenders), offenders
    # the ids the character-shape grammar used to reject are not violations
    assert all("a_valid_id" not in row and "other_valid_id" not in row for row in offenders)
