# Tests for the note (package `oddzeta`)

The suite lives in `tests/`; its support code lives in the importable
package `tests/src/oddzeta` — `oddzeta.constants` (the closed forms the
manuscript derives from: `PHI`, `T`, `LAMBDA_LOG`, `L_ONE_CHI5`, the
regulator, and `DEFAULT_TOL`) and `oddzeta.harness` (the characters `chi5`
and `chi4`, the Dirichlet L-values, the Euler products, the ONE tolerance
assertion, and the readers for the committed artifacts). There is no
computation module: each claim test owns the code that produces its numbers
and asserts them directly — values, never printed stdout.

`main.tex` and the chapters it inputs cite the tests that check their
numbers with `\testref{...}` (six `N` marks, seven ids), which
`tests/test_witness_census.py` parses to prove that every reference the
manuscript makes exists in the suite, that the cited set equals the pinned
set, and that every id is snake_case. The same file holds the guard that
closes the port of the self-baked verification script: the script must not
exist, and no module of `tests/` or `scripts/` may import it (AST sweep).

```bash
# counts:begin id="commands"
uv run pytest tests/ -q                 # whole suite   (113 tests)
uv run pytest tests/ -q -m 'not slow'   # without >10 s (113 tests)
# counts:end id="commands"
pnpm run verify:py                      # the same gate through package.json
```

The pytest configuration lives in `pyproject.toml` under
`[tool.pytest.ini_options]` (`testpaths`, `pythonpath`, `markers`,
`addopts`), so a bare `uv run pytest` collects the same
<!-- counts:begin id="suite-total" -->113<!-- counts:end id="suite-total" -->
tests as `uv run pytest tests/ -q`, and
<!-- counts:begin id="suite-not-slow" -->113<!-- counts:end id="suite-not-slow" -->
of them carry no `slow` mark. The numbers in those two spans are generated
from a real run by `pnpm run counts`; `pnpm run counts:check` (inside
`validate`) fails when they drift.

## Layout

```
tests/
├── conftest.py                     # headless suite (Agg), no fixtures
├── src/oddzeta/
│   ├── __init__.py                 # re-exports of the shared constants
│   ├── constants.py                # PHI, PHI_BAR, LOG_PHI, T, LAMBDA_LOG,
│   │                               # M_PCF, L_ONE_CHI5, R_REGULATOR, DEFAULT_TOL
│   └── harness.py                  # chi5/chi4/fib, L-values, Euler products,
│                                   # assert_close, artifact readers, REPO_ROOT
├── test_pcf_ring_definitions.py    # sections 2, 2.1, 3.6.1
├── test_frobenius_lifts.py         # section 2.2 (+ Lambda-ring, Borger criterion 3)
├── test_mersenne_bridge.py         # sections 2.3, 3.6
├── test_euler_products.py          # sections 3.1, 3.2
├── test_l_function_values.py       # sections 3.3, 3.4, 3.5 (pentagon)
├── test_odd_zeta_determination.py  # section 3.5 (odd values), section 6
├── test_regulator_invariant.py     # sections 4, 4.3 (Props A, B, C)
├── test_spectral_structure.py      # section 4.7
├── test_weil_analogy.py            # section 5.8
├── test_categorical_formalism.py   # section 5 (+ F1-descent functoriality)
├── test_polylog_circuit.py         # section 5.9
├── test_golden_observations.py     # the four committed observation outputs
├── test_golden_n_marks.py          # the INV-WIT-001 §B N marks: their outputs
├── test_arch_window.py             # arch_window.py: the archimedean crossings
└── test_witness_census.py          # \testref <-> suite contract, port guard
```

## Markers

| marker | meaning |
|---|---|
| `slow` | takes more than ~10 s; `verify:py` runs `-m 'not slow'`, the full run is `uv run pytest tests/ -q` |
| `golden` | compares a committed output under `hipotesis/pruebas/salidas` (pinned artifact, nothing recomputed) |
| `witness` | contract test between the manuscript's `\testref` tags and the suite |

## Tolerances

Every comparison inherits the tolerance of the check it ports: `DEFAULT_TOL`
(`1e-45` at the working precision of 50 digits) unless the call site says
otherwise, with `1e-48` wherever the Mersenne exponent appears, `1e-50` /
`1e-49` for the logarithmic and digamma sums, `1e-44` for the Bernoulli,
Gauss and Fourier comparisons, `1e-30` for the eta product and the polylog
series, the per-`s` Euler tolerances `5e-4 … 1e-12`, and `1e-5` for the
Euler quotients. A number that fails is reported with its gap; a tolerance
is never loosened to make it pass. The golden artifacts pin their committed
digits at `1e-12` (far below the four decimals the files print), and the
manuscript figures are reconciled at the precision those sentences claim
(half of their last printed digit).

## The golden artifacts

`tests/test_golden_observations.py` reads the four observation outputs the
manuscript cites by script name — `castelnuovo.txt`,
`corrected_operator.txt`, `law_resolution.txt`, `circle_and_detect.txt` —
pins their numbers, and checks them against the figures of
`src/chapters/04-bridges.tex`. The heavy scripts behind those files are not
re-run: the committed output is the record of the run, so a regenerated or
edited artifact fails the gate instead of drifting the paper.

`tests/test_golden_n_marks.py` does the same for the rest of the corpus
behind the manuscript's bare `N` marks (INV-WIT-001 §B, W6 Fase2): fifteen
tests over the twenty-four sites whose backing is a committed output, one
family per commit, each test naming in its docstring the `file:line` sites
it covers and reconciling the printed figures against the artifact's own
`articulo:` line. The sites with no backing stay untouched and are recorded
as `no-test:<reason>` in INV-WIT-001 §B.

`tests/test_arch_window.py` does the same for `arch_window.py`, the
archimedean form of `ζ_K`: the two crossings of the paragraph of
04-bridges (without the pole the form is negative from support length
`0.453`, the criterion `λ₂(D) > |C₀|` holds up to `1.647`, beyond the
prime-free range `[0, log 4]`), the basis the sentence declares for them,
and the row at `S = log 4` that carries the two window statements.
