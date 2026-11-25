# Witness contract — rationale of the witness mark

| Field | Value |
|---|---|
| **Document** | `docs/witness-contract.md` |
| **Status** | In force as the standard — §6 states what it does and does not claim about a manuscript's body |
| **Version** | 1.1 (portable rationale plus the derived standard; generic across the family) |
| **Date** | 2026-11-23 |
| **Language** | English; identifiers, macros and file names in English and monospace |
| **Scope** | Why the marks of evidence of the manuscript (`\tier`, `\witness` where the manuscript has one, with `\testref`) exist and what they do not assert — the argument behind the contract of `docs/citations.md` §8, free of anything tied to one repository state; §6 states the standard itself, derived from the positions already settled |

**Document:** justification of the witness convention (`\tier`, `\witness`) of the manuscript, written so that the convention has a place in a
paper of pure mathematics.

**Relation to the rest of the documentation.** This document **argues**; the
**operational** rule lives in `docs/citations.md` §8 (grammar, writing
rules, alphabet, conventions and, in §8.5, the quantified criterion for
inline versus a line of its own). The per-site decisions — which witness
supports each claim, what is rewritten and what is removed — and the
measured state of one manuscript live in `docs/reports/`. Nothing asserted
here changes the contract of `docs/citations.md`: if the two documents ever
disagree, `docs/citations.md` governs, because it is the one the build and
the text review use.

**Status and method.** In force with the manuscript. The concrete state of
a manuscript — counters, site tables, verdicts — is measured with `grep` on
`main.tex` and recorded in `docs/reports/`; a site is identified by the
tail of the sentence, not only by the line number, because the manuscript
is edited concurrently.

---

## 1. What is justified here

The manuscript marks, beside each claim, how it was established: `P` when
the statement is proved and machine-checked in Lean, `N` when it is
verified numerically with the name of the test that checks it. The mark is a small, immutable
bracket in its own colour (`\tier{P}`, `\tier{N}`,
`\tier[ids]{X}`), or a right-aligned line of its own when the claim carries
several witnesses (`\witness{X}{ids}`). The two classes are introduced
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

What this document does **not** do: it does not set editing rules. The
rules live in `docs/citations.md`; here the reason for being of each of
them is given.

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
syntactic factor behind §8.5 of `docs/citations.md`.

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
project, and what the real nearest precedent is. The distilled result sat
in `docs/citations.md` §8.4: the real precedents are the per-statement
status of `leanblueprint`, status tables and artefact seals; the rest —
the inline mark, the one-macro grammar, the colour rule — is device proper
to the project and is declared as such.

### 4.2 The WCAG 1.4.1 rule: colour never carries meaning alone

`docs/citations.md` §8.4 already fixes this rule: **colour is redundant
with the letter (WCAG 1.4.1)**; the mark reads the same in greyscale and
the letter suffices to carry the meaning. The rule is upheld here for
three reasons:

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
home in `docs/citations.md` §8.5 and are not restated here; the site table
— every flagged site with the tail of the sentence it closes — is the
criterion-sites report in `docs/reports/`. What this section adds is the
*why*: the four conditions answer four usability demands —

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
once, in `docs/citations.md` §8.5; this document follows that method, it
does not restate it.

### 4.5 Compactness: the measured cost of the device

*Compactness* is not an intuition here: it can be counted. Measured with
`grep` on `main.tex`, the whole apparatus is four numbers — inline marks
(with and without identifiers, split by class), blocks on a line of their
own, witness-list labels, and occurrences of `\testref`. The measurement
is a census of the manuscript, so it belongs to `docs/reports/` of the
repository that measures it; the method is stated here because the
thresholds of `docs/citations.md` §8.5 are argued against it. From that
census follow two consequences:

1. **The block is expensive, so it is asked to pay in return.** It costs a
   line and breaks the paragraph; it is only asked of a list of 35
   characters or more, calibrated against the shortest list the
   manuscript already prints as a block (the calibration facts are the
   criterion-sites report in `docs/reports/`). Without a threshold, a
   twenty-nine-character list would earn a whole line and the cost would
   have no counterpart; the paragraph-close heuristic `p` is what lifts
   gate 2 for such a site (`docs/citations.md` §8.5).
2. **The inline bracket is cheap but not free.** The optional argument of
   `\tier` prints names, never numbers: the cost of the bracket does not
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
`[P] in~\cite{key}`. The optional argument of `\tier` admits **only**
internal identifiers — a `\testref` or the raw name of a declaration of
the repository's Lean file — and the preamble raises a `\PackageError`
before anything else, so a mark bracket never prints a reference number.
A bracket that said "it is cited" would be redundant with the citation
that is already there.

**One claim, one mark.** There are no two adjacent marks, nor a mark and a
`\cite` saying the same thing, nor marks in figure captions (rule 8 of
`docs/citations.md` §8.2). The gloss is exempt from the mandatory-witness
rule because it defines, it does not assert.

**`P*` is internal.** The class exists and works in the preamble (dispatch
`\@namedef{tiercol@P*}`, ochre colour) to mark between compilations a
statement written but not yet verified against the corpus —
the star's one denotation (§6.5) —; the printed text never invokes it,
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

Both eliminations are documented in `docs/citations.md` §8.3 and applied
in the manuscript: the published alphabet of evidence is `P` and `N`.

---

## 6. The standard, as derived

The rules below are this contract's own standard. None of them is a new
decision: each restates a position already settled in the family's
documentation and makes it explicit here, so that one file carries the
argument and the rule together. Where a rule defers, it defers in the
open; nothing in this section decides a question the family documents
leave undecided.

**Standard, not applied state.** This section states the standard; it
does not assert that a manuscript's body already satisfies it. What each
repository's text does today — which sites follow a rule and which do
not — is measured and recorded in that repository's `docs/reports/`,
never here. The shape of a call site is outside it as well: whether the
ids of an own-line accounting line such as `Lean: …` sit in a block of
their own or inside the tag as `P[ids]`, and every other body-form
question, belongs to the convergence that is still pending — W2
(mechanical renames) and W3 (semantic pass) — and is neither decided,
nor changed, nor implied by anything below.

### 6.1 The set of evidence marks

The set of evidence marks is **`P` and `N`, with `\testref` as the test
anchor — nothing else**. No decoration, no accounting line and no label
enters the set. The internal `P*` dispatch of the preamble (§5) is a work
tool, not a class of the printed alphabet.

### 6.2 Placement is prose, never semantics

Whether a mark sits inside the sentence or on a line of its own is a
**prose criterion** — semantic, heuristic, aesthetic — and no rule of this
contract decides it. Placement never changes what a mark asserts: the
shape of a mark tells a reader how many witnesses a claim carries and
where they sit, never which kind of evidence it is. The quantified
criterion of `docs/citations.md` §8.5 stays what it has always been — a
readability aid for that prose decision (cost, rhythm, position) — and it
is not a classifier. The standard governs content and naming only.

### 6.3 Naming (S1–S5)

A name is routed by the job it does in its sentence; the pass that moves
names reads each site, classifies it and restates the classification
before editing:

| Class | Route |
|---|---|
| **S1** witness id | stays inside the mark — `\tier[ids]{X}`, `\witness{X}{ids}`, `\testref{…}` — written raw, never beside the tag |
| **S2** code mention | `\code` |
| **S3** decorated name (`*`, `°`, `†`) | `*` under §6.5; `°` and `†` under §6.7 |
| **S4** `Lean:` accounting line | no canonical form yet: the sites stay where they are and are not migrated in bulk |
| **S5** unclassifiable | recorded in `docs/reports/` as an open site, never guessed |

### 6.4 Grammar

The optional argument of a tag holds **internal ids only** — a `\testref`, or the raw names of
declarations of the repository's own Lean file, several of them separated by `,` — and a
citation key is never written inside a tag; an external source stays an adjacent `\cite`,
printed beside the mark, never fused into it.

The macro does not enforce this by the shape of its argument. A character-shape test
(`\_`, `,` or `\testref` present, otherwise an error) rejects valid internal ids — a Lean name
such as `F1PaperTorus.chi5WeilOrbit` carries none of those markers — and it cannot recognise a
citation key, whose characters are the characters of an identifier. The argument is therefore
read as an arbitrary string: an escaped `\_` and a raw `_` both print as the breakable
typewriter underscore, every other token passes through unchanged, and the only error the macro
raises at run time is a literal `\cite` token inside the argument, which is never an id.

The rule that the bracket holds no external source is enforced where the key set exists: a test
reads every `\tier[…]` and `\witness{…}{…}` argument of the manuscript, splits it on the commas
that sit outside `\testref{…}`, and fails when a part equals the id of a record of
`citation.csl.json` or contains a `\cite` token, reporting `file:line` and the key. The check
runs with the suite and is the only place where the citation-key rule is measured.

Repositories whose tags today accept a wider or a narrower set converge on this grammar by work,
not by relaxation of the rule: the identifiers the previous wording rejected are a measured set,
never a design constraint. Counted in one manuscript (`03-crystalline-worldsheet`, over
`src/chapters/*.tex`, 2026-11-25) **18 of the 100 id parts** of `\tier[…]` fail the repository's
naming standard — **12 label-style identifiers** (10 distinct, at 9 sites) and the **6 ellipsis
placeholders** of the gloss sentences — while `:`-style label keys remain **0**. They remain work
items and are rewritten to snake_case ids; the business rule itself is unchanged, only the layer
that enforces it moves.

### 6.5 The star

`*` has **one denotation**: a name *written, not yet verified against the
corpus*. It marks intermediate process state, it lives only in
intermediate layers, and the passes that verify the corpus resolve it;
the release gate is **zero stars**, so a released text carries none. The
star is not a class of evidence, not a degree of confidence and not a
citation. Any other reading of it — in a comment, in a colour note or in
a rule of the writing guide — is a defect and is corrected where it is
found.

### 6.6 Typography

The canonical render parameters, measured in the built PDF, are
**13 pt for the witness class, 15 pt for the ids and 16 pt for the
prose**, identical for `P` and `N`; only colour differs, and colour is
redundant with the letter (§4.2). Rendering is re-checked by measurement
at each wave, never by eye; reopening these parameters requires a new
measurement.

### 6.7 Open tier, table labels and decorations

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

### 6.8 The alphabet is frozen at `P` and `N`

The published alphabet is `P` and `N` (§5). Any expansion enters only
through the family's gate: measured sites, used *and* documented in all
five repositories, counted by `counts:check` and lintable, with the cost
of each new symbol estimated before it is admitted. Until a gate is
passed, the alphabet does not grow.

## 7. Honesty: the declared novelty

This document does not present the convention as something consecrated.
The verifiable claim is the reverse: **no previous publication marks
verification claim by claim inline, at the exact point where it asserts
it**, and the project says so as much.

- `docs/citations.md` §8.4 states without detour that the inline status is
  "a convention of this project and not one of AMS or Chicago", and points
  to the real precedents — `leanblueprint` with status per statement,
  status tables, artefact seals — as the closest thing that exists.
- The omega-pcf family is, in that sense, **pioneering**: it adopts the
  principle of those precedents and lowers it to the claim, which is a
  level of granularity the precedents do not cover. Being pioneering has a
  declared cost: there is no external norm to appeal to if someone asks
  "where is this specified?", and the answer is this file and
  `docs/citations.md` §8.
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

## 8. Internal references

The sources of this document are the family's documents and the
repository's own files; no external URL is invoked beyond the cited style
authorities.

| File | What it provides |
|---|---|
| `docs/citations.md` §8 (§8.1 grammar, §8.2 writing rules, §8.3 alphabet and why there is no `L` or `R`, §8.4 convention and the WCAG 1.4.1 rule, §8.5 the quantified inline / line-of-its-own criterion) | the contract of the device; the operational rule this document justifies |
| `docs/citations.md` §5, §6, §7 | data hygiene, documentation convention and settled style decisions (AMS alphabetical bibliography, initials) |
| `docs/reports/` (index: `docs/reports/README.md`) | per-site decisions, counters of the harmonisation pass, criterion sites, `u`/`p` verdicts and the author's pending-work list — the applied state of this argument in one repository |
| `README.md` | link to the witness section of `docs/citations.md`; `docs/README.md` is the directory index |
| `main.tex` — preamble (witness system, `\tier` dispatch, definition of `\witness`) and the *Evidence tags* gloss | the implementation and what the reader sees at the first mark of the body |
| the repository's Lean file (`lean/`) | the `P` identifiers the mark can print |
| `tests/` and the census test of the repository | the numerical suite and the census that fixes the test identifiers the manuscript cites |
| `citation.csl.json`, `CITATION.cff` | the bibliographic layer the mark does **not** mix with: the external source is a `\cite`, never a mark identifier |
| `omega-pcf-paper-repos` → `references/decision-gates.md` | the method of the convention research pass (separate discipline standard, device proper, real precedent) and the rule of not writing CI tests for editorial conventions |
| `omega-pcf-paper-repos` → `references/witness-system.md` | the grammar of the family-level witness system, its known defects (italic inheritance in theorem environments, inline marks inside alignments) and the state of propagation to the sibling repositories |

---

## 9. Limits of this document

1. **This document argues, it does not apply.** The applied state of the
   convention in a given repository — counters, verdicts, pending rows —
   is recorded in `docs/reports/` and nowhere else; nothing here asserts
   that a manuscript has already satisfied a rule it states.
2. **Propagation to the family is an editorial decision.** Whether a
   repository renders marks at all, and whether it adopts the criterion of
   `docs/citations.md` §8.5, is decided by the author of that repository,
   never mechanically by this document.
3. **No external guarantee.** While there is no published norm that
   describes the claim-by-claim mark, the convention rests on this
   documentation and on its review; that is declared in §7 and must not be
   presented otherwise.
