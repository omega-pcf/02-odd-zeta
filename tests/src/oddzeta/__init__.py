"""Support package for the verification suite: shared constants and helpers.

``constants`` holds the closed forms the manuscript's numbers derive from;
``harness`` holds the generic helpers (characters, Euler products, the
single tolerance assertion, the artifact readers).  No module here asserts
anything — assertions belong to the tests.
"""

from oddzeta.constants import (
    DEFAULT_TOL,
    L_ONE_CHI5,
    LAMBDA_LOG,
    M_PCF,
    PHI,
    PHI_BAR,
    LOG_PHI,
    T,
)

__all__ = [
    "DEFAULT_TOL",
    "L_ONE_CHI5",
    "LAMBDA_LOG",
    "M_PCF",
    "PHI",
    "PHI_BAR",
    "LOG_PHI",
    "T",
]
