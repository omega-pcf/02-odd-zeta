"""Closed forms and shared numbers of the manuscript (mpmath, 50 digits).

Every constant is defined exactly once here: the ported verification script
computed these expressions inline at each check, and a shared origin is what
keeps a later edit from making two tests disagree.

Working precision follows the script — ``mp.dps = 50`` — set at import so
every test of the suite evaluates at the precision the manuscript states
(``50-digit precision``).

Tolerances
----------
``DEFAULT_TOL`` is the script's own default (its ``check(...)`` helper
compared at ``1e-45``).  A test that needs a different tolerance states it
literally at the call site with a comment naming the script's value, so the
ported tolerance is auditable line by line: a number that fails is reported,
never made to pass by loosening a tolerance.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 50

# Golden ratio, its Galois conjugate and the quantities derived from them.
PHI = (1 + mp.sqrt(5)) / 2
PHI_BAR = -1 / PHI
LOG_PHI = mp.log(PHI)

# Torus period T = 2*pi*log(phi).
T = 2 * mp.pi * LOG_PHI

# Mersenne bridge exponent lambda_log = log(2)/log(phi): phi^lambda_log = 2.
LAMBDA_LOG = mp.log(2) / LOG_PHI

# PCF mass M_PCF = 6*sqrt(3)*pi/log(phi).
M_PCF = 6 * mp.sqrt(3) * mp.pi / LOG_PHI

# Class-number value L(1, chi5) = 2*log(phi)/sqrt(5) = T/(pi*sqrt(5)).
L_ONE_CHI5 = 2 * LOG_PHI / mp.sqrt(5)

# Regulator of Q(sqrt 5): R = log(phi) (the invariant of section "Props A, B, C").
R_REGULATOR = LOG_PHI

# The default comparison tolerance of the verification script this suite
# ported (its ``check`` helper compared at 1e-45 at 50 digits), inherited
# unchanged.
DEFAULT_TOL = mp.mpf("1e-45")
