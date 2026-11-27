# State fragments extracted from the family witness documents

| Field | Value |
|---|---|
| **id** | `WIT-001` |
| **title** | Counts, censuses and commit records moved out of `docs/witness-contract.md` and `docs/witness-decisions.md` |
| **status** | applied |
| **date** | 2026-11-27 |
| **version** | 1.0 |

**Scope.** `02-odd-zeta`, from the working tree of 2026-11-27 before the
extraction. The contract is a norm and the decisions are a decision register;
the fragments below were measured state embedded in them — a commit record, a
site census and a build snapshot — and measured state belongs in a report
(`docs/reports/README.md`). Every figure is copied verbatim from the document
that carried it, and each document now points at the section that holds it.
Nothing else moved: the rules, thresholds and decisions of both documents are
untouched.

## 1. From `docs/witness-contract.md` §6.7 — the `\brk@us` commit record

> `03/main.tex` comment at the definition, commit `b1fec34`, 2026-11-24; the
> unification commits are `2fb29c6` in 02, `4edc048` in 03 and `a82bd8d` in
> 05, all 2026-11-25.

Git already carries the traceability; §6.7 keeps the rule and the divergence
table and drops the hashes.

## 2. From `docs/witness-contract.md` §6.12 S5 — the gate-3 census

> gate `r = 0`, already true at 100% of sites: 0/86, 0/124, 0/43.

A census of applied sites, dated by the pass that measured it, not a rule: the
rule is `r = 0`.

## 3. From `docs/witness-contract.md` §6.12 S6 — the colour applied state

> which is what `\witness` already does in 3/3 repositories that render marks
> … (its ids print black today, measured #000000 against #2659a5 in the block).

§6.6 keeps the palette (the norm) and S6 keeps the scope rule; the counts of
repositories that already comply and the hex snapshot of the inline branch go
here.

## 4. From `docs/witness-decisions.md` WD-34 — the green build snapshot

> `lake build` **18 248 jobs, success**, `lean.sorry` **0**, `lean.axioms`
> **0**, `lean.theorems` **5712**, measured 2026-11-24

WD-34 keeps its ruling and its references; the dated figures behind it live
here. WD-34 also records that the operator's third rejection removed the
subsection from the appendix on 2026-11-27.

## 5. From `docs/witness-decisions.md` WD-33 — the legacy-report divergence counts

> the legacy reports keep their own H1 shape (three of them), three are written
> in Spanish, four carry no `version`, four carry no field table

WD-33 keeps the ruling (recorded, not fixed) and the convention it defers to;
the counts of the legacy corpus are state of one moment, not part of the
decision.

---

## Related documents

- `docs/witness-contract.md` §6.7, §6.12 — the norm these fragments left.
- `docs/witness-decisions.md` WD-33, WD-34 — the decisions they belonged to.
- `docs/reports/README.md` — the reports convention this report follows.
