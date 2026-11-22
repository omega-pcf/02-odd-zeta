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
`figures.md`, `installation.md`, `style-guide.md`, `usage.md`,
`witness-contract.md`, `style/grammar.md`); a report is what a generic
rule *refers to* for its concrete instances. Anything tied to one
repository state goes here — never to a document at the `docs/` root.

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

- `docs/citations.md` §8 — the generic rule this report instantiates.
- `docs/witness-contract.md` — why the device exists.
```

---

---

## Reports of this repository

| id | title | status | date | file |
|---|---|---|---|---|
| `CIT-003` | Verification of the 179 references imported from the v168 set — 49 corrections applied to `citation.csl.json`, 6 declared unverifiable with their original metadata kept | applied — corrections committed to `citation.csl.json`; `no verificable` rows untouched | 2026-11-21 | [20261121_CIT-003_v168_citation_verification.md](20261121_CIT-003_v168_citation_verification.md) |
| `F9-001` | Provenance inventory of every statement citing a literal corpus filename — 295 rows / 156 distinct names; 2 unresolved (`hipotesis/pruebas/`, `F1Paper`), the `*` marks and the Mathlib names at risk classified as process artifacts | report only | 2026-11-22 | [20261122_F9-001_provenance_inventory.md](20261122_F9-001_provenance_inventory.md) |
