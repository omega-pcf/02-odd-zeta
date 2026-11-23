# Tier-use migration map — census, patterns and disposition of the non-standard tier marks

| Field | Value |
|---|---|
| **id** | `FTI-001` |
| **title** | Tier-use migration map: census of every non-standard tier use, context patterns with before/after, disposition (mechanical rows vs decision gate), naming standard and rename inventory |
| **status** | report only — no manuscript, script, test or `lean/` change |
| **date** | 2026-11-22 |
| **version** | 1.0 |

**Scope.** `02-odd-zeta` at `e62d1b5` (`origin/main`, F9 landed), read-only worktree
`wt02_same`. F-TIERS of the merge plan: every use of the marks outside the family
alphabet — `\tierPnew` (P*), `\tierC`, `\tierNc`, `\tierO`, `\tierT`, `\tier{R}` —
plus the tier gloss of §Protocol (`src/chapters/01-introduction.tex:248–263`), counted
and grouped by context pattern with a proposed destination (standard prose, or witness
`P`/`N[ids]` where the evidence fits), split into the rows the wave applies and the rows
that are the author's decision; then the naming standard for the ids this document
proposes, and the rename inventory F11 executes (both orders of Víctor, 2026-11-22).
What this report deliberately does not touch: `main.tex`, `src/chapters`, `lean/`,
`scripts/`, `tests/`, `package.json`. Line numbers refer to `e62d1b5` and move with
editing; the sentence tail identifies each site (reports convention).

## 1. Method — measured, not inherited

- **Census**: one regex per mark over `main.tex` + `src/chapters/*.tex`, every
  occurrence kept as its own row — **471 rows**. Machine data:
  `scratch/ftier_final_rows.json` (`f, l, cls, pos, line, table, caption, zone,
  verdict, pattern`). The counts of F8-001 were not reused as-is; every figure below
  was re-measured on this commit.
- **Zones** tracked with brace depth across lines: `def` (preamble `\newcommand`),
  `gloss` (01-introduction:248–263), `caption` (inside `\caption{…}`), `table` (an
  unclosed `tabular`/`longtable`), `prose`.
- **Classifier** (per row, ±1 line of context): cite/source words (`\cite`, a named
  theorem, `classical`, …) → C has its source; `open`/`conjectur` → O already says the
  word; `reading` → R already says the word; a clause ending in `given` → dangling
  input; a stand-alone mark at line end → bare. Verdict: `mech` when the destination
  (unmarked prose, or prose + the adjacent `\cite`) is already carried by the sentence,
  `judge` when something must be written, decided or re-measured.
- **Sensitivity** (stated because it moves rows): widening the source window to ±3
  lines moves **5 of the 16 `C-bare`** rows to "source named in the sentence" →
  mechanical; only **1 of the 22 `O`** rows without the word gains `open` at ±3. The
  figures below are the ±1 measurement, the sensitivity is reported here and not
  hidden.
- **Independent inputs**: F9-001's 416/416 name-presence verification;
  `tests/verify_odd_zeta_pcf_unified.py` (58 `check` calls, 58 distinct names); the
  unified Lean file itself; fresh gate runs (§8).

## 2. Census (measured)

| class | mark | def | gloss | caption | table | prose | **total** |
|---|---|--:|--:|--:|--:|--:|--:|
| P\* | `\tierPnew` | 1 | 2 | 1 | 121 | 121 | **246** |
| C | `\tierC` | 1 | 1 | 0 | 50 | 91 | **143** |
| Nc | `\tierNc` | 1 | 1 | 0 | 7 | 6 | **15** |
| O | `\tierO` | 1 | 1 | 0 | 16 | 26 | **44** |
| T | `\tierT` | 1 | 1 | 0 | 4 | 5 | **11** |
| R | `\tier{R}` (literal) | 0 | 1 | 0 | 0 | 11 | **12** |
| **total** | | 5 | 7 | 1 | 198 | 260 | **471** |

Standard alphabet for context, same scan: `\tierP` **508** · `\tierN` **122**
(1 def + 1 gloss + 120 body/table) · `\tier[\testref{…}]{N}` **6 marks / 7 ids** ·
`\Ecore` 51 · `\LeanInline` 800 · `\LeanStar` 416 · `\LeanTally` 21 · `\LeanCW` 44 ·
`\todo` 1. The family's late devices are absent: `\witness`, `\wtag` and `\Conj` are
not even defined (0 uses). There is **no `\tierR` macro** — R is written as the literal
`\tier{R}` (12 uses), the only class without its own macro.

Sites per class (`file: line` ranges, one line per occurrence):

- **P*** (246) — `main.tex`: 224 · `01-introduction.tex`: 250,259 · `02-foundations.tex`: 755,850,891 · `03-mechanisms.tex`: 158,167,180,620,869,884,921,941,987,1009,1064,1094,1117,1130,1148,1163,1170,1200,1273,1280,1294,1319,1421,1466,1475,1478,1503,1582,1620,1692,1755,1766,1768,2067,2160,2209,2222,2225,2443,2619,2724,2764,2966,3022,3027,3258,3300,3325,3355,3497,3694,3737-3738,3795,4089,4186,4247,4252,4521,4635 · `04-bridges.tex`: 126,381,395,401,409,457,655,823-824,830-833,867,888,902,912-913,941,944,958,1020,1059,1109,1118,1132,1150,1162,1178,1191,1244,1270,1310,1368,1440,1444,1470,1491,1565,1567,1611,1613,1627,1673,1785,1833,1851,1856,1914,1941,1943,1947 · `05-categorical.tex`: 333,563-569,672,754,899,931,970,1029,1103,1111,1209,1219 · `appendix.tex`: 12,20-24,30,35-43,48-50,52,59-60,66,78,82-97,99,103-104,107-113,117-122,124-127,146-147,149-150,157,163,169-170,172-173,175,179-181,187,191,213-215,218,220-221,240,247,260,267-276,278,280-281,285,287,291,293-294,296,367,395,446
- **C** (143) — `main.tex`: 225 · `01-introduction.tex`: 253 · `03-mechanisms.tex`: 114,287,1095,1422,1542,1567,1625,1646,1705,1740,1743,2000,2044,2084,2104,2161,2226,2238,2240-2241,2245,2267,2284,2290,2296,2298,2301,2316,2320,2366,2379,2570,2660,2684,2764,2806,3028,3104,3561-3562,3564,3620,3741,3744,3844,3947,4186,4212,4316 · `04-bridges.tex`: 46,61,380,396,458,667,748,792,804,867,888,908,930,971,1192-1193,1301,1312,1371,1375,1451,1562,1565,1587,1598,1614,1673,1708,1724,1735,1833,1915,1945 · `05-categorical.tex`: 563,566-567,596,654,683,804,933,1231 · `appendix.tex`: 35,38,40-41,62,64,75,89,91,96,99,110-111,113,128,131,133-134,148,157,183,185,192-193,195-196,198,200-205,211,252,266-267,273-274,279,287,293,322,447
- **Nc** (15) — `main.tex`: 230 · `01-introduction.tex`: 254 · `04-bridges.tex`: 499,529,831-832,1182,1207,1877,1914 · `05-categorical.tex`: 569 · `appendix.tex`: 45-46,100,130
- **O** (44) — `main.tex`: 227 · `01-introduction.tex`: 255 · `02-foundations.tex`: 903 · `03-mechanisms.tex`: 970,987,1315,1622,2247,2308,4416 · `04-bridges.tex`: 396,832,916,986,1031,1137,1168,1311,1422,1424,1429,1433,1436,1509,1944 · `05-categorical.tex`: 555,683,690 · `appendix.tex`: 26,36,39,42,47,71,84,97,123,127,130,171,202,298,447
- **T** (11) — `main.tex`: 228 · `01-introduction.tex`: 250 · `03-mechanisms.tex`: 1542,2319 · `04-bridges.tex`: 1719,1730,1761 · `appendix.tex`: 128,203,212,279
- **R** (12) — `01-introduction.tex`: 255 · `03-mechanisms.tex`: 1984,2268,3278,3588 · `04-bridges.tex`: 1769 · `05-categorical.tex`: 355,435,458,1006,1125,1251

Framework prose — the tier vocabulary outside the macros: **8 prose lines** say
"tier(s)" (`01:251`, `01:275`, `03:142`, `04:14`, `04:643`, `05:1227`,
`appendix:7`, `appendix:136`) and **5 column headers** carry it — `Tier` at
`03:3734`, `03:4206`, `04:652`, `appendix:19`, `status` at `04:822`. All of them
reword or retire with §5; none is a mark, so none is counted in the 471.

## 3. The gloss / §Protocol block — the largest single judgment

### 3.1 What it holds

`src/chapters/01-introduction.tex:248–263`, subsection
`\subsection{Protocol}\label{ssec:protocol}`:

| lines | content | mark uses |
|---|---|---|
| 248 | subsection title + label | — |
| 250–253 | "Statements carry tiers:" the eight-level enumeration — P, **P\***, **T** (with the five-step list "…five steps remain in this tier: the second statement of `prop:fibres-levels`(ii), two computations with Gauss sums …, the gluing of the local models …, and the connectedness step of `rmk:G-motivic`"), **C** | P, P\*, T, C |
| 254–255 | **N**, **Nc**, **O**, **R** with their definitions | N, Nc, O, R |
| 256–258 | "A P citation certifies exactly the Lean statement named, with its hypotheses: when a declaration takes an input as a hypothesis, the input is named with its own tier." | — |
| 258–263 | "Inside a group of P citations, a name marked ∗ is **P\***; a name marked ∘ is a tally …; and a name marked † belongs to the Lean development of `gonzalez26cw` …" | P\* |

The seven non-standard mark uses inside the block are the `gloss-block` rows of the
gate (§6.2): `01:250` (P\* ×2), `01:253` (C), `01:254` (Nc), `01:255` (O and R),
`01:259` (P\*).

### 3.2 Six measured findings against the family standard

1. **Eight levels where the alphabet is two.** The family convention is **P and N**,
   with `P*` internal (documented in `docs/citations.md`, never in the paper's legend)
   and L/R retired by the author. The block defines eight paper-visible levels.
2. **The gloss follows first use.** First mark in the body: `01:112`
   (`(\LeanInline{G\_hom}, \LeanInline{G\_surj}, \LeanInline{G\_kernel} \tierP)`),
   PDF page **7**. Gloss text: page **10**. The family rule is a flat gloss *at the
   first mark in the body*; the no-first-page-footnote rule is already satisfied (there
   is none).
3. **The `N` promise is not measured at 47 sites.** Of the 120 body `\tierN`: 6 marks
   (a separate form, `\tier[…]{N}`) carry a `\testref` id; 71 name a script on the same
   line; **47 name no test and no script within ±1 line**. The family rule: every
   numerical mark carries its test, *or* the sentence says where the check is ours.
4. **The `P*` promise is stale — and its proof is not in this report's reach.**
   "written in Lean with no `sorry` or `axiom`, not yet compiled against the current
   corpus": F9-001 verified **416/416** starred names present in
   `lean/F1_pentagonal_descent_UNIFIED.lean` and `lake build` is green, but F9
   verified *name presence*, not sorry/axiom freedom; the file's own status banners
   disagree (`0 sorry, 0 axiom` at line 49195, older banners still reading `1 sorry`
   at 8001 and 15137). Hence P*→P is **mechanical-subject-to-reconciliation** (D4's
   one-to-one pass), not plain mechanical.
5. **The five-step `T` list is corpus content, not a tier declaration.** It states
   which steps remain unformalised; it must survive as prose with its count
   re-measured (today: 5 prose `T` uses — `03:1542`, `03:2319`, `04:1719`,
   `04:1730`, `04:1761` — plus 4 ledger cells).
6. **The decorations are defined in the wrong place.** `°` and `†` are defined here
   but first used at `02:137` and `02:852`; the family defines label classes at the
   list they label. The hypothesis rule (256–258) is operational — `docs/citations.md`
   §8 territory, not evidence-class content.

Also load-bearing: **5 `\cref{ssec:protocol}` references** — `01:287`, `01:289`,
`01:326` (the notation index), `03:142`, `appendix:11`. Deleting the subsection breaks
them; keeping it (renamed, holding Notation + the index) does not.

### 3.3 Proposed rewrite (one gate, recommended option stated)

1. **Move a flat two-line gloss to before the first mark** (`01:112`), declaring only
   the two evidence classes:
   `"[P] marks a statement proved in Lean 4~\cite{demoura21} with
   Mathlib~\cite{mathlib20}; [N] marks a statement verified numerically, with the
   test named in the mark."` — nothing else, no level count, no legend.
2. **Delete the eight-level enumeration** (250–255). P\*, T, C, Nc, O and R retire to
   prose per §5.
3. **The five-step `T` list moves into prose** (the Compilation item `05:1209`, or a
   remark), with its count re-measured at rewrite time.
4. **P\* leaves the paper** → `docs/citations.md` (where the witness-contract already
   documents it). `°` and `†` get one plain sentence at their first use (`02:137`,
   `02:852`). The hypothesis rule (256–258) → `docs/citations.md` §8.
5. **Keep the subsection and its label** (`ssec:protocol`), holding what remains
   (Notation and the index of statements), or retarget the 5 `\cref`s — decided with
   this gate.
6. **Measure before wording ships**: the new `N` sentence must match finding 3 —
   either F10 supplies the ids for the 47 bare sites, or the gloss says where the
   check is ours.

## 4. Context patterns with before/after (the most repeated)

Each pattern is a disposition class: `(a)` = standard prose without a mark (with its
`\cite` if the source requires one), `(b)` = explicit witness `P`/`N[ids]`.

| # | pattern | n | site | before | after | kind |
|---|---|--:|---|---|---|---|
| 1 | **P\* beside a Lean name** (name blocks) | 114 | `02:755` | `$…=\golden^{\chiv(a)}$ (\LeanStar{F1CW.norm\_cosine\_phi} \tierPnew);` | `(b)` `$…=\golden^{\chiv(a)}$ (\LeanInline{F1CW.norm\_cosine\_phi} \tierP);` — star decoration retires with the class (416 `\LeanStar` uses) | mechanical, subject to D4 reconciliation |
| 2 | **C with the cite adjacent** | 24 | `03:1625` | `\cite[Thm.~9.2, Thm.~9.4]{cox13} \tierC; checked on` | `(a)` `\cite[Thm.~9.2, Thm.~9.4]{cox13}; checked on` | mechanical — the source lives in `\cite`, never in the mark |
| 3 | **C, source named in prose** | 30 | `03:1095` | `…the Teichmüller lift itself by Hensel's lemma \tierC;` | `(a)` delete the mark; the sentence already names the source | mechanical |
| 4 | **C, no source on the line** | 27 | `03:1422` | `(iv) and (v) \tierC; (vii) from (vi) and $…$ \tierC;` | `(a)` `(iv) and (v); (vii) from (vi) and $…$;` | mechanical — unmarked prose is the family signal for a standard claim; whether a `\cite` is *owed* at any of these sites is a citation question for the CIT pass, not a tier decision |
| 5 | **O where prose says "open"** | 10 | `03:2247` | `the odd $s=2k+1\ge3$ it is open \tierO.` | `(a)` `the odd $s=2k+1\ge3$ it is open.` | mechanical |
| 6 | **T whose demonstration is in the text** | 4 | `03:2319` | `the odd values lie where no finite quotient reaches \tierT.` | `(a)` `… reaches.` | mechanical |
| 7 | **R in a "reading" sentence** | 5 | `04:1769` | `… that the open step lies in their assembly is a reading \tier{R}.` | `(a)` `… is a reading.` | mechanical — R is retired by the author; the prose already carries the word |
| 8 | **Nc with an error-accounting script beside** | 8 | `04:499` | `… satisfies $Q(f)\ge0.0445\,\|f\|^2$. \tierNc{} computer-assisted in interval arithmetic, with outward rounding (\cref{rmk:rigour});` | `(a)` `… $Q(f)\ge0.0445\,\|f\|^2$, computer-assisted in interval arithmetic …` **or** `(b)` `… $Q(f)\ge0.0445\,\|f\|^2$ N[weil_window_chi5_threshold], computer-assisted …` | **gate** — no runnable test for this error accounting exists today (`grep` for `interval`/`cholesky`/`0.0445` in `tests/` → 0 hits); option (b) needs F10 |
| 9 | **Ledger `Tier` cell with a non-standard letter** | 58 | `03:3741` | `First zero at $…$ (\LeanInline{NoLowZeros}) & classical; not proved in Lean & \tierC\\` | `(a)` the cell takes a word (`classical`), or the claim moves out of the column | **gate** — one class-convention decision for the column (39 C + 10 O + 5 Nc + 4 T cells), not 58 separate ones |
| 10 | **P\* as a status assertion** | 7 | `appendix:12` | `marked \tierPnew\ are written and not yet compiled, and become \tierP\ or are corrected when they are.` | `(a)` reword: the P\* category retires, and what is compiled must be stated from the corpus | **gate** — the sentence makes a factual claim the author owns |

**Compound marks** (two tags on one claim — the one-claim-one-tag rule): the `/` pairs
`03:114` (`\tierP/\tierC`), `03:2443`, `03:4635` (both `\tierP/\tierPnew`), `03:3028`
(`\tierC/\tierN`), `appendix:99` (`inputs \tierC/\tierN`), the `+` pair `05:567`
(`\tierC+\tierN`) and the `;` pair `05:683` (`\tierC; \tierO`). Where the surviving
mark stands alone the row is mechanical **but the separator must go with the deleted
mark**; where both tags are in question the row is in the gate (`03:2443`,
`03:3028`, `05:683`, `appendix:202` ×2).

## 5. Destination per class (against the convention)

| class | n | mech | gate | destination | why |
|---|--:|--:|--:|---|---|
| **P\*** `\tierPnew` | 246 | 236 | 10 | **`P`**, one-to-one via F11/D4; the star decoration `\LeanStar`→`\LeanInline` (416 uses) retires with it | the alphabet has no paper-visible P\* (it is internal, `docs/citations.md`); F9 verified 416/416 names present and the corpus builds — *subject to D4's per-declaration sorry/axiom reconciliation* (finding 3.2.4) |
| **C** `\tierC` | 143 | 82 | 61 | **prose + the adjacent `\cite`** | the source already sits next to the claim; the family never puts a source inside a mark, and it has no C class. The 61 gate rows are: 16 bare (no source on the line), 5 coupled (dangling `given`/compound), 39 ledger cells, 1 gloss |
| **O** `\tierO` | 44 | 11 | 33 | **prose, with the word "open"** | 11 sites already say it; the 33 gate rows need the word written (13 mid-sentence, 9 stand-alone, 10 ledger cells, 1 gloss) |
| **Nc** `\tierNc` | 15 | 1 | 14 | **gate**: (a) prose, or (b) `N[ids]` with a snake_case id pending F10 | Nc claims computer-assisted error accounting; **no runnable test for it exists in `tests/` today** (0 hits), so the `N[ids]` witness cannot be verified against `verify:py` — every substantive row is a judgment |
| **T** `\tierT` | 11 | 5 | 6 | **prose** (the demonstration is the text) | 4 sites read as ordinary claims; the gate rows are 1 stand-alone mark, 4 ledger cells, 1 gloss |
| **R** `\tier{R}` | 12 | 5 | 7 | **prose** | R was retired by the author; 5 sites already say "reading", the 7 others (6 mechanism sentences without the word, 1 gloss) are the gate |
| **total** | **471** | **340** | **131** | | |

## 6. Disposition — mechanical rows vs the decision gate

### 6.1 Mechanical (340 rows — applied by the wave, no author input)

Grouped by pattern: identical disposition, full site lists. The example row of each
pattern is §4.

| pattern | n | sites (`file: lines`) |
|---|--:|---|
| `P*-name-level` | 114 | `02-foundations.tex`: 755,850,891 · `03-mechanisms.tex`: 158,167,180,620,869,884,921,941,987,1009,1064,1094,1117,1130,1148,1163,1200,1273,1280,1294,1319,1421,1466,1475,1478,1503,1582,1620,1692,1755,1766,1768,2067,2160,2209,2222,2225,2619,2724,2764,2966,3022,3027,3258,3300,3325,3355,3497,3694,3795,4089,4186,4247,4252,4521,4635 · `04-bridges.tex`: 126,381,395,401,409,457,867,888,902,912-913,941,944,958,1020,1059,1109,1118,1132,1150,1162,1178,1191,1244,1270,1310,1368,1440,1444,1470,1491,1565,1567,1611,1613,1627,1673,1785,1833,1851,1856,1914,1941,1943,1947 · `05-categorical.tex`: 333,672,754,899,931,970,1029,1103,1111 |
| `P*-ledger-letter` | 107 | `03-mechanisms.tex`: 3737-3738 · `04-bridges.tex`: 655,823-824,830-831,833 · `appendix.tex`: 21-24,35-41,43,48-50,52,59-60,66,78,82-97,99,103-104,107-112,117-122,124-127,146-147,149-150,157,163,169-170,172-173,175,179-181,187,191,213-215,218,220-221,240,247,260,267-276,278,280-281,285,287,291,293-294,296 |
| `C-source-named` | 30 | `03-mechanisms.tex`: 114,287,1095,1646,1705,2161,2366,2379,3561-3562,3744,3947 · `04-bridges.tex`: 396,458,667,867,888,930,971,1312,1371,1451,1673,1915 · `05-categorical.tex`: 566-567,1231 · `appendix.tex`: 134,447 |
| `C-prose-plain` | 27 | `03-mechanisms.tex`: 1422,1542,1567,2000,2044,2084,2238,2284,2296,2320,2764,2806,3620 · `04-bridges.tex`: 46,748,792,804,908,1192,1301,1562,1587,1724,1945 · `appendix.tex`: 35,40 |
| `C-cite-adjacent` | 24 | `03-mechanisms.tex`: 1625,1740,1743,2104,2226,2240-2241,2245,2267,2290,2298,2301,2316,2570,2684 · `04-bridges.tex`: 380,1375,1565,1598,1708,1735 · `05-categorical.tex`: 563 · `appendix.tex`: 322 |
| `P*-ledger-mixed` | 14 | `04-bridges.tex`: 832 · `05-categorical.tex`: 563-569 · `appendix.tex`: 20,30,42,113 |
| `O-prose-says-open` | 10 | `02-foundations.tex`: 903 · `03-mechanisms.tex`: 2247,2308,4416 · `04-bridges.tex`: 1422,1424 · `05-categorical.tex`: 555,690 · `appendix.tex`: 130,447 |
| `macro-def` | 5 | `main.tex`: 224-225,227-228,230 |
| `R-reading-word` | 5 | `03-mechanisms.tex`: 3588 · `04-bridges.tex`: 1769 · `05-categorical.tex`: 435,458,1251 |
| `T-prose` | 4 | `03-mechanisms.tex`: 1542,2319 · `04-bridges.tex`: 1719,1730 |
| **total** | **340** | |

### 6.2 Decision gate (131 rows — for the author)

One row per site: `site | antes | propuesta | ¿mecánica?`. Every proposal is the
recommended disposition; where real alternatives exist the cell names them
(`(a) … or (b) …`). The block of §3 (the gloss) is **one** decision covering its
seven uses and is the first row.

| site | antes | propuesta | ¿mecánica? |
|---|---|---|:-:|
| `01-introduction.tex:250` | `Statements carry tiers: \tierP\ proved in Lean~4~\cite{demoura21} with Mathlib~\cite{mathlib20}; \tierPnew\ written in Lean with no \texttt{sorry} or \texttt{axiom}, not yet co…` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `01-introduction.tex:250` | `…rPnew\ written in Lean with no \texttt{sorry} or \texttt{axiom}, not yet compiled against the current corpus; \tierT\ proved in the text` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `01-introduction.tex:253` | `gluing of the local models in the remark after it, and the connectedness step of \cref{rmk:G-motivic}); \tierC\ assumed from the` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `01-introduction.tex:254` | `literature and cited where it enters; \tierN\ verified numerically; \tierNc\ computer-assisted with explicit error` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `01-introduction.tex:255` | `accounting, outside Lean; \tierO\ open; \tier{R} a reading: a mechanism proposed to join statements of…` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `01-introduction.tex:255` | `accounting, outside Lean; \tierO\ open; \tier{R} a reading: a mechanism proposed to join statements of the other tiers…` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `01-introduction.tex:259` | `citations, a name marked $^{*}$ is \tierPnew; a name marked $^{\circ}$ is a` | Rewrite the block per §3.3 (flat P/N gloss moved to the first mark; P\*/°/† + hypothesis rule → `docs/citations.md`; five-step T list → prose). **The one decision covering all 7 uses.** | No |
| `03-mechanisms.tex:2443` | `\tierP/\tierPnew` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `05-categorical.tex:1209` | `…wenty-seven modules of this version are compiled (\cref{app:lean}); the other declarations written for it are \tierPnew:` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `05-categorical.tex:1219` | `    \tierPnew.` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `appendix.tex:12` | `marked \tierPnew\ are written and not yet compiled, and become \tierP\ or are correcte…` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `appendix.tex:367` | `…2F1Circle}, \texttt{PhiCelda}, \texttt{W4Isometria} and \texttt{F1PaperClosureClock}.  Their declarations are \tierPnew; cited inside a` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `appendix.tex:395` | `\tierPnew.` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `appendix.tex:446` | `Mersenne numbers, and what the fluctuation takes from each prime. Together they add $156$ proved statements \tierPnew, $26$ open` | Rewrite the status sentence: the P\* category retires (F9 416/416 present, build green); re-count the figures from the corpus. | No |
| `03-mechanisms.tex:1170` | `\tierPnew; up to $p=19$ also \LeanInline{fib\_split\_criterion} \tierP).}` | Move the mark out of the `\caption` into the body sentence (05 §8.2 rule 8 retires caption marks). | No |
| `03-mechanisms.tex:1422` | `(iv) and (v) \tierC; (vii) from (vi) and $\sum_{n\leq N}\phi(n)=3N^2/\pi^2+O(N\log N)$ \t…` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:1542` | `…odd\_level\_doubled} \tierP\ given that $\Phi_m$ is palindromic and $\Phi_{2m}(x)=\Phi_m(-x)$ for odd $m\ge3$ \tierC, the second \tierT; (iii) from $\sum_{m\leq x,\ m\ \mathrm{odd}}\phi(…` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:2660` | `\tierC` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:3104` | `quotients by these properly discontinuous free actions are covering spaces \tierC\par}` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:3564` | `$L^2$, by density \tierC\par}` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:3844` | `(\LeanInline{MateSinG.closed\_under\_mate\_of\_fe\_dual} \tierP; the functional equation \tierC).  The reality` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:4186` | `…_line}, \LeanStar{F1PaperClosure.integral\_trace\_gives\_degenerate} \tierPnew; the bound with the first zero \tierC` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:4316` | `the height of the first zero \tierC\par}` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `04-bridges.tex:1193` | `polynomials of degree $<N$, with that $\varrho$ (\LeanStar{F1PaperTorus.LehmannBounds} \tierC), then gives` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `04-bridges.tex:1614` | `\LeanStar{F1PaperClosure.ClassicalHalfScale} \tierC\par}` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `04-bridges.tex:1833` | `\tierPnew, the expansion \tierC), and through` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `05-categorical.tex:596` | `is not $L(s,\chiv)$, and the local isometry does not give the line.  \tierC` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `05-categorical.tex:654` | `\tierC` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `05-categorical.tex:804` | `\tierP\ in the injectivity of the scale; (ii) the kernel \tierC` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `05-categorical.tex:933` | `\tierP\ given the class-number formula \tierC` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `appendix.tex:113` | `…ment of $r$ and $t$ & \tierP\ (closure under conjugation and mate \tierPnew; confinement given the first zero \tierC) & \cref{prop:each-zero} & None uses that the zero is on the line.\\` | State the source in prose (add `\cite` or the source word), or accept the claim as standard — author wording. | No |
| `03-mechanisms.tex:3028` | `$L(2,\chiv)$, $L(4,\chiv)$ \tierC/\tierN.}` | Split the compound: keep the surviving mark, remove the separator (`/`, `;`, `+`) with the deleted one. | No |
| `04-bridges.tex:61` | `(\LeanInline{four\_equalities\_on\_the\_set} \tierP\ given \tierC).  The first is the multiplicative half of \Ecore, proved for every z…` | Split the compound: keep the surviving mark, remove the separator (`/`, `;`, `+`) with the deleted one. | No |
| `05-categorical.tex:683` | `$C\times C$.  \tierC; \tierO\ for the cohomology.` | Split the compound: keep the surviving mark, remove the separator (`/`, `;`, `+`) with the deleted one. | No |
| `appendix.tex:202` | `$T_K=5L(1,\chiv)L(1,\chi_4\chiv)$; $T_K$ and $\zeta_K(2k+1)$ & \tierP\ given \tierC; \tierC; the values at $s=3$ \tierN; relation with $\log\golden$ \tie…` | Split the compound: keep the surviving mark, remove the separator (`/`, `;`, `+`) with the deleted one. | No |
| `appendix.tex:202` | `$T_K=5L(1,\chiv)L(1,\chi_4\chiv)$; $T_K$ and $\zeta_K(2k+1)$ & \tierP\ given \tierC; \tierC; the values at $s=3$ \tierN; relation with $\log\golden$ \tierO & \te…` | Split the compound: keep the surviving mark, remove the separator (`/`, `;`, `+`) with the deleted one. | No |
| `03-mechanisms.tex:3741` | `First zero at $\gamma\approx6.6485$ (\LeanInline{NoLowZeros}) & classical; not proved in Lean & \tierC\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `03-mechanisms.tex:4212` | `6 & bound & $t\le2.00013$ from the strip and $\|\gamma\|\ge6.6485$ (\cref{prop:rbound}) & \tierP,\,\tierC\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:38` | `The prism at $5$ & \tierPnew, \tierC & \texttt{F1PaperSixty.bk\_delta\_E}, \texttt{bk\_special\_fiber\_is\…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:41` | `Amplitude of clause (ii) & \tierPnew, \tierC & \texttt{W4Isometria.pair\_defect}, \texttt{amplitude\_eq\_iff\_line…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:62` | `First zero at $\gamma\approx6.6485$ & \tierC & \texttt{NoLowZeros} (definition) & Classical; not proved in Lean.  …` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:64` | `Strip bound on $r$ (link 6) & \tierP\ ($t\le2.00013$ also uses \tierC) & \texttt{rSq\_le\_in\_strip} & Previously a numerical observation.\…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:75` | `Power action on zero coordinates $\Leftrightarrow$ \Ecore & \tierP\ given \tierC & \texttt{B\_iff\_E\_one\_hypothesis} & Given \texttt{NoLowZeros}.\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:89` | `What the fluctuation takes from each prime & \tierPnew, \tierC, \tierN & \texttt{F1PaperPadic.local\_phase\_contribution}, \texttt{a…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:91` | `Pappus' parameter: the zeros classified by the eccentricity $e=2/t$ of their conic & \tierPnew, \tierC & \texttt{F1PaperClosure.eccentricity\_eq\_one\_iff}, \texttt{zero\_c…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:96` | `Explicit formula for $L(s,\chi_5)$ & \tierC; coefficients \tierPnew & \texttt{F1WeilFunctional.ExplicitFormulaChi…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:99` | `First window, $L\le0.7447$ & \tierPnew, inputs \tierC/\tierN & \texttt{F1v2.first\_window\_integral} and its steps & $m(\lo…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:110` | `Counting function: weights, local assembly & \tierPnew; global \tierC & \texttt{F1v2.pcf\_counting\_weights}, \texttt{local\_log\_deriv} & …` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:111` | `Residue of $\zeta_K$ at $s=1$ & \tierPnew\ given \tierC & \texttt{L1\_from\_class\_number\_formula}, \texttt{class\_number\_o…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:128` | `The fibres of $G$ on the levels of the clock & \tierP; mass \tierC; one statement of (ii) \tierT & \texttt{FibrasPorNivel}, \texttt{Paso…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:131` | `The mate without the reality of the character & \tierP; functional equation \tierC & \texttt{MateSinG.closed\_under\_mate\_of\_fe\_dual} & New (\cref{rm…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:133` | `What an operator of the level does not separate & \tierP; spectral theorem \tierC & \texttt{PCFGranularity}, \texttt{ObservablesDelNivel}, \texttt{Fibr…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:148` | `Unit ranks & \tierP, \tierC & \texttt{unit\_rank\_splits\_branches}, \texttt{branches\_are\_the\_…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:157` | `The ring of integers & \tierP, \tierPnew, \tierC & \texttt{quadratic\_ring\_is\_Z\_phi}, \texttt{the\_rule\_is\_proved…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:183` | `The golden ratio names the fifth roots of unity & \tierP; Chebotarev \tierC; frequencies \tierN & \texttt{PasosDelTexto.fifth\_root\_trace}, \tex…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:185` | `Ideals of norm $n$; split primes of density $\tfrac12$ & \tierC; the classes \tierP & \texttt{G\_pi2\_is\_chi5} & \cref{sec:dedekind}…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:192` | `The discriminants of the three quadratic fields of the conductor & \tierP; the fields \tierC & \texttt{three\_subfield\_discs}, \texttt{disc\_K\_is\_conductor\_sq…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:193` | `Split laws of the four fields & \tierP; the fields \tierC & \texttt{three\_quadratic\_subfields} & \cref{thm:dedekind-natural}.…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:195` | `Fundamental formula & \tierP, \tierC & \texttt{anchor\_is\_a\_crossed\_identity} & \cref{thm:L1}.\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:196` | `$L(1,\chiv)$ by Gauss--Lerch & \tierP\ given \tierC & \texttt{F1OZ.lerch\_arith} & After \cref{thm:L1}.\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:198` | `Generalised Bernoulli values $B_{2k,\chiv}$, $k\le4$ & \tierN; formula \tierC & \texttt{oz\_carried.py} & \cref{ssec:odd-zeta}.\\ % pending(D7)` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:200` | `Polylogarithmic form; distances on the circle; the conditional on algebraicity & \tierP; Baker \tierC; the forms at $s=1,3,5$ \tierN & \texttt{F1OZ.fourier\_projection}, \…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:201` | `$L(2k,\chiv)$ and $\sum\chiv(a)\mathrm{Li}_{2k}(\zeta_5^a)$ transcendental & \tierP\ given \tierC & \texttt{F1OZ.even\_value\_transcendental} & \cref{rmk:nature-L}; Li…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:203` | `$G$ and the motivic Galois group & \tierC, \tierT & --- & \cref{rmk:G-motivic}.\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:204` | `Hurwitz representation of $L(s,\chi_5)$ & \tierP, \tierC & \texttt{hurwitz\_representation\_L\_chi5} & \cref{thm:hurwitz}.\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:205` | `$\sum\chiv(a)\psi(a/5)=-2\sqrt5\log\golden$ & \tierP\ given \tierC & \texttt{F1OZ.digamma\_sum} & \cref{thm:hurwitz}.\\` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:211` | `The fibre over the tower is $\mu_6$ & \tierP; the cover \tierC & \texttt{PCFGranularity.phiSig\_period\_six}, \texttt{PCFGranularity…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:252` | `Four equalities on the whole zero set & \tierP\ given \tierC & \texttt{four\_equalities\_on\_the\_set} & After \cref{prop:three-re…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:266` | `The two halves & \tierP, \tierC & \texttt{coordinate\_is\_equivariant}, \texttt{coords\_closed\_under…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:267` | `Neither side of the structure is enough alone & \tierPnew; \tierC & \texttt{F1PaperTorus.mertens\_positivity\_mathlib}, \texttt{F1Paper…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:273` | `The archimedean form of $\zeta_K$, explicitly; $D\ge0$ & \tierPnew; \tierC & \texttt{F1PaperTorus.autocorrelation\_le\_energy} & \cref{ssec:gold…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:274` | `The first windows over the whole function space: the low-frequency fraction and Lehmann's bounds & \tierPnew; \tierC & \texttt{F1PaperTorus.lowFrequencyFraction\_nonneg}, \texttt{F1Paper…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:279` | `The index as a degeneracy & \tierP; two Gauss-sum steps \tierT; \tierC, \tierN & \texttt{IndiceComoDegeneracion.count\_residue}, \texttt{Ind…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:287` | `What the individual determines, and where the ensemble enters & \tierP, \tierPnew, \tierC, \tierN & \texttt{extreme\_case\_is\_binary}, \texttt{E\_iff\_no\_sha…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `appendix.tex:293` | `The regulator measures the chain & \tierP, \tierPnew, \tierC & \texttt{F1v2.regulator\_measures\_the\_chain}, \texttt{F1CW.period\…` | Tier cell takes a word (`classical`) — one column convention (§4 row 9), not a per-site choice. | No |
| `04-bridges.tex:499` | `the Weil form of $L(s,\chiv)$ satisfies $Q(f)\ge0.0445\,\|f\|^2$. \tierNc{} computer-assisted in interval arithmetic, with outward rounding (\c…` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:529` | `$0.0261$. \tierNc{} computer-assisted with validated numerics: every rounding error bou…` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:832` | `…planes of the orbit (\cref{prop:W4-from-W3}) & on the planes of the windows \tierPnew; certified for $k\le25$ \tierNc; for every $k$ \tierO\\` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:1182` | `$\approx1.65$, beyond the prime-free range $[0,\log4]$ (\texttt{arch\_window.py} \tierNc). % pending(D7)` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:1207` | `\noindent (\texttt{rigorous\_chain.py}, \texttt{rho\_interval.py} \tierNc.)  So the Weil form of $\Q(\sqrt5)$ is positive on % pending(D7)` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:1877` | `(\texttt{orbita\_cert.py} \tierNc).  The orbit of $\chiv$ computed from the primes alone is fitted by %…` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:1914` | `…alf\_period\_closes} \tierP; (iii) with the tiers of the window theorems, \tierPnew\ with declared inputs and \tierNc;` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `05-categorical.tex:569` | `…he line (\cref{prop:phase-modulus}) \tierPnew; windows (\cref{thm:first-window}); (W4) certified for $k\le25$ \tierNc\ (\cref{ssec:weil-closure}) & the pairing & (W4) fails \\` | (a) prose, no mark; or (b) `N[<snake_case id of §7.2>]` pending F10 — no runnable error-accounting test exists today. | No |
| `04-bridges.tex:831` | `\tierPnew{} with declared inputs, \tierNc\\` | (a) cell word (`computer-assisted`); or (b) `N[<id>]` pending F10 — same decision as the prose Nc rows. | No |
| `appendix.tex:45` | `Window $L\le1$, $Q\ge0.0445\|f\|^2$ & \tierNc & \texttt{weil\_certificates/verify\_iv.py} & Interval arithmetic; su…` | (a) cell word (`computer-assisted`); or (b) `N[<id>]` pending F10 — same decision as the prose Nc rows. | No |
| `appendix.tex:46` | `Windows $L\le1.1,1.2,1.3$ & \tierNc & \texttt{weil\_certificates/op\_rig\_validated.py} & Validated numer…` | (a) cell word (`computer-assisted`); or (b) `N[<id>]` pending F10 — same decision as the prose Nc rows. | No |
| `appendix.tex:100` | `Windows $L\le1$ and $L\le1.3$ & \tierNc & \texttt{weil\_certificates/} & Margins $0.0445$ (interval arithmeti…` | (a) cell word (`computer-assisted`); or (b) `N[<id>]` pending F10 — same decision as the prose Nc rows. | No |
| `appendix.tex:130` | `(W4) is (W3) on the planes of the orbit; half period & \tierP; windows \tierNc & \texttt{W4DeW3}, \texttt{ParidadesJuntas}, \texttt{MedioPeriodo} & …` | (a) cell word (`computer-assisted`); or (b) `N[<id>]` pending F10 — same decision as the prose Nc rows. | No |
| `03-mechanisms.tex:970` | `localisation itself is not formalised, \tierO.}` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `03-mechanisms.tex:987` | `\LeanStar{no\_frobenius\_lift\_at\_five} \tierPnew; the localisation \tierO.}` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `03-mechanisms.tex:1622` | `\tierO, follows from (ii) since $p\equiv1\pmod4$ there: $x^4-x^2-1$ generate…` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:832` | `…ref{prop:W4-from-W3}) & on the planes of the windows \tierPnew; certified for $k\le25$ \tierNc; for every $k$ \tierO\\` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:916` | `(\LeanStar{F1PaperTorus.InverseStructureBound} \tierO; measured $\le1.23\sqrt y$ up to $3\cdot10^7$,` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:1031` | `(\tierO; recorded in Lean only schematically, as \LeanStar{F1PaperTorus.Arith…` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:1168` | `(\tierO; recorded in Lean only schematically, as \LeanStar{F1PaperTorus.Golde…` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:1311` | `\LeanStar{W4Isometria.PythagorasLaw}, \tierO; the limit in (ii) by Schur orthogonality in the` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:1433` | `\tierO, a hypothesis that implies the limit form; the` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:1436` | `\tierO, uniform over a finite set of layers, which` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `04-bridges.tex:1944` | `(W4), \LeanStar{F1PaperTorus.W4Chi5} \tierO; the explicit formula on the orbit,` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `05-categorical.tex:683` | `$C\times C$.  \tierC; \tierO\ for the cohomology.` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `appendix.tex:36` | `…metria.split\_layer\_law}, \texttt{even\_index\_indicator} & New (\cref{prop:phi-layers}); \texttt{KernelLaw} \tierO.\\` | Insert the word `open` at the mark (the word carries it, no legend). | No |
| `03-mechanisms.tex:1315` | `(\LeanInline{GLandsInTheTower} \tierO).  What is proved is` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `04-bridges.tex:396` | `GRH$(\chiv)$ is Weil's criterion \tierC; the bound itself is \tierO.` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `04-bridges.tex:986` | `$\Q(i,\sqrt5)$ are $\ge0$ for every $L$} (\LeanStar{F1PaperTorus.FieldFejerPositivity} \tierO), which gives the` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `04-bridges.tex:1137` | `(\LeanStar{F1PaperTorus.FrobeniusActsByRotations} \tierO).  On one Frobenius orbit this is exactly` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `04-bridges.tex:1429` | `\LeanStar{F1PaperClosure.CorrectionIsLimit} \tierO;` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `04-bridges.tex:1509` | `zeros (\cref{prop:sqrt-x}).  \tierO` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `appendix.tex:39` | `$\sqrt X$ as the root of the energy & \tierPnew, \tierO & \texttt{W4Isometria.symEnergy\_le}, \texttt{sqrt\_law\_of\_pythagor…` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `appendix.tex:84` | `…1CW.norm\_cosine\_phi} & The closed sine formula of \cite{grisales25} is a marker (\texttt{GLandsInTheTower}, \tierO).\\` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `appendix.tex:202` | `…$ and $\zeta_K(2k+1)$ & \tierP\ given \tierC; \tierC; the values at $s=3$ \tierN; relation with $\log\golden$ \tierO & \texttt{F1OZ.period\_from\_the\_chi5\_fibre}, \texttt{degenerate\_o…` | Attach the claim with the word `open`, or drop the mark if the claim is not open. | No |
| `appendix.tex:26` | `& \tierO` | Tier cell word `open`. | No |
| `appendix.tex:39` | `…Pnew, \tierO & \texttt{W4Isometria.symEnergy\_le}, \texttt{sqrt\_law\_of\_pythagoras}; \texttt{PythagorasLaw} \tierO & New (\cref{prop:sqrt-x}).\\` | Tier cell word `open`. | No |
| `appendix.tex:42` | `Second step of the closure, in the form of the clock & \tierO & \texttt{F1PaperClosureClock.ClockLayerEnergyBounded}; \texttt{famil…` | Tier cell word `open`. | No |
| `appendix.tex:47` | `Prismatic route to the closure & \tierO & --- & \cref{conj:prismatic-route}; its clauses' proved parts are li…` | Tier cell word `open`. | No |
| `appendix.tex:71` | `Identification of the two branches of the span & \tierO & \texttt{TheSpanIdentifiesThem} (marker) & The branches meet at $\lo…` | Tier cell word `open`. | No |
| `appendix.tex:97` | `Weil positivity (full) & $\Leftrightarrow$ \Ecore, \tierO; the reduction to the prime side \tierPnew & \texttt{positivity\_is\_…` | Tier cell word `open`. | No |
| `appendix.tex:123` | `Positivity for the field of the four fibres & \tierO & \texttt{FieldFejerPositivity} & The four Fej\'er sums of $\Q(i,\sqr…` | Tier cell word `open`. | No |
| `appendix.tex:127` | `…ng of the primes and entry of the zeros, the conjecture of the two precisions & \tierPnew; closure conjecture \tierO & \texttt{F1PaperClosure.ExactClosure}, \texttt{the\_line\_from\_W4},…` | Tier cell word `open`. | No |
| `appendix.tex:171` | `… exactly one $\Lambda_{\Z,E}$-structure on $\Zphi$, $E$ the primes $\ne5$; none at $5$ & \tierP; localisation \tierO & \texttt{FrobeniusUnico.lambda\_structure\_away\_from\_five}, \textt…` | Tier cell word `open`. | No |
| `appendix.tex:298` | `The closing step: each zero is a member of the structure (\Ecore) & \tierO & \texttt{ConjectureE} & Implied by the closure conjecture (\cref{cor…` | Tier cell word `open`. | No |
| `03-mechanisms.tex:1984` | `\tier{R} The predecessor version` | Insert `a reading` (R retired by the author), or drop the claim. | No |
| `03-mechanisms.tex:2268` | `both algebraic, by \eqref{eq:dedekind} and \LeanInline{PasosDelTexto.algebraic\_scale} \tierP.  \tier{R} The linear form is the same for every $s$ --- the points $\zeta_5^{\,…` | Insert `a reading` (R retired by the author), or drop the claim. | No |
| `03-mechanisms.tex:3278` | `\tier{R} In the same terms the predecessor version \cite{gonzalez26oddzeta} re…` | Insert `a reading` (R retired by the author), or drop the claim. | No |
| `05-categorical.tex:355` | `$\Fone$, the multiplicative relations surviving the loss of addition \tier{R}.` | Insert `a reading` (R retired by the author), or drop the claim. | No |
| `05-categorical.tex:1006` | `cannot be formed (\cref{thm:no-diagonal}), sees them determined \tier{R}.  They are also the periods that Feynman` | Insert `a reading` (R retired by the author), or drop the claim. | No |
| `05-categorical.tex:1125` | `$\chiv$-projection is $L(s,\chiv)$ \tier{R}.  The` | Insert `a reading` (R retired by the author), or drop the claim. | No |
| `04-bridges.tex:1761` | `\tierT` | Attach `proved in the text` to the claim, or drop the mark. | No |
| `appendix.tex:128` | `The fibres of $G$ on the levels of the clock & \tierP; mass \tierC; one statement of (ii) \tierT & \texttt{FibrasPorNivel}, \texttt{PasosDelTexto.palindromic\_norm} &…` | Tier cell word `in text`. | No |
| `appendix.tex:203` | `$G$ and the motivic Galois group & \tierC, \tierT & --- & \cref{rmk:G-motivic}.\\` | Tier cell word `in text`. | No |
| `appendix.tex:212` | `One operator: simple spectrum, modulus and phase, the forms as functions & \tierP, \tierT & \texttt{UnOperador.spec\_injective}, \texttt{UnOperador.norm\_spec}…` | Tier cell word `in text`. | No |
| `appendix.tex:279` | `The index as a degeneracy & \tierP; two Gauss-sum steps \tierT; \tierC, \tierN & \texttt{IndiceComoDegeneracion.count\_residue}, \te…` | Tier cell word `in text`. | No |

## 7. Naming standard and rename inventory (orders of Víctor, 2026-11-22)

### 7.1 The standard

Every id this document **proposes** (destination rows `N[ids]` or `P`) is **mostly
snake_case in English** — descriptive English words, snake_case; proper nouns kept
as they are (`weil`, `chi5`, `castelnuovo`, `zeta`, `mertens`). Acceptable:
`weil_window_chi5_thresholds`. Not acceptable: `weilWindowChi5`, `deteccionCeros`.
Ids the document does not propose (the Lean declaration names it inherits, §7.4) are
not re-spelled by this rule.

### 7.2 Proposed ids — count (i): **5, all compliant (5/5)**

These are the destination ids of the `Nc → N[ids]` option (b) of §4/§5 — future
ids for F10's tests, proposed here so the shape of the row is decided now:

| proposed id | destination rows | snake_case? |
|---|---|:-:|
| `weil_window_chi5_threshold` | `04:499`, `appendix:45` (the single bound $Q(f)\ge0.0445\|f\|^2$, interval arithmetic) | ✓ |
| `weil_window_chi5_thresholds` | `04:529`, `04:831`, `appendix:46`, `appendix:100`, `appendix:130` (the multi-window margins 0.0027 / 0.0077 / 0.0261) | ✓ |
| `weil_arch_window_bound` | `04:1182` (`arch_window.py`, support $\approx1.65$) | ✓ |
| `weil_form_positivity_chain_bound` | `04:1207` (`rigorous_chain.py`, `rho_interval.py`, the chain to $\le2.3$) | ✓ |
| `chi5_orbit_toeplitz_certificate` | `04:1877`, `04:832`, `05:569` (`orbita_cert.py`, $\|t_k\|\le0.1122\,t_0$ for $k\le25$) | ✓ |

`04:1914` (the status sentence that *references* the window theorems) takes no id:
its destination is prose. P-destination rows carry existing Lean declaration names —
they are corpus identifiers, not new ids (§7.4).

### 7.3 Rename inventory for F11 — count (ii): **7 rows**

Every witness id that exists **in the text today** inside a witness bracket
(`\tier[\testref{…}]{N}`) fails the standard: none is snake_case (they are
formula-style English — the "u otros" case). Rename is atomic across text + tests
(F11's scope): **one text site + one `check("…")` line each**. Reports are snapshots
and are **not** rewritten.

| id actual | site | id propuesto (snake_case, English) | dónde más aparece |
|---|---|---|---|
| `a_{0,0} = zeta(2) = pi^2/6` | `02-foundations.tex:7` | `zeta_two_pi_squared_over_six` | `tests:326` (the `check`); F8-001 `:1301, :1311, :1322` (historical); census: `counts.ts:6` mentions `\testref` only in a doc comment — no counter; guards: none |
| `N(phi) = phi * phi_bar = -1  (unit of norm -1)` | `02-foundations.tex:415` | `phi_unit_norm_negative_one` | `tests:85`; F8-001 `:1302, :1323, :224–225`; guards/census: none |
| `2*cos(pi/5) = phi` | `03-mechanisms.tex:103` | `two_cos_pi_over_five_equals_phi` | `tests:224` (`check`; `:422` prints the same expression); F8-001 `:1303, :1324` |
| `L(1,chi5) via digamma = 2*log(phi)/sqrt(5)` | `03-mechanisms.tex:2152` | `l_one_chi5_digamma_value` | `tests:244` (`check`; `:197` comment); F8-001 `:1304, :1325` |
| `Mersenne bridge: phi^{lambda_log} = 2` | `03-mechanisms.tex:2899` | `mersenne_bridge_phi_lambda_log_two` | `tests:152` (`check`; `:26` comment); F8-001 `:1305, :1326`; F9-001 `:445–446` |
| `Root 1 = 3/2` | `04-bridges.tex:232` | `sigma_mu_polynomial_root_three_halves` | `tests:454`; F8-001 `:1306, :1327` |
| `Root 2 = 1/2` | `04-bridges.tex:232` | `sigma_mu_polynomial_root_one_half` | `tests:455`; F8-001 `:1306, :1328` |

Notes. The 6th mark carries two ids separated by `, ` — hence 7 rows for 6 sites.
Each id is present verbatim in exactly one `check` call (F8-001's verification, re-run
for this report: 7/7). Nothing in `scripts/` parses them; `counts.ts` has no
`\testref` counter in this repository (F8-001 §4.1). **0 of the 7 are camelCase or
Spanish** — the Spanish/camelCase identifiers that *do* exist in the text are
categories that cannot be renamed here, listed next.

### 7.4 Excluded from the rename — with reason

| category | measured | why not renamed |
|---|---|---|
| **Lean declaration names** in `\LeanInline`/`\LeanStar`/`\LeanTally`/`\LeanCW`/`\texttt` | **1281 occurrences, 1052 distinct names, 44 namespaces** — of which **22 namespaces look Spanish** (`PasosDelTexto`, `W4Isometria`, `OrbitaLibre`, `FibraYReloj`, `MedioPeriodo`, `DosCarasFibonacci`, `IndiceComoDegeneracion`, `ObservablesDelNivel`, `ParidadesJuntas`, `RelojTres`, `TodoEnLean`, `UnOperador`, `AlcanceZeta`, `CierrePorAltura`, `EstructuraEnGUE`, `FibrasPorNivel`, `FrobeniusUnico`, `LadoAnalitico`, `MateSinG`, `PeriodicasSol`, `ComponentesInvoluciones`, `ZetaPentagonal`) and **36 distinct lowerCamel methods** (`liFix_root`, `rSq_le_in_strip`, `normF_eq_cos`, …) | they are **corpus identifiers, not bracket witness ids** today; after F11/D4 they become `P[…]` keys, but the family standing rule never renames a Lean declaration the manuscript cites, F9-001 verified 416/416 present, and `lean/` is outside F11's atomic scope (text + tests + guards + census). Renaming would desync the manuscript from the compiled corpus |
| **Spanish/camelCase `.py` evidence filenames** cited beside N/Nc marks | **12 of the 77 distinct `.py` names in the text**: Spanish `orbita_cert.py`, `escala_ceros_bajos.py`, `amplitud_clausula_ii.py`, `v27_reloj_ciclotomico.py`, `v28_hiperbola_reloj_tamano.py`, `v12_pitagoras_raiz_X.py`, `v30_vertice_al_azar.py`, `v33_capas_1e9.py`, `W3_orbita_lado_primos.py`; camelCase `rigW.py`, `testB1b.py`, `testGeom.py` — **all 12 absent from the repository** (D7-deferred) | they are **corpus file references, not witness ids** (F9-001's inventory owns them); F12 imports the author's zip `hipotesis/pruebas/` **with the current names**, so a rename must be coordinated there, not in F11. For F12's reference only: `orbita_cert.py`→`chi5_orbit_certificate.py`, `escala_ceros_bajos.py`→`low_zero_scale.py`, `amplitud_clausula_ii.py`→`clause_two_amplitude.py`, `v27_reloj_ciclotomico.py`→`v27_cyclotomic_clock.py`, `v28_hiperbola_reloj_tamano.py`→`v28_clock_size_hyperbola.py`, `v12_pitagoras_raiz_X.py`→`v12_pythagoras_root_x.py`, `v30_vertice_al_azar.py`→`v30_random_vertex.py`, `v33_capas_1e9.py`→`v33_layers_1e9.py`, `W3_orbita_lado_primos.py`→`w3_orbit_prime_side.py`, `rigW.py`→`rigorous_w_check.py`, `testB1b.py`→`test_b1b.py`, `testGeom.py`→`test_geometry.py` — **proposal only, no rename in F11** |

## 8. Gates

| gate | command | result |
|---|---|---|
| `validate` | `pnpm run validate` | `exit 0` — selfcitations ✓ · parity ✓ · counts ✓ · manifest ✓ · verify: lake build **18248 jobs, success** + suite |
| `type-check` | `pnpm run type-check` | `exit 0` — `tsc --noEmit` |

Repository state: `git status --porcelain` clean at `e62d1b5` (`= origin/main`) before
this file; this report adds itself plus one index row to
`docs/reports/README.md` and nothing else.

## 9. Lagunas

1. **F8-001 is not in the index.** `docs/reports/20261122_F8-001_witness_reconciliation.md`
   exists but has no row in `docs/reports/README.md` (and predates the report-header
   template). Not fixed here — this deliverable adds its own row only.
2. **47 bare `N` marks** (§3.2 finding 3): the gloss's "verified numerically" is
   unanchored at those sites until F10 supplies ids or the sentences name their check.
3. **P\*→P reconciliation is open**: name presence (F9) is not sorry/axiom freedom;
   the unified file carries contradictory status banners (§3.2 finding 4). D4's
   one-to-one pass must confirm each declaration.
4. **Counts inside prose** (`05:1209` "the other declarations … are \tierPnew";
   `appendix:446` "156 proved statements \tierPnew, 26 open …, 21 classical inputs
   with a name \tierC, of which three … are now proved") are measured claims about the
   corpus: they must be **re-counted at rewrite**, not translated.
5. **`\Ecore` (51 uses)** is a statement label outside the tier alphabet; the gloss
   does not define it. Out of F-TIERS scope, but the §Protocol rewrite must not break
   its references (the notation index points at `ssec:protocol`).
6. **Column headers** `Tier` ×4 and `status` ×1 ride with the ledger gate (§4 row 9):
   the 58 non-standard cells and the header that names them are one decision.
7. Line numbers are a snapshot of `e62d1b5`; per the reports convention this file is
   never edited to follow the manuscript.

---

## Related documents

- `docs/witness-contract.md` — why the device exists (alphabet P and N).
- `docs/citations.md` §8 — the generic rule this report instantiates (P\* documented
  there, never in the paper's legend).
- `docs/reports/20261122_F8-001_witness_reconciliation.md` — the 6 `N[ids]` marks and
  their verbatim test ids (§3.1 there = §7.3 here).
- `docs/reports/20261122_F9-001_provenance_inventory.md` — the corpus filenames and
  the 416/416 starred-name verification behind §7.4.
- `docs/reports/README.md` — reports convention and index (this report's row).
