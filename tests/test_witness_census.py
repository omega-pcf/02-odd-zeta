"""Contract between the manuscript's witness tags and the suite.

The manuscript marks a numerically verified claim with
``\\tier[\\testref{<id>}]{N}``, where ``<id>`` is a test of THIS suite: the
claim and its evidence are then the same string.  This module parses every
``\\testref{...}`` of main.tex and of the chapters it inputs, and pins the
contract:

* the cited set equals the pinned set exactly (a new citation lands together
  with its line here, and a dropped one cannot stay behind);
* every cited id exists in the suite as a node-id tail — the id is data, so
  it is read from a real ``--collect-only`` run, never from a docstring;
* every cited id is snake_case in English (the repository's naming
  standard), so a formula-style id cannot return.

The sixth mark carries two ids separated by ``, `` inside one bracket;
they are split here into the two citations they name.
"""

from __future__ import annotations

import re
import subprocess
import sys

import pytest

from oddzeta.harness import REPO_ROOT, TEX_SOURCES

_TESTREF = re.compile(r"\\testref\{([^}]*)\}")
_SNAKE_CASE = re.compile(r"^[a-z][a-z0-9_]*$")

# The witness ids the manuscript cites today (six marks, seven ids).
PINNED_CITED_IDS = (
    "test_l_one_chi5_digamma_value",
    "test_mersenne_bridge_phi_lambda_log_two",
    "test_phi_unit_norm_negative_one",
    "test_sigma_mu_polynomial_root_one_half",
    "test_sigma_mu_polynomial_root_three_halves",
    "test_two_cos_pi_over_five_equals_phi",
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
def test_cited_ids_are_snake_case() -> None:
    """Every cited id is snake_case in English (lowercase letters, digits, underscores)."""
    for citation in sorted(set(cited_ids())):
        assert _SNAKE_CASE.match(citation), f"cited id {citation!r} is not snake_case"
