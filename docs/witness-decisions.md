# Witness decisions — one row per question

The family's decision ledger. **One row per question; a count is never a row.**
`resolution` states what was decided or what is still owed; `ref` names the
document and section that carries the evidence. Rows are added when a question
is surfaced — a rule already decided here is never re-surfaced in a brief.
Measured figures are dated and re-measured before reuse. Standard: see
`docs/witness-standard.md`.

## Ruled and derived

| id | question | resolution | ref |
|---|---|---|---|
| WD-01 | Which body forms of a mark exist? | **Ruled:** one inline form `\tier[ids]{X}` printing `X[ids]`, one own-line form `\witness{X}{ids}`; no third form | 2026-11-25 · standard §2 |
| WD-02 | What does `*` denote, and may a release carry it? | **Ruled:** written, not yet verified; intermediate layers only; release gate = **0 stars**; never a tier, a grade or a citation | contract §6.5 · `c7cbd92` retired the 221 family uses |
| WD-03 | May a ledger table carry a `Tier` column? | **Ruled:** no `Tier` column and no tier label in a table; a redesign of what tables carry is a change candidate, decided elsewhere | contract §6.7 · standard §8 |
| WD-04 | Is the tag argument shape-checked or read as a string? | **Ruled:** read as an arbitrary string; the only run-time rejection is a literal `\cite`; the no-keys rule is measured by the lint, not by shape | contract §6.4 · 2026-11-25 |
| WD-05 | What is the state of D7 (deferred scripts and their markers)? | **Applied:** 42/42 scripts ported (`a475748`) → absent scripts = **0**; manuscript markers **68 → 3** (`d5ab1ca`); the 3 remaining markers are residue, listed in the inventory | 2026-11-25 · MRG-001 §3, §5 item 5 |
| WD-06 | What happens to the trivial fills of the appendix corpus? | **Ruled:** **2 applied** (the two archimedean-window crossings, stated and pinned by `tests/test_arch_window.py`); **4 recorded as proof obligations** (still `def … : Prop` in `lean/`) | 2026-11-25 · D7-446-RECON aggregate verdict |
| WD-07 | May a new evidence label be introduced? | **Ruled:** no; the alphabet is frozen at `P` and `N` and expands only through the family gate | contract §6.8 · standard §9 |
| WD-08 | Does the standard decide inline versus own-line placement? | **Ruled:** no — placement is a prose criterion; the standard governs content and naming only | contract §6.2 |
| WD-09 | Should `\brk@us`/`\allowbreak` be unified across the family? | **Ruled:** not unified; the divergence is documented (01/04 OT1, 02/05 T1, 03 T1 without the breakpoint) because unifying reflows 03 and breaks the byte-identical `pdftotext` gate | 2026-11-25 · standard §7 · `b1fec34` |
| WD-10 | May a citation sit inside a tag? | **Ruled and applied:** never; the `\cite` moves to the prose and the tag is kept only when it has real ids (05: 7 own-line blocks reformed) | 2026-11-25 · 05 `main.tex` · standard §4 |
| WD-11 | Which documents are family files? | **Ruled:** `witness-standard.md`, `witness-decisions.md` and `BRIEF-TEMPLATE.md` are byte-identical and manifest-pinned; `witness-inventory.md` is a per-repository census and is not pinned | 2026-11-25 · `scripts/shared-files.json` |
| WD-12 | Which is the canonical `Lean:` own-line accounting (P-5)? | **Derived:** no canonical form; placement is prose and the sites are not migrated in bulk (S4) | WIT-SPEC-002 §4 · contract §6.3 |
| WD-13 | Which is the canonical spelling of an inline name (P-6)? | **Derived:** `\code` for a mention (S2), raw names inside a tag (S1) | WIT-SPEC-002 §4 |
| WD-14 | Which grammar goes family-wide (P-7)? | **Derived:** WD-04 — free string plus lint; ids that do not meet the naming standard are work items | WIT-SPEC-002 §4 · contract §6.4 |
| WD-15 | Where does the contract live and how is it propagated (P-8)? | **Shown, not signed:** `docs/witness-contract.md`, byte-identical in the five repositories, manifest-pinned | WIT-SPEC-002 §4 · `scripts/shared-files.json` |
| WD-16 | Is `\wtag` required of every repository (P-3)? | **Measured, no requirement:** only 05 has a W list (12 sites) | WIT-SPEC-002 §4 |
| WD-17 | Does 01 adopt the tags at all (P-13)? | **Not adopted:** 01 stays tag-free with a declared deferral, as does 04 | WIT-SPEC-002 §4 · inventory (0 marks) |
| WD-18 | Is the star unification (α) still open? | **Closed by measurement:** `c7cbd92` retired the 221 uses; `\LeanStar` has **0** body uses in the family (02 carries the definition only) | MRG-001 §6 α · 2026-11-25 |
| WD-19 | Is the tally (β, `\LeanTally`) kept or folded into `\LeanInline`? | **Open-for-author:** 21 body uses, all in 02 (MRG-001 §6 β); the `°` certifies a count over an enumerated type, not a classification | MRG-001 §6 β |

## Open — for the author

| id | question | resolution | ref |
|---|---|---|---|
| WD-20 | How are the 131 decision-gate sites of FTI-001 disposed? | **Open-for-author**, one row per pattern: gloss/protocol block rewrite (7 uses) · P* status sentences (7) · state the source in prose for `C`/`T` marks (16) · mark open-ness in prose, in a table cell or not at all (32) · `a reading` where `R` is retired (6) · split compound marks (5) · `N`/`Nc` without an in-sentence witness (11) · `in text` / `proved in the text` cell words (5) · move the caption mark to the body (1) · table cell convention (38, superseded by WD-03) | FTI-001 §6.2 · counts as recorded 2026-11-22 |
| WD-21 | What becomes of the 322 `needs-decision` marks of F8-001? | **Open-for-author**, one row per cause: 244 own-line verdicts with no block to move to · 56 `N`/`Nc` without a witness in the sentence (48 were D7-deferred, now ported → re-measure) · 20 `P` without a Lean name in the sentence (8 in tables, witness in the neighbouring cell) · 2 `P` in a "not yet compiled" sentence | F8-001 §2.3 · 2026-11-22 |
| WD-22 | Does the caption tag move into the body sentence? | **Open-for-author:** 1 site (`03-mechanisms.tex` caption mark); no caption rule existed at the port | MRG-001 §5 item 7 · FTI-001 §6.2 |
| WD-23 | Which ids of 03 still fail the naming standard? | **Open work item:** measured 2026-11-25 over `src/chapters/*.tex` — of the 100 id parts of `\tier[…]`, **18** fail snake_case: **12 label-style identifiers** (10 distinct, 9 sites) and the **6 ellipsis placeholders** of the gloss sentences; `:`-style label keys remain **0** | contract §6.4 · WIT-SPEC-002 DSB-4 |
| WD-24 | What are the 0.087 `law_resolution` figures without a reproduction? | **Open-for-author:** carried from F12-001 with the author's original detection figures | MRG-001 §5 item 2 |
| WD-25 | Are the `appendix:446` corpus counts reproducible? | **Open-for-author:** 26 open statements and 21 named classical inputs are stated in prose and irreproducible with the repository's tooling; re-count at rewrite time, never translate | MRG-001 §5 item 3 · D7-446-RECON |
| WD-26 | What is the disposition of D5's absent artifacts? | **Open-for-author:** 3 absent artifacts, `ontologia_lean` highlighted | MRG-001 §5 item 6 |
| WD-27 | Is a bibliography DOI printed twice a defect of this wave? | **Carried laguna, reported not fixed:** 37 of 109 DOI-bearing entries print the DOI twice; the cause is `citation.csl.json`, outside the wave's scope | MRG-001 §5 item 9 |
| WD-28 | Are the `°`/`†` decorations adopted? | **Held:** not adopted while their use stays marginal; nothing certifies them; raw duplicates of the macros are noted, not removed | contract §6.7 · W3 ledger F-6/F-7 |
| WD-29 | May a `conjecture` environment be cast for tidiness? | **Ruled earlier, still binding:** only where the statement is a precise declarative proposition *and* the status belongs to the source; ambiguous sites stay prose | contract §6.7 · W3 ledger F-8 |
| WD-30 | Do the Hodge-index gaps have a witness? | **Open-for-author:** 2 sites (`04-bridges.tex` — the arithmetic Hodge index and the golden-field Hodge index) are open and recorded in Lean only schematically | 2026-11-25 · measured in `src/chapters` |
| WD-31 | Do the unclassifiable sites (S5) have a route? | **Open:** every site that cannot be routed is registered here or in the inventory, never guessed | contract §6.3 S5 |
| WD-32 | Which doubtfuls of the specification remain unanswered? | **Open, tracked by their original ids:** DSB-2 (`°`/`†` fate), DSB-6/DSB-7 (four `citations.md` §8 variants — 04 has no §8), DSB-8 (02 lacks `style-guide.md` and `docs/style/grammar.md`), DSB-9 (contrast ratio and id length unmeasured), DSB-14 (math-mode handling diverges), DSB-17 (`\code` boundary inside captions); DSB-16 is closed (`ad0899d`) | WIT-SPEC-002 §6 |
