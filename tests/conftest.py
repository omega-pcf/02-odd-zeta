"""pytest configuration for the verification suite of the manuscript.

The support code lives in the importable package ``tests/src/oddzeta``
(``oddzeta.constants`` for the closed forms and shared numbers,
``oddzeta.harness`` for the generic helpers), reachable through the
``pythonpath`` entry of ``pyproject.toml``; each claim test owns the
computation that produces its numbers and asserts them directly — no test
imports a script and no module asserts itself.

The suite is headless and generates nothing: it verifies numbers and
committed artifacts only (the manuscript's figures do not belong to this
repository), so ``MPLBACKEND`` is forced to Agg before anything can import
pyplot.
"""

from __future__ import annotations

import os

os.environ.setdefault("MPLBACKEND", "Agg")
