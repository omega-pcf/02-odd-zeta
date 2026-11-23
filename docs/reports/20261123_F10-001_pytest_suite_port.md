# F10 — the self-baked verification script ported to a modular pytest suite

| Field | Value |
|---|---|
| **id** | `F10-001` |
| **title** | Port of `tests/verify_odd_zeta_pcf_unified.py` into a per-module pytest suite, its wiring, the six `N[]` witness tags and the golden observation outputs |
| **status** | applied |
| **date** | 2026-11-23 |
| **version** | 1.0 |

**Scope.** Repository `02-odd-zeta`, from the clean base `5ba9db9` through
the F10 wave: the suite under `tests/`, the `verify:py` wiring and the
deletion of the ported script, the six `N` witness tags of the manuscript
(ids only), the four committed observation outputs as golden artifacts, and
the suite's documentation with its generated counts. It deliberately does
not touch `lean/`, `.release-it.ts`, `docs/usage.md`, `citation.csl.json`,
nor any prose outside the ids inside `N[\ldots]` (§8, laguna 1, records the
one stale sentence that decision leaves behind).

## 1. Before / after

| | before | after |
|---|---|---|
| shape | one 904-line script, module-level flow, `print`-based verdicts | 13 test modules + `conftest.py` + support package `tests/src/oddzeta` (`constants.py`, `harness.py`) |
| assertions | 110 `check(...)` call sites (109 distinct labels) + 9 print-verdict loops + INFO prints | 94 tests: 81 claim tests, 9 golden tests, 4 contract tests (`tests/test_witness_census.py`) |
| entrypoint | `pnpm run verify:py` = `uv run python tests/verify_odd_zeta_pcf_unified.py` | `pnpm run verify:py` = `uv run pytest tests/ -q -m 'not slow'` (through `verify`, so `validate` runs the suite) |
| contract | a printed `RESULT: ALL CHECKS PASSED` summary | pytest assertions with the failing gap in the message; the manuscript's ids resolve to collected node ids |

A test aggregates what the script expressed as several `check` calls
(a loop over primes is one citable node), so the two columns are not a
1:1 count: every surviving check is asserted, and the merges and drops are
listed in §3 and §4.

| module | script sections ported | tests |
|---|---|---:|
| `test_pcf_ring_definitions.py` | 2, 2.1, 3.6.1 | 10 |
| `test_frobenius_lifts.py` | 2.2 (+ Λ-ring, Borger criterion 3) | 5 |
| `test_mersenne_bridge.py` | 2.3, 3.6 | 4 |
| `test_euler_products.py` | 3.1, 3.2 | 1 |
| `test_l_function_values.py` | 3.3, 3.4, 3.5 (pentagon) | 10 |
| `test_odd_zeta_determination.py` | 3.5 (odd values), 6 | 3 |
| `test_regulator_invariant.py` | 4, 4.3 (Props A, B, C) | 12 |
| `test_spectral_structure.py` | 4.7 | 17 |
| `test_weil_analogy.py` | 5.8 | 3 |
| `test_categorical_formalism.py` | 5 (+ F1-descent functoriality) | 8 |
| `test_polylog_circuit.py` | 5.9 | 8 |
| `test_golden_observations.py` | the four `hipotesis/pruebas/salidas` outputs | 9 |
| `test_witness_census.py` | manuscript ↔ suite contract, port guard | 4 |

## 2. Tolerances (inherited, never loosened)

`DEFAULT_TOL = 1e-45` (the script's own `check` default at `mp.dps = 50`)
unless the call site states otherwise: `1e-48` wherever the Mersenne
exponent appears, `1e-50` / `1e-49` for the Gauss logarithmic and digamma
sums, `1e-44` for the Bernoulli, Gauss-sum, Baker and Fourier comparisons,
`1e-30` for the Dedekind-eta product and the polylog series, `1e-14` for
the digamma class-number formula, `1e-12 … 5e-4` per `s` for the Euler
products (section 3.1's values kept where the sections overlap),
`1e-5` for the Euler quotients, `1e-3` for the 25-prime colimit, `1e-40` /
`1e-30` per pair for functoriality. The golden artifacts pin their
committed digits at `1e-12`; the manuscript figures are reconciled at half
of the last digit each sentence prints.

## 3. Merges — exact duplicates owned by one test

1. `M_PCF` (script sections 2.3 and 3.6, the only literally repeated
   label) → `test_pcf_mass_matches_reference_value`.
2. The Fibonacci congruence `chi5(p) = F_p mod p`, stated as the section
   2.2 sweep, the Λ-ring loop and Borger criterion 3 → one test over
   `[3, 60)`, which contains both explicit lists.
3. `lambda_log*R = log 2` (Prop A (iii) and Prop B) →
   `test_regulator_times_mersenne_exponent_is_log_two`.
4. `L(1, chi5)` through digamma (sections 3.3 and 3.5) →
   `test_l_one_chi5_digamma_value`.
5. `T/(pi*sqrt(5)) = L(1, chi5)` (sections 3.3 and 3.6) →
   `test_l_one_matches_t_over_pi_sqrt_five`.
6. The odd-zeta Euler quotient (section 3.5 `k = 1..5`, section 6
   `k = 1..4`) → `test_odd_zeta_values_from_euler_product` over the union.
7. Euler product vs `zeta(s)*L(s, chi5)` (sections 3.1 and 3.2) →
   `test_euler_product_matches_zeta_times_l`, keeping the STRICTER
   tolerance at each `s`.
8. Functoriality (section 5's five pairs at `1e-40`, the F1-descent block's
   nine pairs at `1e-30`) → `test_frobenius_functoriality_adds_exponents`
   with the tolerance of each pair's own site.
9. `|omega^k/2| = 1/2` (sections 4.7 and 5.8) →
   `test_eigenvalue_moduli_are_one_half`.
10. The character-product check printed by the fibre loop of section 5
    (χ₄·χ₅ = χ₄χ₅) → the character-group test.

## 4. Drops and strengthenings

Dropped — a check that compares an expression with itself or an assignment
read back (the family's tautology class), with the claim it stood for
asserted elsewhere:

| dropped | where the claim still lives |
|---|---|
| the four η components of section 5 (`zeta*L` against the identical expression for ℚ, ℚ(√5), ℚ(i), ℚ(−5)) | the non-trivial instance `ζ_{Q(√5)} = ζ·L(s, χ5)` is asserted by `test_euler_product_matches_zeta_times_l` |
| the co-determination arithmetic branch (a `zeta_K(3)` the script defined as `zeta(3)*L(3, chi5)`, divided back by `L`) | `test_odd_zeta_values_from_euler_product`, `test_euler_colimit_converges_at_three` |
| `i^2 = -1` compared with `-1`, `phi` compared with its own definition | no content (arithmetic/definitional identity) |
| `ell = 1` and `G_N = mu_3` assignments read back | stated in `test_brown_henneaux_central_charge_is_three`'s docstring, which computes `c = 3ell/(2G_N)` |
| section 5.8's "exponent 2" identity `(g + g) mod 2 = 0` | `test_character_group_is_exponent_two` (χ₄² = χ₅² = (χ₄χ₅)² = 1) |

Strengthened — reported because the port asserts more than the script did:

* the S-duality fixed point: the script compared the real part of
  `-1/i - i` only; the port asserts the full complex difference;
* `mu_3 = 1/|ker G|`: the script assigned `1/2`; the port computes the
  kernel from the character table (units 1 and 9) and then `1/|ker G|`;
* the map `G = (chi4, chi5)`: the script's membership test could not fail
  (a Kronecker symbol always lies in `{-1,0,1}`); the port asserts the
  non-vanishing on the units, which is what makes the image `Z2 x Z2`;
* the script's bare `assert` on the unique positive real eigenvalue became
  an assertion with the failing list in the message.

## 5. The `N[\ldots]` tags: seven ids, six marks

| site | before | after |
|---|---|---|
| `02-foundations.tex:7` | `a_{0,0} = zeta(2) = pi^2/6` | `test_zeta_two_pi_squared_over_six` |
| `02-foundations.tex:415` | `N(phi) = phi * phi_bar = -1  (unit of norm -1)` | `test_phi_unit_norm_negative_one` |
| `03-mechanisms.tex:103` | `2*cos(pi/5) = phi` | `test_two_cos_pi_over_five_equals_phi` |
| `03-mechanisms.tex:2152` | `L(1,chi5) via digamma = 2*log(phi)/sqrt(5)` | `test_l_one_chi5_digamma_value` |
| `03-mechanisms.tex:2899` | `Mersenne bridge: phi^{lambda_log} = 2` | `test_mersenne_bridge_phi_lambda_log_two` |
| `04-bridges.tex:232` (two ids) | `Root 1 = 3/2, Root 2 = 1/2` | `test_sigma_mu_polynomial_root_three_halves, test_sigma_mu_polynomial_root_one_half` |

**Reported deviation from FTI-001 §7.3.** Each id is the §7.3 proposal for
its site with the pytest node prefix `test_` added: the manuscript cites the
node-id tail, so the id has to be what `pytest --collect-only -q` prints
(the same convention as the siblings' manuscripts, whose `\testref` ids all
carry the prefix); §7.3's proposals predate the suite and named the check
labels of the script. The underscores are written `\_` as the `\testref`
macro requires, and the census undoes that escape before matching. Nothing
outside the ids changed at these six sites.

`tests/test_witness_census.py` polices the contract in the same commit as
the retargeting: exact equality of the cited set against the pinned set,
resolution of every id against a real `--collect-only` run, the snake_case
standard, and the guard that the ported script is absent and unimported
(AST sweep over `tests/` and `scripts/`).

## 6. The four golden observation outputs

Nothing is recomputed — the heavy scripts stay outside the suite and the
committed artifact under `hipotesis/pruebas/salidas` is the record of the
run (marker `golden`).

| observation | golden values pinned | manuscript figures reconciled (`04-bridges.tex`) |
|---|---|---|
| `castelnuovo.txt` | 1.2674 (χ₄), 1.2782 (χ₅), 2.2127 (χ₂₀), 0.7815 (worst fibre) | below 1.27 / 1.28 / 2.22, at most 0.79√x (strict bounds) |
| `corrected_operator.txt` | 0.212 mean, 0.186 median (n ≤ 1000, exact envelope) | 0.21 spacings, median 0.19 |
| `law_resolution.txt` | fixed-window medians 0.194, 0.170, 0.089, 0.041, 0.025 at δ = 1e-2 … 1e-4 | 0.183, 0.087, 0.053, 0.028, 0.023 against 0.20 and 0.020 — the reference (`articulo`) row of the same artifact |
| `circle_and_detect.txt` | 0.1010 (γ = 30), 0.3840 (γ = 100); s_max = 120 row 0.001, 0.009, 0.022, 0.028; minima 1.2e-04 (ζ) … 0.032 (χ₂₀) | δ ≥ 0.10 / 0.38; thresholds 0.001, 0.009, 0.022, 0.028 at γ = 30, 100, 200, 300; minima from 1.2·10⁻⁴ to 0.032 |

The `law_resolution` reconciliation is worth the author's eye (§8, laguna
6): the five figures the sentence prints are the artifact's own reference
row, not the computed window medians the golden test pins.

## 7. Gates

Measured after the F10 content commits (`6835d17`), all exit 0:

| gate | result |
|---|---|
| `uv run pytest tests/ -q` | `94 passed in 1.57s` |
| `pnpm run selfcitations:check` | `✓ README.md regions match … main.tex carries the clean vX.Y.Z token … inside \texttt{…}` |
| `pnpm run counts:check` | `✓ 3 marked region(s) and docs/counts.md match … (pytest.collected=94, pytest.not_slow=94, lean.theorems=5712, lean.axioms=0, lean.sorry=0, images.files=0)` |
| `pnpm run manifest:check` | `✓ 21 shared files match scripts/shared-files.json (sha256); 9 documented exclusions` |
| `pnpm run type-check` | `tsc --noEmit`, no diagnostics |
| `pnpm run build` | `✅ Build completed successfully for v1.7.2`, `build/document-v1.7.2.pdf` (167 pages), log: 0 undefined references, 0 undefined citations, no tier package errors, no new overfull box at the six retargeted sites |
| `pnpm run validate` | `exit 0` — selfcitations ✓ · parity ✓ · counts ✓ · manifest ✓ · verify:py `94 passed` · `lake build` **18248 jobs, success** · tsc ✓ |
| `pdftotext build/document-v1.7.2.pdf` | the six `N[…]` marks print the seven new ids (an id may break at an underscore — the macro's `\brk@us` allows it by design) |

`counts:check` probes: the counters were added in this wave (§1); editing a
region's number makes `counts:check` fail with the diff and restoring it
brings exit 0 back — the observed values above are a real run's.

## 8. Lagunas

1. **One stale caption names the deleted script.**
   `src/chapters/03-mechanisms.tex` (caption of `tab:zeta-values`) still
   says *"numerical entries are verified at 50-digit precision (see
   companion verification script `verify_odd_zeta_pcf_unified.py`)"* while
   F10 deleted that file. Prose was out of this task's scope (only the ids
   inside `N[…]` were to be touched), so the sentence is left as it stands;
   the fix is one clause pointing at the suite (`tests/`, run with
   `pnpm run verify:py`) and needs the manuscript owner's go.
2. `docs/usage.md` §Counts still says this repository's "manuscript carries
   no `\testref{...}` anchor" — true when it was written, false since
   F8-001 (six marks); `docs/usage.md` is outside this task's scope.
3. FTI-001 §7.3's ids were proposals for a script-shaped world (§5 reports
   the `test_` prefix that the pytest node id adds).
4. FTI-001 §9.1 (F8-001 has no row in the reports index) remains open —
   this deliverable adds its own row only.
5. The 46 bare `N` marks and the 15 `Nc` rows of FTI-001 stay unanchored:
   F10 supplied ids only for the marks that already carried them; the
   `Nc → N[ids]` destinations of §7.2 are F11's, and no
   error-accounting test exists for them yet.
6. `law_resolution` pairing (§6): the manuscript's five numbers equal the
   artifact's reference row rather than any computed row of that file; the
   suite pins both, so a change to either side fails loudly, but the
   sentence's tie to the script deserves a read.
7. No test carries the `slow` marker yet (94/94 run under `-m 'not slow'`);
   the marker and `pyproject.toml` wiring exist for the day a test passes
   10 s. `package.json` declares no `test` key (`parity.ts` does not
   require one); the full run is `uv run pytest tests/ -q`.

---

## Related documents

- `tests/README.md` — the suite's reader-facing document (command, layout,
  markers, tolerances, golden artifacts).
- `docs/reports/20261122_FTI-001_tier_uses_migration_map.md` — §7.3, the
  rename inventory this wave applied.
- `docs/reports/20261122_F8-001_witness_reconciliation.md` — the six
  marks and seven ids as first introduced.
- `docs/witness-contract.md` — why the `N` device exists.
- `docs/counts.md` — the ledger the suite's counters feed.
