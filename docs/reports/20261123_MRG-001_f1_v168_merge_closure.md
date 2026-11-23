# MRG-001 — Closure of the v168 merge (phases F0 → F11b, closed by F6/F7)

| Field | Value |
|---|---|
| **id** | `MRG-001` |
| **title** | Closure of the `F1_v168` merge into `02-odd-zeta`: final gate record per phase, the closing census, the registry correction, the open items and the two presentation decisions left to the author |
| **status** | report only — this document changes no content; every change it records is in its own commit |
| **date** | 2026-11-23 |
| **version** | 1.0 |

**Scope.** Repository `02-odd-zeta`, from the pre-merge rest state (`F0`) through the
F11b wave (`166934d`) and the closing F6/F7 wave of this report (usage correction,
typesetting of tags in displays, docs ports, housekeeping, this report). It records
what was measured, with the source of each measurement. It deliberately does **not**
touch `lean/`, `.release-it.ts`, `citation.csl.json`, `package.json`, `scripts/*`, the
author's `[3·10⁷]` clause, any claim or prose outside the wave's scope, or any sibling
repository (read-only checks only).

---

## 1. Fold F0 → F11b: what landed and the gate of each phase

| phase | what landed (commits) | gate evidence |
|---|---|---|
| **F0** base/rest | read-only baseline on `origin/main`; diff artefacts in `scratch/` | rest `validate` **exit 0** — `scratch/02-gates.log`: `counts ✓`, `COUNTS_EXIT=0`, `TYPECHECK_EXIT=0`, `lake build` 6 378 jobs, `VALIDATE_EXIT=0` |
| **F1** `.tex` port | `1fff369` `feat(paper)!` (BREAKING CHANGE footer) · `f028985` build · `8a68e76` D7 markers · `ea0b91d` build | build exit 0 with **0** `undefined` reference/citation in `build/main.log`; `tsc --noEmit` and `parity` green in the same gate run (`scratch/02-gates.log`) |
| **F2** bibliography | `f09f532` v168 reference set · `ee98076` CIT-003 report · `0e026ab` build | biber resolves the whole set: **179 records**, CIT-003 (49 corrections, 6 declared unverifiable); `selfcitations:check ✓` in the rest gate |
| **F3** Lean | `5c41bf5` toolchain 4.36.0-rc2 + Mathlib `a8754b18` · `db849c6` import · `e2404fe` repair · `53b94aa` refresh | **mixed, honest**: `scratch/f3_validate.log` ends `VALIDATE_EXIT=1` — one Lean type mismatch at `F1_pentagonal_descent_UNIFIED.lean:69404` (the orphan `same_def_24`), declared as an external blocker by F8-001 §5; resolved later by `c85e7b7`. Closing state: `lake build` **18 248 jobs, success**; `counts` `lean.axioms=0`, `lean.sorry=0` |
| **F4** scripts/data | `8a68e76` `pending(D7)` markers (deferred by D7) | superseded in substance by **F10** (the self-baked script deleted, 94-test suite green); `verify:py` exit 0 in both states |
| **F5** identity | `7c8cf4e` byline provenance order · `a2395a8` title chain · `e10d9ed` build | `parity ✓` + `selfcitations:check ✓` (rest gate; `scratch/gate_05b.log` `EXIT=0`) |
| **F8** witness reconciliation | `c87fed1` `N[ids]` device + 6 marks · `39e4585` build · `50d5aae` report · `c85e7b7` drop orphan `same_def_24` | F8-001 §4: build exit 0, `counts` no drift, `counts:check`/`selfcitations`/`parity`/`manifest`/`type-check`/`verify:py` ✓; `validate` exit 1 **only** on `verify:lean` (the declared blocker above); each of the 7 ids verified verbatim against a running test |
| **F9** provenance | `e62d1b5` F9-001 (+ addendum `64e283c`/`6a337a5`) | F9-001 *Gates*: `validate` **exit 0**, `type-check` **exit 0**, tree clean (`scratch/f9_validate3.log`: 18 248 jobs success) |
| **F-TIERS** | `b815a51` FTI-001 (+ `6280a4c` correction to 46 bare-N sites) | FTI-001: `validate` **exit 0** (18 248 jobs), `type-check` **exit 0** (`scratch/fti_validate_final2.log`) |
| **F12** author pass | `fd45327` three of four paragraphs · `9a16c41` `hipotesis/pruebas` corpus · `6a337a5` report · `5ba9db9` build | build regenerated for the wave (`5ba9db9`); the fourth paragraph left intact by design (see §4/§8); no counts drift |
| **F10** pytest suite | `13ce8d9`·`17f8cf6`·`7f80293`·`47824b8`·`60e8786`·`6835d17`·`71561a5`·`0258c9a` | F10-001 §7 (all exit 0): `selfcitations` ✓ · `parity` ✓ · `counts:check` ✓ · `manifest:check` ✓ · `verify:py` **94 passed** · `lake build` 18 248 success · `tsc` ✓ · `validate` **exit 0** |
| **F11a** mechanical tier migration | `45db7ef`·`5d09fd9`·`b3ce355` | build regenerated for the wave (`b3ce355`); counts and census green afterwards |
| **F11b** tier decisions + author paragraph 3 | `1dcaa33` gloss to first body use · `209c09e` §6.2 decisions · `0b0f750` segmented law-resolution figures · `166934d` build | `scratch/f11b_validate_final.log`: `selfcitations ✓` · `parity ✓` · `counts:check ✓ (94/94/5712/0/0/0)` · `manifest ✓` · **94 passed** · `lake build` **18 248 jobs, success** · `tsc` ✓ → **exit 0**; PDF 168 pp |
| **F6/F7** closing wave (this report) | `e2beaa7` usage §Counts · `78e4eb8` tags in displays · `4645911` two docstrings · `2e76bbe` citations + witness contract · this report's commit · closing `chore(build)` | measured in §7 below: `build` exit 0 (168 pp, **0** undefined, warnings 97 = 96 hyperref + 1 enumitem), `counts:check` ✓, `selfcitations:check` ✓, `manifest` ✓ (21 files / 9 exclusions), `parity` ✓, `type-check` ✓, `pytest` **94 passed**, `validate` **exit 0** (18 248 jobs), `pdftotext` spot-check ✓ |

Reading of the table: no phase was closed on a green it did not have; the two
red cells (F3, and F8's `validate`) are the **same** declared Lean blocker, and
the record shows where it was closed (`c85e7b7`, before F9).

## 2. Final census (re-measured 2026-11-23, `git grep` over `main.tex` + `src/chapters/*.tex`)

| mark | occurrences (body) | per file (body) |
|---|---:|---|
| `\tierP` | **740** | 01:4 · 02:17 · 03:271 · 04:95 · 05:64 · appendix:289 |
| `\tierN` | **123** | 01:2 · 03:20 · 04:61 · 05:9 · appendix:31 |
| `\tier[\testref{…}]{N}` (marks with ids) | **6** (over **7** ids) | 02:2 · 03:3 · 04:1 |
| `\LeanInline` | **992** body (**996** total: +1 def and 3 uses inside `main.tex` macro definitions) | 01:5 · 02:23 · 03:695 · 04:227 · 05:41 · appendix:1 |
| `\LeanStar` | **221** body (**222** total: +1 def) | 03:136 · 04:59 · 05:7 · appendix:19 (lines: 99 / 54 / 7 / 13) |
| `\LeanTally` | **21** body (**22** total: +1 def) | 02:5 · 03:15 · 04:1 |
| `\LeanCW` | **44** body (**45** total: +1 def) | 02:2 · 03:3 · 05:39 |
| `\leanline` | **67** body (**68** total: +1 def) | 03:67 |
| retired classes `\tierPnew` `\tierC` `\tierO` `\tierT` `\tierNc` `\tier{R}` | **0** each | — |
| `\witness` / `\wtag` / `\Lean{}` uses | **0** | — |
| adjacent tag pairs (one-claim-one-tag) | **0** | — |
| tags inside `\caption` | **1** (`03-mechanisms.tex:1167`, `needs-decision` since F8-001 §1.3) | — |
| cited test ids pinned by `tests/test_witness_census.py` | **7** (snake_case) | — |

Counts ledger (`docs/counts.md`, regenerated by `pnpm run counts`): `pytest.collected`
**94** · `pytest.not_slow` **94** · `lean.theorems` **5712** · `lean.axioms` **0** ·
`lean.sorry` **0** · `images.files` **0**; 3 marked regions, all in `tests/README.md`.

Reconciliation of the two decoration inventories (the numbers behind recommendation α):
the F8 census had `\LeanInline` 801 and `\LeanStar` 417; today 996 and 222 —
**195 marks moved from `\LeanStar` to `\LeanInline`** in the F11 waves (195 = 417−222
= 996−801, both differences agree), and **221 `\LeanStar` uses remain**.

## 3. D5 / D7 state

- **D5 (absent artifacts, de-cited):** `MANIFEST.md`, `LEDGER_ESTADO.md`,
  `ontologia_lean/` — none exists in the tree and none is cited from `main.tex`,
  `src/` or `docs/` outside `docs/reports/` (measured this wave). They stay
  *pending possible inclusion*, with **`ontologia_lean` highlighted for review**, as
  D5 ordered.
- **D7 (deferred scripts/data):** `scratch/f1_v168/d7_pending_scripts.txt` (updated in
  the F12 wave) now lists **42 scripts** (from 76; F12 imported `hipotesis/pruebas/`
  with **38 `.py` + 35 `salidas/*.txt`** and cleared 34 entries). The manuscript still
  carries **68 `pending(D7)` markers** (`03-mechanisms` 13 · `04-bridges` 30 ·
  `appendix` 25). Nothing of D7 entered this merge.

## 4. Registry correction: F11b's laguna 6 is FALSE

F11b recorded a laguna claiming *“otros tres párrafos con cifras viejas”* (three more
paragraphs with stale figures). **Verified false** this wave, with `pdftotext` over the
built `build/document-v1.7.2.pdf` (2026-11-23) and `git grep` over `src/chapters/*.tex`:

| author-pass paragraph (F12-001) | new state in the PDF | old figures in the PDF |
|---|---|---|
| 1 · `ssec:product-surface` (castelnuovo) | `below 1.27, 1.28 and 2.22 … at most 0.79√x` present (`1.27` ×2: this sentence and the unrelated eigenvalue bound `1.27·10⁻⁴`) | `0.80, 1.14 and 1.89` → **0 hits**; `0.80` → 0 hits in the body |
| 2 · `ssec:weil-closure` positions | `it is 0.21 spacings (n ≤ 1000; the median is 0.19)` present | `0.20` as the envelope figure → absent from that sentence |
| 3 · `ssec:weil-closure` law resolution | `the median error of the corrected operator (n = 100 to 3000) is 0.194 at …` present (`0.194`, `0.170`, `0.089`, `0.041`, `0.025` all present) | `0.183` → **0 hits**, `0.087` → **0 hits**, `0.053` → **0 hits** |
| 4 · `ssec:weil-closure` detection | `δ ≥ 0.10 at γ = 30 and δ ≥ 0.38 at γ = 100; above γ ≈ 200 no admissible δ` plus the longer-orbit row `0.001, 0.009, 0.022` present | `0.057` → **0 hits**, `0.31` → **0 hits** in the body, `0.001 at` (old phrasing) → 0 hits |

All four paragraphs of the author's pass are in their **new** state; the three extra
“stale paragraphs” the laguna asserted do not exist. The laguna is closed as false.

## 5. Open items (carried, not closed here)

1. **B2 clause `[3·10⁷]`** — **CLOSED by §11**: the author's proposed *“its maximum
   over `[3·10⁷,e¹⁸]` is 1.13, 1.07 and 1.76”* is now written and recomputed. It was
   deferred in `fd45327` only because the committed
   `hipotesis/pruebas/salidas/castelnuovo.txt` carries the segments `[1e6,1e7)` and
   `[1e7,e^18]`, not this window; §11 records the calculation that fills it.
2. **`0.087` of `law_resolution`** without reproduction, and the author's original
   detection figures `0.001 / 0.057 / 0.31` without an orbit combination — carried
   pending from F12-001.
3. **`appendix:446` — `26` open statements and `21` classical inputs** with a name:
   counts stated in prose and **irreproducible** with the tooling in the repository
   (F11b). They must be re-counted at rewrite time, never translated.
4. **Names at risk** (Mathlib names inventoried by F9-001) — classified as **process
   artifacts** of the composition layers; no content action.
5. **D7**: 42 scripts + 68 `pending(D7)` markers (§3).
6. **D5**: 3 absent artifacts, `ontologia_lean` highlighted (§3).
7. **244 own-line verdicts** (`F8-001` §2.3) and **1 caption tag**
   (`03-mechanisms.tex:1167`) — both `needs-decision`; the ported apparatus has no
   `\witness` block to move them to, and no caption rule existed in the zip.
8. **`\LeanStar` unification** — recommendation α, §6, pending the author.
9. **Bibliography settings divergence — CLOSED by the citation-standardisation wave.**
   This repository rendered with `sorting=none` and no `giveninits` (citation order, full
   given names) while the siblings render `sorting=nyt,giveninits=true`; `main.tex:22`
   now carries the family line verbatim. Verified with `pdftotext` on the rebuilt PDF:
   the 176-entry reference list is alphabetical (Apéry → Apostol → Argand → … →
   Frankenhuijsen → Frobenius → … and Montgomery → de Moura is ordered by *Moura*) and the given
   names print as initials (`J. A. González García et al.`, which printed
   `Jorge Armando González García et al.` before). `docs/citations.md` §3, §5 and §7 and
   `docs/witness-contract.md` §4.3 were rewritten to the same state in that pass.
   **Carried laguna:** 37 of the 109 DOI-bearing entries print the DOI **twice**
   (`doi:10.33571/…` from `note = {doi:…}` and `doi: 10.33571/…` from the `doi` field);
   the cause is in `citation.csl.json` (37 records carry both fields), it is
   **pre-existing** (the reference list carried 146 `doi:` occurrences before and after
   this change), and it is absent from the siblings (01/03/04: 0 entries, 05: 1).
   Reported, **not fixed**: `citation.csl.json` is outside this wave's scope. The
   duplication the §3 contract actually suppresses — a `doi.org` URL printed beside a
   DOI — is **0** entries, as in every sibling.
10. **Two stale claims — CLOSED by the docs micro-fix wave.** `docs/README.md` said
    *“the manuscript itself states no count”* and `docs/architecture.md:88` said *“this
    repository states no count in its prose, so it carries no marked region”*; both are
    false (the manuscript carries six `\tier[\testref{…}]{N}` anchors and the appendix
    states corpus counts, and the mechanism's three marked regions live in
    `tests/README.md`). Both cells were rewritten to that state; `docs/counts.md` itself
    was already correct (it lists the regions) and is generated, so it needed no edit.
11. **Generic docs referenced but absent — CLOSED by the docs micro-fix wave.**
    `docs/figures.md` is now a factual stub (this manuscript generates no figures; it
    points at `docs/counts.md` `images.files` and at row 7 of `docs/architecture.md`
    instead of restating them). `docs/style-guide.md` and `docs/style/grammar.md` were
    **not** created: `docs/reports/README.md` no longer lists them and now says why —
    the editorial style contract arrives with the witness specification (WIT-SPEC, in
    composition).
12. **Local branches kept** (see §7): `scratch/lean-release`, `scratch/granularity`.

## 6. Two presentation decisions left to the author (NOT executed)

**α — `\LeanStar` (221 uses) vs `\LeanInline` (996 occurrences).** The F11 waves
converted 195 of the 416 pre-compilation star marks into plain `\LeanInline`; **221
`\LeanStar` uses remain** (03:136 · 04:59 · appendix:19 · 05:7, plus the definition in
`main.tex`). `F9-001`'s dictamen is that every starred name is present in the compiled
file (416/416, comments stripped) and that the star records **pre-compilation
provenance — a process artefact of the build, not a tier**; the modules compile in the
green build (`validate` exit 0, `lake build` 18 248 jobs). *Recommendation:* unify the
remaining 221 `\LeanStar` into `\LeanInline` and let provenance live in the source map
and the reports, **or** keep the star as a declared provenance decoration and say so in
the gloss; either way the counts above are the evidence to decide from. **Not executed —
it rewrites 221 sites of prose decoration and is the author's call.**

**β — the tally (`\LeanTally` × 21) beside the inline names (`\LeanInline` × 996).**
The `°` tally certifies *a count over an enumerated type*, not a classification, and it
is defined in one sentence at its first use (`02-foundations.tex:137`). It marks 21
sites (02:5 · 03:15 · 04:1) against 996 occurrences of the plain inline name — a ratio
of about 1:47. *Recommendation:* keep the `°` as the only decoration besides `*`/`†`
(its first-use sentence already carries the explanation), and state its census — 21
sites — wherever the apparatus is summarised, so the reader can find every tally with
one grep; alternatively fold the 21 into `\LeanInline` and keep the count in prose where
the classification is claimed. **Not executed — presentation only.**

## 7. Final gates of the closing wave (F6/F7), measured 2026-11-23

| gate | result |
|---|---|
| `pnpm run build` | **exit 0** — `build/document-v1.7.2.pdf`, **168 pages**, `2 015 251` bytes; `checksums.txt`, `CITATION.cff`, `.zenodo.json`, README regions regenerated |
| `build/main.log` warnings | **97** total = 96 `Package hyperref Warning` (pre-existing: *token not allowed in a PDF string*) + 1 `Package enumitem Warning`; **0** `undefined` references/citations |
| the five `Command \Small invalid in math mode` warnings | **0** (were 5 before `78e4eb8`; total warnings 102 → 97, i.e. no new warning of any kind) |
| `pnpm run counts:check` | **exit 0** — 3 regions + `docs/counts.md` match (94 / 94 / 5712 / 0 / 0 / 0) |
| `pnpm run selfcitations:check` | **exit 0** |
| `pnpm run manifest:check` | **exit 0** — 21 shared files, 9 documented exclusions |
| `pnpm exec tsx scripts/tasks/parity.ts` | **exit 0** |
| `pnpm run type-check` | **exit 0** (`tsc --noEmit`) |
| `uv run pytest tests/ -q` | **94 passed** in 1.50 s |
| `pnpm run validate` | **exit 0** — `selfcitations ✓ · parity ✓ · counts:check ✓ · manifest:check ✓ · verify: 94 passed + lake build 18 248 jobs success + tsc ✓` |
| `pdftotext` spot-check | title, byline (four authors in provenance order) and abstract render correctly on page 1 |
| working tree | clean after the wave's commits; no tags created; nothing pushed outside this repository |

## 8. The two decisions already closed in this merge

1. **Author paragraph 3 (law resolution) — segmented ✅.** Applied in `0b0f750`
   (*adopt the segmented law-resolution figures from the author pass*): the five window
   medians are printed as the artifact's fixed-window row, with the scale sentence
   rewritten. Verified in the PDF (`0.194 … 0.025` present, `0.183/0.087/0.053` absent —
   §4).
2. **B2 clause `[3·10⁷]` — ⏸ deferred, then ✅ written (§11).** Deferred in
   `fd45327` because the values are not in `castelnuovo.txt`; carried as open item 1 of
   §5 until the recalculation of §11 confirmed the author's figures and the clause
   landed in `src/chapters/04-bridges.tex`.

## 9. `galois-decoration` (outside this repository)

Read-only check, 2026-11-23: `/mnt/media/dev/galois-decoration` — working tree **clean**,
`main` at `274eead` = `origin/main` (*import the Galois Decoration of Positional Numeration
mini paper and its Lean development*), single-commit history, no stale worktrees or
branches observed. Nothing of it was touched; it is reported, per MERGE_PLAN §F7.

## 10. Housekeeping performed in this wave

- **Worktrees:** the seven stale `wt02_*` worktrees (`wt02-main`, `wt02_f1`, `wt02_f2`,
  `wt02_f3`, `wt02_f8`, `wt02_fix`, `wt02_same`) were removed with `git worktree remove`
  after verifying each was clean and at a commit that is an **ancestor of `main`**, then
  `git worktree prune`. `git worktree list` now shows only the primary checkout.
- **Branches:** **none removed.** Evidence check: `scratch/lean-release` carries **46
  commits not in `main`** (including an unadopted `compile.ts` hardening, an unadopted
  `sorting=nyt,giveninits` preamble change, an old `tests/README.md` and a
  `lean/release/` tree) and `scratch/granularity` carries **16** — neither is merged
  (`git merge-base --is-ancestor` false; `git cherry` shows all patches unique), so
  neither meets the *merged or dead* bar. MERGE_PLAN §F7 also requires `lean-release` to
  be **archived by a push before deletion** and orders `granularity` to be *reported, not
  deleted without an order*. Both are therefore reported here and left in place; no
  `push --delete` was performed.

---

## 11. Addendum (2026-11-23): the B2 clause `[3·10⁷,e¹⁸]` — calculated and confirmed

**What was deferred, and why.** Open item 1 of §5 deferred the author's clause
*“its maximum over $[3\cdot10^7,e^{18}]$ is $1.13$, $1.07$ and $1.76$”* because the
committed artifact `hipotesis/pruebas/salidas/castelnuovo.txt` reports the segments
`[1e6,1e7)` and `[1e7,e^18]` only — the window `[3·10⁷,e¹⁸]` appears in no committed
output. That reason is gone: the window has now been computed.

**Method (the author's, with the window added).** Exactly the semantics of the
author's `hipotesis/pruebas/castelnuovo.py`: sieve the primes up to `int(e^18)`,
build every prime power `p^k ≤ e^18`, form
`ψ(x,χ) = Σ_{n≤x} Λ(n)χ(n)` as a cumulative sum of `log p` weighted by the character
(`χ₄`, `χ₅`, `χ₂₀ = χ₄χ₅`), and take `max |ψ(x,χ)|/√x` over the prime powers `x` of
`[3·10⁷, e^18]`. Evaluating at the prime powers *is* evaluating the maximum: `ψ` is
constant between consecutive prime powers (Λ vanishes elsewhere) and `√x` grows, so
each step attains its maximum at its left end — the argument the script's own
docstring makes. The script itself was **not** modified; the window is an addition
made by this calculation, both in the manuscript test and in the orchestrator's run.

**Exact figures recomputed:**

| character | recomputed `max_[3·10⁷, e^18]` | printed (2 decimals) |
|---|---:|---:|
| `χ₄` | **1.132056** | 1.13 |
| `χ₅` | **1.069538** | 1.07 |
| `χ₂₀` | **1.763632** | 1.76 |

**Conclusion: the author's clause is confirmed** — 1.13 / 1.07 / 1.76 are the
two-decimal roundings of the recomputed maxima, so the sentence is written verbatim
in `src/chapters/04-bridges.tex` (`ssec:product-surface`).

**Where the calculation now lives.** `tests/test_golden_observations.py`
(`test_castelnuovo_window_maxima`) re-derives the three maxima from scratch — sieve,
prime powers and characters inside the test, no script imported — and asserts them
against 1.13 / 1.07 / 1.76 with `_WINDOW_TOL = 5e-3`, a **printing** tolerance: half
of the last digit the manuscript prints (two decimals), not a golden comparison like
the `1e-12` used for the committed artifacts. Runtime measured **4.00 s**, below the
10 s threshold, so the test carries **no `slow` marker**.

**Still open (untouched by this addendum):** the author's `0.087` of `law_resolution`
and his original detection figures — open item 2 of §5, carried as before.

---

## Related documents

- `docs/reports/README.md` — reports convention and index (this report's row, plus the
  F8-001 row added in this wave).
- `docs/reports/20261122_F8-001_witness_reconciliation.md`,
  `20261122_F9-001_provenance_inventory.md`, `20261122_FTI-001_tier_uses_migration_map.md`,
  `20261123_F10-001_pytest_suite_port.md`, `20261122_F12-001_author_text_changes_v168.md`,
  `20261121_CIT-003_v168_citation_verification.md` — the per-phase records folded here.
- `docs/citations.md` §8, `docs/witness-contract.md` — the witness contract this
  manuscript applies (ported in this wave).
- `docs/counts.md` — the measured counters quoted in §2.
