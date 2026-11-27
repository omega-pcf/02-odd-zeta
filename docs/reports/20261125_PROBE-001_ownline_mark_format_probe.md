# Own-line mark format — localized probe (scratch, no family build)

| Field | Value |
|---|---|
| **id** | `PROBE-001` |
| **title** | Own-line mark format — localized probe: variants, definition sites and invocation counts (evidence for `witness-contract.md` §6.12) |
| **status** | report only — measurements of a scratch probe; no repository changed |
| **date** | 2026-11-25 |
| **version** | 1.0 |

Scope: the five family repos are **read-only**; everything here was produced in
`scratch/wit_std/`. Probe compiled with `kjarosh/latex:2024.4-full` (pdflatex),
geometry measured from `pdftotext -bbox-layout` (ink boxes), `pdftohtml -xml`
(font size + colour) and `\showbox` (exact TeX vertical list).

Artifacts: `probe.tex` / `probe.pdf` / `probe_page-1..4.png` (22 variants),
`probe_break.tex` / `probe_break.pdf` / `probe_break.txt` (line-breaking, 6 cases),
`measure.py` / `probe_measures.json` / `measure_out.txt`, `probe.log`.

---

## (a) Inventory — variants that render as a block / line of their own

| # | Variant (what it is) | Def site | Invocation sites per repo |
|---|---|---|---|
| V1 | `\witness{X}{ids}` — flush-right parbox, `\normalfont\footnotesize\bfseries` + `\mdseries{\upshape\small\ttfamily[...]}` | `02-odd-zeta/main.tex:238-242` | **02: 86** |
| V2 | `\witness{X}{X}{ids}` — same shell but `\footnotesize\textbf{...}{\small\texttt{[...]}}`, **no `\normalfont`** | `03-crystalline-worldsheet/main.tex:203-207` | **03: 124** (1 in a comment) |
| V3 | `\witness` byte-identical to V1 | `05-kk-golden-throat/main.tex:125-129` | **05: 43** |
| V4 | `\leanline{...}` — `\par\noindent{\footnotesize\raggedright\textsc{Lean:} …\par}\smallskip` | `02-odd-zeta/main.tex:306` | **02: 2** (`03-mechanisms.tex:957,1382`) |
| V5 | manual `{\raggedright \tier[ids]{P} … prose …\par}` — left-ragged paragraph, prose font | no macro (written inline) | **02: 23** (`03-mechanisms.tex:3044,3117,3282,3375,3450,3504,3550,4152`, `04-bridges.tex:125,865,879,935,998,1035,1059,1217,1243,1578,1592,1640,1751,1815,1877`) |
| V6 | 01 display habit `\medskip` + `\noindent\textit{…}` / `\noindent\textbf{…}` | — | **01: 4 `\medskip`, 19 `\smallskip`** (e.g. `discussion.tex:57` `\smallskip\noindent\textbf{…}` ×17) |
| V7 | 04 display habit `\smallskip` + `\noindent\emph{…}` | — | **04: 5 `\smallskip`** (`01-introduction.tex:237,249,259,270,279`), 1 `\medskip` |
| V8 | `\medskip` before `\paragraph{…}` (run-in head) | — | **02: 3** (`02-foundations.tex:588,609,630`), **03: 5**, 04: 1, 05: 1 |
| V9 | inline `\tier[ids]{X}` (reference form) | 02 `main.tex:222-233`, 03 `main.tex:182-192`, 05 `main.tex:105-121` | 02/03/05 (thousands) |
| V10 | "Lean:" accounting **inline** (not a block) | — | **01: 4** (`(Lean: …)`), **04: 26** (`Lean: \code{…}` / `\emph{Lean:} \code{…}` ×8) |

**Gaps found in the inventory**

- **01 and 04 have no mark macros at all**: `\witness`, `\tier`, `\testref`,
  `\leanline` → 0 occurrences each. Their evidence is plain `\code{…}` prose
  (01: 83, 04: 75) plus "Lean:" mentions. `docs/witness-inventory.md` of both
  records `own-line \witness{P}{…} = 0`, so the standard exists there but is
  unapplied.
- **02 carries two own-line forms at once**: the canonical flush-right `\witness`
  (86) *and* 23 hand-written `{\raggedright \tier[…] …\par}` paragraphs.
- `\leanline` is defined only in 02 (2 uses) and is explicitly *not* a body form
  (`docs/witness-standard.md` §2, §5 S4).
- Colour palette is not shared: 02/05 `tierP/N/W`, 03 `tagP/N/H` (different
  green, plus an extra red), 01/04 no mark colour.

### Definitions read (verbatim, condensed)

```latex
% 02 main.tex:238  == 05 main.tex:125  (bodies identical)
\newcommand{\witness}[2]{%
  \par\noindent\hfill
  \parbox{\dimexpr\linewidth-1em\relax}{\raggedleft
    \normalfont\footnotesize\bfseries\tiercol{#1}#1\mdseries{\upshape\small\ttfamily[\tierids{#2}]}}%
  \par}

% 03 main.tex:203  — the only difference is the body font block
\newcommand{\witness}[2]{%
  \par\noindent\hfill
  \parbox{\dimexpr\linewidth-1em\relax}{\raggedleft
    \footnotesize\tiercol{#1}\textbf{#1}{\small\texttt{[\tierids{#2}]}}}%
  \par}

% 02 main.tex:306
\newcommand{\leanline}[1]{\par\noindent{\footnotesize\raggedright\textsc{Lean:} #1\par}\smallskip}
```

Underscore constant (the breaking difference):
`01/04` `{{\ttfamily\char95\relax}\allowbreak}` (OT1, `main.tex:86/94`) ·
`02` `\textunderscore\allowbreak` (`main.tex:175`) ·
`05` same (`main.tex:45`) ·
`03` `\textunderscore` **without** `\allowbreak` (`main.tex:161`).

Skip amounts (amsart redefines them, `amsart.cls:182-184`):
`\bigskipamount=.7\baselineskip plus .7\baselineskip`,
`\medskipamount=\bigskip/2`, `\smallskipamount=\medskip/2`
→ at `\baselineskip=13pt`: **\medskip = 4.55pt (no shrink), \smallskip = 2.275pt**.

---

## (b) Probe + measurements

Common setup for all five repos: `\documentclass[11pt,reqno]{amsart}` +
`\usepackage[margin=1in]{geometry}` → **\textwidth = \linewidth = 469.755pt**,
`\parskip = 0`, `\baselineskip = 13.0pt`, `\parindent = 11.95pt`, prose font
10.95pt (`pdftohtml` px 16). Page margins in the probe: left 72.0pt, right 540.01pt.

### (b1) Exact vertical rhythm — baseline-to-baseline, from `\showbox` (pt)

| Case | above the mark | below the mark | Δ vs prose (13.000) |
|---|---|---|---|
| H prose → prose (control) | 13.000 | — | — |
| A 02 `\witness`, 1 line | 13.000 | 13.000 | **0 / 0** |
| B 03 `\witness`, 1 line | 13.000 | 13.000 | **0 / 0** |
| C 05 `\witness`, 1 line | 13.000 | 13.000 | **0 / 0** |
| E 02 manual `{\raggedright\tier…}` | 13.000 | 13.000 | **0 / 0** |
| D 02 `\leanline` | **11.000** | **15.275** | **−2.000 / +2.275** |
| F 01/03 `\medskip` + `\noindent` head | **17.550** | 13.000 | **+4.550 / 0** |
| G 04 `\smallskip` + `\noindent` head | **15.275** | 13.000 | **+2.275 / 0** |
| I/J 2-line `\witness` (parbox) | **13.820** | **15.889** | **+0.820 / +2.889** |

Notes on how those numbers arise (from the log):

- single-line block: interline glue `5.6803 = 13 − 0 − 7.3197` above,
  `3.61378 = 13 − 1.84473 − 7.54149` below → exactly `\baselineskip`.
- `\leanline` sets `\footnotesize` **inside** the group where `\par` runs, so
  `\baselineskip` is 11pt there: `4.25165 = 11 − 0 − 6.74835` → 11.000 above;
  `\smallskip` 2.27498 below.
- `\medskip`/`\smallskip` are inserted literally: `4.54997` and `2.27498`.
- multi-line parbox: the whole block is one box (ht 12.8197, dp 7.34473), so TeX
  falls back to `\lineskip = 1.0` above and below → asymmetric 13.820 / 15.889;
  inside the box the lines sit on the 11pt `\footnotesize` rhythm.

### (b2) Ink geometry from the rendered PDF (`measure_out.txt`)

| id | variant | gap_before | gap_after | mark x0 | mark x1 | right gap | after-para indent | letter px/colour | ids px/colour |
|---|---|---|---|---|---|---|---|---|---|
| V0 | prose control | 3.32 | — | — | — | — | 11.95 | 16 / #000000 | — |
| V1 | 02 `\witness` | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V2 | 03 `\witness` | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V3 | 05 `\witness` | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V4 | 02 mid-line call | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V5 | 05 same-line tail | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V6 | 02 `\leanline` | 2.12 | 5.16 | 72.00 | 356.58 | 183.43 | 11.95 | 13 / #000000 (`\textsc`) | [P] 13 / #2659a5 |
| V7 | 02 manual block | — (page break) | 3.32 | 72.00 | 500.97 | 39.04 | 11.95 | 13 / #2659a5 | 15 / **#000000** |
| V8 | 01 `\medskip`+head | 9.11 | — | 72.00 | 540.00 | 0.00 | **0.00** | 16 italic / #000000 | — |
| V9 | 04 `\smallskip`+head | 6.21 | — | 72.00 | 540.00 | 0.00 | **0.00** | 16 italic / #000000 | — |
| V10 | 03 `\medskip`+`\paragraph` | 9.11 | — | 72.00 | 540.00 | 0.00 | **0.00** | 16 roman / #000000 | — |
| V11 | inline `\tier[ids]{P}` | 3.32 | — | (in prose) | — | — | 0.00 | 13 / #2659a5 | 15 / **#000000** |
| V12 | medium ids, 02 | −0.39 | 0.99 | 114.43 | 540.00 | 0.00 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V13 | medium ids, 03 (no `\allowbreak`) | −0.39 | 0.99 | 198.09 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V14 | medium ids, 05 | −0.39 | — (page) | 114.43 | 540.00 | 0.00 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V15 | long ids, 03 | −0.39 | 0.99 | 156.26 | 540.01 | 0.00 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V16 | long ids, 02 manual block | 4.65 | 3.22 | 72.00 | 511.24 | 28.76 | 11.95 | 13 / #2659a5 | 15 / **#000000** |
| V17 | 03 inside `\itshape` | 4.27 | 3.60 | 402.04 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 **SFBI (bold-italic)** | 15 / #2659a5 **SFIT (italic tt)** |
| V18 | 05 inside `\itshape` | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 SFBX | 15 / #2659a5 SFTT |
| V19 | proposed F1-A, own-line | 4.27 | 3.60 | 402.03 | 540.00 | 0.01 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |
| V20 | proposed F1-A, mid-line | — (stays inline) | — | — | — | — | 0.00 | 13 / #2659a5 | 15 / #2659a5 |
| V21 | proposed F1-A, long ids | −0.39 | — | 98.74 | 540.00 | 0.00 | 11.95 | 13 / #2659a5 | 15 / #2659a5 |

`gap_*` are ink-box gaps (they depend on glyph height, hence the −0.39 on
multi-line blocks); the **baseline** numbers in (b1) are the ones to quote.

Sizes confirm `docs/witness-standard.md` §7 exactly: **13 = letter
(`\footnotesize` 9pt), 15 = ids (`\small` 10pt), 16 = prose (10.95pt)** —
`pdftohtml` reports them in px at its 1.5 scale.

### (b3) Line breaking (`probe_break.txt`, 0 Overfull in all 6 cases)

```
02 / 05 ( \textunderscore\allowbreak ):
  P[trZeta_crystallographic_values, trZeta_not_integer_of_ge_seven, twenty_divisor_
    lattice_splits, three_conductors_are_the_minimal_failure]
                                  ^^^^^^^^^^ break INSIDE the identifier

03 ( \textunderscore, no \allowbreak ):
  P[trZeta_crystallographic_values, trZeta_not_integer_of_ge_seven,
    twenty_divisor_lattice_splits, three_conductors_are_the_minimal_failure]
                                  ^ breaks only at the space after the comma
```

Same for the long list (04-implications:733 ids): 02/05 break after
`threshold_`, 03 keeps `threshold_ordering,` whole. Left edge differs too:
114.43pt (02/05) vs 198.09pt (03) for the same text — the ragged shape is not
comparable across repos.

---

## (c) Diagnosis — the "valleys and crests", each with its exact site

1. **Vertical space is not one value, it is five.** Baseline-to-baseline around a
   block reads 11.000 / 13.000 / 13.820 / 15.275 / 15.889 / 17.550 pt depending
   on which form is used:
   - `\witness` and the manual raggedright block: **13.000 = no air at all**
     (`02/main.tex:238`, `03/main.tex:203`, `05/main.tex:125`, the 23 sites of
     `02/src/chapters/03-mechanisms.tex` and `04-bridges.tex`);
   - `\leanline`: **−2.000 above, +2.275 below** (`02/main.tex:306` — the
     `\footnotesize` group changes `\baselineskip` before the `\par`, then
     `\smallskip`);
   - 01/03 `\medskip` heads: **+4.550 above** (`01/src/chapters/introduction.tex:114,470`,
     `background.tex:337`, `methods.tex:1168`, `02/src/chapters/02-foundations.tex:588,609,630`,
     03 ×5);
   - 04 `\smallskip` heads: **+2.275 above** (`04/src/chapters/01-introduction.tex:237,249,259,270,279`);
   - a **multi-line** `\witness` gets +0.820 / +2.889 for free (the parbox becomes
     one tall box and `\lineskip=1.0` takes over) — so the same macro changes its
     own spacing as soon as the id list wraps.
2. **Alignment is split three ways.** flush right (`\hfill` + `\parbox` + `\raggedleft`,
   right edge exactly at 540.00pt) for `\witness`; flush **left** ragged-right for
   `\leanline` (ends 356.58) and for the 23 manual blocks (ragged right edge,
   16–29pt short of the margin); flush left with `\noindent` for every
   `\medskip/\smallskip` head (indent 0.00).
3. **Indentation after the block is inconsistent.** The paragraph that follows a
   `\witness` is a real new paragraph → indent 11.95pt (V1–V5, V12–V16, V19, V21);
   the text that follows a `\medskip`/`\smallskip` head stays in the same
   paragraph → indent 0.00 (V8–V10); `\witness` invoked mid-line (V4) and the
   proposed inline branch (V20) introduce no indent and no break at all.
4. **Ids are coloured in the own-line form and black in every other form.**
   `\witness` sets `\tiercol{#1}` before `#1` and never closes the colour group,
   so it bleeds into the ids (`02/main.tex:241`, `03/main.tex:206`,
   `05/main.tex:128`) — measured #2659a5. The inline `\tier` closes the group with
   `\textbf{…}`, so its ids print **#000000** (`02/main.tex:219`,
   `03/main.tex:190`, `05/main.tex:107`) — measured. Same for the 23 manual
   blocks (V7/V16 ids black).
5. **The green of class N differs between repos.** 02/05 `tierN = (0.05,0.40,0.20)`
   (`02/main.tex:163`, `05/main.tex:41`) vs 03 `tagN = (0.15,0.55,0.25)`
   (`03/main.tex:86`); 03 additionally defines `tagH` (0.70,0.25,0.10) that no
   other repo has; 01/04 define no mark colour at all (only `linkred`).
6. **Font-shape leak in 03.** 03's body lacks `\normalfont`/`\mdseries`
   (`03/main.tex:206`): inside an `\itshape` run the letter prints **SFBI0900
   (bold-italic)** and the ids **SFIT1000 (italic tt)** (V17), while 05/02 stay
   SFBX/SFTT (V18). 05's own comment (`05/main.tex:34-35`) states this is exactly
   what `\normalfont` is for — 03 does not comply.
7. **Breaking policy is split 3 vs 2.** 02 and 05 break after every `_`
   (`02/main.tex:175`, `05/main.tex:45`) → the block splits an identifier
   (`twenty_divisor_` / `lattice_splits`); 03 does not (`03/main.tex:161`) → it
   breaks only at `, `. Consequence: identical id lists produce different line
   shapes and different left edges (114.43 vs 198.09pt), and 03's form is the one
   that can go overfull on very long ids (an intermediate compile of the probe
   reported one `Overfull \hbox (23.6245pt)` on the 03 long list; the final
   isolated run of the same six cases reported 0 Overfull — the difference is
   paragraph context, so the claim to record is "03's no-break form has less
   slack", not "it always overfulls").
8. **Two of five repos have no own-line form at all** (01, 04: 0 `\witness`,
   0 `\tier`), and their accounting style differs from each other: 01 uses
   parenthetical `(Lean: \code{…})` ×4, 04 uses sentence-initial
   `Lean: \code{…}` ×26 with `\emph{Lean:}` in 8 of them. Neither is a block.
9. **Terminal punctuation: consistent by luck, not by rule.** 0 sites in the
   family put `.`/`,`/`;` after `\witness{…}{…}` (02: 0, 03: 0, 05: 0) — the
   sentence closes *before* the block (gate `r = 0`, `05/docs/citations.md` §8.5).
   The 23 manual blocks, by contrast, carry prose and punctuation *inside* the
   block (`…]{P}; (ii) with the witness marks…`), so the punctuation regime of a
   block depends on which variant you hit.
10. **Placement in the source is already mixed**: 02 → 86/86 own-line in source;
    03 → 87 own-line, **37 invoked mid-line** after prose; 05 → 42 own-line,
    **1 mid-line**, and **19 with trailing text on the same source line**. Same
    macro, three source shapes.

---

## (d) Uniform spec — draft, ready for docs

> **Own-line mark — rendering spec (proposed).** Applies to `\witness{X}{ids}`
> in all five repositories; the inline form `\tier[ids]{X}` keeps its current
> contract (`05/docs/citations.md` §8.1).

**S1. One shape, one macro.** The block form is exactly one macro,
`\witness{X}{ids}`, defined once per repository with the *same body* (byte-level
identical, as `\witness-standard.md` already demands for family files). No
hand-written `{\raggedright \tier[…] …\par}` paragraph survives: the 23 sites of
02 become `\witness{P}{ids}` where the criterion §8.5 holds, otherwise inline
`\tier[ids]{P}` in the prose. `\leanline` is retired as a rendering form (it is
already "not a body form", standard §2).

**S2. Vertical spacing — one number, and it is `\medskip` above and below.**

```latex
\newcommand{\witness}[2]{%
  \par\medskip\noindent\hfill
  \parbox{\dimexpr\linewidth-1em\relax}{\raggedleft …}%   % body as below
  \par\medskip}
```

*Chosen with reason.* Today the block sits at 13.000pt on both sides — the same
as an ordinary line wrap — which is why a block reads as a broken line instead of
as a mark (valley), while the `\medskip`/`\smallskip` heads around it read at
17.550/15.275 (crest). One symmetric, class-defined quantity removes the spread:
`\medskip` = 4.55pt in amsart 11pt, it is the same amount the manuscript already
uses for its own paragraph heads (`02/02-foundations.tex:588` etc.), and it is a
*documented* skip (amsart redefines it as `.35\baselineskip`), not a magic
number. Do **not** use `\parskip` (it is 0 here and would be invisible) and do
**not** use `\bigskip` (9.1pt, twice the head spacing). Because `\witness` issues
`\par` on both sides, the two `\medskip`s never stack with `\parskip`.

**S3. Indentation: 0, always.** `\par\medskip\noindent` before the box (no
`\indent`), and the paragraph *after* the block is a normal new paragraph → it
takes the document `\parindent` (11.95pt). Never `\noindent` after the block,
never a run-in head. Edge cases:
- macro invoked mid-line (`\ifhmode`): see S7 — it does not create a block, so
  the question does not arise;
- after `\noindent` (a head or a `\smallskip\noindent…`): the preceding
  paragraph is already flush left; the block still emits its own `\par`, so
  spacing stays S2;
- inside `enumerate`/`itemize`: forbidden by gate `i = 0` (§8.5) — the block
  would close the item's paragraph; keep inline;
- inside a theorem/proof environment: allowed, same S2 (amsthm environments are
  `\trivlist`-based and the following line is indented anyway — see R1);
- at the very top/bottom of a page: `\par\medskip` at the start of a page is
  absorbed by `\topskip`; acceptable, no special case.

**S4. Width: full measure, right edge on the margin.** `\parbox{\dimexpr
\linewidth-1em\relax}` after `\hfill` — the box's right edge lands exactly on the
right margin (measured 540.00pt, gap 0.01pt) and its left edge is free to stop up
to `1em` short of the left margin. Do not switch to `\hfill` + `\raggedleft`
without a box (that is what the 23 manual blocks do: their right edge is ragged,
16–29pt short) and do not use `\begin{flushright}` (adds `\topsep`/`\partopsep`).

**S5. Punctuation.** The mark never carries terminal punctuation: **no `.`, no
`,` after the closing `}` and none inside the bracket**; the sentence closes
before the block (gate `r = 0`, already true at 100% of sites: 0/86, 0/124,
0/43). A `,` or `;` may only appear *between ids*, and only as the separator
`", "`. The 23 manual blocks violate this by construction (prose inside the
block) — that is one more reason they are retired.

**S6. Colour by class, on the whole mark or on none.** One palette for the
family: `tierP = (0.15,0.35,0.65)`, `tierN = (0.05,0.40,0.20)`,
`tierPs = (0.70,0.45,0.05)`, `tierW = (0.00,0.35,0.45)` — i.e. the 02/05 values,
which are the ones the family colour redundancy rule (WCAG 1.4.1) was calibrated
against; 03's `tagN` (0.15,0.55,0.25) and `tagH` are dropped (or `tagH` is
registered as a published class with a cost estimate first, standard §9).
Colour scope: **the letter only, or the whole mark — pick one and state it.**
Recommendation: **whole mark** (letter *and* ids in the class colour), because
that is what `\witness` already does in 3/3 repos and it makes the block read as
one object; then the inline `\tier` must be changed the same way (its ids are
black today, measured #000000 vs #2659a5 in the block). Colour is redundant with
the letter either way.

**S7. Placement rule (`\ifvmode` / `\ifhmode`) and its edge cases.**

```latex
\newcommand{\witness}[2]{%
  \ifvmode                      % own line in the source -> block (S2–S6)
    \par\medskip\noindent\hfill
    \parbox{\dimexpr\linewidth-1em\relax}{\raggedleft <body>}\par\medskip
  \else                         % mid-line in the source -> inline, no break
    {\normalfont\footnotesize\bfseries\tiercol{#1}#1%
     \mdseries{\upshape\small\ttfamily[\tierids{#2}]}}%
  \fi}
```

- `\ifvmode` after a blank line or at the start of a line → block, as today.
- `\ifhmode` (the 37 mid-line sites of 03, the 1 of 05) → the mark stays inside
  the sentence: **no `\par`, no indent, no space is eaten** (V20 measured: the
  paragraph does not break). This removes the current behaviour where a mid-line
  call silently ends the paragraph and strands the rest of the sentence.
- After `\noindent` or after a head the mode is `\hmode` → inline: correct, the
  text there is one paragraph.
- Inside a group started with `{\itshape …}`: the body must begin with
  `\normalfont` and reset with `\mdseries` (V17 vs V18) — otherwise the letter
  prints bold-italic.
- The argument is still read as an arbitrary string (contract §6.4); the `\cite`
  guard stays.

**S8. Line breaking of long id lists.** Break priority: **`, ` first, `_`
only as a fallback.** Concretely:

```latex
% \brk@us = \textunderscore\penalty500\hskip0pt   % discouraged, still legal
% after every ", " keep the natural interword break (penalty 0)
```

- TeX prefers the lower-penalty break, so a list splits at commas whenever it
  can and only splits inside an identifier when the id itself is longer than the
  remaining measure — which is the case where breaking is unavoidable anyway.
- Today's `\allowbreak` (= `\penalty0`) after every `_` makes the mid-identifier
  break *equally* attractive, hence `twenty_divisor_` / `lattice_splits` in the
  02/05 PDF; today's 03 form (no break at all) is the opposite extreme and is the
  one that can go overfull. The penalty-tuned form sits between them.
- Do **not** adopt `\seqsplit`/`xurl`-style break-everywhere for witness ids:
  that maximises raggedness (R4). `\seqsplit`/`xurl` remain the right tool for
  URLs and for *single* identifiers longer than the measure, not for a list.
- Acceptance: compile the family, assert **0 Overfull/Underfull `\hbox`** in the
  blocks and re-check the byte-identical `pdftotext` gate (the family's own rule;
  a break change reflows text, so it must be measured, not assumed).

**S9. Measurement, not eyeballing.** Keep the family rule of
`witness-standard.md` §7 ("rendering is re-checked by measurement") and pin the
numbers above as the measurable targets: 13/15/16 px sizes, right edge on the
margin, `\medskip` both sides, indent 11.95 after the block, 0 overfull, letter
colour on ids.

---

## (e) Best practice — 5 verified sources

1. **amsthm manual (AMS, v2.20.3, 2017)** — theorem-like blocks declare their
   spacing explicitly: `\newtheoremstyle{…}{<space above>}{<space below>}{<body
   font>}{<indent amount>}{<head font>}{<punctuation>}{<space after head>}{<head
   spec>}`; and *"after the end of a theorem or proof, the following line of text
   is assumed to start a new paragraph, and will always be indented, whether or
   not a blank line or `\par` is present."* → supports S2 (declare the space, one
   named quantity), S3 (indent 0 for the block, normal paragraph after) and the
   `\ifvmode`→block / paragraph-after reading of S7.
   <https://texdoc.org/serve/amsthm/0>
2. **tex.stackexchange 37472, "Spacing before and after with `\newtheoremstyle`"**
   — the accepted answer documents the same three knobs (Space above / Space
   below / Indent amount), notes the default above/below is `\topsep`
   (`8.0pt plus 2.0pt minus 4.0pt`), and that `\theoremstyle{remark}` is *"the
   same as `definition` except that it doesn't add extra space above and below"* —
   i.e. the spacing difference between styles is a *declared parameter*, not a
   side effect. → the direct precedent for choosing one skip and writing it in
   the macro instead of letting it fall out of font size and `\lineskip`.
   <https://tex.stackexchange.com/questions/37472/spacing-before-and-after-with-newtheoremstyle>
3. **The TeX FAQ, "(La)TeX makes overfull lines"** — line breaking is governed by
   `\pretolerance`/`\tolerance`/`\emergencystretch` plus hyphenation/break points;
   an overfull box means *"TeX has given up"*, and `\emergencystretch` is a
   further pass that must be "treated with a degree of caution". → supports S8:
   fix the *break points and their penalties* (the ids' `_`/`, `), don't patch the
   symptom with a global tolerance; also explains why 05's `\emergencystretch=2em`
   (`05/main.tex:133`) hides some raggedness that 03 does not have.
   <https://texfaq.org/FAQ-overfull>
4. **CTAN: `xurl`** — *"loads `url` by default and defines possible URL breaks for
   all alphanumerical characters"*, i.e. break-anywhere is a deliberately
   documented, opt-in policy for unbreakable strings. → the contrast that fixes
   S8: witness ids are *meant* to stay legible, so the family adopts comma-first
   breaking instead of break-everywhere, and reserves `xurl`/`\seqsplit` for URLs
   and single oversized identifiers.
   <https://ctan.org/pkg/xurl>
5. **CTAN: `parskip`** — *"Simply changing `\parskip` and `\parindent` leaves a
   layout that is untidy; this package … helps alleviate this untidiness."* →
   the standing caution behind S2/S3: paragraph-level spacing and block-level
   spacing are separate knobs; the family must not try to express the mark's
   spacing through `\parskip` (which is 0 in amsart here) but must put it in the
   macro, and must keep the indent rule coherent with the rest of the layout.
   <https://ctan.org/pkg/parskip>

---

## (f) Gaps / open questions

- **F1-A was measured as a *candidate*, not as shipped code**: no `\ifvmode`
  macro exists in any repo today (0 hits in the five preambles), so V19–V21
  measure *my* proposal of the accepted principle. The parent must decide whether
  the inline branch of S7 reproduces the accepted design verbatim.
- **S6 "whole mark in colour" changes inline `\tier` too** (ids black → class
  colour). That is a visual change to thousands of inline marks and to the
  byte-identical `pdftotext` gate? (colour does not affect `pdftotext`, but the
  gate is worth re-running). Flagged, not decided.
- **S8's penalty value (500) is a proposal.** It needs one measured pass over the
  family to confirm (i) no overfull and (ii) an acceptable number of reflows.
- **The 23 manual blocks in 02 have no `\witness` equivalent for their prose
  tail**: several end with a clause *after* the tag (`…]{P}; (ii) …`), which gate
  `r = 0` forbids for a block. Converting them is a content edit, not a macro
  edit — needs the §8.5 criterion applied site by site (out of scope here).
- **01 and 04 have no marks at all.** Whether they migrate to `\tier`/`\witness`
  is a separate decision; until then the "family format" covers 3 of 5 repos.
- **`\leanline`'s 2 sites** in 02 still carry prose inside the block; standard
  §5 S4 says "no canonical form; the sites stay where they are" — so S1's
  retirement of `\leanline` as a *rendering* form must be reconciled with that
  sentence (either amend S4 or keep the macro and give it S2 spacing).
- **Page-break artifacts**: V7/V14/V21 gap values are `null` in the table because
  the block crossed a page boundary in the probe; their TeX-level numbers are in
  (b1) and are unaffected.
- `pdftohtml -xml` writes page coordinates at a 1.5 scale and duplicates boxes
  per page — `measure.py` now filters by page; if the probe is re-run, regenerate
  `probe_bbox.html`, `probe.xml` and the PNGs together (`pdftotext -bbox-layout`,
  `pdftohtml -xml -i -stdout`, `pdftoppm -r 110 -png`).
