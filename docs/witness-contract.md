# Witness contract — rationale of the witness mark

| Field | Value |
|---|---|
| **Document** | `docs/witness-contract.md` |
| **Status** | In force as the standard — §6 states what it does and does not claim about a manuscript's body |
| **Version** | 2.0 (rationale, derived standard and wave-brief shape in one file; generic across the family) |
| **Date** | 2026-11-25 |
| **Language** | English; identifiers, macros and file names in English and monospace |
| **Scope** | Why the marks of evidence of the manuscript (`\witness`, with `\testref`) exist and what they do not assert — the rationale (§1–§5, §7), the standard itself (§6), the quantified inline / own-line criterion (§6.10), the own-line rendering form (§6.12) and the shape of a wave brief (§10); free of anything tied to one repository state |
| **Index** | §0 where things live · §1–§5 the argument · §6 the standard (§6.0–§6.13) · §7 honesty · §9 limits · §10 wave brief shape |

**Relation to the rest of the documentation.** This document is the
**single living norm** of the witness device: §6 states the rules, §1–§5
and §7 argue them, and §10 fixes the shape of a wave brief.
`docs/citations.md` ends with an **index** — a pointer to §6 of this
document — and states no rule of its own. `docs/witness-decisions.md`
holds one row per question, `docs/witness-inventory.md` holds this
repository's generated census, and the per-site decisions — which
witness supports each claim, what is rewritten and what is removed —
plus every measured state of one manuscript live in `docs/reports/`.
Nothing asserted here is contradicted elsewhere, because there is no
other document that states a rule.

**Status and method.** In force with the manuscript. The concrete state of
a manuscript — counters, site tables, verdicts — is measured with `grep` on
`main.tex` and recorded in `docs/reports/`; a site is identified by the
tail of the sentence, not only by the line number, because the manuscript
is edited concurrently.

---

## 0. Where things live

| File | What it provides |
|---|---|
| this document §6 | the standard itself: precedence (§6.0), syntax (§6.1), what each mark asserts (§6.2), placement (§6.3), naming (§6.4), grammar and the writing rules (§6.5), the star (§6.6), typography and the family's deliberate divergences (§6.7), the witness gates (§6.8), the alphabet and decorations (§6.9), the inline / own-line criterion (§6.10), standard versus applied state (§6.11), the own-line form (§6.12) and the ledger segmentation (§6.13) |
| this document §10 | the required shape of a wave brief (five blocks) |
| `docs/witness-decisions.md` | one row per question; a count is never a row |
| `docs/witness-inventory.md` | the census of *this* repository, generated from a measurement, never hand-written; per repository by design, therefore not a family file and not manifest-pinned |
| `docs/citations.md` §8 | an index only: a pointer to §6 of this document; it states no rule |
| `docs/reports/` (index: `docs/reports/README.md`) | per-site decisions, counters, criterion sites, `u`/`p` verdicts, applied states and the author's pending-work list — the applied state of this argument in one repository; a superseded one carries `superseded-by:` |
| `docs/README.md` | the directory index of `docs/` |
| `docs/style-guide.md` | the family style guide as this repository applies it |
| `README.md` | link to the witness section of the documentation; `docs/README.md` is the directory index |
| `main.tex` — preamble (witness system: the one placement-driven `\witness`) and the *Evidence tags* gloss | the implementation and what the reader sees at the first mark of the body |
| the repository's Lean file (`lean/`) | the `P` identifiers the mark can print |
| `tests/` and the census test of the repository | the numerical suite and the census that fixes the test identifiers the manuscript cites |
| `citation.csl.json`, `CITATION.cff` | the bibliographic layer the mark does **not** mix with: the external source is a `\cite`, never a mark identifier |
| `scripts/shared-files.json` | the family manifest: this document and `docs/witness-decisions.md` are pinned and byte-identical in the five repositories; the census is excluded because its counts differ by design |
| `omega-pcf-paper-repos` → `references/decision-gates.md` | the method of the convention research pass (separate discipline standard, device proper, real precedent) and the rule of not writing CI tests for editorial conventions |
| `omega-pcf-paper-repos` → `references/witness-system.md` | the grammar of the family-level witness system, its known defects (italic inheritance in theorem environments, inline marks inside alignments) and the state of propagation to the sibling repositories |

---

## 1. What is justified here

The manuscript marks, beside each claim, how it was established: `P` when
the statement is proved and machine-checked in Lean, `N` when it is
verified numerically with the name of the test that checks it. The mark is a small, immutable
bracket in its own colour (`\witness{P}`, `\witness{N}`,
`\witness[ids]{X}`), or a right-aligned line of its own when the claim
carries several witnesses — the same macro, `\witness[ids]{X}`, written
on a line of its own (§6.12). The two classes are introduced
by an in-text gloss — *Evidence tags* — that sits before the first mark of
the body and defines the classes and nothing else.

That device is not a typographic fashion nor an ornament: it is the answer
to a real problem of reading and of attribution, and its shape — inline or
a line of its own — is decided by a quantified criterion. What this
document maintains is precisely that: that the convention is
**legitimate** (it solves something the bibliographic citation does not
solve), **coherent** with contemporary verification practice, **usable**
(it costs neither legibility nor extra printable space) and **honestly
declared** (it is not presented as an AMS or Chicago norm, and it warns of
its novelty).

What this document does **not** do: it does not set editing rules that
belong to the manuscript's prose. The rules of the device live in §6;
here the reason for being of each of them is given.

---

## 2. Why a witness mark in a paper of pure mathematics

### 2.1 The problem it solves

A bibliographic reference answers *where a statement has been published*.
It does not answer *how the statement the reader has in front of them was
established*. In a paper that mixes three kinds of statement — identities
proved with Lean, numbers computed and checked against a suite, and results
read from external sources — that omission has three concrete consequences:

1. **The direction of the reference stays ambiguous.** A `\cite` at the
   end of a claim says there is a source; it does not say whether the
   source *proves* the claim, only *reports* the number, or is the origin
   of a hypothesis the paper borrows. The reader of mathematics is used to
   reading the bibliography as the provenance of the statement, not as its
   verification. The mark separates the two planes: the citation sits
   beside the claim in its own form (`[N]~\cite{key}` for a value read off
   a source, `[P] in~\cite{key}` for a result proved in one), and the mark
   carries the internal witness, by identifier.

2. **The referent is not unique.** When a claim rests on several proofs of
   the repository's Lean file and on several tests of the suite, citing
   "the proof" in the singular forces a choice of one and the hiding of
   the others, or the writing of an enumeration in prose that breaks the
   sentence. The grammar of the device — one claim, one mark; the list of
   identifiers inside the bracket or on its own line — gives the reader the
   complete and verifiable referent: each identifier is a name that can be
   searched for in the Lean file or in the suite.

3. **The typographic cost matters.** A claim with a single witness fits in
   the sentence; a claim with five forty-character names does not. Without
   a shape rule, the text accumulates long brackets in the middle of the
   phrase and the reader loses the thread of the sentence that contains
   them. Hence the inline / line-of-its-own distinction is not aesthetic:
   it is the condition that the device be legible.

### 2.2 What the reader gains

- **Checks the statement without leaving the text.** The identifier is on
  the page; the Lean file and the suite are in the repository. A number
  marked `N[test_…]` can be reproduced with one command; an identity
  marked `P[thm_name]` locates the theorem.
- **Distinguishes at a glance the nature of the evidence**, without reading
  the bibliography: the letter carries the meaning, the colour only repeats
  it (§4.2).
- **Knows what is not marked.** The absence of a mark is information: an
  unmarked claim is a claim the paper does not verify where it asserts it.
  That asymmetry is useful only if the mark is systematic, and systematics
  requires an explicit shape rule.

---

## 3. The post-2025 argument

Víctor maintains that, **from 2025 onwards and with the state of the art
of artificial intelligence, the trend towards exhaustive numerical
verification and verification with Lean and other proof assistants came to
stay** in formal mathematics, physics and other disciplines. The argument
breaks down into three steps.

1. **Verification stopped being exceptional.** The generation and review of
   proofs by language models, together with the maturity of ecosystems
   such as Lean and Mathlib, have lowered the cost of checking an identity
   or reconstructing a calculation to the point where *not verifying*
   begins to be the option that requires justification. What was once the
   privilege of a few developments — a theorem formalised by hand over
   years — is today a reasonable reader expectation for numerical
   statements and for calculus identities.

2. **The editorial consequence is a new class of evidence.** If an
   increasing share of a paper's statements is established by execution or
   by machine check, the paper needs to say so *where it asserts it*, and
   not only in a "methods" section or in a descriptive appendix. The
   bibliographic reference cannot do that work: it does not distinguish
   between "proved in a source", "computed here" and "assumed by
   hypothesis". A convention that **marks the nature of the evidence
   beside the claim answers that reality**: it describes the real state of
   how each statement is established, with the same criterion across the
   discipline.

3. **The discipline is already moving in that direction.** The nearby
   precedents — work plans with a status per statement (`leanblueprint`),
   status tables per result, and artefact seals or badges that certify
   which part of a paper has been checked — exist precisely because formal
   and numerical verification has become a structural datum of the result,
   not an implementation detail. The mark of the manuscript takes that
   principle and lowers it to the level of the claim, which is the unit in
   which a reader of mathematics reads and judges.

Hence the device is not presented as a taste of the authors: it is
presented as the editorial answer to a change in the practice of the
discipline. That does not turn the mark into a scholarly-society norm; see
§7, where exactly what the convention is and what it is not is declared.

---

## 4. Usability and compactness

The usability criterion and the *compactness* one — what the mark costs in
space and in attention — are gathered here, together with the in-prose
syntactic factor behind §6.10 of this document.

### 4.1 Inheritance from the secondary notation of software engineering

The device does not spring from mathematical typography, but from a
practice consolidated in software engineering and interface design:

- **Semantic typing:** names say what they are. An identifier
  `test_…` needs no gloss; the reader who looks for the check finds it.
  The bracket of the witness inherits that discipline: it admits only
  internal identifiers, never bibliography keys or printed numbers, so its
  content is always a searchable name.
- **Colour as a *UX* marker, redundant with the label:** in serious
  interfaces colour speeds up reading, but the label still carries the
  meaning; colour is never the only path. Applied to the manuscript: blue
  `P`, green `N`, ochre `P*` — and the letter, not the
  shade, is what the reader in black and white, with low vision or with
  colour deficiency perceives.
- **Status mark beside the object, not in a separate list:** like a green
  *build* indicator next to the commit, the mark lives next to the claim.
  Moving it to a table at the end of the paper would make it cheaper and
  less useful, in exchange for saving a few characters.

The prior research pass on the convention — its scope and method are
described in the family *skill* `omega-pcf-paper-repos`, file
`references/decision-gates.md`, section *"When the convention itself is
questioned"* — went through that literature with a declared purpose: to
separate what is standard in the discipline, what is device proper to the
project, and what the real nearest precedent is. The distilled result is
stated in §7: the real precedents are the per-statement status of
`leanblueprint`, status tables and artefact seals; the rest — the inline
mark, the one-macro grammar, the colour rule — is device proper to the
project and is declared as such.

### 4.2 The WCAG 1.4.1 rule: colour never carries meaning alone

§6.7 fixes this rule: **colour is redundant with the letter (WCAG 1.4.1)**;
the mark reads the same in greyscale and the letter suffices to carry the
meaning. The rule is upheld here for three reasons:

1. **Print.** The paper is read on paper and in reduced-colour PDF; the
   PDF is archived and cited in formats that lose colour.
2. **Accessibility.** 1.4.1 is the condition that a reader with colour
   deficiency distinguishes `P` from `N` without chromatic help.
3. **System consistency.** If colour carried its own meaning, the palette
   would be a second grammar to keep synchronised with the alphabet; being
   redundant, adding a class requires a letter, not a shade.

None of the three reasons is decorative: all three are usability
conditions of the device in its medium of circulation.

### 4.3 The contrast with the alphabetic numbering of AMS and Chicago

The natural temptation, before a statement with several parts, is to
number them — `(a)`, `(b)`, `(c)` or `(i)`, `(ii)`, `(iii)` — which is the
practice AMS and Chicago use to break down a statement and that every
reader of mathematics knows. That numbering **orders**, and therefore it
does not serve here:

- **It does not certify.** The letter `(a)` says there is a first part; it
  does not say it is proved or why. The mark says exactly that: how it was
  established.
- **It is not portable across claims.** Alphabetic numbering restarts at
  every statement and is local to the statement; the witness is a global
  identifier, searchable in the repository's Lean file or in the suite.
- **It does not distinguish sources.** Numbering parts does not separate
  "proved here" from "read in a source"; the device does, with distinct
  forms for each case.
- **Comparative cost.** An alphabetic enumeration adds a level of
  structure to the statement; the mark adds a bracket. In a one-line
  claim, the enumeration is more expensive than the mark.

The convention, therefore, **does not compete** with alphabetic numbering:
it uses it for what it is good at (breaking down) and leaves status to
the mark. In the same way, the mark does not replace the bibliography: the
alphabetic ordering of the paper's bibliography (`sorting=nyt`, the AMS
convention the family follows, `docs/citations.md` §7) keeps ordering the
references by author; the mark does not enter that layer.

### 4.4 The quantified criterion: usability, compactness and syntax

The shape of each mark is decided with five quantities read directly from
`main.tex`, with no judgement of taste. The definitions of the five
quantities, the four thresholds and the rule in one sentence have a single
home in §6.10 of this document; the site table — every flagged site with
the tail of the sentence it closes — is the criterion-sites report in
`docs/reports/`. What this section adds is the *why*: the four conditions
answer four usability demands —

- `k` and `L` address **cost**: the block pays a paragraph break, so it is
  only asked of lists that truly need the line.
- `r` addresses **reading**: since `\witness` emits `\par` before and
  after, the sentence that follows it would start a new paragraph; a
  residual of a single word (a reference parenthesis, a closing
  `\testref`) would already break the sentence. The residual is counted,
  not estimated.
- `d` addresses **rhythm**: if the paragraph already carries a block less
  than seventy-five words away, the second block is monotony; the
  manuscript itself marks the empirical floor, which is the tightest block
  pair it already accepts.
- `i` addresses **position**: a block inside an enumeration would separate
  the witness from the rest of the item; no block of the manuscript sits
  inside one.

The criterion is reproducible by anyone who opens `main.tex`, and it
reproduces the applied state of the manuscript without a single exception;
the complete table, with the tail of the sentence each mark closes, and
the counters of the last pass are in `docs/reports/`.

**Review.** The review method — the reading pass over that site table, its
one question per row, and why no CI test is written for it — is stated
once, in §6.10, and applied there.

### 4.5 Compactness: the measured cost of the device

*Compactness* is not an intuition here: it can be counted. Measured with
`grep` on `main.tex`, the whole apparatus is four numbers — inline marks
(with and without identifiers, split by class), blocks on a line of their
own, witness-list labels, and occurrences of `\testref`. The measurement
is a census of the manuscript, so it belongs to `docs/reports/` of the
repository that measures it; the method is stated here because the
thresholds of §6.10 are argued against it. From that
census follow two consequences:

1. **The block is expensive, so it is asked to pay in return.** It costs a
   line and breaks the paragraph; it is only asked of a list of 35
   characters or more, calibrated against the shortest list the
   manuscript already prints as a block (the calibration facts are the
   criterion-sites report in `docs/reports/`). Without a threshold, a
   twenty-nine-character list would earn a whole line and the cost would
   have no counterpart; the paragraph-close heuristic `p` is what lifts
   gate 2 for such a site (§6.10).
2. **The inline bracket is cheap but not free.** The optional argument of
   `\witness` prints names, never numbers: the cost of the bracket does not
   grow with the numbering of references, and the identifiers break in
   line thanks to the permitted underscores (`\brk@us`). The real limit is
   not the width, it is the sentence: hence `r` rules, not `L`.

With that, the budget of the device is predictable: one line of its own
per block, and a bracket per claim. It is a price that the information it
buys — how each statement was established — justifies, and it is also the
reason the shape rule exists: without it, the budget would grow with the
prose and the apparatus would begin to read as noise.

---

## 5. What it is and what it is not

**It is not a peer-review class.** The mark `P` says that a proof is
formalised and machine-checked in the project's file; `N` says that a
number is recomputed in the suite and checked against a declared
tolerance. Neither says that a third party has read the paper, nor that
the proof has been reviewed by a human, nor that the result is published.
Confusing machine verification with peer review would be the gravest error
this device could induce, and that is why the gloss at the first mark
defines the classes and nothing else: the explanation of the apparatus
lives in this documentation, not in that gloss.

**It does not replace the citation.** The external source is and remains
the `\cite`, in its own form beside the claim: `[N]~\cite{key}` and
`[P] in~\cite{key}`. The optional argument of `\witness` admits **only**
internal identifiers — a `\testref` or the raw name of a declaration of
the repository's Lean file — and the preamble raises a `\PackageError`
before anything else, so a mark bracket never prints a reference number.
A bracket that said "it is cited" would be redundant with the citation
that is already there.

**One claim, one mark.** There are no two adjacent marks, nor a mark and a
`\cite` saying the same thing, nor marks in figure captions (rule 8 of
§6.5). The gloss is exempt from the mandatory-witness
rule because it defines, it does not assert.

**`P*` is internal.** The class exists and works in the preamble (dispatch
`\@namedef{markcol@P*}`, ochre colour) to mark between compilations a
statement written but not yet verified against the corpus —
the star's one denotation (§6.6) —; the printed text never invokes it,
the gloss does not mention it and the prose does not speak of it. It is a
work tool, not a class of the published alphabet.

**`L` and `R` were eliminated, and why.** Both carried information the
paper already gave:

- `L` meant "it is cited", which is exactly what the numeric citation
  says, repeated according to the AMS norm every time it is cited again
  (mathematics has no second-reference form; `op. cit.` and `ibid.` belong
  to the Chicago bibliographic note). The class added no information and
  was the only one that sometimes stood with no reference beside it. Its
  content was absorbed into prose: each claim keeps its citation beside
  it.
- `R` marked the direction of the reading — a "this is read as" —, not how
  the claim is established, so it did not belong to an alphabet of
  witnesses. Its sites repeated what the prose already said; the only one
  that worked was written as prose (`a reading of the records, not a
  result about them`), and sites added in one round contradicted the
  "proved here" section they were in.

Both eliminations are documented here (§5 and §6.9) and applied
in the manuscript: the published alphabet of evidence is `P` and `N`.

---

## 6. The standard

The rules below are this contract's own standard. None of them is a new
decision: each restates a position already settled in the family's
documentation and makes it explicit here, so that one file carries the
argument and the rule together. Where a rule defers, it defers in the
open; nothing in this section decides a question the family documents
leave undecided.

### 6.0 Precedence

**The manuscript is king.** A mark never overrides what the text states:
where the text and a mark disagree, the text is read first and the mark is
corrected to it. A mark is a pointer to evidence, never a verdict — it
tells a reader where the check lives, not that the claim is true. A count
in a document is a measurement with a date, not an argument.

### 6.1 The set and its syntax

There is **one body form**, `\witness[ids]{X}`, and it is
**placement-driven**: the position of the call in the source picks the
rendering (§6.12 S7), never the class of the mark.

| role | source | prints |
|---|---|---|
| own line | `\witness[ids]{X}` written where the mode is vertical (`\ifvmode`: a blank line, a heading, the end of an environment) | `X[ids]` on a line of its own, flush right (§6.12) |
| inline | `\witness[ids]{X}` written where a paragraph is already open (`\ifhmode`, mid-sentence or mid-paragraph) | `X[ids]` where the sentence put it, no break, no indent, no space eaten |

The source is identical in both roles — one macro, one argument order,
one name; only the position in the manuscript differs, and §6.10 decides
that position as prose. The former second form, an inline macro of its
own, is abolished: every site of the five repositories is `\witness`.

`X` is `P` or `N` (§6.9). The body form is `P[id1, id2]`: **one tag, its
ids inside the same brackets, separated by `, `** — the bracket belongs to
the tag itself and never follows it as a second group. A mark with no id
keeps the bracket class-pure (`[P]`); no id is invented for it. No third
body form exists; an accounting line (`\leanline`, a `Lean:` line) is not
a form of the mark (§6.4 S4).

The set of evidence marks is **`P` and `N`, with `\testref` as the test
anchor — nothing else**. No decoration, no accounting line and no label
enters the set. The internal `P*` dispatch of the preamble (§5) is a work
tool, not a class of the printed alphabet.

### 6.2 What each mark asserts

- **`P`** — an artefact of the named formalization, checked by that
  formalization's own machine. The correspondence between that artefact
  and the statement of the paper is a human reading of both, and is not
  asserted by the mark.
- **`N`** — an executable numerical test with a stated tolerance and
  condition. The test is evidence; it is not a proof.
- **A mark** is never an alias for *proved*, and no mark carries a degree
  of confidence, a provenance grade or a citation.

### 6.3 Placement is prose, never semantics

Whether a mark sits inside the sentence or on a line of its own is a
**prose criterion** — semantic, heuristic, aesthetic — and no rule of this
contract decides it. Placement never changes what a mark asserts: the
shape of a mark tells a reader how many witnesses a claim carries and
where they sit, never which kind of evidence it is. The quantified
criterion of §6.10 stays what it has always been — a
readability aid for that prose decision (cost, rhythm, position) — and it
is not a classifier. The standard governs content and naming only.

### 6.4 Naming (S1–S5)

A name is routed by the job it does in its sentence; the pass that moves
names reads each site, classifies it and restates the classification
before editing:

| Class | Route |
|---|---|
| **S1** witness id | stays inside the mark — `\witness[ids]{X}`, `\testref{…}` — written raw, never beside the tag |
| **S2** code mention | `\code` |
| **S3** decorated name (`*`, `°`, `†`) | `*` under §6.6; `°` and `†` under §6.9 |
| **S4** `Lean:` accounting line | no canonical form yet: the sites stay where they are and are not migrated in bulk |
| **S5** unclassifiable | recorded as an open site in `docs/witness-inventory.md`, never guessed |

Names follow the repository's naming standard (snake_case, English); an id
that does not is a work item, not an exception.

### 6.5 Grammar of the tag argument

The optional argument of a tag holds **internal ids only** — a
`\testref{…}` or the raw names of the repository's own declarations,
several of them separated by `,` — and a citation key is never written
inside a tag; an external source stays an adjacent `\cite`, printed beside
the mark, never fused into it.

The macro does not enforce this by the shape of its argument. A
character-shape test (`\_`, `,` or `\testref` present, otherwise an error)
rejects valid internal ids — a Lean name such as
`F1PaperTorus.chi5WeilOrbit` carries none of those markers — and it cannot
recognise a citation key, whose characters are the characters of an
identifier. The argument is therefore read as an arbitrary string: an
escaped `\_` and a raw `_` both print as the breakable typewriter
underscore, every other token passes through unchanged, and the only error
the macro raises at run time is a literal `\cite` token inside the
argument, which is never an id.

The rule that the bracket holds no external source is enforced where the
key set exists: a test reads every `\witness[…]` argument of the
argument of the manuscript, splits it on the commas that sit outside
`\testref{…}`, and fails when a part equals the id of a record of
`citation.csl.json` or contains a `\cite` token, reporting `file:line` and
the key. The check runs with the suite and is the only place where the
citation-key rule is measured.

Repositories whose tags today accept a wider or a narrower set converge on
this grammar by work, not by relaxation of the rule: the identifiers the
previous wording rejected are a measured set, never a design constraint.
They remain work items and are rewritten to snake_case ids; the business
rule itself is unchanged, only the layer that enforces it moves.

The render of a legal tag is always the same shape: **the tag first, its
ids inside the brackets** — `P[name1, name2]`, `N[test_x]`. The ids never
precede the tag either, so a test witnessed in prose appears as
`\witness{N} (\testref{test_x})`, never as `(\testref{test_x}) \witness{N}`.
External sources stay outside the tag: the claim keeps its `\cite` next to
it, in the standard form `[P] in~\cite{key}` for a result proved in a
source and `[N]~\cite{key}` for a value quoted from one. Two bracket
groups in a row (`[P] in [12]`) are then the tag's own bracket plus the
citation's, each printed by its own macro — and a tag alone never carries
a number.

**There is no `\Lean{}` (nor any per-repository variant of it) any more.**
They were the artefact of the previous convention: a name printed in tt
brackets of its own, standing next to the tag of the same claim (`P[…]`
beside `N[test_x]`), which is the duplication this standard replaced. Every
internal name now lives **inside** the tag — `\witness[name1, name2]{P}` — or
inside a `\witness{}` block, and an external name (a theorem of a sibling
repository) is never printed at all: the claim keeps its citation,
`in~\cite{key}`.

#### The writing rules

1. **One claim, one tag.** No two tags are ever adjacent — `\witness{P}
   \witness{N}` is a bug, not a summary.
2. **An external source is the citation, not a tag — and never the key of
   one.** The source of a claim is its `\cite`, set immediately after the
   claim it supports: no tag says "this is cited", because the bracket of
   the citation already says it, and in numeric style a repeat carries its
   number like any other reference. What a tag carries is an *internal*
   witness, by identifier: a Lean name inside its brackets,
   `\witness{}` or `\testref{}`. `\witness[key]{X}` does not exist — the
   optional argument of `\witness` holds internal ids only and the preamble
   errors on anything else.
3. **A bare tag needs a witness in its sentence.** If the sentence has
   none, add the most honest one (the `\testref{}` of the test that checks
   the number, the Lean declaration that proves it — written inside the
   tag, so the tag is bare no longer — or an `\eqref`/`\ref`); never
   invent a citation.
4. **Every `\witness{N}` carries a `\testref{}`** when a test verifies it —
   either folded into the tag, `\witness[\testref{test_x}]{N}`, or, when the
   sentence already carries other witnesses, as `\testref{}` in the prose
   of that same sentence, after the tag. The set of cited tests is pinned
   by the census test of the repository, so a new witness is added there
   too, after checking the test really recomputes the number next to it.
5. **`\witness{P}` without a bracket** means proved here, with no theorem
   name quoted at that point; the name, when it is quoted, goes into the
   tag itself (`\witness[name]{P}`) or, when the claim carries two ids or
   more and closes its sentence, into a `\witness{}` block — the criterion
   of §6.10 (four gates and two labelled heuristics) decides which of the
   two. Proved in an external source is not "here": that is
   `[P] in~\cite{key}`, one bracket for the tag and one for the citation,
   each printed by its own macro.
6. **The gloss** (the *Evidence tags* paragraph, before the first mark of
   the body) defines the classes and nothing else — one sentence each. It
   is exempt from rule 3 — it defines, it does not claim — and it never
   mentions `P*`.
7. **`P*` is available; the released text uses `P`.** The class is fully
   functional in the preamble — the dispatch `\@namedef{markcol@P*}` and
   the ochre `tierPs` colour — so `\witness{P*}` renders `[P*]` exactly like
   any other class, and it is there for intermediate commits between
   builds (an agent without Lean, in draft) that need to tag a claim as
   written but not yet verified against the corpus — the star's one
   denotation (§6.6), which lives only in intermediate layers, the
   release gate being zero stars. The printed text never invokes it: the
   body marks those claims `P`, the gloss does not mention it and the
   prose no longer speaks of it.
8. **No status tags in captions.** A caption already names the test that
   generates the figure (`\testref{…}` of that test, and the test of the
   claim itself), which carries the status; a `\witness` inside
   `\caption{…}` is removed, not kept. Tags belong to the body.

### 6.6 The star

`*` has **one denotation**: a name *written, not yet verified against the
corpus*. It denotes written, not yet verified; it lives only in
intermediate layers, and the passes that verify the corpus resolve it; the
release gate is **zero stars**, so a released text carries none. The star
is not a class of evidence, not a degree of confidence and not a
citation. Any other reading of it — in a comment, in a colour note or in a
rule of the writing guide — is a defect and is corrected where it is
found.

### 6.7 Typography, and the family's deliberate divergences

The canonical render parameters, measured in the built PDF, are **13 pt
for the witness class, 15 pt for the ids and 16 pt for the prose**,
identical for `P` and `N`; only colour differs, and colour is redundant
with the letter (§4.2, WCAG 1.4.1). Rendering is re-checked by measurement
at each wave, never by eye; reopening these parameters requires a new
measurement.

The underscore inside an id prints through the repository's `\brk@us`.
The break-per-character decision is typography, so the family states it
once and S8 (§6.12) has unified it where marks are printed:

| repository | encoding | `\brk@us` |
|---|---|---|
| 01, 04 | OT1 (no `fontenc`; the tt glyph, OT1 has no extractable `\textunderscore`) | `{{\ttfamily\char95\relax}\allowbreak}` |
| 02, 03, 05 | T1 | `\textunderscore\penalty500\hskip0pt\relax` |

The row of 02/03/05 **is** the S8 form: one penalty per underscore, 500
(discouraged, still legal), after which the natural break at penalty 0
keeps following `, ` — a list splits at its commas and only an identifier
longer than the remaining measure splits at all. The two extremes it
replaced are retired: `\allowbreak` (= penalty 0) after every `_`, which
made the mid-identifier break equally attractive and printed
`twenty_divisor_` / `lattice_splits` in the 02/05 PDF, and 03's bare
`\textunderscore` with no breakpoint, which is the form that can go
overfull (`03/main.tex` comment at the definition, commit `b1fec34`,
2026-11-24; the unification commits are `4edc048` in 03 and `a82bd8d` in
05, 2026-11-26). 01 and 04 keep the OT1 form of their preamble: their
`\brk@us` serves `\code` and `\tierids` only, and no mark is printed
there, so nothing of theirs was reflowed. Re-opening any of these numbers
requires a new measurement.

### 6.8 Gates

1. **Citation-key lint** — no part of a `\witness[…]`
   argument may equal an id of `citation.csl.json` or contain a `\cite`
   token; it runs with the suite and reports `file:line`.
2. **Zero stars** at release (§6.6).
3. **No `Tier` column** in a ledger table; a table carries no tier label.
4. **Render** — tag before ids, `P`/`N` only, colour redundant with the
   letter.

### 6.9 The alphabet, open statements and decorations

The published alphabet is frozen at **`P` and `N`** (§5): an expansion
enters only through the family's gate — measured sites, used *and*
documented in all five repositories, counted by `counts:check` and
lintable, with the cost of each new symbol estimated before it is
admitted. Until a gate is passed, the alphabet does not grow.

- **Open statements are prose by default.** No `[o]` label is adopted.
- A `conjecture` environment is used only where **both** conditions hold:
  (a) the statement is a precise declarative proposition — a question or
  a task is not one — and (b) the conjecture-status belongs to the source
  that states it. An environment asserts belief-status, so it is never
  assigned for tidiness and never attributes a position the source did
  not take; ambiguous sites stay prose.
- **No new tier labels in ledger tables.** Redesigning what the tables
  carry is a change candidate, noted here and decided elsewhere.
- **The decorations `°` and `†` are held**: not adopted while their use
  stays marginal, and nothing in this contract certifies them.
- **No shorthand** is adopted now.

### 6.10 Inline or a line of its own — the criterion

The **shape** of a mark is decided by its ids, never by its class. `P` and
`N` both appear inline and on a line of its own, so the shape tells a
reader how many witnesses a claim carries and where they sit, not what
kind of evidence it is; reading the shape as "the proof is a block, the
test is inline" was the drift this rule closes. Placement itself is prose
— semantic, heuristic, aesthetic — and never a semantic axis (§6.3): the
criterion below measures cost and position for that decision, it does not
classify.

The criterion is **quantitative**: five quantities read off `main.tex`
with no judgement call, four gates, two labelled heuristics, one reading
pass to review it.

**The rule in one sentence.** A claim whose id list carries **two ids or
more and 35 characters or more** goes on a line of its own
`\witness[ids]{X}` **only if the mark closes its sentence, does not close
a list item, and stands at least 75 words from the nearest block of its
paragraph**; every other site stays inline `\witness[ids]{X}`. Two labelled
**heuristics** amend the cost and position conditions (gates 2 and 4): `u`
takes the verdict from the list the mark sits in, `p` prefers a line of
its own at a paragraph close — both stated below. Gates 1 and 3 (`k ≥ 2`,
`r = 0`) are absolute: no heuristic lifts them.

#### The quantities

| Symbol | Quantity | How to measure |
|---|---|---|
| `k` | ids of the claim | count of `,` + 1 in the optional argument of `\witness` |
| `L` | length of the id list, in characters | that argument with `\_` unescaped to `_`, `\testref{…}` reduced to its name, braces dropped |
| `r` | **sentence residual** — words of the *same sentence* that follow the mark | words between the mark and the next `.`, `!` or `?`, math and macros not counted; `r = 0` means the mark is the last element of its sentence |
| `d` | distance in words to the nearest `\witness` block of the same paragraph | paragraphs are blank-line separated; `—` when the paragraph has no block |
| `i` | 1 if the mark closes a `\item` of an enumeration, 0 otherwise | the last `\item`/`\item[` before the mark opens the item the mark ends |

#### The four gates

A claim with `k ≥ 2` is set as a block **iff all four hold**, unless one of
the heuristics below decides otherwise:

1. **`k ≥ 2`.** One id never earns a line of its own: a single identifier
   fits in the bracket of the sentence it marks (calibration: the
   criterion-sites report in `docs/reports/`).
2. **`L ≥ 35`.** Below 35 characters the flush-right line costs a
   paragraph break and buys no room: the bracket fits in the sentence
   (calibration: the criterion-sites report in `docs/reports/`).
3. **`r = 0`.** `\witness` issues `\par … \par` (preamble), so it always
   ends the paragraph where it sits and the text after it opens a new one.
   Any residual — a trailing clause (`; …`, `, so …`, `which …`), a
   parenthetical (`(Figure~\ref{fig:background}(a))`), a closing
   `\testref` — would be stranded at the head of a new paragraph, and the
   sentence it belongs to would be torn in two. **`r ≥ 1` ⇒ inline, no
   exception.** The residual is counted, not estimated: a residual of a
   few words is a reference parenthetical or a closing `\testref` — a part
   of the sentence it follows, not a sentence of its own.
4. **`i = 0` and `d ≥ 75`.** A block inside an enumeration would close
   the item's paragraph and set the mark off from the rest of the list;
   no block of the manuscript sits inside one. And a second block a few
   lines below the first is monotone prose: 75 words is the tightest
   block-to-block distance the manuscript already accepts (calibration:
   the criterion-sites report in `docs/reports/`), so `d < 75` keeps the
   claim inline.

The four gates read as a paragraph, but they are each a number: the
criterion is reproducible by anyone who opens `main.tex`, and the applied
inventory it reproduces — every block, every flagged site, every counter —
is recorded in `docs/reports/` (the criterion-sites report of this
repository).

#### The two heuristics — `u` and `p`

Both are **heuristics**, labelled as such wherever they are applied: they
act only on the cost and position conditions of gates 2 and 4, never on
gates 1 and 3. Each is a measurable positional signal, not a quantity of
the criterion.

**`u` — uniformity of a newline-separated list (HEURISTIC).** In a list
whose elements already sit on their own lines — an `enumerate`, `itemize`
or `description` whose `\item`s each begin a line, and the numbered
sequence of `imported` statements — every mark of the run takes the same
form: all inline or all on a line of its own, never mixed. The verdict is
therefore taken **from the run, not from the item**: census the other
marks of the run (the inline mark vs the `\witness` block), then

- run all inline → the mark stays inline, whatever gates 2 and 4 would say;
- run all own-line → the mark goes on a line of its own, whatever gate 4's
  `i` would say;
- run mixed → `u` gives no verdict (it abstains), the run is recorded as a
  uniformity defect for a later harmonising pass, and the site falls
  through to `p` and to the four gates;
- run with no other mark → `u` abstains for lack of a census.

Measurable: the run is delimited by `\begin{…}`/`\end{…}`; the census
counts `\witness` occurrences inside it, excluding the mark
under review.

Best practice: visual rhythm — a list whose marks change shape from item
to item forces the eye to re-acquire the pattern, while a consistent form
keeps the list scannable
([How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)).

**`p` — paragraph close (HEURISTIC).** A mark that is the last element of
its paragraph — only punctuation and commands follow it before the break —
adds a preference for a line of its own: the paragraph break the block
would cost is already there, and no residual can be stranded. The
condition is positional: it is read without reference to `k` or `L`, and
it acts on whichever of gates 2 and 4 would keep the mark inline. Among
candidates (`k ≥ 2`, `r = 0`), `p = 1` therefore sets the mark on a line of
its own; `p = 0` leaves the four gates to decide. Gate 1 stays absolute:
a single id never earns a line of its own, at a paragraph close or
anywhere else.

Measurable: from the mark to the end of its paragraph (blank line, the
close of the enclosing environment) there is no word — only punctuation
and commands.

Best practice: do not split what the reader is following — a sentence
closed at its paragraph close keeps its parts together, which is the
reading side of the same rule that `r = 0` enforces
([PlainLanguage.gov — Sentences](https://www.plainlanguage.gov/guidelines/sentences/)).

**Order of decision.** 1. gate 1 (`k ≥ 2`), 2. gate 3 (`r = 0`) — both
absolute; 3. `u`, when it gives a verdict; 4. `p`; 5. gates 2 and 4
(`L ≥ 35`, `i = 0`, `d ≥ 75`). A mark goes on a line of its own only when
one of steps 3–5 sets it there; otherwise it stays inline. The verdicts
for the current manuscript — every candidate site by the tail of its
sentence, with its `u`/`p` values and the counter delta — are recorded in
`docs/reports/` (the `u`/`p` verdicts report of this repository).

#### How the criterion is reviewed

One reading pass over the site table of the criterion-sites report in
`docs/reports/` — it prints, for every flagged site, the tail of the
sentence the mark closes, so the whole check is one question per row: *does
any word of that sentence follow the mark?* The same pass is what confirms
gates 4 (`i`, `d`) and the census of `u` for a new site, since all three
are read from the lines around it. No style test is written for this: a CI
check that re-derives what this section already guarantees would test the
document against itself; the census test guards what the build depends on
— the test references the manuscript cites — and nothing here does.

#### Concrete material of this rule

The site table with the sentence tails, the calibration facts behind the
thresholds, the applied state of the last harmonising pass, and the
pending `u`/`p` verdict table all live in `docs/reports/` of the
repository that applies the rule — indexed by its
[`README.md`](reports/README.md). A report is a snapshot of one
repository state; the rule itself is this section.

### 6.11 Standard, not applied state

This section states the standard; it does not assert that a manuscript's
body already satisfies it. What each repository's text does today — which
sites follow a rule and which do not — is measured and recorded in that
repository's `docs/reports/` and in its generated
`docs/witness-inventory.md`, never here. The shape of a call site is
outside it as well: whether the ids of an own-line accounting line such as
`Lean: …` sit in a block of their own or inside the tag as `P[ids]`, and
every other body-form question, belongs to the convergence that is still
pending — W2 (mechanical renames) and W3 (semantic pass) — and is neither
decided, nor changed, nor implied by anything below.

### 6.12 The own-line form

> **Own-line mark — rendering spec.** Applies to `\witness[ids]{X}` in
> all five repositories, in the branch its position selects (`\ifvmode`,
> S7); the inline branch of the same macro keeps the contract of §6.5.
> Every number below was measured, not chosen by eye: the probe and its
> artefacts are listed under *Sources* at the end of this section.

**S1. One shape, one macro.** The mark is exactly one macro,
`\witness[ids]{X}`, defined once per repository with the *same body*
(byte-level identical, as the family files are), and the position of the
call in the source picks the branch (S7). No hand-written
`{\raggedright \witness[…] …\par}` paragraph survives: those sites become
an own-line `\witness[ids]{P}` where the criterion of §6.10 holds,
otherwise the same macro inline in the prose. `\leanline` is retired as a *rendering form
of the mark* (it is already "not a body form"); the `Lean:` accounting
line itself remains class S4 (§6.4): its sites stay where they are and are
not migrated in bulk.

**S2. Vertical spacing — one number, and it is `\medskip` above and below.**

```latex
\newcommand{\witness}[2]{%
  \par\medskip\noindent\hfill
  \parbox{\dimexpr\linewidth-1em\relax}{\raggedleft …}%   % body as below
  \par\medskip}
```

*Chosen with reason.* The block used to sit at 13.000 pt on both sides —
the same as an ordinary line wrap — which is why a block read as a broken
line instead of as a mark (valley), while the `\medskip`/`\smallskip`
heads around it read at 17.550/15.275 (crest). One symmetric,
class-defined quantity removes the spread: `\medskip` = 4.55 pt in amsart
11pt, it is the same amount the manuscript already uses for its own
paragraph heads, and it is a *documented* skip (amsart redefines it as
`.35\baselineskip`), not a magic number. Do **not** use `\parskip` (it is
0 here and would be invisible) and do **not** use `\bigskip` (9.1 pt,
twice the head spacing). Because `\witness` issues `\par` on both sides,
the two `\medskip`s never stack with `\parskip`.

**S3. Indentation: 0, always.** `\par\medskip\noindent` before the box
(no `\indent`), and the paragraph *after* the block is a normal new
paragraph → it takes the document `\parindent` (11.95 pt). Never
`\noindent` after the block, never a run-in head. Edge cases:

- macro invoked mid-line (`\ifhmode`): see S7 — it does not create a
  block, so the question does not arise;
- after `\noindent` (a head or a `\smallskip\noindent…`): the preceding
  paragraph is already flush left; the block still emits its own `\par`,
  so spacing stays S2;
- inside `enumerate`/`itemize`: forbidden by gate `i = 0` (§6.10) — the
  block would close the item's paragraph; keep inline;
- inside a theorem/proof environment: allowed, same S2 (amsthm
  environments are `\trivlist`-based and the following line is indented
  anyway — see S9);
- at the very top/bottom of a page: `\par\medskip` at the start of a page
  is absorbed by `\topskip`; acceptable, no special case.

**S4. Width: full measure, right edge on the margin.**
`\parbox{\dimexpr\linewidth-1em\relax}` after `\hfill` — the box's right
edge lands exactly on the right margin (measured 540.00 pt, gap 0.01 pt)
and its left edge is free to stop up to `1em` short of the left margin. Do
not switch to `\hfill` + `\raggedleft` without a box (that is what the
hand-written blocks do: their right edge is ragged, 16–29 pt short) and do
not use `\begin{flushright}` (adds `\topsep`/`\partopsep`).

**S5. Punctuation.** The mark never carries terminal punctuation: **no
`.`, no `,` after the closing `}` and none inside the bracket**; the
sentence closes before the block (gate `r = 0`, already true at 100% of
sites: 0/86, 0/124, 0/43). A `,` or `;` may only appear *between ids*, and
only as the separator `", "`. A hand-written block that carries prose
inside the block violates this by construction — that is one more reason
they are retired.

**S6. Colour by class, on the whole mark or on none.** One palette for the
family: `tierP = (0.15,0.35,0.65)`, `tierN = (0.05,0.40,0.20)`,
`tierPs = (0.70,0.45,0.05)`, `tierW = (0.00,0.35,0.45)` — i.e. the 02/05
values, which are the ones the family colour redundancy rule (WCAG 1.4.1,
§4.2) was calibrated against; 03's `tagN` (0.15,0.55,0.25) and `tagH` are
dropped (or `tagH` is registered as a published class with a cost
estimate first, §6.9). Colour scope: **the whole mark — the letter *and*
the ids in the class colour**, which is what `\witness` already does in
3/3 repositories that render marks and it makes the block read as one
object; the inline branch must be changed the same way (its ids print
black today, measured #000000 against #2659a5 in the block). Colour is
redundant with the letter either way.

**S7. Placement rule (`\ifvmode` / `\ifhmode`) and its edge cases.**

```latex
\newcommand{\witness}[2][]{%          % #1 = ids (optional), #2 = class
  \ifvmode                      % own line in the source -> block (S2–S6)
    \par\medskip\noindent\hfill
    \parbox{\dimexpr\linewidth-1em\relax}{\raggedleft <body>}\par\medskip
  \else                         % mid-line in the source -> inline, no break
    {\normalfont\footnotesize\bfseries\markcol{#2}#2%
     \mdseries{\upshape\small\tttfamily[\tierids{#1}]}}%
  \fi}
```

- `\ifvmode` after a blank line or at the start of a line → block, as
  today.
- `\ifhmode` (a mark written where a paragraph is already open — the 37
  mid-line sites of 03, the 1 of 05) → the mark stays inside the
  sentence: **no `\par`, no indent, no space is eaten** — the paragraph
  does not break. This removes the behaviour the inline macro had, where a
  mid-line call silently ended the paragraph and stranded the rest of the
  sentence.
- After `\noindent` or after a head the mode is `\hmode` → inline:
  correct, the text there is one paragraph.
- Inside a group started with `{\itshape …}`: the body must begin with
  `\normalfont` and reset with `\mdseries` — otherwise the letter prints
  bold-italic (measured: SFBI0900 against SFBX0900).
- The argument is still read as an arbitrary string (§6.5); the `\cite`
  guard stays.
- **No id (`\witness{X}`)**: both branches print the class-pure bracket
  `[X]` (§6.1) — never `X[]`, and no id is invented for the site.

**S8. Line breaking of long id lists.** Break priority: **`, ` first, `_`
only as a fallback.** Concretely:

```latex
% \brk@us = \textunderscore\penalty500\hskip0pt   % discouraged, still legal
% after every ", " keep the natural interword break (penalty 0)
```

- TeX prefers the lower-penalty break, so a list splits at commas whenever
  it can and only splits inside an identifier when the id itself is longer
  than the remaining measure — which is the case where breaking is
  unavoidable anyway.
- The previous `\allowbreak` (= `\penalty0`) after every `_` made the
  mid-identifier break *equally* attractive, hence `twenty_divisor_` /
  `lattice_splits` in the 02/05 PDF; the 03 form (no break at all) is the
  opposite extreme and is the one that can go overfull. The
  penalty-tuned form sits between them.
- Do **not** adopt `\seqsplit`/`xurl`-style break-everywhere for witness
  ids: that maximises raggedness. `\seqsplit`/`xurl` remain the right tool
  for URLs and for *single* identifiers longer than the measure, not for a
  list.
- Acceptance: compile the family, assert **0 Overfull/Underfull `\hbox`**
  in the blocks and re-check the byte-identical `pdftotext` gate (the
  family's own rule; a break change reflows text, so it must be measured,
  not assumed).

**S9. Measurement, not eyeballing.** Keep the family rule of §6.7
("rendering is re-checked by measurement") and pin the numbers above as
the measurable targets: 13/15/16 px sizes, right edge on the margin,
`\medskip` both sides, indent 11.95 after the block, 0 overfull, letter
colour on ids.

#### Sources

1. **amsthm manual (AMS, v2.20.3, 2017)** — theorem-like blocks declare
   their spacing explicitly: `\newtheoremstyle{…}{<space above>}{<space
   below>}{<body font>}{<indent amount>}{<head font>}{<punctuation>}{<space
   after head>}{<head spec>}`; and *"after the end of a theorem or proof,
   the following line of text is assumed to start a new paragraph, and
   will always be indented, whether or not a blank line or `\par` is
   present."* → supports S2 (declare the space, one named quantity), S3
   (indent 0 for the block, normal paragraph after) and the
   `\ifvmode`→block / paragraph-after reading of S7.
   <https://texdoc.org/serve/amsthm/0>
2. **tex.stackexchange 37472, "Spacing before and after with
   `\newtheoremstyle`"** — the accepted answer documents the same three
   knobs (Space above / Space below / Indent amount), notes the default
   above/below is `\topsep` (`8.0pt plus 2.0pt minus 4.0pt`), and that
   `\theoremstyle{remark}` is *"the same as `definition` except that it
   doesn't add extra space above and below"* — i.e. the spacing difference
   between styles is a *declared parameter*, not a side effect. → the
   direct precedent for choosing one skip and writing it in the macro
   instead of letting it fall out of font size and `\lineskip`.
   <https://tex.stackexchange.com/questions/37472/spacing-before-and-after-with-newtheoremstyle>
3. **The TeX FAQ, "(La)TeX makes overfull lines"** — line breaking is
   governed by `\pretolerance`/`\tolerance`/`\emergencystretch` plus
   hyphenation/break points; an overfull box means *"TeX has given up"*,
   and `\emergencystretch` is a further pass that must be "treated with a
   degree of caution". → supports S8: fix the *break points and their
   penalties* (the ids' `_`/`, `), don't patch the symptom with a global
   tolerance; also explains why 05's `\emergencystretch=2em` hides some
   raggedness that 03 does not have.
   <https://texfaq.org/FAQ-overfull>
4. **CTAN: `xurl`** — *"loads `url` by default and defines possible URL
   breaks for all alphanumerical characters"*, i.e. break-anywhere is a
   deliberately documented, opt-in policy for unbreakable strings. → the
   contrast that fixes S8: witness ids are *meant* to stay legible, so the
   family adopts comma-first breaking instead of break-everywhere, and
   reserves `xurl`/`\seqsplit` for URLs and single oversized identifiers.
   <https://ctan.org/pkg/xurl>
5. **CTAN: `parskip`** — *"Simply changing `\parskip` and `\parindent`
   leaves a layout that is untidy; this package … helps alleviate this
   untidiness."* → the standing caution behind S2/S3: paragraph-level
   spacing and block-level spacing are separate knobs; the family must not
   try to express the mark's spacing through `\parskip` (which is 0 in
   amsart here) but must put it in the macro, and must keep the indent
   rule coherent with the rest of the layout.
   <https://ctan.org/pkg/parskip>

### 6.13 Status ledgers segment by purpose

A status ledger is segmented in three lists, each with a use of its own:
a **`Proved claims registry`** (only claims with an explicit id), an
**`Open problems`** list (the format of open problems) and a
**`Classical inputs`** table (a compact claim + source table). A single
list that mixes them and is not segmented does not satisfy the criterion.

---

## 7. Honesty: the declared novelty

This document does not present the convention as something consecrated.
The verifiable claim is the reverse: **no previous publication marks
verification claim by claim inline, at the exact point where it asserts
it**, and the project says so as much.

- This document states without detour (§4.1, §6.9) that the inline status
  is a convention of this project and not one of AMS or Chicago, and
  points to the real precedents — `leanblueprint` with status per
  statement, status tables, artefact seals — as the closest thing that
  exists.
- The omega-pcf family is, in that sense, **pioneering**: it adopts the
  principle of those precedents and lowers it to the claim, which is a
  level of granularity the precedents do not cover. Being pioneering has a
  declared cost: there is no external norm to appeal to if someone asks
  "where is this specified?", and the answer is this file (§6).
- The research pass on the convention committed to reporting the split
  honestly — which part is discipline standard, which part is device
  proper to the project, and what the nearest precedent is — and so it was
  recorded. Nothing this document asserts is presented as a published norm
  when it is not.

The declared novelty is, besides, the best argument in favour of the
convention: if the state of the evidence is today a structural datum of
the result (§3), saying so at the point of assertion is more honest than
silencing it, and doing so with a quantified and reproducible criterion
(§4.4) is what separates a convention from a whim.

---

## 9. Limits of this document

1. **This document argues, it does not apply.** The applied state of the
   convention in a given repository — counters, verdicts, pending rows —
   is recorded in `docs/reports/` and in that repository's generated
   `docs/witness-inventory.md`, and nowhere else; nothing here asserts
   that a manuscript has already satisfied a rule it states.
2. **Propagation to the family is an editorial decision.** Whether a
   repository renders marks at all, and whether it adopts the criterion of
   §6.10, is decided by the author of that repository, never mechanically
   by this document.
3. **No external guarantee.** While there is no published norm that
   describes the claim-by-claim mark, the convention rests on this
   documentation and on its review; that is declared in §7 and must not be
   presented otherwise.

---

## 10. Wave brief shape

Every wave brief carries these five blocks, in this order. A brief that
omits one is not dispatched. The blocks are headings, not prose — fill
them, do not introduce new rules.

### 1. Standard

The literal citation the brief relies on:

> `docs/witness-contract.md` §6.… — *<the rule, quoted or paraphrased in one line>*

No rule may appear in a brief that is not in §6 of this document. If a
rule has to be re-framed to do the work, that is a row in
`docs/witness-decisions.md`, not an edit of the standard.

### 2. Rows in scope

> `docs/witness-decisions.md` WD-…, WD-… — *<state each row's current resolution>*

Only rows in this list may be acted on. A row not listed stays untouched,
and no other row may be surfaced in the same brief.

### 3. Layer, and what this wave does not cover

> Layer: *preamble | body | docs | tests* — `<the files this wave may edit>`
> Not covered: *<what is out of scope, and who or which wave covers it>*

### 4. Ruling cited

> `<msg id>` — *<the operator's ruling, verbatim, ≤ 5 lines>*

A brief quotes at most one ruling, and only when the standard alone does
not settle the case. A decision already recorded in
`docs/witness-decisions.md` is cited by its row id instead of being
re-quoted.

### 5. Gates expected

> `validate` exit 0 · `build` with 0 undefined · clean tree ·
> `origin/main..HEAD` = 0 after push

`validate` already runs `manifest:check` (with `counts:check` and
`inventory:check`), so it is never listed a second time. Add the wave's
own gate (a lint, a count, a render check) as a sixth line.
