# Wave brief template

Every wave brief carries these five blocks, in this order. A brief that omits
one is not dispatched. The blocks are headings, not prose — fill them, do not
introduce new rules.

## 1. Standard

The literal citation the brief relies on:

> `docs/witness-standard.md` §… — *<the rule, quoted or paraphrased in one line>*

No rule may appear in a brief that is not in `docs/witness-standard.md`. If a
rule has to be re-framed to do the work, that is a row in
`docs/witness-decisions.md`, not an edit of the standard.

## 2. Rows in scope

> `docs/witness-decisions.md` WD-…, WD-… — *<state each row's current resolution>*

Only rows in this list may be acted on. A row not listed stays untouched, and no
other row may be surfaced in the same brief.

## 3. Layer, and what this wave does not cover

> Layer: *preamble | body | docs | tests* — `<the files this wave may edit>`
> Not covered: *<what is out of scope, and who or which wave covers it>*

## 4. Ruling cited

> `<msg id>` — *<the operator's ruling, verbatim, ≤ 5 lines>*

A brief quotes at most one ruling, and only when the standard alone does not
settle the case. A decision already recorded in `docs/witness-decisions.md` is
cited by its row id instead of being re-quoted.

## 5. Gates expected

> `validate` exit 0 · `build` with 0 undefined · `manifest:check` ✓ ·
> clean tree · `origin/main..HEAD` = 0 after push

Add the wave's own gate (a lint, a count, a render check) as a sixth line.
