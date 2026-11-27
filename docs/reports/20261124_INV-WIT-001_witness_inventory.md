# INV-WIT-001 — Inventario de witnesses de `02-odd-zeta`

| Field | Value |
|---|---|
| **id** | `INV-WIT-001` |
| **title** | Witness inventory of `02-odd-zeta` — census of the marks of `main.tex` + `src/chapters/*.tex` |
| **status** | report only — census from a measurement; the generated counterpart is `docs/witness-inventory.md` |
| **date** | 2026-11-24 |
| **version** | 1.0 |

| Campo | Valor |
|---|---|
| Documento | `INV-WIT-001_witness_inventory.md` (salida en scratch; el repositorio no se toca) |
| Fecha | 2026-11-24 |
| Repo | `/mnt/media/dev/02-odd-zeta`, `main` = HEAD, árbol limpio (verificado antes y después) |
| Alcance | `main.tex` + `src/chapters/*.tex` (los 10 fuentes que el build inputs); `docs/` y `docs/reports/` sólo como referencia, no como sitio |
| Método | parseo de argumentos con llaves balanceadas (`\tier`, `\LeanInline`, `\LeanStar`, `\LeanTally`, `\LeanCW`, `\leanline`, `\code`, `\testref`), contexto = fila de tabla si el sitio está dentro de `tabular/longtable`, si no el párrafo separado por línea en blanco |
| Estandar de comparación | sintaxis única de 05-kkgt: `\tier[id1, id2]{P}` → `P[id1, id2]`; own-line `\witness{P}{id1, id2}` |

## Base de verificación (medida, no supuesta)

| Hecho | Valor | Cómo se obtuvo |
|---|---|---|
| Suite | **112 tests** coleccionados (`uv run pytest tests/ -q --collect-only`, 2026-11-24 tras W6 Fase2; eran 97 al cierre de W5a) | id-list guardada en `node_ids.txt` junto a este informe |
| Build Lean | **verde**: `lake build` → `Build completed successfully (18248 jobs)`, exit 0 (re-ejecutado el 2026-11-24) | `cd lean && lake build` |
| `lean.sorry` | **0** · `lean.axioms` **0** · `lean.theorems` 5712 | `pnpm run counts` → `docs/counts.md` (ledger vivo, `counts:check` en CI) |
| D7 | lista viva en `scratch/f1_v168/d7_pending_scripts.txt` (42 scripts aún pendientes; 34 ya portados y borrados de la lista); 68 marcadores `% pending(D7)` en el manuscrito (03:13 · 04:30 · appendix:25) | `git grep -c 'pending(D7)'` |
| Scripts portados | 38 `.py` en `hipotesis/pruebas/` (git-tracked) | `git ls-files hipotesis/pruebas/` |
| Tests que importan scripts | **ninguno**: `git grep -l hipotesis -- tests/` vacío | el corpus numérico vive en `oddzeta.*`, no en los `.py` |

---

## A. Formas de tag en el tex (agrupadas por forma)

Censo global de marcas de clase: **869** (`P` = 740, `N` = 129). Fuera de ellas: 995 `\LeanInline`, 221 `\LeanStar`, 44 `\LeanCW`, 21 `\LeanTally`, 67 `\leanline`, 18 `\code`, 6 `\testref`.

### A1 — `\tier[ids]{X}` canónico ✓ (6 sitios, 7 ids)

Cumple la sintaxis única: display `N[ids]`. **Los 6 son `N`; no existe ni un `\tier[ids]{P}`.**

| `archivo:línea` | tex literal | display |
|---|---|---|
| `02-foundations.tex:7` | `$\zeta(2)=\pi^2/6$ \tier[\testref{test\_zeta\_two\_pi\_squared\_over\_six}]{N}.` | `N[test_zeta_two_pi_squared_over_six]` |
| `02-foundations.tex:417` | `$N(\golden)=-1$ \tier[\testref{test\_phi\_unit\_norm\_negative\_one}]{N} \textup{(\cref{sec:ring})}` | `N[test_phi_unit_norm_negative_one]` |
| `03-mechanisms.tex:103` | `... \tier[\testref{test\_two\_cos\_pi\_over\_five\_equals\_phi}]{N} \eqref{eq:pentagon-id}` | `N[test_two_cos_pi_over_five_equals_phi]` |
| `03-mechanisms.tex:2151` | `$L(1,\chiv)=2\log\golden/\sqrt5$ \tier[\testref{test\_l\_one\_chi5\_digamma\_value}]{N}` | `N[test_l_one_chi5_digamma_value]` |
| `03-mechanisms.tex:2896` | `$\golden^{\lng}=2$ \tier[\testref{test\_mersenne\_bridge\_phi\_lambda\_log\_two}]{N}` | `N[test_mersenne_bridge_phi_lambda_log_two]` |
| `04-bridges.tex:232` | `... \tier[\testref{test\_sigma\_mu\_polynomial\_root\_three\_halves, test\_sigma\_mu\_polynomial\_root\_one\_half}]{N}` | `N[test_..., test_...]` (2 ids) |

Los 7 ids están en la suite y en el pin de `tests/test_witness_census.py::PINNED_CITED_IDS` (7 ids / 6 marcas) — los cuatro tests de censo pasan hoy.

### A2 — pares `[\LeanInline{id}] \tier{P}`: id fuera del tag (486 marcas) ✗

Definición usada: marca **sin** argumento opcional cuyo grupo (texto entre la marca anterior y la marca siguiente, o inicio de párrafo) contiene `\LeanInline/\LeanStar/\LeanTally/\LeanCW`.

| Subforma | Nº | display derivado | ¿cumple? |
|---|---:|---|---|
| ids sólo **antes** del tag | 68 | `[…], […] [P]` | ✗ |
| ids **antes y después** (el grupo abarca 2+ marcas) | 351 | `[…] [P]; […] [P]` (una sola lista colgando de la primera marca) | ✗ |
| ids sólo **después** del tag (orden invertido) | 67 | `[P]: […]` | ✗ |
| **sin ningún id** en el grupo | 377 | `[P]` / `[N]` | ✗ (tag sin testigo) |
| total marcas desnudas | 863 | | |

Ejemplos literales:

```
01-introduction.tex:116   (\LeanInline{G\_hom}, \LeanInline{G\_surj}, \LeanInline{G\_kernel} \tier{P}).
                          display: [G_hom], [G_surj], [G_kernel] [P]
03-mechanisms.tex:33      $\golden=2\cos(\pi/5)\qquad(\LeanInline{phi\_eq\_two\_cos\_pi\_fifth}\ \tier{P}).$
                          display: (… ) ([phi_eq_two_cos_pi_over_five] [P])
03-mechanisms.tex:2761    \leanline{… ; its components are \tier{P}: \LeanInline{F1CW.von\_mangoldt\_k\_values}, …}
                          display (own-line): Lean: … P: [F1CW.von_mangoldt_k_values], …   ← orden tag→ids
04-bridges.tex:35         (\LeanInline{DoubleCount}, \LeanInline{invariant\_two\_on\_measured\_range} \tier{N})
                          display: [DoubleCount], [invariant_two_on_measured_range] [N]   ← N con ids Lean, no con \testref
```

Distribución por archivo (marca por marca, misma definición): con id en el grupo = 486 → `03` 284 · `04` 124 · `05` 55 · `02` 17 · `01` 3 · `appendix` 3; sin id = 377 → `appendix` **317** (el ledger pone los ids en la columna `Declaration`, fuera del tag) · `04` 32 · `05` 18 · `03` 7 · `01` 3. Detalle por línea de las marcas sin id en `03`, `04` y `05` está en `N_ctx`/`tier_marks.json` (scratch).

### A3 — `\LeanInline{id}` sin tag en su párrafo (31 usos / 25 sitios) ✗

Criterio: ocurrencias de `\LeanInline` cuyo párrafo no contiene `\tier` ni `\leanline`. Ninguna lleva nombre de archivo (0 usos con `.py`/`.txt`/`.json`), así que ninguna es candidata natural a `\code` por el nombre; la ruta S1/S2 se decide por la oración:

| `archivo:línea` | nombre | contexto (cola de la oración) | clase | veredicto |
|---|---|---|---|---|
| `02-foundations.tex:906` | `TheSpanIdentifiesThem` | "the span (`…`); every form of it is proved" | S1 | falta el tag de la claim |
| `03-mechanisms.tex:2761` ×4 | `F1CW.von_mangoldt_k_values`, `F1CW.kappa_k_two_real_places`, `F1CW.kappa_k_simple_pole`, `F1CW.kappa_per_real_place` | dentro de `\leanline`, **después** de `\tier{P}:` | A2-orden | reordenar: ids dentro del tag |
| `03-mechanisms.tex:3717` | `Chi5Zero` | "A zero is a structure, not a hypothesis: `Chi5Zero` carries ρ…" | S2 | mención de tipo → `\code{Chi5Zero}` o prosa |
| `03-mechanisms.tex:3722` | `Chi5Zero` | `$\forall z\in\text{`Chi5Zero`}$` (fórmula) | S2 | tipo en display |
| `03-mechanisms.tex:3738` | `NoLowZeros` | celda de tabla `Input & Lean & Tier` ("classical; not proved in Lean") | D | ver tabla T1 |
| `03-mechanisms.tex:3746, 3748` | `Chi5Zero.companion(_re)` | "…so that `…` is a function and not a hypothesis" | S2 | mención de tipo |
| `03-mechanisms.tex:3749, 3944` | `NoLowZeros` | "Only `NoLowZeros` remains as a classical input" | S2 | mención de hipótesis clásica |
| `03-mechanisms.tex:4097` | `the_surviving_value_is_the_kernel` | "(…)." cierra una claim | S1 | falta el tag |
| `03-mechanisms.tex:4277, 4278, 4281` | `algebraic_integer_gives_MonomialHalf`, `UnitStructure`, `unit_is_a_power_of_phi` | "The corpus states (b) as …", "input … that omits…" | S2 | mención de nombres del corpus |
| `03-mechanisms.tex:4331` | `TernaryLZero` | definición ("A ternary L-zero is…") | S2 | tipo en definición |
| `03-mechanisms.tex:4363, 4416` | `BridgeAxiom` | "the identification is the hypothesis `BridgeAxiom`" | S2 | mención de hipótesis |
| `03-mechanisms.tex:4378` ×2 | `hecke_chi5_derived`, `Chi5Zero` | "…five proved in Lean and three not: … (`\LeanTally{…}`)" | S3 | sitio de tally, ver A6 |
| `03-mechanisms.tex:4379` | `MembershipStillOpen` | "The earlier statement `…` is therefore superseded" | S2 | mención de statement retirado |
| `03-mechanisms.tex:4412, 4413` | `TheSpanIdentifiesThem`, `BridgeIsCToP` | "…the identification is a marker, `…`, defined as `True`" | S2 | mención de marcador del corpus |
| `03-mechanisms.tex:4569` | `Chi5Zero` | "A zero is a structure (`Chi5Zero`)" | S2 | tipo |
| `03-mechanisms.tex:4695` ×2 | `MonomialHalfP`, `monomial_is_in_image_of_realiseP` | "(…)." cierra una claim | S1 | falta el tag |
| `04-bridges.tex:126` | `CountingLaw` | "…`…` \tier{P}, on the counting law of the corpus (`CountingLaw`)" | S2 | nombre del corpus |
| `04-bridges.tex:192` | `G_genus_zero` | "as $2=2-2g$ with $g=0$ (`G_genus_zero`); the proved content is…" | S1 | falta el tag de la claim |
| `04-bridges.tex:402` ×2 | `position_is_interval_meets_discreteness`, `radius_one_is_E` | "Given E, `…`, `…`" | S1 | falta el tag |

**Resumen A3:** 8 usos S1 (candidatos a mover al tag), 21 usos S2 (mención de código/tipo/hipótesis → `\code` o prosa), 1 sitio de orden invertido dentro de `\leanline`, 1 celda de tabla (D). No hay ningún uso que sea nombre de archivo (ningún `\code` pendiente por esta vía).

### A4 — líneas `\leanline` (67, todas en `03-mechanisms.tex`)

Definición: `\leanline{…}` = `​\par\noindent{\footnotesize\raggedright\textsc{Lean:} #1\par}\smallskip` → **display propio `Lean: [a], [b] [P]`** — forma NO conforme (el id vive fuera del tag y en una línea propia distinta del `\witness` de 05).

Líneas (las 67): 62, 89, 113, 166, 180, 203, 220, 234, 285, 294, 369, 385, 398, 431, 482, 524, 615, 650, 767, 868, 881, 921, 941, 969, 985, 1009, 1034, 1064, 1094, 1113, 1130, 1147, 1200, 1216, 1236, 1251, 1294, 1343, 1411, 1503, 1539, 1580, 1616, 1644, 1682, 1753, 1821, 1831, 1851, 1867, 1898, 1944, 1969, 2039, 2066, 2083, 2154, 2204, 2363, 2409, 2618, 2721, 2761, 2801, 2900, 2963, 3016.

Variantes de contenido (59 líneas de una sola clase `P`, 8 mezcladas `P`+`N`):

| variante | nº | tex literal | display |
|---|---:|---|---|
| sólo `P`, lista de ids + tag al final | 38 | `03:1064 \leanline{\LeanInline{F1PaperPadic.delta\_structure\_exists}, \LeanInline{F1PaperPadic.delta\_table\_inert}, \LeanInline{F1PaperPadic.delta\_table\_split} \tier{P}.}` | `Lean: [a], [b], [c] [P]` |
| `P` con estrella (ids `\LeanStar`) | 14 | `03:180 \leanline{\LeanInline{FrobeniusUnico.endo\_dichotomy}, \LeanInline{FrobeniusUnico.hom\_ext} \tier{P}; \LeanInline{endo\_on\_\ensuremath{\omega}} \tier{P}.}` | `Lean: [a], [b] [P]; [c] [P]` |
| `P` + `\code` | 2 | `03:369 \leanline{\LeanInline{phi\_continued\_fraction} \tier{P}\ for the convergence; the identity is \code{φ\_self\_ref}.}` | `Lean: [phi_continued_fraction] [P] for …; the identity is φ_self_ref` |
| `P` + `\cite` | 2 | `03:1200 \leanline{\LeanInline{pisano\_five\_is\_twenty} \tier{P}; the period is classical~\cite{wall60}.}` | `Lean: [pisano_five_is_twenty] [P]; … classical [wall60]` |
| `P` + `\LeanCW` + `\cite` | 1 | `03:431 \leanline{\LeanInline{norm\_Omega\_is\_half} \tier{P}; \LeanCW{normP\_eq\_tan}, \LeanCW{normF\_eq\_cos}, …}` | `Lean: [norm_Omega_is_half] [P]; [normP_eq tan]†, …` |
| `P`+`N`+estrella+`\texttt` (D7) | 3 | `03:1644 (i), (iii) \LeanInline{PasosDelTexto.fifth\_root\_trace}, … \tier{P}; (ii) Chebotarev …` | `Lean: (i),(iii) [a],[b] … [P]; (ii) …` |
| `P`+`N`+`\texttt` | 3 | `03:3560 … by \texttt{retro109.py} for the primes below $400$ \tier{N}; …` | `Lean: … retro109.py [N]; …` |
| `P`+`\texttt` (axiomas / nombre de lema Mathlib) | 2 | `03:2204 \leanline{\LeanInline{zeta\_odd\_pentagonal\_determination}, … \tier{P}, with axioms \texttt{[propext, Classical.choice, Quot.sound]} only, …}` | `Lean: [a], … [P], with axioms [propext, …] only` |
| `P`+`N`+estrella+`\cite` | 1 | `03:1616 \leanline{\LeanStar{W4Isometria.split\_layer\_law}, … \tier{P}; (iii), stated as \LeanStar{…}` | `Lean: [a]*, … [P]; (iii), …` |
| tag **antes** de los ids | 1 | `03:2761 … its components are \tier{P}: \LeanInline{F1CW.von\_mangoldt\_k\_values}, …` | `Lean: … [P]: [id], …` |

**Plan de conversión (no ejecutado):** por cada `\leanline{…}` extraer la(s) clase(s) y los ids del cuerpo; si una sola clase → `\witness{P}{id1, id2}` en el mismo sitio own-line (display `P[id1, id2]`); si mezcla `P` y `N` → dos bloques `\witness{P}{…}` / `\witness{N}{…}`; si arrastra `\cite` o `\code`, éstos quedan en prosa después del bloque. **Precondición:** `02` no define `\witness` (`grep '\newcommand{\witness}'` → vacío) — hay que portar el macro de 05 antes de la ola. Restricción: los `\cite` y los `\texttt{…py}` de esas líneas no entran en el argumento de ids (la gramática de `\tier` sólo admite ids internos).

### A5 — marcas BARE con `\texttt{archivo.py}` en prosa/fila (128 marcas: 51 `P`, 77 `N`)

Lista completa con estado del script (importado = `git ls-files hipotesis/pruebas/`; D7 = en `d7_pending_scripts.txt` o marcador `% pending(D7)` en la línea; test = nombre de test de la suite que contiene el stem del script):

| `archivo:línea` | clase | script(s) | importado | D7 | test en suite |
|---|---|---|---|---|---|
| `03:1421` | P | retro69.py, v27_reloj_ciclotomico.py | no | sí | no |
| `03:1425, 1427` | N | retro69.py, v27_reloj_ciclotomico.py | no | sí | no |
| `03:1503, 1504, 1505, 1508, 1509` | P×4, N×1 | retro119.py | no | sí | no |
| `03:1542`×2, `1545` | P×2, N×1 | retro94.py | no | sí | no |
| `03:1644` | P | retro78.py | no | sí | no |
| `03:1647` | N | retro78.py | no | sí | no |
| `03:1691, 1692, 1695` | P×2, N×1 | v28_hiperbola_reloj_tamano.py | no | sí | no |
| `03:2151, 2159, 2162` | N, P, N | kisin.py | **sí** | no | no |
| `03:2215…2521` (14 marcas: P×11, N×3) | P/N | oz_carried.py | no | sí | no |
| `03:3557, 3560` | P, N | retro109.py | no | sí | no |
| `03:3614, 3616, 3617` | P×2, N×1 | retro104.py | no | sí | no |
| `03:3663, 3664` | P, N | retro105.py | no | sí | no |
| `04:177` | N | chi5_zeros.py, retro105.py | no | sí | no |
| `04:381, 385` | P, N | verify_weil_chi5.py | no | sí | no |
| `04:429` | N | weil_window_chi5.py | no | sí | no |
| `04:457, 458, 460` | P, N, P | weil_window_rigorous_check.py | no | sí | no |
| `04:579, 583` | N×2 | cert.py | no | sí | no |
| `04:607` | N | weil_window_chi5.py, zeroside_check.py | no | sí | no |
| `04:874, 876` | N×2 | testB1b.py, testGeom.py | **sí** | no | no |
| `04:909, 912, 913, 914, 917` | N×3, P×2 | dh.py, mertens341.py, mobius.py | **sí** | no | no |
| `04:923, 925` | N×2 | dh_logderiv.py, retro99.py | no | sí | no |
| `04:941, 944, 945` | P×2, N×1 | blocks.py, fejer_check.py | **sí** | no | no |
| `04:965, 970, 973` | N×3 | balance.py, dedekind.py, fibres.py | **sí** | no | no |
| `04:979` | N | offline.py | **sí** | no | no |
| `04:1008` | N | castelnuovo.py | **sí** | no | **sí** (`test_castelnuovo_*` ×3) |
| `04:1029` | N | gram.py | **sí** | no | no |
| `04:1065` | N | bridge.py | **sí** | no | candidato débil (`*bridge*` ×3, ver B) |
| `04:1085, 1094`×2 | P×1, N×2 | retro101.py, retro93.py | no | sí | no |
| `04:1163`×2, `1167` | P×1, N×2 | field_signature.py | **sí** | no | no |
| `04:1179` | P | arch_window.py | **sí** | no | no |
| `04:1252` | N | corrected_operator.py | **sí** | no | **sí** (`test_corrected_operator_*` ×2) |
| `04:1311, 1314, 1318` | P×1, N×2 | escala_ceros_bajos.py (sí) + v12_pitagoras_raiz_X.py (no) | mixto | mixto | no |
| `04:1335` | N | v30_vertice_al_azar.py, v33_capas_1e9.py | no | sí | no |
| `04:1470, 1491, 1504` | P×2, N×1 | v33_capas_1e9.py | no | sí | no |
| `04:1519, 1526, 1527` | N×2, P×1 | retro66.py, retro67.py | no | sí | no |
| `04:1565, 1567, 1572` | P×2, N×1 | amplitud_clausula_ii.py | **sí** | no | no |
| `04:1648, 1651, 1655` | N×3 | law_resolution.py (sí) + classes_test.py (sí) + x_sweep.py (no) | mixto | mixto | **sí** (`test_law_resolution_*` ×2) |
| `04:1688` | N | t1_index.py, t2_loo.py | **sí** | no | no |
| `04:1713, 1732, 1736` | P×2, N×1 | retro81.py, retro87.py | no | sí | no |
| `04:1757, 1762` | N×2 | retro88.py, retro89.py | no | sí | no |
| `04:1800` | N | euler_link.py | **sí** | no | no |
| `04:1864` | N | zeroside.py | **sí** | no | no |
| `04:1870, 1872, 1890` | N×3 | circle_and_detect.py (+ sweep.py en 1870/1872) | **sí** | no | **sí** (`test_circle_and_detect_*` ×2) |
| `04:1880, 1883` | N×2 | orbita_cert.py (sí) + W3_orbita_lado_primos.py (no) | mixto | mixto | no |
| `04:1934` | N | retro102.py | no | sí | no |
| `appendix:51` | N | fermat_quintic_points.py | **sí** | no | no |
| `appendix:98, 260` | N×2 | weil_window_chi5.py | no | sí | no |
| `appendix:101` | N | envelope.py, tstar.py | no | sí | no |
| `appendix:132` | N | dh_logderiv.py, retro99.py | no | sí | no |
| `appendix:135` | P, N | retro105.py | no | sí | no |
| `appendix:183` | P, N | retro78.py | no | sí | no |
| `appendix:198, 200, 202, 206` | N×4 (y P×3 en 200/202/206) | oz_carried.py | no | sí | no |
| `appendix:277` | P, N | retro66.py, retro67.py | no | sí | no |

El caso citado en el encargo existe tal cual: `04-bridges.tex:458` = `… the numerical values of the potential \tier{N}` con `(\texttt{weil\_window\_rigorous\_check.py})` en `04-bridges.tex:459` y `% pending(D7)` en la misma línea — script **no portado**.

### A6 — otras formas (taxonomía completa desde el grep)

| forma | nº | display | ¿cumple la sintaxis única? |
|---|---:|---|---|
| `\LeanStar{X}` (estrella) | 221 | `[X]∗` | S3 — ver C |
| `\LeanCW{X}` (†, dev companion) | 44 (05:39, 03:3, 02:2) | `[X]†` | S3 — fuera del alfabeto `P/N`, declarado en contract §6.7 ("held") |
| `\LeanTally{X}` (°) | 21 (03:15, 02:5, 04:1) | `[X]°` | S3 — contract §6.7 ("held") |
| `\code{X}` | 18 (03:12, 04:6) | `X` en tt al tamaño de prosa | ✓ S2 conforme |
| `\leanline{…}` | 67 | `Lean: …` own-line | ✗ (A4) |
| `\testref{…}` | 6 | tt pequeño | ✓ (sólo dentro de A1) |
| tags dentro de tablas | 363 (P 330, N 33) | celda con `[P]`/`[N]` | ✗ — ver D |
| glosa de las clases | 2 (`01:104`, `01:255`) | `[N]` / `[P]` | exenta (define, no afirma) |
| `\witness{X}{ids}` | **0** | — | **ausente**: el macro de 05 no está portado (laguna) |
| `\tierP` / `\tierN` / `\tierW` legacy | 0 en el cuerpo (sólo `\definecolor{tierP…}` en el preamble) | — | ✓ |
| `% pending(D7)` como testigo | 68 líneas | no se imprime | señal de prosa, no tag |

Líneas con `\code` (todas): `03:369, 385, 2048, 2392, 2463, 2467, 2469, 2471, 2474, 2475, 2484`; `04:267, 276, 277, 278`.

---

## B. Diff numérico de todos los testigos `N` contra la suite

**129 marcas `N`** (123 desnudas + 6 con id). Censo final:

| veredicto | nº |
|---|---:|
| **ya conforme** (id citado existe en la suite) | **6** |
| **convertir a `\tier[\testref{id}]{N}`** (el test existe, sólo falta escribirlo) | **9** |
| **falta test** (el sitio queda sin `N` hasta que exista) | **69** |
| **script no portado** (prose `pending(D7)`, quitar `N`) | **43** |
| **glosa** (exenta: define la clase) | **2** |
| total | **129** |

### B1 — ya conforme (6)

`02:7` · `02:417` · `03:103` · `03:2151` · `03:2896` · `04:232` — los 7 ids resuelven a node-id real (`--collect-only`), coinciden con `PINNED_CITED_IDS` y son snake_case: los 4 tests de `tests/test_witness_census.py` pasan.

### B2 — convertir a `\tier[\testref{id}]{N}` (9)

| sitio | ancla hoy | id candidato (existe en suite) |
|---|---|---|
| `04:1008` | `(\texttt{castelnuovo.py} \tier{N})` | `test_castelnuovo_golden_values, test_castelnuovo_matches_manuscript_claim, test_castelnuovo_window_maxima` |
| `04:1065` | `(\texttt{bridge.py} \tier{N})` | candidato **débil**: `test_mersenne_bridge_*` / `test_regulator_form_of_bridge_equals_l_one_form` — coincidencia de stem, revisar a mano |
| `04:1252` | `(\texttt{corrected\_operator.py} \tier{N})` | `test_corrected_operator_golden_values, test_corrected_operator_matches_manuscript_claim` |
| `04:1648`, `04:1651`, `04:1655` | `(\texttt{law\_resolution.py} \tier{N})` (+ `classes_test.py`, `x_sweep.py` en prosa) | `test_law_resolution_golden_values, test_law_resolution_matches_manuscript_claim` |
| `04:1870`, `04:1872`, `04:1890` | `(\texttt{circle\_and\_detect.py} \tier{N})` (+ `sweep.py` en 1870/1872) | `test_circle_and_detect_golden_values, test_circle_and_detect_matches_manuscript_claim` |

Restricción de ejecución: cada id nuevo debe entrar en `PINNED_CITED_IDS` de `tests/test_witness_census.py` **en el mismo commit** (`test_cited_ids_match_the_pinned_set` falla en caso contrario). Los scripts acompañantes sin test (`classes_test.py`, `x_sweep.py`, `sweep.py`) quedan en prosa como `\code{…}`.

### B3 — script no portado: prose `pending(D7)`, quitar `N` (43)

Todos tienen el script en `d7_pending_scripts.txt` y el marcador `% pending(D7)` en la línea (salvo indicado). Ninguno tiene test en la suite (ningún test importa `hipotesis/pruebas/`).

`03`: 1425, 1427, 1508, 1545, 1647, 1695, 2232, 2256, 2290, 2521, 3560, 3617, 3664 (13)
`04`: 177, 385, 429, 458, 579, 583, 607, 923, 925, 1094 (×2 marcas), 1335, 1504, 1519, 1526, 1736, 1757, 1762, 1934 (19)
`appendix`: 98, 101, 132, 135, 183, 198, 200, 202, 206, 260, 277 (11)

Scripts implicados: `retro66/67/69/78/93/94/99/101/102/104/105/109/119`, `v12_pitagoras_raiz_X`, `v27_reloj_ciclotomico`, `v28_hiperbola_reloj_tamano`, `v30_vertice_al_azar`, `v33_capas_1e9`, `W3_orbita_lado_primos`, `cert`, `chi5_zeros`, `dh_logderiv`, `envelope`, `oz_carried`, `retro88/89`, `tstar`, `verify_weil_chi5`, `weil_window_chi5`, `weil_window_rigorous_check`, `x_sweep`, `zeroside_check`.

### B4 — falta test: script portado pero sin test de la suite (24)

`03:2162` (kisin.py) · `04`: 874, 876 (testB1b/testGeom), 909, 914, 917 (dh/mertens341/mobius), 941, 945 (blocks/fejer_check), 965, 970, 973 (balance/dedekind/fibres), 979 (offline), 1029 (gram), 1163, 1167 (field_signature), 1314, 1318 (escala_ceros_bajos + v12 pendiente), 1572 (amplitud_clausula_ii), 1688 (t1_index/t2_loo), 1800 (euler_link), 1864 (zeroside), 1880, 1883 (orbita_cert + W3 pendiente) · `appendix:51` (fermat_quintic_points).

→ veredicto por sitio: **falta test**; hasta que exista, el sitio queda **sin `N`** (o el `N` se retira y la claim queda sin marca, que es la asimetría declarada del contract).

### B5 — falta test: ancla que no es un test (37)

Los sitios citan ids **Lean** (`\LeanInline{…}`) o nombres `\texttt` que no son node-ids, o filas del ledger cuya columna `Declaration` sólo contiene nombres Lean/`.py`:

`03`: 1476, 1626, 3025, 3435, 3877 · `04`: 31, 35, 52, 65, 68, 107, 414, 1384, 1441 · `05`: 432, 435, 802, 1234 · `appendix`: 86, 89, 90, 96, 99, 105, 120, 122, 124, 126, 181, 227, 251, 253, 255, 269, 275, 279, 287.

Nota: `04:35` (`DoubleCount`, `invariant_two_on_measured_range`), `04:65` (`extended_window`) etc. son el patrón "id Lean delante de un `N`" — el id es de Lean, no de la suite; para `N` el id debe ser un `\testref`.

### B6 — sin ningún ancla (8)

`03:1068` (valores `1.236, 1.146 …`), `04:16`, `04:830` (celda de tabla `& \tier{N}; angles … \tier{P}`), `05:60`, `05:99`, `05:567` (fila de tabla), `05:595`, `05:701` → **falta test**.

### B7 — glosa (2)

`01:104`, `01:255`: definen `\tier{N}` como clase; exentas de la regla del testigo (el contract las exime: "defines, it does not asserts").

### Censo final N

- total sitios `N`: **129**
- con id-en-suite: **6** (conforme) + **9** candidatas a conversión (test existe)
- sin test: **69**
- no portados (D7): **43**
- glosa: **2**


### B8 — W6 Fase2: re-auditoría y veredicto de los 69 (2026-11-24, `cfae72c`)

Método: cada sitio de B3/B4/B5/B6 se re-localizó en el árbol por la cola de su
oración (los números de línea de este informe son de la ola previa), se le
exigió un respaldo de una de tres fuentes — un test de `tests/`, una salida
commitada en `hipotesis/pruebas/salidas/` (incluye el corpus D7 portado en
`a475748`), o ninguna — y se escribió el test sólo donde el respaldo existía.
De los 69 sitios: **49 siguen llevando la marca** y **20 la perdieron** con la
columna `Tier` (`cff8f95` y las reescrituras de tablas T5/T7).

**Veredicto de los 49 vivos — 25 `tested:`, 24 `no-test:`**

| grupo | sitio (línea de la ola → línea actual de `cfae72c`) | veredicto |
|---|---|---|
| B4 | `03-mechanisms.tex:2162` → `03-mechanisms:2117` | tested:`test_kisin_interpolation_is_pinned` |
| B4 | `04-bridges.tex:1029` → `04-bridges:1006` | tested:`test_intersection_form_signature_is_pinned` |
| B4 | `04-bridges.tex:1163` → `04-bridges:1133` | tested:`test_field_signature_is_pinned` |
| B4 | `04-bridges.tex:1167` → `04-bridges:1137` | tested:`test_field_signature_is_pinned` |
| B4 | `04-bridges.tex:1314` → `04-bridges:1284` | no-test:salida-no-portada (v12_pitagoras_raiz_X.py portado, sin salida en salidas/) |
| B4 | `04-bridges.tex:1318` → `04-bridges:1288` | tested:`test_residual_scales_are_pinned` |
| B4 | `04-bridges.tex:1572` → `04-bridges:1535` | tested:`test_residual_scales_are_pinned` |
| B4 | `04-bridges.tex:1688` → `04-bridges:1651` | tested:`test_angular_index_statistics_are_pinned` |
| B4 | `04-bridges.tex:1800` → `04-bridges:1763` | tested:`test_euler_link_second_term_is_pinned` |
| B4 | `04-bridges.tex:1864` → `04-bridges:1825` | tested:`test_zeroside_orbit_agrees_with_the_zeros` |
| B4 | `04-bridges.tex:1880` → `04-bridges:1841` | no-test:salida-no-portada (W3_orbita_lado_primos.py portado, sin salida en salidas/) |
| B4 | `04-bridges.tex:1883` → `04-bridges:1844` | no-test:scripts-no-portados (v09--v11 no estan en hipotesis/pruebas/) |
| B4 | `04-bridges.tex:874` → `04-bridges:851` | tested:`test_fluctuation_law_is_the_same_everywhere` |
| B4 | `04-bridges.tex:876` → `04-bridges:853` | tested:`test_fluctuation_law_is_the_same_everywhere` |
| B4 | `04-bridges.tex:909` → `04-bridges:886` | tested:`test_additive_side_statistics_are_pinned` |
| B4 | `04-bridges.tex:914` → `04-bridges:891` | tested:`test_additive_side_statistics_are_pinned` |
| B4 | `04-bridges.tex:917` → `04-bridges:894` | tested:`test_additive_side_statistics_are_pinned` |
| B4 | `04-bridges.tex:941` → `04-bridges:918` | tested:`test_fejer_window_is_pinned` |
| B4 | `04-bridges.tex:945` → `04-bridges:922` | tested:`test_fejer_window_is_pinned` |
| B4 | `04-bridges.tex:965` → `04-bridges:942` | tested:`test_orbit_balance_is_pinned` |
| B4 | `04-bridges.tex:970` → `04-bridges:947` | tested:`test_orbit_balance_is_pinned` |
| B4 | `04-bridges.tex:973` → `04-bridges:950` | tested:`test_orbit_balance_is_pinned` |
| B4 | `04-bridges.tex:979` → `04-bridges:956` | tested:`test_offline_minimum_stays_positive` |
| B5 | `03-mechanisms.tex:1476` → `03-mechanisms:1446` | no-test:cifra-solo-en-el-manuscrito (1,2,2,2) |
| B5 | `03-mechanisms.tex:1626` → `03-mechanisms:1593` | no-test:cifra-solo-en-el-manuscrito (555 primos) |
| B5 | `03-mechanisms.tex:3025` → `03-mechanisms:2978` | tested:`test_even_l_values_match_bernoulli_formula` |
| B5 | `03-mechanisms.tex:3435` → `03-mechanisms:3353` | no-test:sin-salida (T*(n) vs gamma_n) |
| B5 | `03-mechanisms.tex:3877` → `03-mechanisms:3755` | no-test:sin-salida (6.6484 / 4.8999; chi5_zeros.json es dato, no salida) |
| B5 | `04-bridges.tex:107` → `04-bridges:106` | no-test:cifra-solo-en-el-manuscrito (1.008 en q=5) |
| B5 | `04-bridges.tex:1384` → `04-bridges:1354` | no-test:scripts-no-portados (v20--v26 no estan en hipotesis/pruebas/) |
| B5 | `04-bridges.tex:1441` → `04-bridges:1410` | no-test:cifra-solo-en-el-manuscrito (nivel 80) |
| B5 | `04-bridges.tex:31` → `04-bridges:31` | no-test:cifra-solo-en-el-manuscrito (cut-offs 5.1614..6.7838) |
| B5 | `04-bridges.tex:35` → `04-bridges:35` | no-test:cifra-solo-en-el-manuscrito (33 ceros bajo 70) |
| B5 | `04-bridges.tex:414` → `04-bridges:407` | no-test:cifra-solo-en-el-manuscrito (0.63 a 1.3e-9) |
| B5 | `04-bridges.tex:52` → `04-bridges:52` | no-test:cifra-solo-en-el-manuscrito (3.5695e-4 / 3.472359e-7) |
| B5 | `04-bridges.tex:65` → `04-bridges:65` | no-test:cifra-solo-en-el-manuscrito (0.0443) |
| B5 | `04-bridges.tex:68` → `04-bridges:68` | no-test:cifra-solo-en-el-manuscrito (12 contra 13) |
| B5 | `05-categorical.tex:1234` → `05-categorical:1223` | no-test:sin-salida (valores del potencial, thm:first-window) |
| B5 | `05-categorical.tex:432` → `05-categorical:430` | no-test:sin-ancla-numerico (los ceros computados no muestran la clase) |
| B5 | `05-categorical.tex:435` → `05-categorical:433` | no-test:sin-ancla-numerico (hechos P y N sin cifras) |
| B5 | `05-categorical.tex:802` → `05-categorical:799` | no-test:sin-salida (medicion del sobre) |
| B5 | `appendix.tex:105` → `appendix:104` | no-test:sin-salida (inyectividad de la cadena) |
| B5 | `appendix.tex:96` → `appendix:95` | no-test:salida-no-portada (verify_weil_chi5.py portado, sin salida en salidas/) |
| B6 | `03-mechanisms.tex:1068` → `03-mechanisms:1051` | tested:`test_delta_p_tower_ratios_are_pinned` |
| B6 | `04-bridges.tex:16` → `04-bridges:16` | no-test:cifra-solo-en-el-manuscrito (7.3241 / 33 / 3.5695e-4) |
| B6 | `05-categorical.tex:595` → `05-categorical:593` | tested:`test_fermat_quintic_point_counts_are_pinned` |
| B6 | `05-categorical.tex:60` → `05-categorical:60` | tested:`test_fluctuation_law_is_the_same_everywhere` |
| B6 | `05-categorical.tex:701` → `05-categorical:698` | no-test:fuente-externa-citada (gonzalez26cw, 7.6) |
| B6 | `05-categorical.tex:99` → `05-categorical:99` | tested:`test_zero_side_correction_matches_the_manuscript` |

Los 15 tests nuevos viven en `tests/test_golden_n_marks.py`, agrupados en cinco
familias (una por commit): ley de la fluctuación, arco de positividad, forma de
campo y escalas residuales, estadísticas del cierre, mecanismos y capítulo 5.
Cada test fija los dígitos de la salida a `1e-12` y reconcilia la cifra impresa
del manuscrito con la línea `articulo:` de la propia salida (F10: nada se
recalcula). La suite pasó de 97 a **112 tests**; `tests/test_witness_census.py`
no cambió porque Fase2 no cita ningún id nuevo en el `\tex` — los sitios
quedan con su marca desnuda hasta la ola que los convierta en
`\tier[\testref{...}]{N}`.

**Los 20 que la perdieron (ya sin marca; no se tocan)**

- B4 `appendix.tex:51` → la marca ya no existe en `appendix:50`
- B5 `appendix.tex:86` → la marca ya no existe en `appendix:85`
- B5 `appendix.tex:89` → la marca ya no existe en `appendix:88`
- B5 `appendix.tex:90` → la marca ya no existe en `appendix:89`
- B5 `appendix.tex:99` → la marca ya no existe en `appendix:98`
- B5 `appendix.tex:120` → la marca ya no existe en `appendix:119`
- B5 `appendix.tex:122` → la marca ya no existe en `appendix:121`
- B5 `appendix.tex:124` → la marca ya no existe en `appendix:123`
- B5 `appendix.tex:126` → la marca ya no existe en `appendix:125`
- B5 `appendix.tex:181` → la marca ya no existe en `appendix:180`
- B5 `appendix.tex:227` → la marca ya no existe en `appendix:226`
- B5 `appendix.tex:251` → la marca ya no existe en `appendix:250`
- B5 `appendix.tex:253` → la marca ya no existe en `appendix:252`
- B5 `appendix.tex:255` → la marca ya no existe en `appendix:254`
- B5 `appendix.tex:269` → la marca ya no existe en `appendix:268`
- B5 `appendix.tex:275` → la marca ya no existe en `appendix:274`
- B5 `appendix.tex:279` → la marca ya no existe en `appendix:278`
- B5 `appendix.tex:287` → la marca ya no existe en `appendix:286`
- B6 `04-bridges.tex:830` → la marca ya no existe en `04-bridges:376`
- B6 `05-categorical.tex:567` → la marca ya no existe en `05-categorical:565`

**Residuo `no-test:` por motivo (24)**

- `salida-no-portada` (3): `04:1284` (v12_pitagoras_raiz_X.py), `04:1841`
  (W3_orbita_lado_primos.py), `appendix:95` (verify_weil_chi5.py) — scripts
  portados en `a475748` sin salida commitada en `salidas/`.
- `scripts-no-portados` (2): `04:1844` (v09–v11), `04:1354` (v20–v26).
- `cifra-solo-en-el-manuscrito` (11): `03:1446`, `03:1593`, `04:16`, `04:31`,
  `04:35`, `04:52`, `04:65`, `04:68`, `04:106`, `04:407`, `04:1410` — la cifra
  no aparece en ningún test ni en ninguna salida, sólo en el `tex`.
- `sin-salida` (5): `03:3353`, `03:3755`, `05:799`, `05:1223`, `appendix:104`.
- `sin-ancla-numerico` (2): `05:430`, `05:433`.
- `fuente-externa-citada` (1): `05:698` (el factor 7.6 es de `gonzalez26cw`,
  ya citado en la frase).

**Re-auditoría de B4/B5/B6 contra el árbol de `cfae72c`**

- B4 (24): 20 `tested:` + 3 `no-test:`; 1 (`appendix:51`) ya no tiene marca.
- B5 (37): 1 `tested:` con un test que ya existía (`03:3025`→`2978`,
  `test_even_l_values_match_bernoulli_formula`), 16 `no-test:`, 20 sin marca
  (17 filas de la tabla-ledger + 3 reescritas).
- B6 (8): 4 `tested:` (`03:1051`, `05:60`, `05:99`, `05:593`), 2 `no-test:`,
  2 sin marca (`04:830`, `05:567`).

---

## C. Censo de estrellas (`\LeanStar`)

**Base de compilación:** `lake build` verde con **18248 jobs** (exit 0, re-ejecutado el 2026-11-24) y `docs/counts.md` → `lean.sorry = 0`, `lean.axioms = 0` sobre `lean/F1_pentagonal_descent_UNIFIED.lean` (5712 teoremas). Un nombre que existe en ese archivo y entra en ese build está compilado y aprobado.

| magnitud | valor |
|---|---:|
| usos de `\LeanStar` | **221** |
| líneas distintas | 173 |
| nombres distintos | **194** |
| existentes en `lean/F1_pentagonal_descent_UNIFIED.lean` | **194/194** (100 %) |
| **REMOVABLE** | **221 (100 %)** |
| NOT-REMOVABLE | **0** |

Comprobación: cada nombre se busca en el archivo Lean tras normalizar `\_`→`_` y `\ensuremath{X}`→letra griega (`Z\ensuremath{\varphi}`→`Zφ`, `\ensuremath{\omega}\_sq`→`ω_sq`, `f\ensuremath{\varphi}\_map…`→`fφ_map…`, `\ensuremath{\psi}\_of\_split`→`ψ_of_split` — los 4 "fallos" iniciales existen con la forma unicode). Los 4 nombres con `\ensuremath` dentro del argumento están en `03:157` (×2), `03:166`, `03:1116`.

Usos por archivo: `03-mechanisms` 136 · `04-bridges` 59 · `appendix` 19 · `05-categorical` 7.

Líneas con estrella:

- `03-mechanisms.tex` (104 líneas): 63, 64, 94, 95, 96, 97, 157, 166, 288, 297, 298, 313, 498, 619, 803, 1034, 1035, 1116, 1147, 1169, 1323, 1344, 1411–1420, 1474, 1580, 1581, 1616–1619, 1621, 1682–1690, 1721, 1725, 1732, 1753, 1835, 1852, 1969, 2088, 2106, 2154–2158, 2172, 2173, 2175, 2214, 2215, 2447, 2739, 2803, 3016, 3017, 3018, 3022, 3023, 3251–3254, 3256, 3257, 3319–3321, 3340, 3417, 3424, 3690, 3734, 3735, 3791, 4168, 4204, 4280, 4308, 4309, 4517, 4556
- `04-bridges.tex` (54 líneas): 382, 455, 456, 655, 669, 916, 986, 1032, 1058, 1059, 1109, 1117, 1118, 1132, 1138, 1169, 1170, 1194, 1307–1310, 1312, 1364–1368, 1424, 1425, 1428, 1429, 1432, 1435, 1439, 1442, 1443, 1445, 1451, 1456, 1461, 1462, 1469, 1484, 1489, 1490, 1496, 1563, 1564, 1614, 1832, 1833, 1946, 1947
- `05-categorical.tex` (7): 332, 802, 899, 900, 931, 968, 1101
- `appendix.tex` (13): 357, 358, 406–411, 419–422, 430

**Veredicto de la regla ("revisó, compiló, pasó → se quita el asterisco"):** los 221 son **REMOVABLE**; **0 NOT-REMOVABLE**. Ningún nombre está ausente del corpus compilado y el build está verde con `sorry = 0`.

**Tracking post-remoción (laguna):** el censo de estrellas **no** vive en un contador automático. `scripts/tasks/counts.ts` sólo mide `pytest.*`, `lean.theorems/axioms/sorry`, `images.files` (verificado: no hay contador `\LeanStar` ni `\tier`); `tests/test_witness_census.py` sólo parsea `\testref`; la cifra 221 está sólo en el snapshot fechado `docs/reports/20261123_MRG-001_f1_v168_merge_closure.md`. Después de la remoción, el seguimiento quedará huérfano salvo que se añada un contador a `counts.ts` (o una aserción "cero estrellas" al estilo del gate de release).

**W6 Fase2 (2026-11-24) — relación con §B:** la fase no toca ninguna
estrella; el censo de arriba sigue midido sobre el mismo árbol (221 usos,
194 nombres, 0 not-removable). Lo que cambió en esta pasada es sólo el lado
`N` de §B: 15 tests nuevos (`tests/test_golden_n_marks.py`), 49 sitios
vivos con veredicto `tested:`/`no-test:` (tabla B8) y la suite en 112 tests.

---

## D. Tablas con columna `Tier` (ruling: no caben en un documento formal)

Inventario completo de tablas del manuscrito: 18 entornos `tabular/longtable`; **7 llevan tag o columna de estatus con tags**.

| # | sitio | cabecera | columnas | filas | filas con tag | formas de celda |
|---|---|---|---|---:|---:|---|
| T1 | `appendix.tex:18-299` (cabecera `:19`) | `Claim & Tier & Declaration & Note` | 4 | **252** | 245 | tag sólo (205) · tag+palabra (38) · sólo palabra `classical/open` (7) · vacía (2) |
| T2 | `04-bridges.tex:651-663` (cabecera `:652`) | `Form of the step & Equivalence & Condition & Tier` | 4 | 10 | 10 | tag sólo (`\tier{P}` ×10) |
| T3 | `03-mechanisms.tex:4202-4212` (cabecera `:4203`) | `# & Link & Content & Tier` | 4 | 8 | 8 | tag sólo |
| T4 | `03-mechanisms.tex:3730-3739` (cabecera `:3731`) | `Input & Lean & Tier` | 3 | 7 | 6 | tag sólo ×6; 1 fila con palabra (`classical; not proved in Lean & classical`) |
| T5 | `05-categorical.tex:559-571` (cabecera `:561`) | `Clause & Already proved… & Open & Refuted if` | 4 | 8 | 7 | tags **dentro de la celda de prosa** (no hay columna Tier; los tags están embebidos: `\cref{…} \tier{P}`) |
| T6 | `05-categorical.tex:389-401` (cabecera `:391`) | `Input of \cite{gonzalez25hp} & Status here & Where` | 3 | 8 | 4 | palabra + tag (`discharged \tier{P}`, `theorems \tier{P}`) — columna "Status" |
| T7 | `04-bridges.tex:821-834` (cabecera `:822`) | `step & here & status` | 3 | 4 | 4 | tag sólo (`\tier{P}, \tier{P}`) — columna "status" |

Muestras de 2 filas:

- **T1** `appendix:51` → `Point counts of the Fermat quintic equal … & \tier{N} & \texttt{fermat\_quintic\_points.py} & \cref{rmk:fermat-model}` · `appendix:96` → `Explicit formula for L(s,χ₅) & classical; coefficients \tier{P} & \texttt{F1WeilFunctional.…} & Checked numerically to 10⁻¹⁸ with 40 zeros \tier{N}`
- **T2** `04:653` → `The real part of each zero is a spectral position of Ω_H … & \LeanInline{GDS\_iff\_E}, \LeanInline{landing\_iff\_E} & none & \tier{P}` · `04:662` → `The primes act by powers on the zero coordinates & \LeanInline{B\_iff\_E\_one\_hypothesis} & height of the first zero & \tier{P}`
- **T3** `03:4204` → `1 & \LeanStar{F1CW.tower\_ham\_is\_hermitian} Hermitian & real diagonal … (\LeanInline{towerH}) & \tier{P}` · `03:4211` → `8 & closure & t=2⇔r=1⇔Reρ=½ & \tier{P}`
- **T4** `03:3732` → `Functional equation of Λ(s,χ₅) & \LeanInline{functionalEquation\_chi5\_discharged} & \tier{P}` · `03:3738` → `First zero at γ≈6.6485 (\LeanInline{NoLowZeros}) & classical; not proved in Lean & classical`
- **T7** `04:823` → `W1 & Frob_p on Z[φ], Euler factor = characteristic polynomial… & \tier{P}, \tier{P}` · `04:833` → `W5 & bounded orbit ⇒ no zero off the line & \tier{P}`

**Plan por tabla (para la ola siguiente; NO ejecutar):**

- **T1 (ledger, 252 filas)** — eliminar la columna `Tier`. La información del tag se **duplica** con la columna `Declaration` (que ya lista los ids `\texttt`): la forma conforme es mover el tag a la celda Claim como `\tier[\testref{id}]{N}` / `\tier[ids]{P}` cuando el id exista. **Se pierde** la clase visual por fila (P/N/`classical`/`open`) y las 7 filas cuyo estatus es sólo palabra (`open`, `classical`) — éstas deben reescribirse como prosa ("classical", "open") según contract §6.7 (no `[o]` label). Es la fila más cara: 245 marcas.
- **T2 (10 filas)** — eliminar `Tier`; los ids ya están en la columna `Equivalence` → `\tier[ids]{P}` en la celda Claim; **no se pierde nada** (la clase está implícita en el id Lean).
- **T3 (8 filas)** — igual que T2; cuidado: una fila lleva `\LeanStar` (remover por C antes de reescribir).
- **T4 (7 filas)** — eliminar `Tier`; la fila 7 (`classical`) pierde la palabra duplicada de la columna Lean → dejar "classical" en prosa.
- **T5 (8 filas, tags embebidos)** — no hay columna; los tags viven en la celda "Already proved". Decidir si la tabla conserva tags inline (fuera del ruling de columna) o se mueve la clase a una sola columna `Evidence`. **Se pierde** si se elimina: la distinción entre "probado con `P`" y "abierto" de las columnas Open/Refuted.
- **T6 (8 filas, columna `Status here`)** — mezcla palabra + tag (`discharged \tier{P}`). Plan: una columna `Evidence` sólo con el tag, la palabra a prosa.
- **T7 (4 filas, columna `status`)** — eliminar; la celda `here` ya contiene el contenido → tag inline con ids.

Coste agregado: **363 marcas viven dentro de tablas** (330 `P`, 33 `N`); sólo T1 concentra 245.

---

## E. Prosa con la palabra "tier" (13 sitios de capítulo + 3 de `main.tex`)

Grep `(?<![\\a-zA-Z])[Tt]iers?(?![a-zA-Z])` sobre los 10 fuentes: 16 apariciones.

| sitio | antes (tex) | después propuesto |
|---|---|---|
| `01-introduction.tex:268` | "the corpus, with its **tier** and its declaration, is listed in `\cref{app:ledger}`" | "…with its **evidence tag** and its declaration…" |
| `03-mechanisms.tex:142` | "why the **tiers** of `\cref{ssec:protocol}` can be assigned" | "why the **evidence marks** of `\cref{ssec:protocol}` can be assigned" |
| `04-bridges.tex:14` | "The **tiers** are…" (tras la cota numérica) | "The **evidence marks** are…" |
| `04-bridges.tex:643` | "Every step above is proved or carries its **tier**." | "Every step above is proved or carries its **witness mark**." |
| `04-bridges.tex:1916` | "(iii) with the **tiers** of the window theorems, `\tier{P}` with declared inputs" | "(iii) with the **witness marks** of the window theorems, …" |
| `05-categorical.tex:1230` | "instantiated; the rest carry their **tier**." | "…the rest carry their **evidence tag**." |
| `appendix.tex:7` | "The table lists every claim … with its **tier**, the declaration…" | "…with its **evidence tag**, the declaration…" |
| `appendix.tex:11` | "**Tiers** are those of `\cref{ssec:protocol}`. The entries of the compiled modules are `\tier{P}`…" | "**Tags** are those of `\cref{ssec:protocol}`…" |
| `appendix.tex:136` | "Statements of the body not listed above, with the **tiers** and the declarations the body gives" | "…with the **evidence tags** and the declarations…" |
| `03:3731` (cabecera T4) | `Input & Lean & Tier` | `Input & Lean & Evidence` (o columna eliminada, ver D) |
| `03:4203` (cabecera T3) | `# & Link & Content & Tier` | `# & Link & Content` (columna eliminada) |
| `04:652` (cabecera T2) | `Form of the step & Equivalence & Condition & Tier` | `… & Condition` (columna eliminada) |
| `appendix:19` (cabecera T1) | `Claim & Tier & Declaration & Note` | `Claim & Declaration & Note` (columna eliminada) |
| `main.tex:183, 195` | `\PackageError{tier}{…}` (texto interno del macro) | no tocar: es el nombre del macro, no prosa |
| `main.tex:252` | comentario `% … not a tier --` | comentario de origen; bajo prioridad, puede quedarse |

Los usos como nombre de macro (`\tier`, `\tiercol`, `\definecolor{tierP}`) quedan fuera: 2135 apariciones de `\tier` en el árbol son en su mayoría `docs/reports/` (informes fechados, no se editan).

---

## Lagunas y notas

1. **`\witness` no existe en 02** — la forma own-line canónica de 05 (`\witness{P}{id1, id2}`) no está portada; la conversión de los 67 `\leanline` exige portarla antes (preamble de 05-kkgt).
2. **Ningún `\tier[ids]{P}`** — los 6 ids sólo cubren `N`; los 740 `P` están todos con el id fuera del tag o sin id.
3. **Contrato de id**: toda id nueva citada debe entrar en `PINNED_CITED_IDS` (`tests/test_witness_census.py`) en el mismo commit.
4. **No hay contador automático de estrellas ni de marcas** en `counts.ts`; el censo 221 sólo vive en un informe fechado (ver C).
5. **Ningún test importa `hipotesis/pruebas/`**: la equivalencia script→test sólo puede fijarse por nombre (5 stems coinciden) — `bridge.py` es coincidencia débil y requiere revisión manual.
6. **`x_sweep.py`** sigue en la lista D7 pese a que `sweep.py` está portado (04:1651 los nombra juntos) — posible desfase entre la lista D7 y el marcador de línea.
7. El fichero D7 referenciado por los informes (`scratch/f1_v168/d7_pending_scripts.txt`) **no está en el repo**; está en el scratch del perfil (`/home/aficio/.hermes/profiles/academic/cache/scratch/f1_v168/`).
8. Los números de línea se han medido sobre el árbol limpio de hoy; el contract aconseja identificar los sitios por la cola de la oración, no sólo por la línea.

### Artefactos generados (scratch, no en el repo)

`node_ids.txt` · `tier_marks.json` (869 marcas) · `macros.json` · `N_verdicts.json` (129 veredictos) · `N_ctx.json` · `A5.json` (128 sitios con `.py`) · `stars.json` (221) · `star_names.txt` (194) · `leaninline_untagged.json` (31) · `tables.json` (18 tablas) · `py_tier_lines.json` · `bare_N_sites.txt`.
