# Numerical port — final reconciliation

| Field | Value |
|---|---|
| **id** | `NUMPORT-001` |
| **title** | Reconciliation of the `hipotesis/pruebas/` → `tests/` port campaign |
| **status** | closed — the folder the campaign ported is removed from the tree |
| **date** | 2026-11-27 |
| **version** | 2.0 (reconciliation only: the per-script provenance columns and the per-wave logs are retired with the folder; git history holds both) |

**Scope.** One row per numerical script of `hipotesis/pruebas/` (83 `.py`),
reconciled against the suite that owns the evidence now: `tests/`, 228 tests,
`uv run pytest tests/`. This document records state only; it edits no test and
no manuscript. The scripts are gone from the working tree — `git rm -r
hipotesis/pruebas/` in `71a407f` — and the committed outputs they produced
moved to `tests/fixtures/` in the same commit, byte-identical, so every golden
pin still reads the same bytes. Line numbers quoted by the campaign are
snapshots and move with the manuscript — the convention the six test modules
cite here. The sources behind these counts are the
closed tracker of `a667a48` and its predecessors (the per-script table, the
`salidas/`/`datos/` sub-tables and the wave logs live there), and
`docs/reports/20261126_SCRIPTS-RECON-003_scripts_reconciliation.md` (the
inventory against zip1/zip2).

## Final counts — the 83 rows of the closed tracker

| destino propuesto | rows |
|---|--:|
| `<test-name>` (owed a test) | 44 |
| `absorbed` | 32 |
| `generator:<… kept as fixture>` | 2 |
| `orphan-no-cited` | 4 |
| `blocked:<motivo>` | 1 |
| **total** | **83** |

| status | rows |
|---|--:|
| `ported:<test> · verified-against-corpus` | 41 |
| `ported:<test>` | 3 |
| `verified-against-corpus` | 28 |
| `absorbed` | 4 |
| `absorbed-into:<test>` | 5 |
| `orphan-no-cited` | 1 |
| `blocked:<motivo>` | 1 |
| `pending` · `in-progress` | 0 · 0 |
| **total** | **83** |

**Reconciliation, measured over the closed table before it was retired:** the
44 rows whose `destino` named a test are exactly the 44 rows whose `status`
starts `ported` — same set, no `pending`, no `in-progress` — and the six
modules they owe (`test_bridge_boosts`, `test_closures_and_sweeps`,
`test_envelope_bounds`, `test_retro_sprints`, `test_v_layer_claims`,
`test_weil_certificates`) exist in `tests/`. The 35 committed `salidas/*.txt`
are pinned by a golden test each (0 unread), and the input caches
(`zeros.txt`, `zeta_zeros_3000.npy`, `chi5_zeros*.json`, `dh_zeros.json`,
`datos/*`, the three `weil_certificates/` artefacts) are read by the claim
tests that need them. `uv run pytest` is green with the folder gone.

## Evidence of the closure

* **`git rm -r hipotesis/pruebas/`** — 84 tracked files (83 `.py` +
  `correr_todo.sh`), commit `71a407f`, in the same commit as the 53 renames
  that moved every committed data file to `tests/fixtures/` and repointed its
  readers (`tests/src/oddzeta/harness.py`, the six test modules,
  `pyproject.toml`'s `golden` marker, `tests/README.md`).
* Measured before the removal: `git grep hipotesis` over `tests/`, `scripts/`
  and `package.json` found only data paths — no `import`/`from` of any script
  of the folder anywhere in the repository — so each hit moved first and
  nothing was left reading a deleted path.
* The manuscript's census sentence (`appendix`, *Numerical scripts*) now says
  the census lives in `tests/` with its outputs in `tests/fixtures/salidas/`;
  the source-map table still names `hipotesis/pruebas` as a corpus source,
  tables being out of scope for this wave.

## Still open with the author

| row | status |
|---|---|
| `retro65.py` | `blocked:never-delivered; ask-the-author-or-declare-unavailable` |
| `retro66.py` | `blocked:retro65-never-delivered` — `retro66.py:99-101` `exec`s `retro65.py`, which no delivery contains (not zip1, not zip2, not the repo, not the MANIFEST's unavailable list), so the script does not run as it stands |
| `comun_pruebas.py` | `orphan-no-cited` — 0 citations in the manuscript, no artefact of its own, no reader; the author's cite-or-drop call stays open |
| `unfold_by_conductor.txt` | `blocked:no entregado por el autor` — cited at `04-bridges:107`, in neither zip; the one `pending(D7)` marker still open |
| the ten `datos/` files of the zip1 MANIFEST | `orphan-no-cited:no-readers` — never delivered, 0 readers in the repository (measured); the zip's description of the tree stays with the operator |

---

## Related documents

- `docs/reports/20261126_SCRIPTS-RECON-003_scripts_reconciliation.md` — the inventory this campaign acted on.
- `docs/reports/20261123_F10-001_pytest_suite_port.md` — the pattern the campaign extended.
- `tests/README.md` — suite layout, tolerances, the `tests/fixtures/` corpus and the golden artifacts.
