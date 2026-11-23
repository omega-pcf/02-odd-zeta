"""Section "Mersenne bridge and localization at 2" (script sections 2.3, 3.6).

The bridge ``phi^{lambda_log} = 2`` with its exponent
``lambda_log = log(2)/log(phi)``, the primality reading of 2 (inert under
``chi5``), and the PCF mass ``M_PCF = 6*sqrt(3)*pi/log(phi)``.  The mass was
compared twice by the script (sections 2.3 and 3.6, same value, same
tolerance): one test now owns it.

Tolerances: the bridge is the script's ``1e-48``; the rest, its default
``1e-45``.
"""

from __future__ import annotations

import mpmath as mp

from oddzeta.constants import DEFAULT_TOL, LAMBDA_LOG, M_PCF, PHI
from oddzeta.harness import assert_close, chi5

# Reference values of the script (its sections 2.3 and 3.6).
_LAMBDA_LOG_REFERENCE = mp.mpf("1.4404200904125564790175514995878638024586041426841")
_M_PCF_REFERENCE = mp.mpf("67.84618925807164969673577804862763915006644544716")


def test_mersenne_bridge_phi_lambda_log_two() -> None:
    """phi^{lambda_log} = 2 with lambda_log = log(2)/log(phi).

    Witness id cited by ``src/chapters/03-mechanisms.tex``.
    Script tolerance for this check: 1e-48.
    """
    assert_close(PHI**LAMBDA_LOG, mp.mpf(2), mp.mpf("1e-48"), "Mersenne bridge")


def test_mersenne_exponent_matches_reference_value() -> None:
    """lambda_log = log(2)/log(phi) equals the reference value of the script."""
    assert_close(LAMBDA_LOG, _LAMBDA_LOG_REFERENCE, DEFAULT_TOL, "Mersenne bridge exponent")


def test_two_is_inert() -> None:
    """p = 2 is inert: chi5(2) = -1."""
    assert chi5(2) == -1, f"chi5(2) = {chi5(2):+d}, expected -1 (inert)"


def test_pcf_mass_matches_reference_value() -> None:
    """M_PCF = 6*sqrt(3)*pi/log(phi) equals the reference value of the script.

    Checked twice by the script (sections 2.3 and 3.6), identical value and
    tolerance; the port owns it once.
    """
    assert_close(M_PCF, _M_PCF_REFERENCE, DEFAULT_TOL, "PCF mass")
