# Witness inventory — 02-odd-zeta

Generated 2026-11-25 from the working tree at `675c957` (`git rev-parse --short HEAD`), over `main.tex` and `src/**/*.tex` — 11 files. Every number below is read from those files at run time; nothing here is copied from an older document. The form taxonomy comes from FTI-001 §2, F8-001 §1, WIT-RECON-001 and INV-WIT-001 §A, which this file supersedes (`superseded-by: docs/witness-inventory.md`).

## Marks

| form | count |
|---|--:|
| `\tier[ids]{P}` | 272 |
| `\tier[ids]{N}` | 40 |
| `\tier{P}` (bare) | 61 |
| `\tier{N}` (bare) | 26 |
| own-line `\witness{P}{…}` | 86 |
| own-line `\witness{N}{…}` | 0 |
| `\tier[\testref{…}]{N}` marks | 40 |

Ids carried by `N` tags: **52 citations over 34 distinct ids**.

## Decoration and accounting macros

| macro | occurrences in the manuscript |
|---|--:|
| `\LeanInline` | 176 |
| `\LeanStar` | 0 |
| `\LeanTally` | 21 |
| `\LeanCW` | 44 |
| `\leanline` | 2 |
| `\code` | 39 |
| `\testref` | 40 |
| `\witness` | 86 |

## Gates measured here

| gate | result |
|---|---|
| citation-key lint (no key, no `\cite` inside a tag) | **0 failures** |
| stars (`\LeanStar` body uses) | **0** |
| `Tier` column in a table | **0** |
| `pending(D7)` markers | **3** |
| `\tier[…]` id parts that are neither a `\testref`, a snake_case id nor a qualified declaration | **104** |
| open sites (`(open;`) | **2** |

`\tier[…]` ids that are neither a `\testref`, a snake_case id nor a namespace-qualified declaration (104 occurrences, 82 distinct):

- `G\_hom` ×4
- `G\_kernel` ×4
- `Tstar\_rewritten\_in\_phi` ×4
- `functionalEquation\_chi5\_discharged` ×3
- `G\_pi2\_is\_chi5` ×3
- `G\_surj` ×2
- `premise\_A\_iff\_GRH\_chi5` ×2
- `toMu6\_bijective` ×2
- `isometry\_with\_common\_modulus₅` ×2
- `norm\_Omega\_is\_half` ×2
- `Tstar\_carries\_both\_faces` ×2
- `E\_iff\_no\_shared\_ordinate\_chi5` ×2
- `rSq\_le\_in\_strip` ×2
- `radius\_one\_is\_E` ×2
- `zeta20\_pow\_five\_eq\_I` ×1
- `M\_is\_mul\_by\_phi` ×1
- `det\_M\_eq\_norm\_phi` ×1
- `F1\_monoidal\_descent\_data` ×1
- `disc\_K\_is\_conductor\_squared` ×1
- `Tstar\_in\_connector\_clauses` ×1
- `det\_M\_sq` ×1
- `omegaZ\_kernel\_three` ×1
- `fiftynine\_is\_M2\_times\_conductor\_minus\_one` ×1
- `three\_readings\_are\_G\_invariants` ×1
- `sigma\_is\_M2\_over\_two` ×1
- `toMu6\_additive` ×1
- `convergents\_are\_the\_entries\_of\_M\_pow` ×1
- `M\_cube\_sub\_one` ×1
- `U\_comp` ×1
- `U\_commute` ×1
- `twistedTrace` ×1
- `E\_iff\_no\_free\_orbit` ×1
- `E\_iff\_no\_shared\_ordinate` ×1
- `mem\_target\_iff\_spectralPoly\_zero` ×1
- `minSpacing\_on\_the\_spectrum` ×1
- `klein\_orbits\_on\_Z20\_are\_two\_and\_four` ×1
- `orbit\_radius\_vanishes\_iff\_E` ×1
- `zeroCoord\_is\_a\_distance\_ratio` ×1
- `liMap\_sq\_defect` ×1
- `noLowZeros\_forces\_a\_small\_defect` ×1
- `discBound\_of\_high\_gamma` ×1
- `valPhi\_phi\_pow` ×1
- `valPhi\_is\_the\_bridge\_to\_psi` ×1
- `valPhi\_inversion\_is\_negation` ×1
- `monomial\_iff\_valPhi\_int` ×1
- `the\_zero\_pair\_in\_valPhi\_has\_opposite\_signs` ×1
- `unconditional\_valPhi\_bound` ×1
- `li\_coordinate\_reads\_E` ×1
- `liFix\_root` ×1
- `liFix\_re\_is\_half` ×1
- `liFix\_abs\_one` ×1
- `liMap\_sq` ×1
- `liMap\_pair\_reciprocal` ×1
- `integrality\_of\_valuation\_is\_E` ×1
- `monomial\_alone\_gives\_E` ×1
- `witness\_T3` ×1
- `E\_is\_one\_sided` ×1
- `realCoefficients\_chi5` ×1
- `closedUnderMate\_chi5` ×1
- `liMap\_on\_unit\_circle\_iff` ×1
- … 22 further distinct ids

`pending(D7)` markers:

- `src/chapters/04-bridges.tex:107`
- `src/chapters/appendix.tex:385`
- `src/chapters/appendix.tex:654`

Open sites:

- `src/chapters/04-bridges.tex:1009`
- `src/chapters/04-bridges.tex:1139`

## Per-file marks

| file | `\tier[…]` + `\tier{…}` marks |
|---|--:|
| `src/chapters/01-introduction.tex` | 6 |
| `src/chapters/02-foundations.tex` | 20 |
| `src/chapters/03-mechanisms.tex` | 181 |
| `src/chapters/04-bridges.tex` | 122 |
| `src/chapters/05-categorical.tex` | 58 |
| `src/chapters/appendix.tex` | 12 |

Re-generate with the measurement of the wave that owns this file; a hand-edited figure is a defect.
