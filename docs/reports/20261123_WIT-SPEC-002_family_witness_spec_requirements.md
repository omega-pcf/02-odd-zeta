# WIT-SPEC-002 — Family witness & citation standard: requirements (second pass)

| Field | Value |
|---|---|
| **id** | `WIT-SPEC-002` |
| **title** | Requirements for the witness/citation apparatus of the 01–05 family, consolidated |
| **status** | Second-pass consolidation; supersedes `WIT-SPEC-001_draft.md` (retained unchanged as the first-pass record). Migrates nothing, edits no repository, commits nothing. |
| **date** | 2026-11-23 |
| **version** | 1.0 |
| **inputs** | `WIT-RECON-001` (inventory, O1–O3, (a)–(h), L1–L15) · `WIT-CONTRAST-001` (tally facts, options P4/P10/P11/P1, 01 scope) · `witness-contract.md`, `citations.md` §3+§8 · `MRG-001` §2/§6/§13 · `FTI-001` §6–§7 · `F10-001` §5/§7 · `F8-001` §2.3 · `05/main.tex:40–110`, `02/main.tex:215–245` · FOCUS-B measurement of the built PDF |
| **reading rule** | §3 records settled positions; §4 lists what remains open, one row each, for individual ruling. No global approval of this document is requested or implied — outside a §4 row nothing awaits a decision. |

---

## 1. Purpose and principles

The family marks the evidential status of claims — inline status tag, own-line witness,
test anchor, decorations — so a reader or auditor can move from any marked claim to its
evidence (Lean declaration, test name, certified count), and so aggregate statements are
regenerated rather than transcribed.

1. **One function → one canonical implementation.** The unit of standardization is the
   function (what a mark does), not the macro name; two live implementations of one
   function are redundancy *and* divergence.
2. **Counts are measured, never typed** (`counts:check`, census tests, stated `git grep`
   recipes).
3. **Intermediate process state is not release state.** Markers for work written but
   not yet verified live in intermediate layers, are resolved by verification passes,
   and never appear in a release. *(Inspiration: lifecycle markers such as `TODO`/`FIXME`
   bounded by CI — an analogy for behaviour, not an authority for the mark's semantics.)*
4. **Doubtful sites are surfaced, never silently resolved.**
5. **Passes are layered and reported:** preamble, mechanical renames, judgment,
   documentation — separate waves, each closing with counts and a gate table; mixing
   layers destroys the count trail.

Framing: requirements of non-redundancy, non-divergence and verifiability — not a
catalogue of permitted shapes.

---

## 2. Vocabulary — the system as it stands

Counts = uses (excl. definitions/comments) / lines, from WIT-RECON-001 (grep over
tracked `*.tex`, HEADs 2026-11-23) unless another source is named; `—` = function absent
in that repo.

| Function | Canonical implementation today | 01 | 02 | 03 | 04 | 05 |
|---|---|---|---|---|---|---|
| **F-1** inline tag `[P]/[N]` | 05 `\tier[ids]{X}`: guarded colour, `PackageError` grammar, bare `[X]`, ids 13/15 | — | `\tierP` 740/693 + `\tierN` 123/122 + `\tier` 8 (no colour) | `\tier` 101/101 (81 P, 19 N; unguarded colour; lax grammar; bare branch bracketless) | — | 208/168 (198 with ids) |
| **F-2** own-line witness `P[ids]` | 05 `\witness{X}{ids}`: flush right, ids 13/15 | — | none; 244 own-line verdicts carry no form | 123/123 (same name; ids `\footnotesize`, no `\brk@us`) | — | 50/50 |
| **F-3** W-list label | 05 `\wtag{L}{text}` | — | — | — | — | 12/12 |
| **F-4** inline code name | undecided (P-6) | `\lean` 103/83 | `\LeanInline` 992/607 + `\lean` 18/15 | raw names inside marks + `\PytestInline` 1 | `\lean` 89/75 | `\code` 40/25 (3 in captions) |
| **F-5** own-line `Lean:` accounting | undecided (P-5) | raw prose 2 | `\leanline` 67/67 | — | raw prose 5–9 | — |
| **F-6** tally `°` | position §3.7 | — | `\LeanTally` 21/20 + 5 raw in appendix | — | — | — |
| **F-7** companion `†` | position §3.7 | — | `\LeanCW` 44/39 + 1 raw in appendix | — | — | — |
| **F-8** conjecture/open/empty states | none live (prose + `conjecture` environments, §3.9) | — | 3 defs, 0 uses | `\Conj` 0, `\Open` 0, `\Empty` 1 | — | `\pending` 0 |
| **F-9** pre-compilation star `*` | process marker, position §3.2 | — | `\LeanStar` 221/173 (195 of 416 already folded into `\LeanInline` in F11) | — | — | — |
| **F-10** test anchor | 05 `\testref{…}` + census test | — | 9 uses (7 ids / 6 marks), `test_witness_census.py` | raw ids inside `\tier[…]` | — | 95/71, `test_section_census.py` |
| **F-11** colour dispatch | 05 `\tiercol` with unknown-key guard | n/a | absent (only repo with black tags) | `tag*` without guard | n/a | guarded (`tierP/tierPs/tierN/tierW`) |
| **F-12** grammar guard | undecided (P-7) | n/a | strict: `\testref` only; comment states 05's rule | lax: only `\cite` forbidden; 23 of 100 ids would fail 05's rule | n/a | strict-medium (`\testref` ∨ `\_` ∨ `,`, else error) |

Cross-cutting (MRG-001 §2, 02 census, 2026-11-23): adjacent tag pairs **0** · tags in
`\caption` **1** · empty tag groups **6** · retired classes (`\tierPnew \tierC \tierO
\tierT \tierNc \tier{R}`) **0 each** · pinned cited test ids **7** · definitions with
0 uses **7** (plus `\Empty` 1, `\PytestInline` 1 "Legacy") · raw `°` duplicates **5
sites**, raw `†` **1 site** in 02's appendix (re-measured 2026-11-23; recon's ~8/~4
superseded).

FOCUS-B (built PDF, 05): 13 pt witness class / 15 pt ids / 16 pt prose, identical for P
and N; only colour differs (P `#2659a5`, N `#0c6633`); contrast ratio and id length
unmeasured.

---

## 3. Decisions and standing positions (folded)

Nothing here is open; anything open is a row of §4.

**3.1 Direction O1 — one canonical implementation per function, reference = 05.**
WIT-RECON-001 recorded O1 (converge on 05), O2 (context-detecting single macro), O3
(two forms with a canonical implementation each). Position: O1. O2 is
excluded — inline vs own-line is a prose-context judgment mode detection cannot derive,
and it removes name-based lintability while saving no call sites; O3 stays on record
(recon §4) but leaves F-5/F-6/F-7 without a canonical. Cost estimates (≈2 150 lines)
are re-measured at W0.

**3.2 The star (α) — process marker, kept, zero at release.**
MRG-001 §6 proposed unifying the 221 remaining `\LeanStar` uses into `\LeanInline`; the
reframing in MRG-001 §13 supersedes it. The star marks a name written but not yet
verified against the corpus — the state every mechanical pass produces — and is
unrelated to the inline/own-line axis. Disposition: tracking, not rendering — kept in
intermediate layers, resolved by verification passes, release gate = zero stars, no
unification implied. (Inspiration: lifecycle markers whose expiry the pipeline
enforces — principle 3.)

**3.3 Semantic pass rule (S1–S5) — no blind rename.**
Classified by the job each name does in its sentence: **S1** witness id → stays inside
the mark (`\tier[ids]{…}`, `\witness{…}{…}`, `\testref{…}`), never beside the tag;
**S2** code mention → spelling per P-6; **S3** decorated name (`*`, `°`, `†`) → §3.7;
**S4** `Lean:` accounting line → P-5; **S5** unclassifiable → registered in §6, never
guessed. Restated after the first pass; governs W3.

**3.4 Citation preamble standard — applied.** Family standard:
`sorting=nyt,giveninits=true` (`citations.md` §3); the MRG-001 §5.9 divergence (02:
`sorting=none`, no `giveninits`) is closed — 02 carries the family style (commit
`ad0899d`). First-pass P-12 closed.

**3.5 First-use gloss.** Every mark's meaning is stated in prose at its first use (P/N
`01-introduction.tex:103`/`:254`, `°` `02-foundations.tex:137`, `†` `:853`, all in 02).
A mark without one is a defect.

**3.6 Tier classes retired; alphabet frozen at P/N.** `P*`, `C`, `O`, `T`, `Nc`, `R`
were retired in F8/F11/F11b; census = 0 each (MRG-001 §2). Any future class enters only
through an expansion gate: measured sites, used ∧ documented in all five repositories,
census in `counts:check`, a `wit-lint` rule (R-1/R-3/R-7 as gate).

**3.7 Tally `°` and companion `†` — declared provenance decorations with a census.**
*Semantics (measured):* the glyph certifies that the count of an enumerated type was
closed by `decide`; it does not certify the text's classification — macro comment and
first-use sentence state this in two layers. Grounding: 7 of the 12 ids under `°` have
`decide` in their proof block (read to the next top-level declaration, cap 200 lines);
the other 5 close by other means and were not audited further. *Position:* `°`/`†`
enter the contract as provenance decorations, not evidence classes, with census
declared (21 sites / 12 ids; 44 sites); the 5 raw `°` and 1 raw `†` duplicates in 02's
appendix are removed (R-9); census joins `counts`. *Utility:* one grep finds every
certified count. *Practicability:* one contract entry, one counter, one lint rule,
6 site edits, no prose change. *(Inspiration: declared provenance records — an
SBOM-style inventory — and lint suppressions carrying a stated reason; neither is an
authority for the mark's meaning.)* Closes MRG-001 §6 β.

**3.8 Typography — keep the measured parameters.** 13 pt witness class / 15 pt ids /
16 pt prose is the canonical render spec, written into the contract (R-15). FOCUS-B
found no size defect between P and N (§2); rendering is re-checked by measurement per
wave, never by eye — reopening requires a new measurement.

**3.9 Open tier — prose by default; statement environments only under a per-site gate;
shorthand evaluated at W3.** An *open problem* and a *conjecture* are **not interchangeable**:
a conjecture is a **precise declarative proposition**, with its terms defined, asserted as
believed-true-but-unproved; an open problem or question is a task whose resolution is unknown
and need not have a truth value as stated. Casting one as the other changes what the text
claims. Two conditions therefore gate every site before any environment is used:
(a) **logical form** — the statement is a precise proposition, not a question or task;
(b) **provenance** — the conjecture-status belongs to the source that states it (the principal
author's own open claim, a problem quoted from the literature, or an observation of this text);
an environment asserts belief-status and reads as the paper's conjecture, so it is never
assigned for tidiness and never attributes a position the source did not take. Disposition:
prose by default (questions stay questions, in prose); a `conjecture` environment only where
both conditions hold; ambiguous sites stay prose and are recorded as tracking, not cast. No
shorthand is adopted now: it is evaluated in W3 **after** this form-and-provenance
classification, against the measured open-statement sites (26 in `appendix:446` plus proxy
counts), and enters the contract only under §3.6's gate.

---

## 4. Open decisions (one row each, for individual ruling)

Evidence columns point at sources rather than re-argue them; recommendations are
advisory.

| id | question | options | evidence | recommendation |
|---|---|---|---|---|
| **P-3** | Is `\wtag` (W-list label) required of every repository, or conditional on having a W list? | (i) conditional · (ii) required · (iii) defer to W4 | recon (c): only 05 has a W list (12 sites); §8.1 already says "where the manuscript has one" | *(advisory)* (i) — requiring it would create zero-use definitions |
| **P-5** | Which is the canonical `Lean:` own-line accounting (F-5)? | (i) adopt 02's `\leanline` (67 sites) · (ii) fold into `\witness` · (iii) retire to prose | recon (e), L3: 3 implementations (1 macro + raw prose in 01/04); coupled to the 244 own-line verdicts (OI-2) | *(advisory)* evaluate in W3 with OI-2 — the answer depends on whether 02 gains `\witness` sites |
| **P-6** | What is the canonical spelling of an inline name (F-4)? | (i) `\code` family-wide · (ii) raw names everywhere · (iii) per context: raw inside marks (S1), `\code` for mentions (S2) | recon (f), L2: `\code` has 40 uses in 05 and 0 mentions in its own §8; 03 already works with raw names | *(advisory)* (iii) — the S1/S2 rule already separates the two jobs; P-6 fixes only the S2 spelling |
| **P-7** | Which `PackageError` grammar goes family-wide? | (i) 05's · (ii) 05's + `\label`-style ids admitted · (iii) 02's | recon (g): three variants; (i) requires rewriting 23 ids in 03 (label keys with `:`); 02's 6 live uses conform | *(advisory)* (i), with the 23 ids as a named W3 task |
| **P-8** | Where does the contract live and how is it propagated? | (i) h1: §8 of 05's `citations.md` + verified copies · (ii) h2: dedicated `docs/specs/…` file + verified copies · (iii) h3: per-repo text + parity test | four documentary variants today (DSB-6/7); `witness-contract.md` byte-identical in 01/03/05 (24 236 B), pinnable now; `manifest:check` exists (R-10) | *(advisory)* h2 + manifest pin: a file without per-repo sections is the only clean pin target; the `witness-contract.md` pin does not wait on this ruling |
| **P-13** | Does 01 adopt the tags at all? | (i) 01 tag-free with a declared deferral (04's pattern) · (ii) 01 adopts `\tier` · (iii) decide after W0's re-measure | 01 has 0 tags while its `citations.md` §8 documents them (L1; violates R-7 either way); CONTRAST §4 estimates (ii) at ≈15 mechanical definitions + 45–55 judgment rows + 1 census test | *(advisory)* (i) unless adoption is decided explicitly; 04 needs no ruling |

Closed rows of the first pass: P-1, P-9 → §3.1/§3.6 · P-4 → §3.7 · P-10 → §3.8 ·
P-11 → §3.9 · P-12 → §3.4.

Closed by ruling or derivation (2026-11-23, second review):
- **P-13 → not adopted for now**: `01-hilbert-polya` stays tag-free (deferral; the contract
  still propagates to it as documentation).
- **P-5 / P-6 / P-7 → derived, no longer questions.** Placement (own-line versus inline) is a
  prose criterion — semantic, heuristic, aesthetic — and is **never** treated as a semantic axis;
  the standard governs content and naming only (S1–S5), leaving placement to prose. P-6's
  spelling follows from the same rule (raw inside marks for witness ids; `\code` for code
  mentions). P-7 adopts the strict `PackageError` grammar; `03`'s 23 label-style ids are work
  items, not design constraints.
- **P-8 → shown, not signed**: the standard lands as edits to the existing
  `docs/witness-contract.md` / `docs/citations.md` §8, propagated as visible diffs with manifest
  pins; no separate approval document.
- **Open-tier label `[o]` → not adopted** (prose formalism preferred; not standard, no concrete
  witness name). Tier labels in ledger tables are flagged as **antagonistic to the table's
  purpose** — the table-information redesign is surfaced in W3 as a change candidate, not
  decided here. **Decorations (`°`/`†`) → held**, no adoption while their use stays marginal.
- **W-tags (P-3, F-3)**: measured — `05` only, 12 uses, as the labels of one description list of
  twelve premises (`\item[\wtag{W1}{CLPW}.]` → `W1[CLPW]`); a list-label typographic device,
  **not part of the evidence-mark set** (the standard's mark set remains P/N with `\testref`).

---

## 5. Tracking (not decisions)

Kept in view with their counts; an item closes only by reference to a §4 row or by a
measured change in a wave.

| item | count | source | state |
|---|---|---|---|
| Prose counts in `appendix:446` ("26 open / 21 classical"), not reproducible with repo tooling | 26 / 21 | MRG-001 §5.3 | re-count at rewrite time, never translated |
| Own-line verdicts in 02 with no form to move to | 244 (of 322 needs-decision; 778 keep) | F8-001 §2.3 | blocked on P-5; no bulk migration |
| Status tag inside `\caption{}` (line `:1167` per MRG-001, `:1170` per FTI-001 — snapshot drift) | 1 | MRG-001 §2; FTI-001 §6.2 | move to the body sentence once located |
| Starred sites pending verification (F-9) | 221 → 0 at release | MRG-001 §6/§13 | resolved by verification passes |
| Decoration censuses (F-6 `°`, F-7 `†`) | 21 sites / 12 ids (+5 raw); 44 sites (+1 raw) | MRG-001 §6 β; CONTRAST §1.2; RECON §1 | censuses enter `counts` under §3.7 |
| D7 deferred scripts and `pending(D7)` markers | 42 scripts + 68 markers (03:13, 04:30, app:25) | MRG-001 §3/§5.5 | outside witness scope; marker lint only |
| D5 absent artifacts (`MANIFEST.md`, `LEDGER_ESTADO.md`, `ontologia_lean/`) | 3 | MRG-001 §3/§5.6 | reported, not edited |
| Claims with no runnable test (bare `N`, computer-assisted rows) | 46 bare N + 15 Nc | FTI-001 §9.2; F10-001 §8.5 | needs tests, not marks |
| Empty tag groups `\tierP{}` / `\tierN{}` | 6 | RECON L11 | mechanical cleanup in W2 |
| Stale claims in 02 docs (`docs/README.md`, `docs/architecture.md:88`) | 2 documents | MRG-001 §5.10 | corrected in W4 |
| Definitions with 0 uses (02 `\Lean \keyres \todo \pending`; 03 `\Conj \Open`; 05 `\pending`) | 7 (plus 2 single-use legacy) | RECON L9 | delete or document in W3/W4 (R-7) |

---

## 6. Doubtfuls (surface list; nothing pre-resolved)

- **DSB-1** `\wtag` exists only in 05 (12 sites) → P-3.
- **DSB-2** contract fate of `°`/`†` → §3.7; raw duplicates removed under R-9.
- **DSB-3** 05's comment (`main.tex:99`) names `\ProofWitnessBlock` in 03, which defines `\witness`; 02's `\leanline` has no canonical → W1 + P-5.
- **DSB-4** 23 of 100 `\tier` ids in 03 are label keys with `:` and fail 05's grammar → P-7, W3.
- **DSB-5** 02's tags carry no colour (863 sites); its ported §8.1 documents "without colour" → W1/W2.
- **DSB-6** four variants of `citations.md` §8: 05 25 108 B full · 01 = 03 24 476 B older copy · 04 ends §7 (6 905 B) · 02 adapted port 21 715 B → P-8, W4.
- **DSB-7** `witness-contract.md`: 01 = 03 = 05 (24 236 B) vs 02's port (24 730 B, "inline-only device") → P-8, W4.
- **DSB-8** 02 lacks `style-guide.md`, `docs/style/grammar.md`, `docs/figures.md` (listed by its own reports README); 04 lacks `witness-contract.md` → W4.
- **DSB-9** FOCUS-B measured size and colour only (§2); contrast ratio and id length unmeasured → §3.8.
- **DSB-10** 02 defines `\Lean` with 0 uses while §8.1 states there is no `\Lean{}` → R-7, W3/W4.
- **DSB-11** 03's bare branch renders `X` without brackets (0 live uses; contradicts its own comment) → W2 with the 101-site rename.
- **DSB-12** 02's grammar comment promises 05's rule while its code accepts only `\testref` (6/6 uses conform) → W1 + P-7.
- **DSB-13** 03's `\tiercol` has no unknown-key guard → W1.
- **DSB-14** math-mode handling diverges (02 `\ifmmode` guard 3 tags; 03 `\mbox` 4; 05 plain, 0) and "line contains `$`" is a coarse marker → W0 re-measure, W2.
- **DSB-15** raw `°`/`†` in 02's appendix duplicate the macros in the same repo (5 + 1 sites) → §3.7, W3.
- **DSB-16** 02's citation preamble divergence — **closed** by `ad0899d` (§3.4); kept for register completeness.
- **DSB-17** `\code` undocumented in the canonical repo (40 uses, 0 in its own §8; 3 in captions while §8.2 rule 8 bans *status tags* — boundary unstated) → P-6, W4.
- **DSB-18** FTI-001 §7.3's test ids predate the pytest suite; F10-001 applied node-id tails (6 marks / 7 ids) → W4, mark the report superseded.

---

## 7. Waves and gates

Layering per principle 5; every wave re-measures first (W0). Order is risk-ordered:
**03** (same macro names; typography/grammar only) → **01/04** (single macro + docs) →
**02** last (823 renames, new colours, 607-line semantic pass); each repo completes its
own gates before the next starts.

Semantic-pass rule for W3: a name functioning as a witness id stays inside the mark or
`\testref`; only genuine code mentions take `\code`. Decorations/accounting route to
§3.7/P-5; anything unclassifiable goes to §6, never guessed.

| wave | layer | content (recon/report figures, re-measured at W0) | gates to exit |
|---|---|---|---|
| **W0** measure freeze | read-only | re-run the census on all five HEADs; reconcile with §2 (02's docs changed post-recon: `2e76bbe`) | deltas vs §2 explained in the report before W1 |
| **W1** preamble/defs | preamble only | 02 gains tag colours + guarded `\tiercol`; 03 guards `\tiercol`; grammar per P-7; 05's dead comment fixed; dead definitions flagged | G-1 with 0 new warnings; G-9 no visual change; diff touches preambles/comments only |
| **W2** mechanical renames | body, no judgment | 03: `\tier` 101 + `\witness` 123 · 02: 823 tag lines + `\lean` 15 + 6 empty groups · 01: `\lean` 83 · 04: `\lean` 75 · ≈1 099 lines | grep before/after match per repo; G-1…G-5, G-7…G-9 (colour present in 02; ids at 13/15 in 03) |
| **W3** semantic pass | judgment, site by site | 02: `\LeanInline` 607 lines + `\leanline` 67 + Star/Tally/CW 232 + 6 raw `°/†` · 01: raw `Lean:` 2 · 04: 5–9 · 03: 23 ids + bare branch · family: 244 verdicts, caption tag 1, empty groups 6, `appendix:446`, open-tier (§3.9) | ledger rows = grep count; S5 rows land in §6; full G-8 per repo; no decision outside a §4 row |
| **W4** docs | documentation | contract home per P-8; copies or declared deferrals; 01's §8 aligned to what it prints; 02 gains its three missing documents; `usage.md` §Counts joins the census; SPEC-004 manifest amended | G-4 with the contract file pinned; docs-parity green; R-7 bijection greps return ∅ |
| **W5** family gates | verification | full gate sweep in five repos; byte-parity of pinned files; first `wit-lint` run (live implementations per function = 1) | G-1…G-10 all exit 0; `wit-lint` report attached; tree clean |

Gates, one line each: **G-1** `build` exit 0, 0 undefined references, no new warning
class · **G-2** `counts:check` · **G-3** `selfcitations:check` · **G-4** `manifest:check`
(21 files today, + contract after W4) · **G-5** `parity.ts` · **G-6** `type-check` ·
**G-7** `pytest` green (02: 94 tests incl. `test_witness_census.py`) · **G-8**
`validate` · **G-9** `pdftotext` spot-check + FOCUS-B-style size/colour measurement vs
canonical parameters · **G-10** wave report with before/after counts, ledger rows and
real exit codes. (`wit-lint` is specified here by R-1/R-3; not built yet.)

---

## 8. Document reconciliation (executed in W4)

| document | current state (measured 2026-11-23) | destination |
|---|---|---|
| `citations.md` §8 | 05 canonical 25 108 B · 01 = 03 24 476 B older copy · 04 absent (ends §7) · 02 adapted port 21 715 B | contract text under P-8; 01/03 copies replaced by verified propagation or a one-line deferral; 04 keeps its deferral; 02 matches the text or declares its divergence in one header line |
| `citations.md` §3 | preamble contract (`nyt`, `giveninits`, biber); 02 aligned (§3.4) | states per-repo reality; no third state |
| `witness-contract.md` | **01 = 03 = 05 byte-identical, 24 236 B — pinnable today**; 02's port 24 730 B | pin in `scripts/shared-files.json` (R-10); 02 returns to the generic text or carries a declared reason for exclusion |
| `usage.md` §Counts | family mechanism | witness census joins the measured numbers (R-6): regenerated, never typed |
| 01's §8 | documents `\tier`/`\witness`/`\testref`, implements none (L1) | aligned under P-13: adopt, or become a deferral like 04's |
| 04's §8 / style-guide | explicit deferral to 05, link target stated | kept; link verified against P-8's home |
| 02's docs | three family documents absent (DSB-8); two stale claims (OI-11) | gain `style-guide.md`, `docs/style/grammar.md`, `docs/figures.md`; stale claims corrected |
| `scripts/shared-files.json` (SPEC-004 §3) | pins 21 files; contract not among them | amended in W4; `manifest` regenerated and committed in all five repos |

h1/h2/h3 and the propagation mechanism are row P-8; the `witness-contract.md` pin does
not wait on it.

---

*Consolidation of `WIT-SPEC-001_draft.md` (retained as the first-pass record) from the
inputs listed above; rulings as recorded in MRG-001 §13 (2026-11-23). No repository was
modified; nothing was migrated; §4 rows are undecided by design.*
