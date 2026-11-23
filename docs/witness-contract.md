# Witness contract — rationale of the witness mark

| Field | Value |
|---|---|
| **Document** | `docs/witness-contract.md` |
| **Status** | In force with the manuscript |
| **Version** | 1.0 (portable rationale; family standard, adapted to this repository's P/N, inline-only device) |
| **Date** | 2026-11-23 |
| **Language** | English; identifiers, macros and file names in English and monospace |
| **Scope** | Why the witness marks (`\tier`, `\LeanInline`, `\LeanStar`, `\LeanTally`, `\LeanCW`) exist and what they do not assert — the argument behind the contract of `docs/citations.md` §8, free of anything tied to one repository state |

**Document:** justification of the witness convention of the manuscript,
written so that the convention has a place in a paper of pure mathematics.

**Relation to the rest of the documentation.** This document **argues**; the
**operational** rule lives in `docs/citations.md` §8 (grammar, writing
rules, alphabet, conventions and the inline / own-line criterion). The
per-site decisions — which witness supports each claim, what is rewritten
and what is removed — and the measured state of one manuscript live in
`docs/reports/`. Nothing asserted here changes the contract of
`docs/citations.md`: if the two documents ever disagree,
`docs/citations.md` governs, because it is the one the build and the text
review use.

**Status and method.** In force with the manuscript. The concrete state of
a manuscript — counters, site tables, verdicts — is measured with `git
grep` on `main.tex` and `src/chapters/*.tex` and recorded in
`docs/reports/`; a site is identified by the tail of the sentence, not only
by the line number, because the manuscript is edited concurrently.

---

## 1. What is justified here

The manuscript marks, beside each claim, how it was established: `P` when
the statement is proved and machine-checked in Lean, `N` when it is
verified numerically with the name of the test that checks it. In this
repository the mark is always a small inline bracket set in `\footnotesize`
and bold — `\tier{P}`, `\tier{N}`, `\tier[\testref{ids}]{N}` — printed in
black like the surrounding text (there is no colour dispatch and no
own-line block form in this repository's preamble; see `docs/citations.md`
§8.1). The two classes are introduced by an in-text gloss that sits before
the first mark of the body and defines the classes and nothing else; the
*Protocol* subsection repeats the definition where the reader meets the
index of statements. The label of a numbered list of steps (`W1`, `W2`, …
— the five steps of Weil's proof) is not a class of evidence: it is
defined in a sentence at the list itself.

That device is not a typographic fashion nor an ornament: it is the answer
to a real problem of reading and of attribution, and its shape is decided —
where a block form exists — by a quantified criterion. What this document
maintains is precisely that: that the convention is **legitimate** (it
solves something the bibliographic citation does not solve), **coherent**
with contemporary verification practice, **usable** (it costs neither
legibility nor extra printable space) and **honestly declared** (it is not
presented as an AMS or Chicago norm, and it warns of its novelty).

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
   beside the claim as a citation, and the mark carries the internal
   witness, by identifier.

2. **The referent is not unique.** When a claim rests on several proofs of
   the repository's Lean file and on several tests of the suite, citing
   "the proof" in the singular forces a choice of one and the hiding of
   the others, or the writing of an enumeration in prose that breaks the
   sentence. The grammar of the device — one claim, one mark; the list of
   identifiers inside the bracket — gives the reader the complete and
   verifiable referent: each identifier is a name that can be searched for
   in the Lean file or in the suite.

3. **The typographic cost matters.** A claim with a single witness fits in
   the sentence; a claim with five forty-character names does not. Without
   a shape rule, the text accumulates long brackets in the middle of the
   phrase and the reader loses the thread of the sentence that contains
   them. In this repository the bracket is the only shape there is, so the
   cost is bounded by construction: a bracket per claim, never a block.

### 2.2 What the reader gains

- **Checks the statement without leaving the text.** The identifier is on
  the page; the Lean file and the suite are in the repository. A number
  marked `N[test_…]` can be reproduced with one command (`uv run pytest
  tests/ -q`); an identity marked `P` with a named declaration locates the
  theorem in `lean/F1_pentagonal_descent_UNIFIED.lean`.
- **Distinguishes at a glance the nature of the evidence**, without reading
  the bibliography: the letter carries the meaning (§4.2).
- **Knows what is not marked.** The absence of a mark is information: an
  unmarked claim is a claim the paper does not verify where it asserts it.
  That asymmetry is useful only if the mark is systematic.

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
   beside the claim answers that reality**.

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
§6, where exactly what the convention is and what it is not is declared.

---

## 4. Usability and compactness

### 4.1 Inheritance from the secondary notation of software engineering

The device does not spring from mathematical typography, but from a
practice consolidated in software engineering and interface design:

- **Semantic typing:** names say what they are. An identifier `test_…`
  needs no gloss; the reader who looks for the check finds it. The bracket
  of the witness inherits that discipline: it admits only internal
  identifiers, never bibliography keys or printed numbers, so its content
  is always a searchable name.
- **Colour as a *UX* marker, redundant with the label:** in serious
  interfaces colour speeds up reading, but the label still carries the
  meaning; colour is never the only path. This repository's marks carry no
  colour at all (§4.2), so nothing hangs on the shade.
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
the inline mark, the one-macro grammar, the letter rule — is device proper
to the project and is declared as such.

### 4.2 The WCAG 1.4.1 rule: colour never carries meaning alone

`docs/citations.md` §8.4 fixes this rule: **colour is redundant with the
letter (WCAG 1.4.1)**; the mark reads the same in greyscale and the letter
suffices to carry the meaning. In this repository the rule holds
trivially: the tags are typeset in the text colour, so the letter is the
only carrier by construction. The reasons it is stated anyway:

1. **Print.** The paper is read on paper and in reduced-colour PDF; the
   PDF is archived and cited in formats that lose colour.
2. **Accessibility.** 1.4.1 is the condition that a reader with colour
   deficiency distinguishes `P` from `N` without chromatic help.
3. **System consistency.** If a colour were ever added, it would have to
   be redundant with the letter, not a second grammar to keep synchronised
   with the alphabet.

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
reference list keeps ordering the references — in this repository
alphabetically (`sorting=nyt`, `docs/citations.md` §3) — and the mark
does not enter that layer.

### 4.4 The quantified criterion

Where the family's block form (`\witness{X}{ids}`) exists, the shape of
each mark is decided with five quantities read directly from `main.tex`,
with no judgement of taste (`k`, `L`, `r`, `d`, `i`; four gates and two
labelled heuristics). The single home of the definitions is
`docs/citations.md` §8.5; this document does not restate them.

**In this repository the criterion has no block to assign.** The preamble
defines no `\witness{}` and no `\wtag{}`, so every mark is inline by
construction and the criterion ran over the manuscript as a measurement,
not as a rewrite: `F8-001` §2 measured 1 100 marks and recorded 856
inline / 244 own-line verdicts, the 244 remaining `needs-decision` because
the ported apparatus had no own-line form to move them to. The decision
(port the block form, or accept inline everywhere) belongs to the author;
nothing was rewritten in block form on the strength of the criterion alone
(D4: *never in bloque*).

What the four conditions answer, where they can act:

- `k` and `L` address **cost**: the block pays a paragraph break, so it is
  only asked of lists that truly need the line.
- `r` addresses **reading**: a block ends the paragraph where it sits, so
  any residual would strand the sentence that follows it; the residual is
  counted, not estimated.
- `d` addresses **rhythm**: a second block less than seventy-five words
  from the first is monotony; the manuscript itself marks the empirical
  floor.
- `i` addresses **position**: a block inside an enumeration would separate
  the witness from the rest of the item.

The review method — the reading pass over the site table, its one question
per row, and why no CI test is written for it — is stated once, in
`docs/citations.md` §8.5; this document follows that method, it does not
restate it.

### 4.5 Compactness: the measured cost of the device

*Compactness* is not an intuition here: it can be counted. Measured with
`git grep` on the manuscript, the whole apparatus of this repository is a
handful of numbers — inline class tags (`\tierP`, `\tierN`), the marks that
carry a `\testref` id, and the name decorations (`\LeanInline`,
`\LeanStar`, `\LeanTally`, `\LeanCW`, `\leanline`). The measurement is a
census of the manuscript, so it belongs to `docs/reports/` of the
repository that measures it (the current census is in the MRG-001 closure
report); the method is stated here because the thresholds of
`docs/citations.md` §8.5 are argued against it. From that census follow
two consequences:

1. **The block is expensive, so it is asked to pay in return.** It costs a
   line and breaks the paragraph; it is only asked of a list of 35
   characters or more. Without a threshold, a twenty-nine-character list
   would earn a whole line and the cost would have no counterpart; the
   paragraph-close heuristic `p` is what lifts gate 2 for such a site
   (`docs/citations.md` §8.5).
2. **The inline bracket is cheap but not free.** The optional argument of
   `\tier` prints names, never numbers: the cost of the bracket does not
   grow with the numbering of references, and the identifiers break in
   line thanks to the permitted underscores (`\brk@us`). The real limit is
   not the width, it is the sentence: hence `r` rules, not `L`.

With that, the budget of the device is predictable: a bracket per claim.
It is a price that the information it buys — how each statement was
established — justifies, and it is also the reason the shape rule exists:
without it, the budget would grow with the prose and the apparatus would
begin to read as noise.

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
the `\cite`, beside the claim. The optional argument of `\tier` admits
**only** internal identifiers — a `\testref{…}` in this repository — and
the preamble raises a `\PackageError` before anything else, so a mark
bracket never prints a reference number. A bracket that said "it is cited"
would be redundant with the citation that is already there.

**One claim, one mark.** There are no two adjacent marks (measured: 0),
nor a mark and a `\cite` saying the same thing. The gloss is exempt from
the mandatory-witness rule because it defines, it does not assert.

**`P*` is retired here, and what the star means now.** The class existed
in the ported preamble — a statement written for this version, not yet
compiled against the corpus — and was used 246 times before the F11
reconciliation, which retired it: the census of the closing wave reads
`P* = 0` and `git grep -F '\tierPnew'` over the manuscript returns
nothing. What survives is the **decoration** `\LeanStar{…}` (221 uses),
whose superscript `*` records the pre-compilation provenance of the name —
`F9-001` classifies every starred name as present in the compiled file and
the mark itself as a **process artefact of the build**, not a tier: the
modules compile in the green build. The gloss never mentions `P*`, and the
prose does not speak of it; whether the 221 stars are unified with plain
`\LeanInline` is a presentation decision recorded for the author in the
MRG-001 closure report. It is a work tool's residue, not a class of the
published alphabet.

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
  result about them`).

The same fate met the port's other non-standard classes (`C`, `O`, `T`,
`Nc`): each named a status the sentence states in words, and the F11
reconciliation retired them to prose — the closing census reads
`C 0 · O 0 · T 0 · R 0 · Nc 0` (see `docs/citations.md` §8.3). The
published alphabet of evidence is `P` and `N`.

**The hypothesis rule.** A `\tierP` mark certifies exactly the Lean
statement it names, **with its hypotheses**: when a declaration takes an
input as a hypothesis, that input is named with its own mark where it is
stated. The rule was carried out of the retired gloss into
`docs/citations.md` §8.3 (the operational home FTI-001 designated); the
text still applies it — the appendix's ledger and the *Hypotheses of
compiled lemmas* item of `05-categorical.tex` are written to it.

---

## 6. Honesty: the declared novelty

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

## 7. Internal references

The sources of this document are the family's documents and the
repository's own files; no external URL is invoked beyond the cited style
authorities.

| File | What it provides |
|---|---|
| `docs/citations.md` §8 (§8.1 grammar, §8.2 writing rules, §8.3 alphabet and why there is no `L`, `R`, `C`, `O`, `T`, `Nc`, plus the hypothesis rule and the `P*` history, §8.4 convention and the WCAG 1.4.1 rule, §8.5 the criterion) | the contract of the device; the operational rule this document justifies |
| `docs/citations.md` §3, §5, §6, §7 | data hygiene, documentation convention and settled style decisions of this repository (citation-order bibliography, URLs suppressed by DOI) |
| `docs/reports/` (index: `docs/reports/README.md`) | per-site decisions, counters of the reconciliation pass, the `N[ids]` inventory and the author's pending-work list — the applied state of this argument in one repository |
| `README.md` | link to the citation/witness documentation; `docs/README.md` is the directory index |
| `main.tex` — preamble (`\tier` dispatch with its `\PackageError` guard, `\LeanInline`, `\LeanStar`, `\LeanTally`, `\LeanCW`, `\leanline`) and the gloss before the first mark | the implementation and what the reader sees at the first mark of the body |
| `lean/F1_pentagonal_descent_UNIFIED.lean` | the `P` side the mark points at |
| `tests/` and `tests/test_witness_census.py` | the numerical suite and the census that pins the test identifiers the manuscript cites |
| `citation.csl.json`, `CITATION.cff` | the bibliographic layer the mark does **not** mix with: the external source is a `\cite`, never a mark identifier |
| `omega-pcf-paper-repos` → `references/decision-gates.md` | the method of the convention research pass (separate discipline standard, device proper, real precedent) and the rule of not writing CI tests for editorial conventions |
| `omega-pcf-paper-repos` → `references/witness-system.md` | the grammar of the family-level witness system, its known defects and the state of propagation to the sibling repositories |

---

## 8. Limits of this document

1. **This document argues, it does not apply.** The applied state of the
   convention in a given repository — counters, verdicts, pending rows —
   is recorded in `docs/reports/` and nowhere else; nothing here asserts
   that a manuscript has already satisfied a rule it states.
2. **Propagation to the family is an editorial decision.** Whether a
   repository renders marks at all, and whether it adopts the block form or
   the criterion of `docs/citations.md` §8.5, is decided by the author of
   that repository, never mechanically by this document.
3. **No external guarantee.** While there is no published norm that
   describes the claim-by-claim mark, the convention rests on this
   documentation and on its review; that is declared in §6 and must not be
   presented otherwise.
