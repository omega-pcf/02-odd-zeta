# docs/reports/ — specific reports

| Field | Value |
|---|---|
| **Document** | `docs/reports/README.md` |
| **Status** | In force |
| **Version** | 1.0 (generic template + local index) |
| **Date** | 2026-11-17 |
| **Scope** | The reports convention of the family: what a report is, how it is named and headed, and the index of the reports of *this* repository |

Reports are the *specific* material of the documentation: per-site
inventories, decision logs, verdict tables, audits and incident records
tied to one repository state. The generic, portable documents live one
level up in `docs/` (`README.md`, `architecture.md`, `citations.md`,
`figures.md`, `installation.md`, `usage.md`,
`witness-contract.md`); a report is what a generic
rule *refers to* for its concrete instances. Anything tied to one
repository state goes here — never to a document at the `docs/` root: the
applied inventory of the placement criterion, the counters, the verdicts
and the pending rows are archived here, and the documents at the `docs/`
root are rules and rationale only.

Two names of that list are **not** documents of this repository: there is
no `style-guide.md` and no `style/grammar.md` here. The editorial style
contract arrives with the witness specification (WIT-SPEC, in composition);
until it lands these documents are neither linked nor created.

## Naming

`YYYYMMDD_<ID>_<slug>.md` — ISO date of the report, stable id, slug in
kebab-case. The id is `<AREA>-<NNN>` with a sequence number that never
reuses a retired number; the area names the concern, e.g. `DEC`
(decisions), `WIT` (witness), `FIG` (figures), `AUD` (audits), `CIT`
(citations), `MRG` (merges), `SEC` (sections). A proposal that changes
the pipeline or a shared artifact is not a report: it is a specification
under `docs/specs/`, same naming, `SPEC-NNN` id.

## Report header

Every report opens with its title and an ISO field table:

```markdown
# <Title>

| Field | Value |
|---|---|
| **id** | `AREA-001` |
| **title** | <full title> |
| **status** | <applied / report only / snapshot / pending — the honest state> |
| **date** | YYYY-MM-DD |
| **version** | 1.0 |
```

A scope paragraph follows, naming the repository and, where relevant, the
commit the report was written from. Statuses are never optimistic: a
report that changed nothing says `report only`, and a row left to the
author says so.

## Index

The index of the reports of this repository is the table at the end of
this file, under *Reports of this repository*. Its columns are
`id · title · status · date · file`, one row per report, ordered by date.

## Snapshots

Reports are snapshots: their line numbers refer to the manuscript as
written and move with concurrent editing; the sentence tail (or the id)
identifies each site. A report is never edited to follow the manuscript —
a later state is a later report.

---

## Template for a new report

```markdown
# <Title>

| Field | Value |
|---|---|
| **id** | `AREA-001` |
| **title** | <full title> |
| **status** | <honest state> |
| **date** | YYYY-MM-DD |
| **version** | 1.0 |

**Scope.** <what this report holds, which repository, which commit if it
matters, and what it deliberately does not touch.>

<Body: the inventory, the table, the verdicts, the incident — with the
evidence and the method.>

---

## Related documents

- `docs/witness-contract.md` §6 — the generic rule this report instantiates (`docs/citations.md` §8 is only its index).
- `docs/witness-contract.md` — why the device exists.
```

---

---

## Reports of this repository

| id | title | status | date | file |
|---|---|---|---|---|
| `CIT-003` | Verification of the 179 references imported from the v168 set — 49 corrections applied to `citation.csl.json`, 6 declared unverifiable with their original metadata kept | applied — corrections committed to `citation.csl.json`; `no verificable` rows untouched | 2026-11-21 | [20261121_CIT-003_v168_citation_verification.md](20261121_CIT-003_v168_citation_verification.md) |
| `F8-001` | Witness reconciliation — zero old-form marks found; the `N[ids]` device ported (6 marks / 7 verbatim test ids, rule 13/15); 1 100 marks contrast-passed (856 inline / 244 own-line, the 244 `needs-decision`); counts and gates re-measured | applied — the marks and the census are in the tree; the 244 own-line verdicts and the caption tag remain `needs-decision` | 2026-11-22 | [20261122_F8-001_witness_reconciliation.md](20261122_F8-001_witness_reconciliation.md) |
| `F9-001` | Provenance inventory of every statement citing a literal corpus filename — 295 rows / 156 distinct names; 2 unresolved (`hipotesis/pruebas/`, `F1Paper`), the `*` marks and the Mathlib names at risk classified as process artifacts | report only | 2026-11-22 | [20261122_F9-001_provenance_inventory.md](20261122_F9-001_provenance_inventory.md) |
| `FTI-001` | Tier-use migration map — census of all 471 non-standard tier uses (P\*, C, Nc, O, T, R + the §Protocol gloss) grouped by context pattern with before/after; disposition 340 mechanical vs 131 gate rows; naming standard and the 7-row F11 rename inventory | report only | 2026-11-22 | [20261122_FTI-001_tier_uses_migration_map.md](20261122_FTI-001_tier_uses_migration_map.md) |
| `F12-001` | Author's v168 text-change pass — verbatim copy of the four paragraph changes (current text / proposed text / rationale) with the origin paths of the scripts | snapshot — verbatim copy of the author's document; the wave's application record is in the F12 commits | 2026-11-22 | [20261122_F12-001_author_text_changes_v168.md](20261122_F12-001_author_text_changes_v168.md) |
| `F10-001` | Port of the self-baked verification script to a per-module pytest suite — 94 tests in 13 modules, `verify:py` wired through pytest, the script deleted, the six `N[]` tags retargeted to seven snake_case ids, the four observation outputs pinned as golden; merges, drops, strengthenings, gates | applied | 2026-11-23 | [20261123_F10-001_pytest_suite_port.md](20261123_F10-001_pytest_suite_port.md) |
| `MRG-001` | Closure of the v168 merge — gate record per phase F0…F11b, final census (740 `\tierP` / 123 `\tierN` / 6 `N[ids]` marks over 7 ids / 221 `\LeanStar`), D5/D7 state, the registry correction closing F11b's laguna 6 as false, the open items, the two presentation decisions (α `\LeanStar` unification, β tally) and the housekeeping record | report only — measurements and record; the two recommendations are not executed | 2026-11-23 | [20261123_MRG-001_f1_v168_merge_closure.md](20261123_MRG-001_f1_v168_merge_closure.md) |
| `WIT-SPEC-002` | Requirements for the witness/citation apparatus of the 01–05 family, consolidated (second pass) — supersedes `WIT-SPEC-001_draft`, records the settled positions and the open rows one by one | report only — migrates nothing, edits no repository | 2026-11-23 | [20261123_WIT-SPEC-002_family_witness_spec_requirements.md](20261123_WIT-SPEC-002_family_witness_spec_requirements.md) |
| `INV-WIT-001` | Witness inventory of `02-odd-zeta` — census of the marks of `main.tex` + `src/chapters/*.tex` from a measurement; the id the suite's docstrings cite (`INV-WIT-001 §B`) | report only — census; the generated counterpart is `docs/witness-inventory.md` | 2026-11-24 | [20261124_INV-WIT-001_witness_inventory.md](20261124_INV-WIT-001_witness_inventory.md) |
| `PROBE-001` | Own-line mark format — localized probe: the ten variants, their definition sites and the invocation counts per repository; the measurement behind `witness-contract.md` §6.12 | report only — scratch probe; no repository changed | 2026-11-25 | [20261125_PROBE-001_ownline_mark_format_probe.md](20261125_PROBE-001_ownline_mark_format_probe.md) |
| `SCRIPTS-RECON-003` | Inventory of the 83 numerical scripts against the author's two deliveries (zip1/zip2) and the manuscript — 100 % `.py` coverage, the 3 `pending(D7)` markers, the 8 uncited modules, `retro65.py` and `zeros.txt` | report only — read-only reconciliation; the campaign that acts on it is tracked in `docs/numerical-port.md` | 2026-11-26 | [20261126_SCRIPTS-RECON-003_scripts_reconciliation.md](20261126_SCRIPTS-RECON-003_scripts_reconciliation.md) |
