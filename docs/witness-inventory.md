# Witness inventory — 02-odd-zeta

> **GENERATED** — `pnpm run witness:inventory` (`scripts/tasks/witness-inventory.ts`) rewrites
> this file from the working tree; `pnpm run inventory:check` (inside `validate`) fails with
> a diff when it drifts. Do not edit by hand.

Measured over the tracked manuscript sources (`main.tex` and `src/**/*.tex`) — 11 files. TeX comments (a line whose first non-space character is `%`) and the lines that *define* a counted macro are excluded; nothing here is copied from an older document. The form taxonomy is the one of `docs/witness-contract.md` §6.1.

## Marks

| form | count |
|---|--:|
| `\tier[ids]{P}` | 270 |
| `\tier[ids]{N}` | 40 |
| `\tier{P}` (bare) | 61 |
| `\tier{N}` (bare) | 26 |
| own-line `\witness{P}{…}` | 86 |
| own-line `\witness{N}{…}` | 0 |
| mid-line `\witness{…}` (no block) | 0 |
| `\tier[\testref{…}]{N}` marks | 40 |

Ids carried by `N` marks: **40 ids over 27 distinct**.

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
| `\tier[…]` id parts that are neither a `\testref`, a snake_case id nor a qualified declaration | **111** |
| open sites (`(open;`) | **2** |

`\tier[…]` ids that are neither a `\testref`, a snake_case id nor a namespace-qualified declaration (111 occurrences, 89 distinct):

- `G\_hom` ×4
- `G\_kernel` ×4
- `Tstar\_rewritten\_in\_phi` ×4
- `G\_pi2\_is\_chi5` ×3
- `functionalEquation\_chi5\_discharged` ×3
- `E\_iff\_no\_shared\_ordinate\_chi5` ×2
- `G\_surj` ×2
- `Tstar\_carries\_both\_faces` ×2
- `isometry\_with\_common\_modulus₅` ×2
- `norm\_Omega\_is\_half` ×2
- `premise\_A\_iff\_GRH\_chi5` ×2
- `rSq\_le\_in\_strip` ×2
- `radius\_one\_is\_E` ×2
- `toMu6\_bijective` ×2
- `B\_iff\_E\_one\_hypothesis` ×1
- `Chi5Zero` ×1
- `E\_iff\_no\_free\_orbit` ×1
- `E\_iff\_no\_shared\_ordinate` ×1
- `E\_is\_one\_sided` ×1
- `F1Lawvere.\ensuremath{\psi}\_fixes\_int` ×1
- `F1Lawvere.reflection\_fixedPointFree\_Z\ensuremath{\omega}` ×1
- `F1\_monoidal\_descent\_data` ×1
- `GDS\_gives\_premiseA` ×1
- `GDS\_gives\_routeB` ×1
- `M\_cube\_sub\_one` ×1
- `M\_is\_mul\_by\_phi` ×1
- `MonomialHalfP` ×1
- `Tstar\_in\_connector\_clauses` ×1
- `U\_commute` ×1
- `U\_comp` ×1
- `Z20star\_pi2\_fiber\_is\_mod5` ×1
- `Z\ensuremath{\varphi}` ×1
- `\ensuremath{\iota}\_pow` ×1
- `\ensuremath{\omega}\_sq` ×1
- `\ensuremath{\psi}\_of\_inert` ×1
- `\ensuremath{\psi}\_of\_split` ×1
- `closedUnderMate\_chi5` ×1
- `convergents\_are\_the\_entries\_of\_M\_pow` ×1
- `det\_M\_eq\_norm\_phi` ×1
- `det\_M\_sq` ×1
- `discBound\_discharged\_high` ×1
- `discBound\_of\_high\_gamma` ×1
- `disc\_K\_is\_conductor\_squared` ×1
- `fiftynine\_is\_M2\_times\_conductor\_minus\_one` ×1
- `hasDegree\_gives\_monomial` ×1
- `integer\_trace\_gives\_SL2\_eigenvalue` ×1
- `integrality\_iff\_E` ×1
- `integrality\_of\_valuation\_is\_E` ×1
- `isMonomial\_inv` ×1
- `klein\_acts\_on\_Z20\_by\_two\_involutions` ×1
- `klein\_orbits\_on\_Z20\_are\_two\_and\_four` ×1
- `liFix\_abs\_one` ×1
- `liFix\_re\_is\_half` ×1
- `liFix\_root` ×1
- `liMap\_on\_unit\_circle\_iff` ×1
- `liMap\_pair\_reciprocal` ×1
- `liMap\_sq` ×1
- `liMap\_sq\_defect` ×1
- `li\_coordinate\_reads\_E` ×1
- `mem\_target\_iff\_spectralPoly\_zero` ×1
- … 29 further distinct ids

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
| `src/chapters/appendix.tex` | 10 |

Re-generate with `pnpm run witness:inventory`; a hand-edited figure is a defect.
