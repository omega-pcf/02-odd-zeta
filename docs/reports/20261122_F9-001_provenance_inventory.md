# Provenance inventory of the literal corpus filenames cited by the manuscript

| Field | Value |
|---|---|
| **id** | `F9-001` |
| **title** | Provenance inventory of every statement that cites a literal corpus filename (Source map, column corpus, annexes, body) |
| **status** | report only — no manuscript, script or test changed |
| **date** | 2026-11-22 |
| **version** | 1.0 |

**Scope.** `02-odd-zeta` at `623c20a` (`origin/main`, read-only worktree). F9 of the merge plan
is pure inventory: zero prose. Every literal filename cited as a corpus file by the tracked
manuscript (`main.tex` + `src/chapters/*.tex`, 983 `\texttt{…}` occurrences scanned) is a row
below, with what names it, where it was checked, and its status. What this report deliberately
does not touch: `main.tex`, `src/chapters`, `lean/`, `scripts/`, `tests/`, `package.json`.

## Method

Three independent existence checks per name:

1. **Repository** — `git ls-files` for paths; for the Lean corpus blocks and modules, the
   headers of `lean/F1_pentagonal_descent_UNIFIED.lean` (`-- BLOCK n. <file>.lean`, the
   `namespace` declarations, the `F1Paper/<file>.lean` comment paths) and word-boundary search
   in the file with `--`/`/- … -/` comments stripped (a mention inside a comment is recorded
   as such and does **not** count as an existing file).
2. **Author's zip package** (`F1_v168_completo/`) — full tree walk (78 files) plus both tables
   of its `MANIFEST.md` (the cited-and-shipped table, and the "cited and not available in this
   session" list).
3. **D7 deferrals** — the `d7_pending_scripts.txt` list *and* the manuscript's own
   `% pending(D7)` markers (103 lines), which are a separate, line-scoped signal.

Excluded from the rows: Lean **declaration** names (the Status ledger's Declaration column —
not filenames), the Mathlib names at risk (reclassified below), LaTeX comments, and the preamble's
`\addbibresource{src/bibliography.bib}` (a build input of this repository, present at that
path).

## Counts

| status | rows | distinct names |
|---|---|---|
| verificado (repo) | 138 | 71 |
| verificado (zip, no portado) | 1 | 1 |
| deferido-D7 (`% pending(D7)` marker) | 153 | 82 |
| NO IDENTIFICADO (`hipotesis/pruebas/`) | 2 | 1 |
| NO IDENTIFICADO (`F1Paper`, Lake project name) | 1 | 1 |
| **total** | **295** | **156** |

Split by kind: **160 rows / 85 distinct** are filenames with an extension or a path
(`.py`, `.lean`, `.md`, `.txt`, `.json`, directories); **135 rows / 71 distinct** are corpus
block or module names cited as files (Lean audit "Files and roles", the Source map's Corpus
column, and the same names cited in the body).

Cross-cutting signals (a name can carry more than one): 93 distinct names carry a D7 signal
(82 marked `% pending(D7)` in the manuscript, all 76 entries of the D7 list cited, 6 marked but
absent from that list — the list is `.py`-only); 48 distinct cited names exist in the zip
(traceable provenance, deferred from this merge); 0 names are D5 (`MANIFEST.md`,
`LEDGER_ESTADO.md`, `ontologia_lean/` are de-cited as D5 ordered — no row, confirmed).

## The NO IDENTIFICADO names

Only two of the 156 distinct names cannot be resolved, and both are structural rather than
missing data:

1. **`hipotesis/pruebas/`** (`appendix.tex:451`, `:502`, `:650`) — the directory the annex
   names as the home of the numerical scripts of `sec:results-verdict`. Absent from the
   repository, absent from the zip (which re-packages those scripts under `scripts/`, an
   equivalence inferred from the matching filenames, never declared), absent from the D7 list.
   Dictamen: **ruta de origen no portada** — the directory itself is not an identifiable
   artifact; its members are individually cited and are D7/zip-backed. Not a missing file claim,
   an unported path.
2. **`F1Paper`** (`appendix.tex:337`, "The same content is also a Lake project, `F1Paper`") —
   the repository's Lake project is `name = "odd_zeta"` with library
   `F1_pentagonal_descent_UNIFIED`; the zip ships no lakefile at all. The token `F1Paper/`
   survives only as a source-path prefix inside the unified file's comments
   (`F1Paper/PhiCelda.lean`, `F1Paper/W4Isometria.lean`). Dictamen: **nombre de proyecto heredado
   del paquete, sin counterpart en el repo** — recorded, not corrected (prose is frozen).

Two further tokens are resolved by inference and flagged as such in their row: the bare
`scripts` and `certificates` of the Source map (`appendix.tex:649`, `:650`) map to the zip's
`scripts/` and `scripts/weil_certificates/`.

## The `*` marks — dictamen each

| mark | occurrences | recheck at `623c20a` | dictamen |
|---|---|---|---|
| `\LeanStar{…}` | 416 (268 sites) | **416 / 416 present** in the compiled file (comments stripped; 13 apparent misses were `\ensuremath{ψ,ω,ι,φ,σ}` forms that resolve after Unicode normalisation) — matches `f3_guard_report.json` (`LeanStar` 416 ok, 0 absent) | **artefacto del proceso**: the mark is the pre-compilation state ("written for this version, not yet compiled"); the modules are compiled in the green build (`validate` exit 0, `lake build` 18 248 jobs). `P* → P` is the F11/D4 reconciliation, not content. |
| `\LeanCW{…}` | 44 | **43 absent, 1 present** (`Omega_eigenvalues`) — matches the guard (`LeanCW` 44 / 1 ok / 43 absent) | **fuente externa no portada, por diseño**: the CW development is not part of the file and the manuscript says so (`appendix.tex:384`–`389`); the `†` names are that paper's. Not a process artifact, a declared external dependency. |
| `\LeanTally{…}` | 21 | 21 / 21 present | verified. |
| `\texttt{trZeta\_*}` (`appendix.tex:93`) | 1 | wildcard over declarations, not files: 6 `trZeta_*` declarations exist in the file | verificado — resolvable family shorthand. |
| `\texttt{F1PaperNew.*\_holds}` (`appendix.tex:117`) | 1 | 25 `*_holds` declarations exist in the block | verificado — resolvable family shorthand. |
| the `*` attached to declarations of the not-yet-compiled modules (`appendix.tex:368`) | — | same population as `\LeanStar` | artefacto del proceso (same verdict as the first row). |

No filename in the manuscript carries an asterisk: every `*` in the file names is a
declaration-family wildcard, and every `\LeanStar` resolves.

## Mathlib names at risk → artefactos del proceso

The 71 `\texttt{…}` tokens of `appendix.tex:467`–`492` (Mathlib lemmas, tactics and the
`type_of%` elaborator to be checked against the build's Mathlib) are reclassified here as
**process artifacts**: a pre-compile checklist layer of the composition, with no case as
permanent content once the build compiles against the pinned Mathlib `a8754b18`. The final
presentation of the subsection is an F7 decision; nothing is changed now. (No per-name audit
against the pinned Mathlib was run in F9 — that would be a build-time check, not an inventory.)

## Source map / column corpus — what the evidence marks

*Refactor-candidate signals* (evidence only, no proposal — the refactor stays deferred until
every statement is confirmed):

- The Corpus column mixes five vocabularies in 49 rows: full block names
  (`F1_PCF_session_modules`), abbreviations (18 rows: `F1_compilado`, `M12`, `08_18`,
  `PCF_granularity`, `F1_v2`, `F1_spectra_anchor_G` — each mapped to its block in the table),
  directories (`scripts`, `certificates`, `hipotesis/pruebas`), a data file (`fqn_map.json`)
  and one declaration (`F1PaperNew.triad_isometry`).
- The same names are listed on three annex surfaces (Lean audit "Files and roles" 127 rows,
  Source map 49, the numerical-scripts paragraph) *and* again in the body — `oz_carried.py`
  appears at 9 sites, `weil_window_chi5.py` at 6, `F1_pentagonal_descent_UNIFIED.lean` at 4.
- 2 names are unresolvable as stated (`hipotesis/pruebas/`, `F1Paper`), and 11 **repo-verified**
  names inherit a D7 marker from the line-scoped `% pending(D7)` at `appendix.tex:650`
  (`EstructuraEnGUE`, `F1PaperClosure`, `F1PaperHyp`, `F1PaperPadic`, `F1PaperPending`,
  `F1PaperTorus`, `F1_cw_equivalents`, `F1_v2`, `F1_weil_functional`, `W4Isometria`,
  `certificates`) — the marker marks the row, not those files.

*Untouchable on this evidence*:

- The whole deferred set — 82 distinct names / 153 rows are D7; the operator's precondition
  "todos los statements confirmados" is not met until F4/D7 resolves them.
- The "Source in the companions" column and the **Comparative landscape** table: **0 filename
  rows** — they cite companion papers and literature, so this inventory finds nothing to
  reconcile there.
- The Status ledger's Declaration column: declarations, not filenames; they are pinned by the
  census and the guards, not by this report.

## Gates

- `pnpm run validate` at rest: **exit 0** (`selfcitations:check && parity && counts:check &&
  manifest:check && verify`, including `lake build` — 18 248 jobs, "Build completed
  successfully").
- `pnpm run type-check`: **exit 0**.
- The tree was clean before and after; this commit carries the report and its index row only.

## Lagunas

- The F3 guard report predates F8: its `LeanInline` total is 797 against 800 occurrences now
  (`LeanStar` 416, `LeanCW` 44, `LeanTally` 21 agree exactly). The inline drift is unexplained
  here and belongs to the F8/F11 reconciliation, not to this inventory.
- The equivalence `hipotesis/pruebas/` ↔ the zip's `scripts/` is inferred from identical
  filenames; no document in the repo or the zip declares it.
- The zip's own "cited and not available" list (41 files) is the author's declaration; every
  one of them is inside the D7 set above, and none was independently located elsewhere.
- Block numbering verified while checking names: 28 numbered `BLOCK` headers (the 27 blocks
  plus the paper block) and 26 session blocks labelled S1–S27 with S14 unused — consistent with
  the manuscript's "twenty-seven blocks" and "twenty-six modules … blocks S1–S27".
- `\LeanInline` was not re-audited name-by-name in F9 (only counted); the guard's 797/797 is
  the last per-name result on record.

---

## Related documents

- `docs/reports/20261122_F8-001_witness_reconciliation.md` — the witness pass that precedes this one.
- `docs/counts.md` — the living counters this report does not modify.

---

## Appendix A — filename rows (extension or path): 160 rows / 85 distinct names

| # | filename | claim / statement that names it | site | section | in repo | in zip | D7 | status |
|---|---|---|---|---|---|---|---|---|
| 1 | `F1_pentagonal_descent_UNIFIED.lean` | F1_pentagonal_descent_UNIFIED.lean, whose last block is the paper itself: a | `src/chapters/01-introduction.tex:271` | Introduction / Protocol | lean/F1_pentagonal_descent_UNIFIED.lean | lean/F1_pentagonal_descent_UNIFIED.lean | - | verificado (repo) |
| 2 | `v27_reloj_ciclotomico.py` | (v27_reloj_ciclotomico.py, ), and (vii), whose ratio to the main term is | `src/chapters/03-mechanisms.tex:1425` | The clock and the cyclotomic polynomials | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/v27_reloj_ciclotomico.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 3 | `retro69.py` | (retro69.py ). | `src/chapters/03-mechanisms.tex:1427` | The clock and the cyclotomic polynomials | - | scripts/retro69.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 4 | `retro119.py` | (retro119.py ); the first two, $47$ inert and $139$ split, are TodoEnLean.witness_47, | `src/chapters/03-mechanisms.tex:1508` | The classes and the angular part of $$ | - | scripts/retro119.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 5 | `retro94.py` | (retro94.py ). | `src/chapters/03-mechanisms.tex:1545` | The classes and the angular part of $$ | - | scripts/retro94.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 6 | `retro78.py` | and the two exchanged parts of the prime side coincide (retro78.py ). | `src/chapters/03-mechanisms.tex:1648` | Residue symbols and the index of $$ | - | scripts/retro78.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 7 | `v28_hiperbola_reloj_tamano.py` | (v28_hiperbola_reloj_tamano.py) . | `src/chapters/03-mechanisms.tex:1696` | Residue symbols and the index of $$ | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/v28_hiperbola_reloj_tamano.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 8 | `kisin.py` | Kubota--Leopoldt interpolation (kisin.py) . | `src/chapters/03-mechanisms.tex:2163` | The fundamental formula and the regulator $R_K = $ | no existe como archivo en repo (mencionado en comentarios del .lean) | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 9 | `oz_carried.py` | (oz_carried.py ); | `src/chapters/03-mechanisms.tex:2233` | The pentagonal determination of the odd zeta values | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 10 | `oz_carried.py` | $40$ digits, oz_carried.py ); and $L(s,)$ is the Hurwitz sum divided by $5^s$. Both | `src/chapters/03-mechanisms.tex:2257` | The pentagonal determination of the odd zeta values | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 11 | `oz_carried.py` | (oz_carried.py ), and with $=5(/2)$ and $5=2-1$ | `src/chapters/03-mechanisms.tex:2291` | The pentagonal determination of the odd zeta values | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 12 | `verify_odd_zeta_pcf_unified.py` | script verify_odd_zeta_pcf_unified.py). | `src/chapters/03-mechanisms.tex:2487` | The data of the determination | tests/verify_odd_zeta_pcf_unified.py | - | - | verificado (repo) |
| 13 | `oz_carried.py` | oz_carried.py ). | `src/chapters/03-mechanisms.tex:2522` | The data of the determination | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 14 | `retro109.py` | by retro109.py for the primes below $400$ ; in (iii), the passage from trigonometric polynomials to | `src/chapters/03-mechanisms.tex:3563` | One operator, several forms | - | scripts/retro109.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 15 | `retro104.py` | functions, the spectral theorem ; in (iii), that a unitary character factors through the abelianisation ; (iv) also retro104.py | `src/chapters/03-mechanisms.tex:3620` | One operator, several forms | - | scripts/retro104.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 16 | `retro105.py` | (ii) also retro105.py ; the classes of (ii) are Dyson's dyson62threefold | `src/chapters/03-mechanisms.tex:3667` | One operator, several forms | - | scripts/retro105.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 17 | `unfold_by_conductor.txt` | unfold_by_conductor.txt). The conductor, derived in | `src/chapters/04-bridges.tex:108` | The zeros select the conductor | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 18 | `chi5_zeros.py` | $$ shows a sector, a doublet, or the multiplicity six of an operator of the level (chi5_zeros.py, | `src/chapters/04-bridges.tex:176` | The zeros select the conductor | - | scripts/chi5_zeros.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 19 | `retro105.py` | retro105.py ). If the zeros of $L(s,)$ are the spectrum of a self-adjoint operator, the data | `src/chapters/04-bridges.tex:177` | The zeros select the conductor | - | scripts/retro105.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 20 | `verify_weil_chi5.py` | both sides agree to $10^-18$ (verify_weil_chi5.py, ). | `src/chapters/04-bridges.tex:385` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/verify_weil_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 21 | `weil_window_chi5.py` | eigenvalue. Then (, weil_window_chi5.py): | `src/chapters/04-bridges.tex:429` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_window_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 22 | `weil_window_chi5.py` | $10^-6$ at $2$; weil_window_chi5.py); | `src/chapters/04-bridges.tex:435` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_window_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 23 | `weil_window_rigorous_check.py` | (weil_window_rigorous_check.py); the value $(12)=-_E-22$ it | `src/chapters/04-bridges.tex:459` | Correspondence between Weil and PCF / The Weil route: positivity in windows | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/weil_window_rigorous_check.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 24 | `verify_iv.py` | the Weil form of $L(s,)$ satisfies $Q(f)0.0445,\|f\|^2$. computer-assisted in interval arithmetic, with outward rounding (rmk:rigour); cert... | `src/chapters/04-bridges.tex:499` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/verify_iv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 25 | `weil_certificates/cert_L1.0.json` | the Weil form of $L(s,)$ satisfies $Q(f)0.0445,\|f\|^2$. computer-assisted in interval arithmetic, with outward rounding (rmk:rigour); cert... | `src/chapters/04-bridges.tex:499` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/cert_L1.0.json | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 26 | `verify_rig.py` | The earlier double-precision replay (verify_rig.py, Lipschitz cells) gave $0.0431$. | `src/chapters/04-bridges.tex:523` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/verify_rig.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 27 | `weil_certificates/op_rig_validated.py` | $0.0261$. computer-assisted with validated numerics: every rounding error bounded explicitly and the top eigenvalue bounded by a verified... | `src/chapters/04-bridges.tex:529` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/op_rig_validated.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 28 | `rigW.py` | library routine, only bounded below (rigW.py), and its monotonicity lets | `src/chapters/04-bridges.tex:558` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/rigW.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 29 | `op_rig_validated.py` | evaluated quantity is subtracted. The pointwise certificate at $L=1$ is replayed in interval arithmetic with outward rounding (verify_iv.... | `src/chapters/04-bridges.tex:561` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/op_rig_validated.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 30 | `verify_iv.py` | evaluated quantity is subtracted. The pointwise certificate at $L=1$ is replayed in interval arithmetic with outward rounding (verify_iv.... | `src/chapters/04-bridges.tex:561` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/verify_iv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 31 | `cert.py` | $-0.573$ (cert.py, ). The replaced sequence is not the character of any $L$-function, so this | `src/chapters/04-bridges.tex:579` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/cert.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 32 | `cert.py` | positivity. The certificate method reaches $L=1.08$ (margin $0.013$, cert.py, ); beyond, | `src/chapters/04-bridges.tex:583` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/cert.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 33 | `weil_window_chi5.py` | weil_window_chi5.py, zeroside_check.py, ), because the | `src/chapters/04-bridges.tex:607` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_window_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 34 | `zeroside_check.py` | weil_window_chi5.py, zeroside_check.py, ), because the | `src/chapters/04-bridges.tex:607` | Correspondence between Weil and PCF / The Weil route: positivity in windows | - | scripts/weil_certificates/zeroside_check.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 35 | `testGeom.py` | Kolmogorov--Smirnov $p$-values between $0.14$ and $0.69$ (testGeom.py ). Its | `src/chapters/04-bridges.tex:874` | W1--W2. The fluctuation as geometry | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 36 | `testB1b.py` | requires $p$ to precision $1/T$ (testB1b.py ); its law is fixed by the | `src/chapters/04-bridges.tex:876` | W1--W2. The fluctuation as geometry | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 37 | `dh.py` | its inverse grow like $y^0.788$, those of $$ like $y^0.443$ (dh.py ). | `src/chapters/04-bridges.tex:909` | W1--W2. The two sides of the structure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 38 | `mertens341.py` | $0.9$ (mertens341.py ). What would join them is the bound | `src/chapters/04-bridges.tex:914` | W1--W2. The two sides of the structure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 39 | `mobius.py` | mobius.py ), while the direct side is bounded by a constant. | `src/chapters/04-bridges.tex:917` | W1--W2. The two sides of the structure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 40 | `retro99.py` | (retro99.py ). What it lacks is on the prime side: the coefficients of $-L'/L$ of an Euler | `src/chapters/04-bridges.tex:923` | W1--W2. The two sides of the structure | - | scripts/retro99.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 41 | `dh_logderiv.py` | outside them, the first at $n=6$ (dh_logderiv.py ). An argument that reaches the line must | `src/chapters/04-bridges.tex:925` | W1--W2. The two sides of the structure | - | scripts/dh_logderiv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 42 | `blocks.py` | (F1PaperTorus.forcedLimit, F1PaperTorus.character_block_gives_the_line ; blocks.py ). Equivalently, the Fej'er sum over the | `src/chapters/04-bridges.tex:941` | W3. Positivity on the fibres of $G$: the Fej'er form of $(i,5)$ | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 43 | `fejer_check.py` | $310^-4$, fejer_check.py ). | `src/chapters/04-bridges.tex:945` | W3. Positivity on the fibres of $G$: the Fej'er form of $(i,5)$ | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 44 | `balance.py` | conductor plus the squares (balance.py ). For the four fibres, the deviation | `src/chapters/04-bridges.tex:965` | W3. Positivity on the fibres of $G$: the Fej'er form of $(i,5)$ | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 45 | `fibres.py` | (fibres.py ). The four characters are those of $(i,5)$, the field of | `src/chapters/04-bridges.tex:970` | W3. Positivity on the fibres of $G$: the Fej'er form of $(i,5)$ | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 46 | `dedekind.py` | positive (dedekind.py ). | `src/chapters/04-bridges.tex:973` | W3. Positivity on the fibres of $G$: the Fej'er form of $(i,5)$ | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 47 | `offline.py` | without it the minimum over $2L[2,240]$ is $+6.310^-4$ (offline.py ). | `src/chapters/04-bridges.tex:979` | W3. Positivity on the fibres of $G$: the Fej'er form of $(i,5)$ | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 48 | `castelnuovo.py` | most $0.63x$ (castelnuovo.py ). | `src/chapters/04-bridges.tex:1007` | W3. The intersection form in finite dimension | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 49 | `gram.py` | is nonnegative (gram.py ). That is the signature of the Hodge index, in | `src/chapters/04-bridges.tex:1028` | W3. The intersection form in finite dimension | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 50 | `bridge.py` | its two members by $1.2148$ and $0.8232$, with product $1$ (bridge.py ). With | `src/chapters/04-bridges.tex:1064` | W3. Rotations on the line, boosts off it | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 51 | `retro101.py` | two of each (retro101.py ). In the form of $L(s,)$ with two zeros replaced by a quadruple, the index is $0$ or $2$ on every window tried,... | `src/chapters/04-bridges.tex:1093` | W3. Rotations on the line, boosts off it | - | scripts/retro101.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 52 | `retro93.py` | two of each (retro101.py ). In the form of $L(s,)$ with two zeros replaced by a quadruple, the index is $0$ or $2$ on every window tried,... | `src/chapters/04-bridges.tex:1093` | W3. Rotations on the line, boosts off it | - | scripts/retro93.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 53 | `field_signature.py` | (field_signature.py ). The open statement, in this language, is that the | `src/chapters/04-bridges.tex:1166` | W3. The golden field: Hodge index and the first windows | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 54 | `arch_window.py` | $1.65$, beyond the prime-free range $[0,4]$ (arch_window.py ). | `src/chapters/04-bridges.tex:1182` | W3. The golden field: Hodge index and the first windows | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 55 | `rho_interval.py` | (rigorous_chain.py, rho_interval.py .) So the Weil form of $(5)$ is positive on | `src/chapters/04-bridges.tex:1207` | W3. The golden field: Hodge index and the first windows | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 56 | `rigorous_chain.py` | (rigorous_chain.py, rho_interval.py .) So the Weil form of $(5)$ is positive on | `src/chapters/04-bridges.tex:1207` | W3. The golden field: Hodge index and the first windows | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 57 | `corrected_operator.py` | (corrected_operator.py ). What separates the structural positions from the | `src/chapters/04-bridges.tex:1251` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 58 | `v12_pitagoras_raiz_X.py` | $(X)^2<E(X)$ at every scale measured (v12_pitagoras_raiz_X.py) . From the primes up to $10^6$, the | `src/chapters/04-bridges.tex:1313` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/v12_pitagoras_raiz_X.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 59 | `escala_ceros_bajos.py` | $31%$ and $48%$ of $_1/\|\|^2$ (escala_ceros_bajos.py) | `src/chapters/04-bridges.tex:1317` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 60 | `v30_vertice_al_azar.py` | to $210^-10$ and $610^-12$ (v30_vertice_al_azar.py, | `src/chapters/04-bridges.tex:1333` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/v30_vertice_al_azar.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 61 | `v33_capas_1e9.py` | v33_capas_1e9.py, ). What the geometry does not give is that $$ spreads over | `src/chapters/04-bridges.tex:1334` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/v33_capas_1e9.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 62 | `v33_capas_1e9.py` | (range $0.42$--$0.59$) (v33_capas_1e9.py, ). With the family taken to | `src/chapters/04-bridges.tex:1504` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/v33_capas_1e9.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 63 | `retro66.py` | ideals and the prime side summed level by level equals the direct sum, retro66.py ). | `src/chapters/04-bridges.tex:1519` | W4--W5. The closure | - | scripts/retro66.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 64 | `retro67.py` | $N0.38,L$ and positive above, whatever its level (retro67.py ). | `src/chapters/04-bridges.tex:1526` | W4--W5. The closure | - | scripts/retro67.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 65 | `amplitud_clausula_ii.py` | ranges, while single classes deviate by $-54%$ to $+68%$ (amplitud_clausula_ii.py) | `src/chapters/04-bridges.tex:1571` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 66 | `law_resolution.py` | $0.020$ prime by prime (law_resolution.py ). Taken as a sum over the primes up to a fixed $X$, the | `src/chapters/04-bridges.tex:1648` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 67 | `x_sweep.py` | weight $1-n/X$ on each prime power $n$ (x_sweep.py ). The improvement is gradual, and at | `src/chapters/04-bridges.tex:1651` | W4--W5. The closure | - | scripts/x_sweep.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 68 | `classes_test.py` | the law: it is the explicit formula, and as a construction it is circular; the classes are the part of the law that is not, and they are ... | `src/chapters/04-bridges.tex:1653` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 69 | `t1_index.py` | (t1_index.py, t2_loo.py ). | `src/chapters/04-bridges.tex:1686` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 70 | `t2_loo.py` | (t1_index.py, t2_loo.py ). | `src/chapters/04-bridges.tex:1686` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 71 | `retro81.py` | (retro81.py--retro87.py ). The systematic degeneracies of the quantised map are those of | `src/chapters/04-bridges.tex:1734` | W4--W5. The closure | - | scripts/retro81.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 72 | `retro87.py` | (retro81.py--retro87.py ). The systematic degeneracies of the quantised map are those of | `src/chapters/04-bridges.tex:1734` | W4--W5. The closure | - | scripts/retro87.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 73 | `retro88.py` | extra state is the delta at the fixed point $0$ (retro88.py ). At $5^k$ the same holds layer by layer: | `src/chapters/04-bridges.tex:1755` | W4--W5. The closure | - | scripts/retro88.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 74 | `retro89.py` | prop:clock-cyclotomic at the primes of $N$ whose clock divides $n$ (retro89.py ). | `src/chapters/04-bridges.tex:1760` | W4--W5. The closure | - | scripts/retro89.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 75 | `euler_link.py` | (the second term is $-2.510^-4$ at $e=13$ and $-9.710^-10$ at $e=31$, euler_link.py ); of the other primes it gives none one by one; on each | `src/chapters/04-bridges.tex:1799` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 76 | `zeroside.py` | archimedean side in the variable $u$, so no interpolation enters (zeroside.py ). | `src/chapters/04-bridges.tex:1863` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 77 | `sweep.py` | (sweep.py ). On the circle of $p=3$ the Fej'er density is positive in all eight | `src/chapters/04-bridges.tex:1869` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 78 | `circle_and_detect.py` | (circle_and_detect.py ). | `src/chapters/04-bridges.tex:1871` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 79 | `orbita_cert.py` | (orbita_cert.py ). The orbit of $$ computed from the primes alone is fitted by | `src/chapters/04-bridges.tex:1877` | W4--W5. The closure | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 80 | `W3_orbita_lado_primos.py` | (W3_orbita_lado_primos.py ). The three power-residue symbols of prop:phi-layers have $L$-functions with | `src/chapters/04-bridges.tex:1879` | W4--W5. The closure | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/W3_orbita_lado_primos.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 81 | `retro102.py` | (retro102.py ). | `src/chapters/04-bridges.tex:1932` | W4--W5. The closure | - | scripts/retro102.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 82 | `F1_pentagonal_descent_UNIFIED.lean` | F1_pentagonal_descent_UNIFIED.lean and of the twenty-seven modules compiled for this version | `src/chapters/appendix.tex:9` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean | lean/F1_pentagonal_descent_UNIFIED.lean | - | verificado (repo) |
| 83 | `weil_certificates/verify_iv.py` | Window $L1$, $Q0.0445\|f\|^2$ | `src/chapters/appendix.tex:45` | Status ledger | - | scripts/weil_certificates/verify_iv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 84 | `weil_certificates/op_rig_validated.py` | Windows $L1.1,1.2,1.3$ | `src/chapters/appendix.tex:46` | Status ledger | - | scripts/weil_certificates/op_rig_validated.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 85 | `fermat_quintic_points.py` | Point counts of the Fermat quintic equal $p+1+J$, all $\|J\|=p$, $p71$ | `src/chapters/appendix.tex:51` | Status ledger | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 86 | `weil_window_chi5.py` | Semilocal positivity | `src/chapters/appendix.tex:98` | Status ledger | - | scripts/weil_window_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 87 | `weil_certificates/` | Windows $L1$ and $L1.3$ | `src/chapters/appendix.tex:100` | Status ledger | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 88 | `envelope.py` | Envelope and fluctuation | `src/chapters/appendix.tex:101` | Status ledger | - | scripts/envelope.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 89 | `tstar.py` | Envelope and fluctuation | `src/chapters/appendix.tex:101` | Status ledger | - | scripts/tstar.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 90 | `dh_logderiv.py` | Davenport--Heilbronn as a test of routes | `src/chapters/appendix.tex:132` | Status ledger | - | scripts/dh_logderiv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 91 | `retro99.py` | Davenport--Heilbronn as a test of routes | `src/chapters/appendix.tex:132` | Status ledger | - | scripts/retro99.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 92 | `retro105.py` | What a symmetry shows in a spectrum; the spacings of the zeros | `src/chapters/appendix.tex:135` | Status ledger | - | scripts/retro105.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 93 | `retro78.py` | The golden ratio names the fifth roots of unity | `src/chapters/appendix.tex:183` | Status ledger | - | scripts/retro78.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 94 | `oz_carried.py` | Generalised Bernoulli values $B_2k,$, $k4$ | `src/chapters/appendix.tex:198` | Status ledger | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 95 | `oz_carried.py` | Polylogarithmic form; distances on the circle; the conditional on algebraicity | `src/chapters/appendix.tex:200` | Status ledger | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 96 | `oz_carried.py` | $T_K=5L(1,)L(1,_4)$; $T_K$ and $_K(2k+1)$ | `src/chapters/appendix.tex:202` | Status ledger | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 97 | `oz_carried.py` | Local factors at $s=3$; $_K(3)$ and $L(3,)$ | `src/chapters/appendix.tex:206` | Status ledger | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 98 | `weil_window_chi5.py` | The prime side split by the Frobenius, and the numerics of the bound | `src/chapters/appendix.tex:260` | Status ledger | - | scripts/weil_window_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 99 | `retro66.py` | The prime side in a window, given by the clock | `src/chapters/appendix.tex:277` | Status ledger | - | scripts/retro66.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 100 | `retro67.py` | The prime side in a window, given by the clock | `src/chapters/appendix.tex:277` | Status ledger | - | scripts/retro67.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 101 | `F1_pentagonal_descent_UNIFIED.lean` | The formalization is delivered as one file, F1_pentagonal_descent_UNIFIED.lean: | `src/chapters/appendix.tex:335` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean | lean/F1_pentagonal_descent_UNIFIED.lean | - | verificado (repo) |
| 102 | `CW_EQUIVALENCIAS.md` | or in F1_cw_equivalents (the correspondence is CW_EQUIVALENCIAS.md) | `src/chapters/appendix.tex:386` | Lean formalization audit / Files and roles | no existe como archivo en repo (mencionado en comentarios del .lean) | datos/CW_EQUIVALENCIAS.md | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 103 | `hipotesis/pruebas/` | redefined. The numerical tests are the scripts of hipotesis/pruebas/. | `src/chapters/appendix.tex:451` | Lean formalization audit / Ontology of the corpus: connections and reconnections | - | - | - | NO IDENTIFICADO |
| 104 | `verify_weil_chi5.py` | verify_weil_chi5.py (explicit formula, $10^-18$), | `src/chapters/appendix.tex:495` | Lean formalization audit / Numerical scripts | - | scripts/verify_weil_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 105 | `weil_window_chi5.py` | weil_window_chi5.py (semilocal eigenvalues), | `src/chapters/appendix.tex:496` | Lean formalization audit / Numerical scripts | - | scripts/weil_window_chi5.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 106 | `weil_window_rigorous_check.py` | weil_window_rigorous_check.py (constants of | `src/chapters/appendix.tex:497` | Lean formalization audit / Numerical scripts | no existe como archivo en repo (mencionado en comentarios del .lean) | scripts/weil_window_rigorous_check.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 107 | `weil_certificates/` | thm:first-window), weil_certificates/ (certificates of | `src/chapters/appendix.tex:498` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 108 | `cert.py` | thm:second-window,thm:third-window: cert.py, rigW.py, | `src/chapters/appendix.tex:499` | Lean formalization audit / Numerical scripts | - | scripts/weil_certificates/cert.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 109 | `rigW.py` | thm:second-window,thm:third-window: cert.py, rigW.py, | `src/chapters/appendix.tex:499` | Lean formalization audit / Numerical scripts | - | scripts/weil_certificates/rigW.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 110 | `op_rig_validated.py` | opcert_rig.py; the rigorous replays verify_iv.py, in interval arithmetic, and op_rig_validated.py, validated with a verified eigenvalue b... | `src/chapters/appendix.tex:500` | Lean formalization audit / Numerical scripts | - | scripts/weil_certificates/op_rig_validated.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 111 | `opcert_rig.py` | opcert_rig.py; the rigorous replays verify_iv.py, in interval arithmetic, and op_rig_validated.py, validated with a verified eigenvalue b... | `src/chapters/appendix.tex:500` | Lean formalization audit / Numerical scripts | - | scripts/weil_certificates/opcert_rig.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 112 | `verify_iv.py` | opcert_rig.py; the rigorous replays verify_iv.py, in interval arithmetic, and op_rig_validated.py, validated with a verified eigenvalue b... | `src/chapters/appendix.tex:500` | Lean formalization audit / Numerical scripts | - | scripts/weil_certificates/verify_iv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 113 | `zeroside_check.py` | opcert_rig.py; the rigorous replays verify_iv.py, in interval arithmetic, and op_rig_validated.py, validated with a verified eigenvalue b... | `src/chapters/appendix.tex:500` | Lean formalization audit / Numerical scripts | - | scripts/weil_certificates/zeroside_check.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 114 | `envelope.py` | from the zero side), envelope.py and tstar.py | `src/chapters/appendix.tex:501` | Lean formalization audit / Numerical scripts | - | scripts/envelope.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 115 | `tstar.py` | from the zero side), envelope.py and tstar.py | `src/chapters/appendix.tex:501` | Lean formalization audit / Numerical scripts | - | scripts/tstar.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 116 | `hipotesis/pruebas/` | (prop:envelope-exact); and, in hipotesis/pruebas/, the scripts of sec:results-verdict: | `src/chapters/appendix.tex:502` | Lean formalization audit / Numerical scripts | - | - | - | NO IDENTIFICADO |
| 117 | `balance.py` | testGeom.py, testB1b.py, fejer_check.py, balance.py, | `src/chapters/appendix.tex:503` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 118 | `fejer_check.py` | testGeom.py, testB1b.py, fejer_check.py, balance.py, | `src/chapters/appendix.tex:503` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 119 | `testB1b.py` | testGeom.py, testB1b.py, fejer_check.py, balance.py, | `src/chapters/appendix.tex:503` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 120 | `testGeom.py` | testGeom.py, testB1b.py, fejer_check.py, balance.py, | `src/chapters/appendix.tex:503` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 121 | `bridge.py` | fibres.py, castelnuovo.py, gram.py, bridge.py, offline.py, | `src/chapters/appendix.tex:504` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 122 | `castelnuovo.py` | fibres.py, castelnuovo.py, gram.py, bridge.py, offline.py, | `src/chapters/appendix.tex:504` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 123 | `fibres.py` | fibres.py, castelnuovo.py, gram.py, bridge.py, offline.py, | `src/chapters/appendix.tex:504` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 124 | `gram.py` | fibres.py, castelnuovo.py, gram.py, bridge.py, offline.py, | `src/chapters/appendix.tex:504` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 125 | `offline.py` | fibres.py, castelnuovo.py, gram.py, bridge.py, offline.py, | `src/chapters/appendix.tex:504` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 126 | `dh.py` | dh.py, mertens341.py, mobius.py, rigorous_chain.py, | `src/chapters/appendix.tex:505` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 127 | `mertens341.py` | dh.py, mertens341.py, mobius.py, rigorous_chain.py, | `src/chapters/appendix.tex:505` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 128 | `mobius.py` | dh.py, mertens341.py, mobius.py, rigorous_chain.py, | `src/chapters/appendix.tex:505` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 129 | `rigorous_chain.py` | dh.py, mertens341.py, mobius.py, rigorous_chain.py, | `src/chapters/appendix.tex:505` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 130 | `arch_window.py` | rho_interval.py, field_signature.py, arch_window.py, | `src/chapters/appendix.tex:506` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 131 | `field_signature.py` | rho_interval.py, field_signature.py, arch_window.py, | `src/chapters/appendix.tex:506` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 132 | `rho_interval.py` | rho_interval.py, field_signature.py, arch_window.py, | `src/chapters/appendix.tex:506` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 133 | `circle_and_detect.py` | w4exact.py, zeroside.py, sweep.py, circle_and_detect.py, | `src/chapters/appendix.tex:507` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 134 | `sweep.py` | w4exact.py, zeroside.py, sweep.py, circle_and_detect.py, | `src/chapters/appendix.tex:507` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 135 | `w4exact.py` | w4exact.py, zeroside.py, sweep.py, circle_and_detect.py, | `src/chapters/appendix.tex:507` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 136 | `zeroside.py` | w4exact.py, zeroside.py, sweep.py, circle_and_detect.py, | `src/chapters/appendix.tex:507` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 137 | `chi5_zeros.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/chi5_zeros.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 138 | `classes_test.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 139 | `corrected_operator.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 140 | `dh_logderiv.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/dh_logderiv.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 141 | `dh_zeros.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/dh_zeros.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 142 | `euler_link.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 143 | `law_resolution.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | no existe como archivo en repo (mencionado en comentarios del .lean) | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 144 | `oz_carried.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/oz_carried.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 145 | `retro101.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro101.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 146 | `retro102.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro102.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 147 | `retro104.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro104.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 148 | `retro105.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro105.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 149 | `retro119.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro119.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 150 | `retro93.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro93.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 151 | `retro94.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro94.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 152 | `retro99.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/retro99.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 153 | `t1_index.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | no existe como archivo en repo (mencionado en comentarios del .lean) | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 154 | `t2_loo.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 155 | `teich.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 156 | `x_sweep.py` | corrected_operator.py, classes_test.py, law_resolution.py, x_sweep.py, oz_carried.py, teich.py, t1_index.py, t2_loo.py, euler_link.py, re... | `src/chapters/appendix.tex:508` | Lean formalization audit / Numerical scripts | - | scripts/x_sweep.py | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 157 | `F1_pentagonal_descent_UNIFIED.lean` | F1_pentagonal_descent_UNIFIED.lean. | `src/chapters/appendix.tex:629` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean | lean/F1_pentagonal_descent_UNIFIED.lean | - | verificado (repo) |
| 158 | `hipotesis/pruebas` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 159 | `orbita_cert.py` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | - | - | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |
| 160 | `fqn_map.json` | Appendices | `src/chapters/appendix.tex:657` | Source map | - | datos/fqn_map.json | si | deferido-D7 (marcado % pending(D7) en el manuscrito) |

## Appendix B — corpus block and module names cited as files: 135 rows / 71 distinct names

| # | filename | claim / statement that names it | site | section | in repo | in zip | D7 | status |
|---|---|---|---|---|---|---|---|---|
| 1 | `F1_compilado_sin_axiomas` | HP ssec:squeeze (L4307); F1_compilado_sin_axiomas; | `src/chapters/03-mechanisms.tex:4442` | The span and the bridge / The thread from $$ | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 2 | `PCF_sesion_M12_unificado` | PCF_unificado; PCF_sesion_M12_unificado 129--205; | `src/chapters/03-mechanisms.tex:4443` | The span and the bridge / The thread from $$ | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 3 | `PCF_unificado` | PCF_unificado; PCF_sesion_M12_unificado 129--205; | `src/chapters/03-mechanisms.tex:4443` | The span and the bridge / The thread from $$ | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_unificado) | - | - | verificado (repo) |
| 4 | `everything_descends` | everything_descends | `src/chapters/03-mechanisms.tex:4444` | The span and the bridge / The thread from $$ | lean/F1_pentagonal_descent_UNIFIED.lean (bloque everything_descends) | - | - | verificado (repo) |
| 5 | `F1_compilado_sin_axiomas` | Seven geometric axioms ($^2=+1$, $i^2=-1$, $z=y$, basis of $E^3$, continued fraction, nested radical, $\|\|=12$) | `src/chapters/05-categorical.tex:394` | What the Primitive Structure declared, and what is settled here | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 6 | `F1_cw_equivalents` | written against the other blocks of the unified file, F1_cw_equivalents among them (app:lean), with no sorry | `src/chapters/05-categorical.tex:1210` | Limitations | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_cw_equivalents) | - | - | verificado (repo) |
| 7 | `F1_v2_formalizations` | discharges of O of the block F1_v2_formalizations, and the closure modules of | `src/chapters/05-categorical.tex:1214` | Limitations | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_v2_formalizations) | - | - | verificado (repo) |
| 8 | `F1_v2` | Crystallographic restriction, pentagonal nodes | `src/chapters/appendix.tex:93` | Status ledger | lean/… (abreviatura de F1_v2_formalizations) | - | - | verificado (repo) |
| 9 | `F1v2` | Reconnections of compiled lemmas | `src/chapters/appendix.tex:117` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (namespace F1v2) | - | - | verificado (repo) |
| 10 | `FibrasPorNivel` | The fibres of $G$ on the levels of the clock | `src/chapters/appendix.tex:128` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque FibrasPorNivel) | - | - | verificado (repo) |
| 11 | `MedioPeriodo` | (W4) is (W3) on the planes of the orbit; half period | `src/chapters/appendix.tex:130` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque MedioPeriodo) | - | - | verificado (repo) |
| 12 | `ParidadesJuntas` | (W4) is (W3) on the planes of the orbit; half period | `src/chapters/appendix.tex:130` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque ParidadesJuntas) | - | - | verificado (repo) |
| 13 | `W4DeW3` | (W4) is (W3) on the planes of the orbit; half period | `src/chapters/appendix.tex:130` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque W4DeW3) | - | - | verificado (repo) |
| 14 | `FibraYReloj` | What an operator of the level does not separate | `src/chapters/appendix.tex:133` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque FibraYReloj) | - | - | verificado (repo) |
| 15 | `ObservablesDelNivel` | What an operator of the level does not separate | `src/chapters/appendix.tex:133` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque ObservablesDelNivel) | - | - | verificado (repo) |
| 16 | `PCFGranularity` | What an operator of the level does not separate | `src/chapters/appendix.tex:133` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (namespace PCFGranularity) | - | - | verificado (repo) |
| 17 | `DosCarasFibonacci` | The two faces of the Fibonacci dynamics: periodic on the torsion, mixing on the characters | `src/chapters/appendix.tex:134` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque DosCarasFibonacci) | - | - | verificado (repo) |
| 18 | `PeriodicasSol` | The two faces of the Fibonacci dynamics: periodic on the torsion, mixing on the characters | `src/chapters/appendix.tex:134` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PeriodicasSol) | - | - | verificado (repo) |
| 19 | `EstructuraEnGUE` | What a symmetry shows in a spectrum; the spacings of the zeros | `src/chapters/appendix.tex:135` | Status ledger | lean/F1_pentagonal_descent_UNIFIED.lean (bloque EstructuraEnGUE) | - | si | verificado (repo) |
| 20 | `F1Paper` | file. The same content is also a Lake project, F1Paper. The blocks are of | `src/chapters/appendix.tex:337` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (mención) | - | - | NO IDENTIFICADO (proyecto Lake; el lakefile del repo se llama odd_zeta) |
| 21 | `F1_spectra_anchor_G_standalone` | [Compiled, unchanged] F1_spectra_anchor_G_standalone, | `src/chapters/appendix.tex:340` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_spectra_anchor_G_standalone) | - | - | verificado (repo) |
| 22 | `F1_PCF_session_modules` | F1_PCF_session_modules, PCF_sesion_2026_08_18_unificado, | `src/chapters/appendix.tex:341` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_PCF_session_modules) | - | - | verificado (repo) |
| 23 | `PCF_sesion_2026_08_18_unificado` | F1_PCF_session_modules, PCF_sesion_2026_08_18_unificado, | `src/chapters/appendix.tex:341` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_2026_08_18_unificado) | - | - | verificado (repo) |
| 24 | `PCF_sesion_M12_unificado` | PCF_sesion_M12_unificado, | `src/chapters/appendix.tex:342` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 25 | `PCF_granularity_UNIFIED_with_mathlib_verified` | PCF_granularity_UNIFIED_with_mathlib_verified, | `src/chapters/appendix.tex:343` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_granularity_UNIFIED_with_mathlib_verified) | - | - | verificado (repo) |
| 26 | `everything_descends` | everything_descends, the_anchor_segments_the_circle and | `src/chapters/appendix.tex:344` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque everything_descends) | - | - | verificado (repo) |
| 27 | `the_anchor_segments_the_circle` | everything_descends, the_anchor_segments_the_circle and | `src/chapters/appendix.tex:344` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque the_anchor_segments_the_circle) | - | - | verificado (repo) |
| 28 | `the_mate_carries_the_conjugate` | the_mate_carries_the_conjugate are the compiled files of the project, | `src/chapters/appendix.tex:345` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque the_mate_carries_the_conjugate) | - | - | verificado (repo) |
| 29 | `F1_compilado_sin_axiomas` | [Compiled, with a documented edit] F1_compilado_sin_axiomas, the | `src/chapters/appendix.tex:347` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 30 | `PCF_unificado` | numbers of the earlier version; PCF_unificado (its one | `src/chapters/appendix.tex:353` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_unificado) | - | - | verificado (repo) |
| 31 | `PCF_sesion_completa` | removed); PCF_sesion_completa (its two sorry, in | `src/chapters/appendix.tex:356` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_completa) | - | - | verificado (repo) |
| 32 | `S1_chi5_fib` | pisano_five_is_twenty, closed by S1_chi5_fib and by a | `src/chapters/appendix.tex:358` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque S1_chi5_fib) | - | - | verificado (repo) |
| 33 | `S1_chi5_fib` | [Written for this version, not yet compiled] S1_chi5_fib, | `src/chapters/appendix.tex:360` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque S1_chi5_fib) | - | - | verificado (repo) |
| 34 | `F1_frobenius_eigenvalue` | F1_pendientes, F1_pendientes_2, F1_frobenius_eigenvalue, | `src/chapters/appendix.tex:361` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_frobenius_eigenvalue) | - | - | verificado (repo) |
| 35 | `F1_pendientes` | F1_pendientes, F1_pendientes_2, F1_frobenius_eigenvalue, | `src/chapters/appendix.tex:361` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_pendientes) | - | - | verificado (repo) |
| 36 | `F1_pendientes_2` | F1_pendientes, F1_pendientes_2, F1_frobenius_eigenvalue, | `src/chapters/appendix.tex:361` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_pendientes_2) | - | - | verificado (repo) |
| 37 | `D16_hconj` | F1_weil_functional, F1_primon_space, D16_hconj, | `src/chapters/appendix.tex:362` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque D16_hconj) | - | - | verificado (repo) |
| 38 | `F1_primon_space` | F1_weil_functional, F1_primon_space, D16_hconj, | `src/chapters/appendix.tex:362` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_primon_space) | - | - | verificado (repo) |
| 39 | `F1_weil_functional` | F1_weil_functional, F1_primon_space, D16_hconj, | `src/chapters/appendix.tex:362` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_weil_functional) | - | - | verificado (repo) |
| 40 | `F1_cw_equivalents` | F1_cw_equivalents (the facts of gonzalez26cw that sec:background,sec:methods,sec:results use; | `src/chapters/appendix.tex:363` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_cw_equivalents) | - | - | verificado (repo) |
| 41 | `F1PaperNew` | F1_v2_formalizations, and the modules of the paper F1PaperNew, | `src/chapters/appendix.tex:366` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperNew) | - | - | verificado (repo) |
| 42 | `F1_v2_formalizations` | F1_v2_formalizations, and the modules of the paper F1PaperNew, | `src/chapters/appendix.tex:366` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_v2_formalizations) | - | - | verificado (repo) |
| 43 | `F1PaperClosure` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperClosure) | - | - | verificado (repo) |
| 44 | `F1PaperClosureClock` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (namespace F1PaperClosureClock) | - | - | verificado (repo) |
| 45 | `F1PaperHyp` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperHyp) | - | - | verificado (repo) |
| 46 | `F1PaperPadic` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperPadic) | - | - | verificado (repo) |
| 47 | `F1PaperPending` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperPending) | - | - | verificado (repo) |
| 48 | `F1PaperSixty` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (namespace F1PaperSixty) | - | - | verificado (repo) |
| 49 | `F1PaperSixtyWeil` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (namespace F1PaperSixtyWeil) | - | - | verificado (repo) |
| 50 | `F1PaperTorus` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperTorus) | - | - | verificado (repo) |
| 51 | `M12F1Circle` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (namespace M12F1Circle) | - | - | verificado (repo) |
| 52 | `PhiCelda` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (namespace PhiCelda) | - | - | verificado (repo) |
| 53 | `W4Isometria` | F1PaperHyp, F1PaperTorus, F1PaperPending, F1PaperClosure and F1PaperPadic; and, for the clock, the index, the energy and the prism at $5$... | `src/chapters/appendix.tex:367` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (namespace W4Isometria) | - | - | verificado (repo) |
| 54 | `CierrePorAltura` | the index as a degeneracy, CierrePorAltura, IndiceComoDegeneracion, MasaDelReloj and | `src/chapters/appendix.tex:371` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque CierrePorAltura) | - | - | verificado (repo) |
| 55 | `IndiceComoDegeneracion` | the index as a degeneracy, CierrePorAltura, IndiceComoDegeneracion, MasaDelReloj and | `src/chapters/appendix.tex:371` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque IndiceComoDegeneracion) | - | - | verificado (repo) |
| 56 | `MasaDelReloj` | the index as a degeneracy, CierrePorAltura, IndiceComoDegeneracion, MasaDelReloj and | `src/chapters/appendix.tex:371` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque MasaDelReloj) | - | - | verificado (repo) |
| 57 | `FibrasPorNivel` | NivelesYOrientacion; for the inertia index and the mate, FibrasPorNivel, | `src/chapters/appendix.tex:372` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque FibrasPorNivel) | - | - | verificado (repo) |
| 58 | `NivelesYOrientacion` | NivelesYOrientacion; for the inertia index and the mate, FibrasPorNivel, | `src/chapters/appendix.tex:372` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque NivelesYOrientacion) | - | - | verificado (repo) |
| 59 | `MateSinG` | OrbitaLibreEIndice, ParidadesJuntas, MedioPeriodo, W4DeW3 and MateSinG; for | `src/chapters/appendix.tex:373` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque MateSinG) | - | - | verificado (repo) |
| 60 | `MedioPeriodo` | OrbitaLibreEIndice, ParidadesJuntas, MedioPeriodo, W4DeW3 and MateSinG; for | `src/chapters/appendix.tex:373` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque MedioPeriodo) | - | - | verificado (repo) |
| 61 | `OrbitaLibreEIndice` | OrbitaLibreEIndice, ParidadesJuntas, MedioPeriodo, W4DeW3 and MateSinG; for | `src/chapters/appendix.tex:373` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque OrbitaLibreEIndice) | - | - | verificado (repo) |
| 62 | `ParidadesJuntas` | OrbitaLibreEIndice, ParidadesJuntas, MedioPeriodo, W4DeW3 and MateSinG; for | `src/chapters/appendix.tex:373` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque ParidadesJuntas) | - | - | verificado (repo) |
| 63 | `W4DeW3` | OrbitaLibreEIndice, ParidadesJuntas, MedioPeriodo, W4DeW3 and MateSinG; for | `src/chapters/appendix.tex:373` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque W4DeW3) | - | - | verificado (repo) |
| 64 | `FibraYReloj` | the operators of the level and the symmetries of a spectrum, ObservablesDelNivel, FibraYReloj | `src/chapters/appendix.tex:374` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque FibraYReloj) | - | - | verificado (repo) |
| 65 | `ObservablesDelNivel` | the operators of the level and the symmetries of a spectrum, ObservablesDelNivel, FibraYReloj | `src/chapters/appendix.tex:374` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque ObservablesDelNivel) | - | - | verificado (repo) |
| 66 | `DosCarasFibonacci` | and EstructuraEnGUE; for the two faces of the Fibonacci dynamics, DosCarasFibonacci and | `src/chapters/appendix.tex:375` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque DosCarasFibonacci) | - | - | verificado (repo) |
| 67 | `EstructuraEnGUE` | and EstructuraEnGUE; for the two faces of the Fibonacci dynamics, DosCarasFibonacci and | `src/chapters/appendix.tex:375` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque EstructuraEnGUE) | - | - | verificado (repo) |
| 68 | `AlcanceZeta` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque AlcanceZeta) | - | - | verificado (repo) |
| 69 | `ComponentesInvoluciones` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque ComponentesInvoluciones) | - | - | verificado (repo) |
| 70 | `F1Lawvere` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1Lawvere) | - | - | verificado (repo) |
| 71 | `FrobeniusUnico` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque FrobeniusUnico) | - | - | verificado (repo) |
| 72 | `LadoAnalitico` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque LadoAnalitico) | - | - | verificado (repo) |
| 73 | `OZCierres` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque OZCierres) | - | - | verificado (repo) |
| 74 | `OZTraidos` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque OZTraidos) | - | - | verificado (repo) |
| 75 | `PasosDelTexto` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PasosDelTexto) | - | - | verificado (repo) |
| 76 | `PeriodicasSol` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PeriodicasSol) | - | - | verificado (repo) |
| 77 | `RelojTres` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque RelojTres) | - | - | verificado (repo) |
| 78 | `TodoEnLean` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque TodoEnLean) | - | - | verificado (repo) |
| 79 | `UnOperador` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque UnOperador) | - | - | verificado (repo) |
| 80 | `ZetaPentagonal` | PeriodicasSol; the steps that earlier versions proved only in the text, PasosDelTexto; for the diagonal argument and the reflection $x1-x... | `src/chapters/appendix.tex:376` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque ZetaPentagonal) | - | - | verificado (repo) |
| 81 | `PCF_sesion_M12_unificado` | PCF_sesion_M12_unificado) and PCF_session_unified ($313$ of $314$ | `src/chapters/appendix.tex:382` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 82 | `PCF_sesion_completa` | in PCF_sesion_completa; the remaining one, the auxiliary definition | `src/chapters/appendix.tex:383` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_completa) | - | - | verificado (repo) |
| 83 | `F1_cw_equivalents` | or in F1_cw_equivalents (the correspondence is CW_EQUIVALENCIAS.md) | `src/chapters/appendix.tex:386` | Lean formalization audit / Files and roles | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_cw_equivalents) | - | si | verificado (repo) |
| 84 | `F1PaperNew` | kinds of repair came out of it, both in the block F1PaperNew and all | `src/chapters/appendix.tex:394` | Lean formalization audit / Ontology of the corpus: connections and reconnections | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperNew) | - | - | verificado (repo) |
| 85 | `F1_v2_formalizations` | and the discharges of O of F1_v2_formalizations). | `src/chapters/appendix.tex:412` | Lean formalization audit / Ontology of the corpus: connections and reconnections | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_v2_formalizations) | - | - | verificado (repo) |
| 86 | `F1PaperHyp` | F1PaperHyp, which connects the forms of the open statement to the corpus (the index form of the | `src/chapters/appendix.tex:437` | Lean formalization audit / Ontology of the corpus: connections and reconnections | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperHyp) | - | - | verificado (repo) |
| 87 | `F1PaperTorus` | Frobenius action, the partition of the operator's error), and F1PaperTorus, the | `src/chapters/appendix.tex:438` | Lean formalization audit / Ontology of the corpus: connections and reconnections | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperTorus) | - | - | verificado (repo) |
| 88 | `F1PaperPending` | F1PaperPending, which contains only the Weil face of what remains, stated on the explicit | `src/chapters/appendix.tex:442` | Lean formalization audit / Ontology of the corpus: connections and reconnections | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperPending) | - | - | verificado (repo) |
| 89 | `F1PaperClosure` | orbit --- (W4) and the explicit formula on the orbit --- with the closing theorem restated from them; and F1PaperClosure, the closure of ... | `src/chapters/appendix.tex:443` | Lean formalization audit / Ontology of the corpus: connections and reconnections | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperClosure) | - | - | verificado (repo) |
| 90 | `F1_v2_formalizations` | Real.log_zpow; and in F1_v2_formalizations: the tactic | `src/chapters/appendix.tex:476` | Lean formalization audit / Mathlib names at risk | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_v2_formalizations) | - | - | verificado (repo) |
| 91 | `F1Lawvere` | sec:f1-programme--sec:manin The $$ programme, Manin | `src/chapters/appendix.tex:635` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1Lawvere) | - | - | verificado (repo) |
| 92 | `F1PaperNew.triad_isometry` | sec:f1-programme--sec:manin The $$ programme, Manin | `src/chapters/appendix.tex:635` | Source map / columna Corpus | lean/F1_pentagonal_descent_UNIFIED.lean (mención) | - | - | verificado (repo) |
| 93 | `F1_PCF_session_modules` | sec:choice The route | `src/chapters/appendix.tex:636` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_PCF_session_modules) | - | - | verificado (repo) |
| 94 | `F1_compilado` | sec:choice The route | `src/chapters/appendix.tex:636` | Source map | lean/… (abreviatura de F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 95 | `F1_pendientes` | sec:ring The ring $$ | `src/chapters/appendix.tex:637` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_pendientes) | - | - | verificado (repo) |
| 96 | `M12` | sec:ring The ring $$ | `src/chapters/appendix.tex:637` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 97 | `F1_compilado` | sec:lambda-monoid The $$-monoid | `src/chapters/appendix.tex:638` | Source map | lean/… (abreviatura de F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 98 | `F1_spectra_anchor_G` | sec:lambda-monoid The $$-monoid | `src/chapters/appendix.tex:638` | Source map | lean/… (abreviatura de F1_spectra_anchor_G_standalone) | - | - | verificado (repo) |
| 99 | `F1_frobenius_eigenvalue` | sec:lambda-ring The Artin $$-structure | `src/chapters/appendix.tex:639` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_frobenius_eigenvalue) | - | - | verificado (repo) |
| 100 | `F1_pendientes` | sec:lambda-ring The Artin $$-structure | `src/chapters/appendix.tex:639` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_pendientes) | - | - | verificado (repo) |
| 101 | `F1_pendientes_2` | sec:lambda-ring The Artin $$-structure | `src/chapters/appendix.tex:639` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_pendientes_2) | - | - | verificado (repo) |
| 102 | `PCFGranularity` | sec:lambda-ring The Artin $$-structure | `src/chapters/appendix.tex:639` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (namespace PCFGranularity) | - | - | verificado (repo) |
| 103 | `S1_chi5_fib` | sec:chi5 The Fibonacci character | `src/chapters/appendix.tex:640` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque S1_chi5_fib) | - | - | verificado (repo) |
| 104 | `F1_compilado` | sec:grisales Golden Prime classification | `src/chapters/appendix.tex:641` | Source map | lean/… (abreviatura de F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 105 | `F1_cw_equivalents` | sec:grisales Golden Prime classification | `src/chapters/appendix.tex:641` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_cw_equivalents) | - | - | verificado (repo) |
| 106 | `PCFGranularity` | sec:grisales Golden Prime classification | `src/chapters/appendix.tex:641` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (namespace PCFGranularity) | - | - | verificado (repo) |
| 107 | `W4Isometria` | sec:grisales Golden Prime classification | `src/chapters/appendix.tex:641` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (namespace W4Isometria) | - | - | verificado (repo) |
| 108 | `F1_compilado` | sec:dedekind--sec:factorisation Euler factors, colimit, odd values | `src/chapters/appendix.tex:642` | Source map | lean/… (abreviatura de F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 109 | `F1_cw_equivalents` | sec:dedekind--sec:factorisation Euler factors, colimit, odd values | `src/chapters/appendix.tex:642` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_cw_equivalents) | - | - | verificado (repo) |
| 110 | `F1_v2_formalizations` | sec:counting The counting function | `src/chapters/appendix.tex:643` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_v2_formalizations) | - | - | verificado (repo) |
| 111 | `F1_compilado` | sec:mersenne The Mersenne bridge | `src/chapters/appendix.tex:644` | Source map | lean/… (abreviatura de F1_compilado_sin_axiomas) | - | - | verificado (repo) |
| 112 | `M12` | sec:mersenne The Mersenne bridge | `src/chapters/appendix.tex:644` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 113 | `F1_v2` | ssec:base-phi Values in base $$ | `src/chapters/appendix.tex:645` | Source map | lean/… (abreviatura de F1_v2_formalizations) | - | - | verificado (repo) |
| 114 | `M12` | ssec:base-phi Values in base $$ | `src/chapters/appendix.tex:645` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 115 | `08_18` | sec:operator The operator | `src/chapters/appendix.tex:646` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_2026_08_18_unificado) | - | - | verificado (repo) |
| 116 | `M12` | sec:operator The operator | `src/chapters/appendix.tex:646` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 117 | `PCF_granularity` | sec:operator The operator | `src/chapters/appendix.tex:646` | Source map | lean/… (abreviatura de PCF_granularity_UNIFIED_with_mathlib_verified) | - | - | verificado (repo) |
| 118 | `M12` | sec:machinery The structure that places the zeros | `src/chapters/appendix.tex:647` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 119 | `PCF_sesion_completa` | sec:machinery The structure that places the zeros | `src/chapters/appendix.tex:647` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_completa) | - | - | verificado (repo) |
| 120 | `PCF_unificado` | sec:machinery The structure that places the zeros | `src/chapters/appendix.tex:647` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_unificado) | - | - | verificado (repo) |
| 121 | `PCF_sesion_completa` | sec:topological-proof The thread | `src/chapters/appendix.tex:648` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_completa) | - | - | verificado (repo) |
| 122 | `PCF_unificado` | sec:topological-proof The thread | `src/chapters/appendix.tex:648` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_unificado) | - | - | verificado (repo) |
| 123 | `M12` | sec:results-zeros The zero set | `src/chapters/appendix.tex:649` | Source map / columna Corpus (token sin \texttt) | lean/… (abreviatura de PCF_sesion_M12_unificado) | - | - | verificado (repo) |
| 124 | `PCF_sesion_completa` | sec:results-zeros The zero set | `src/chapters/appendix.tex:649` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque PCF_sesion_completa) | - | - | verificado (repo) |
| 125 | `scripts` | sec:results-zeros The zero set | `src/chapters/appendix.tex:649` | Source map / columna Corpus (token sin \texttt) | - | scripts/ (directorio del zip) | - | verificado (zip, no portado) |
| 126 | `F1PaperClosure` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperClosure) | - | si | verificado (repo) |
| 127 | `F1PaperHyp` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperHyp) | - | si | verificado (repo) |
| 128 | `F1PaperPadic` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperPadic) | - | si | verificado (repo) |
| 129 | `F1PaperPending` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperPending) | - | si | verificado (repo) |
| 130 | `F1PaperTorus` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1PaperTorus) | - | si | verificado (repo) |
| 131 | `F1_v2` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/… (abreviatura de F1_v2_formalizations) | - | si | verificado (repo) |
| 132 | `F1_weil_functional` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (bloque F1_weil_functional) | - | si | verificado (repo) |
| 133 | `W4Isometria` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map | lean/F1_pentagonal_descent_UNIFIED.lean (namespace W4Isometria) | - | si | verificado (repo) |
| 134 | `certificates` | sec:results-weil--sec:results-verdict Weil analogy, windows, verdict | `src/chapters/appendix.tex:650` | Source map / columna Corpus (token sin \texttt) | lean/F1_pentagonal_descent_UNIFIED.lean (mención) | scripts/weil_certificates/ (directorio del zip) | si | verificado (repo) |
| 135 | `F1_v2` | sec:disc-cw Crystalline Worldsheet | `src/chapters/appendix.tex:654` | Source map | lean/… (abreviatura de F1_v2_formalizations) | - | - | verificado (repo) |
