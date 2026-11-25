# Witness standard — the family's evidence marks

This is the canonical page: the rules every wave brief cites. The rationale is
`docs/witness-contract.md` (§1–§5, §7–§9); the questions still open are
`docs/witness-decisions.md`; the measured state of a repository is
`docs/witness-inventory.md`. This file is a family file — pinned in
`scripts/shared-files.json` and byte-identical in the five repositories.

## 1. Precedence

**The manuscript is king.** A mark never overrides what the text states: where
the text and a mark disagree, the text is read first and the mark is corrected
to it. A mark is a pointer to evidence, never a verdict — it tells a reader
where the check lives, not that the claim is true. A count in a document is a
measurement with a date, not an argument.

## 2. Syntax — one form each

| role | source | prints |
|---|---|---|
| inline | `\tier[ids]{X}` | `X[ids]` — the tag first, its ids inside the brackets |
| own-line | `\witness{X}{ids}` | `X[ids]` on a line of its own, flush right |

`X` is `P` or `N` (§9). The body form is `P[id1, id2]`: one tag, its ids
separated by `, ` inside one bracket. No third body form exists; an accounting
line (`\leanline`, a `Lean:` line) is not a form of the mark (contract §6.3 S4).

## 3. What each mark asserts

- **`P`** — an artefact of the named formalization, checked by that
  formalization's own machine. The correspondence between that artefact and the
  statement of the paper is a human reading of both, and is not asserted by the
  mark.
- **`N`** — an executable numerical test with a stated tolerance and condition.
  The test is evidence; it is not a proof.
- **`tier`** is never an alias for *proved*, and no mark carries a degree of
  confidence, a provenance grade or a citation.

## 4. Grammar of the tag argument

The optional argument holds **internal ids only** — a `\testref{…}` or the raw
names of the repository's own declarations, several separated by `,`. The macro
reads the argument as an arbitrary string (contract §6.4): a character-shape test
would reject valid ids and cannot recognise a citation key. A literal `\cite`
token inside the argument is rejected at run time; an external source stays an
adjacent `\cite` in the prose, printed beside the mark, never fused into it.

## 5. Naming — a name is routed by its job

| class | route |
|---|---|
| S1 witness id | inside the mark — `\tier[ids]{X}`, `\witness{X}{ids}`, `\testref{…}` — raw, never beside the tag |
| S2 code mention | `\code` |
| S3 decorated name (`*`, `°`, `†`) | §6 and §8 |
| S4 `Lean:` accounting line | no canonical form; the sites stay where they are |
| S5 unclassifiable | recorded as an open site in `docs/witness-inventory.md`, never guessed |

Names follow the repository's naming standard (snake_case, English); an id that
does not is a work item, not an exception.

## 6. The star

`*` denotes **written, not yet verified against the corpus**. It lives only in
intermediate layers; verification passes resolve it and the release gate is
**zero stars**, so a released text carries none. It is not a class of evidence,
not a degree of confidence and not a citation.

## 7. Typography, and the family's deliberate divergences

The canonical render parameters, measured in the built PDF, are **13 pt for the
witness class, 15 pt for the ids and 16 pt for the prose**, identical for `P`
and `N`; only colour differs, and colour is redundant with the letter. Rendering
is re-checked by measurement, never by eye.

The underscore inside an id prints through the repository's `\brk@us`, and the
family does **not** unify it — the break-per-character decision is typography:

| repository | encoding | `\brk@us` |
|---|---|---|
| 01, 04 | OT1 | `{{\ttfamily\char95\relax}\allowbreak}` |
| 02, 05 | T1 | `\textunderscore\allowbreak` |
| 03 | T1 | `\textunderscore` — **no** `\allowbreak` |

03 keeps the form without the breakpoint because adding the family's
`\allowbreak` would open a break after every underscore of a witness list,
reflow the manuscript and break the family's byte-identical `pdftotext` gate
(`03/main.tex` comment at the definition; commit `b1fec34`, 2026-11-24).

## 8. Gates

1. **Citation-key lint** — no part of a `\tier[…]` or `\witness{…}{…}` argument
   may equal an id of `citation.csl.json` or contain a `\cite` token; it runs
   with the suite and reports `file:line`.
2. **Zero stars** at release (§6).
3. **No `Tier` column** in a ledger table; a table carries no tier label.
4. **Render** — tag before ids, `P`/`N` only, colour redundant with the letter.

## 9. The alphabet, open statements and decorations

The published alphabet is frozen at **`P` and `N`**: an expansion enters only
through measured sites, documented in all five repositories, counted by
`counts:check` and lintable, with its cost estimated first. Open statements are
prose by default (no `[o]` label); a `conjecture` environment is used only where
the statement is a precise declarative proposition *and* the status belongs to
the source that states it. No new tier labels, no shorthand; the decorations `°`
and `†` are held, not adopted.

## 10. Where things live

- `docs/witness-decisions.md` — one row per question; a count is never a row.
- `docs/witness-inventory.md` — the census of *this* repository, generated from
  a measurement, never hand-written; per repository by design, therefore not a
  family file and not manifest-pinned.
- `docs/witness-contract.md` — the rationale; §6 defers to this page.
- `docs/reports/` — historical traces; a superseded one carries `superseded-by:`.
- `docs/BRIEF-TEMPLATE.md` — the required shape of a wave brief.
