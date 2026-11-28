# Witness inventory — 02-odd-zeta

> **GENERATED** — `pnpm run witness:inventory` (`scripts/tasks/witness-inventory.ts`) rewrites
> this file from the working tree; `pnpm run inventory:check` (inside `validate`) fails with
> a diff when it drifts. Do not edit by hand.

Measured over the tracked manuscript sources (`main.tex` and `src/**/*.tex`) — 11 files. TeX comments (a line whose first non-space character is `%`) and the lines that *define* a counted macro are excluded; nothing here is copied from an older document. The form taxonomy is the one of `docs/witness-contract.md` §6.1.

## Marks

| form | count |
|---|--:|
| own-line `\witness[ids]{P}` | 122 |
| own-line `\witness[ids]{N}` | 0 |
| own-line `\witness{P}` (bare) | 0 |
| own-line `\witness{N}` (bare) | 0 |
| inline `\witness[ids]{P}` | 253 |
| inline `\witness[ids]{N}` | 45 |
| inline `\witness{P}` (bare) | 35 |
| inline `\witness{N}` (bare) | 21 |
| `\witness[\testref{…}]{N}` marks | 45 |

Ids carried by `N` marks: **45 ids over 33 distinct**.

## Decoration and accounting macros

| macro | occurrences in the manuscript |
|---|--:|
| `\LeanInline` | 3 |
| `\LeanStar` | 0 |
| `\LeanTally` | 17 |
| `\LeanCW` | 44 |
| `\leanline` | 0 |
| `\code` | 290 |
| `\testref` | 45 |
| `\witness` | 479 |

## Gates measured here

| gate | result |
|---|---|
| citation-key lint (no key, no `\cite` inside a tag) | **0 failures** |
| stars (`\LeanStar` body uses) | **0** |
| `Tier` column in a table | **0** |
| `pending(D7)` markers | **1** |
| `\witness[…]` id parts that are neither a `\testref`, a snake_case id nor a qualified declaration | **156** |
| open sites (`(open;`) | **2** |

`\witness[…]` ids that are neither a `\testref`, a snake_case id nor a namespace-qualified declaration (156 occurrences, 123 distinct):

- `G\_hom` ×5
- `G\_kernel` ×5
- `G\_pi2\_is\_chi5` ×4
- `Tstar\_rewritten\_in\_phi` ×4
- `G\_surj` ×3
- `functionalEquation\_chi5\_discharged` ×3
- `hurwitz\_representation\_L\_chi5` ×3
- `norm\_Omega\_is\_half` ×3
- `E\_iff\_no\_shared\_ordinate` ×2
- `E\_iff\_no\_shared\_ordinate\_chi5` ×2
- `F1\_monoidal\_descent\_data` ×2
- `Tstar\_carries\_both\_faces` ×2
- `isometry\_with\_common\_modulus₅` ×2
- `premise\_A\_iff\_GRH\_chi5` ×2
- `rSq\_le\_in\_strip` ×2
- `radius\_one\_is\_E` ×2
- `toMu6\_bijective` ×2
- `ψ\_of\_inert` ×2
- `ψ\_of\_split` ×2
- `B\_iff\_E\_one\_hypothesis` ×1
- `Chi5Zero` ×1
- `E\_iff\_no\_free\_orbit` ×1
- `E\_is\_one\_sided` ×1
- `F1Lawvere.reflection\_fixedPointFree\_Zω` ×1
- `F1Lawvere.ψ\_fixes\_int` ×1
- `F1\_descends\_to\_Galois` ×1
- `F1\_spectra\_anchor\_G\_bridge` ×1
- `FrobeniusUnico.Q.σ` ×1
- `FrobeniusUnico.Q.σ\_ω` ×1
- `G` ×1
- `GDS\_gives\_premiseA` ×1
- `GDS\_gives\_routeB` ×1
- `G\_diagonal\_characterisation` ×1
- `G\_diagonal\_unique` ×1
- `G\_genus\_zero` ×1
- `G\_pi1\_is\_chi4` ×1
- `G\_psi\_equivariant` ×1
- `M\_cube\_sub\_one` ×1
- `M\_is\_mul\_by\_phi` ×1
- `MonomialHalfP` ×1
- `TheSpanIdentifiesThem` ×1
- `Tstar\_in\_connector\_clauses` ×1
- `U\_commute` ×1
- `U\_comp` ×1
- `X\_PCF` ×1
- `Z20star\_pi2\_fiber\_is\_mod5` ×1
- `Zφ` ×1
- `chi5\_Z\_mul` ×1
- `closedUnderMate\_chi5` ×1
- `convergents\_are\_the\_entries\_of\_M\_pow` ×1
- `decoration\_matches\_G` ×1
- `det\_M\_eq\_norm\_phi` ×1
- `det\_M\_sq` ×1
- `discBound\_discharged\_high` ×1
- `discBound\_of\_high\_gamma` ×1
- `disc\_K\_is\_conductor\_squared` ×1
- `endo\_on\_ω` ×1
- `eps\_ne\_zero'` ×1
- `exactClosure\_of\_assembledLim` ×1
- `fiftynine\_is\_M2\_times\_conductor\_minus\_one` ×1
- … 63 further distinct ids

`pending(D7)` markers:

- `src/chapters/04-bridges.tex:107`

Open sites:

- `src/chapters/04-bridges.tex:1017`
- `src/chapters/04-bridges.tex:1149`

## Per-file marks

| file | `\witness` marks |
|---|--:|
| `src/chapters/01-introduction.tex` | 6 |
| `src/chapters/02-foundations.tex` | 20 |
| `src/chapters/03-mechanisms.tex` | 262 |
| `src/chapters/04-bridges.tex` | 121 |
| `src/chapters/05-categorical.tex` | 58 |
| `src/chapters/appendix.tex` | 9 |

Re-generate with `pnpm run witness:inventory`; a hand-edited figure is a defect.
