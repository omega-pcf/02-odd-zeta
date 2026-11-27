# SCRIPTS-RECON-003 — inventario de numerical scripts contra las entregas del autor

| Field | Value |
|---|---|
| **id** | `SCRIPTS-RECON-003` |
| **title** | Inventory of the numerical scripts against the author's two deliveries (v168) |
| **status** | report only — read-only reconciliation of `hipotesis/pruebas/` against zip1/zip2 and the manuscript |
| **date** | 2026-11-26 |
| **version** | 1.0 |

Fecha: 2026-11-26 · modo: **solo lectura** (ningún commit, ningún build, ningún `lake build`).
Fuentes: zip1 `F1_v168_completo.zip` extraído en `scratch/f1_v168/F1_v168_completo/` (con `MANIFEST.md`),
zip2 `~/Downloads/F1_v168_scripts_faltantes.zip` extraído en `scratch/f1_v168/scripts_faltantes/`,
repo `/mnt/media/dev/02-odd-zeta` (`hipotesis/pruebas/`, `src/chapters/*.tex`, `main.tex`, `docs/`),
y el censo de nombres del manuscrito `docs/reports/20261122_F9-001_provenance_inventory.md` (Apéndice A: 160 filas / 85 nombres distintos).

Criterios medidos:

* **entregado** = el nombre de archivo está en el zip del autor (rastro real en disco, no el MANIFEST);
* **portado** = existe en el árbol del repo;
* **referenciado** = aparece en `main.tex` + `src/chapters/*.tex` (con `\_` → `_` normalizado; la detección
  por subcadena literal falla justo en los sitios donde LaTeX escapa el guion bajo, p. ej.
  `\code{weil\_window\_chi5.py}`);
* **con salida** = hay un artefacto de salida comprometido en el repo (`hipotesis/pruebas/salidas/<nombre>.txt`
  o el fichero de salida entregado por zip1).

## (a) Inventario

### A1. Qué trajo cada entrega

| entrega | archivos | `.py` | no-`.py` |
|---|---:|---:|---:|
| **zip1** `F1_v168_completo` | 78 | 46 | 32 (artículo `.tex/.pdf/.bbl/.bib` + `MANIFEST.md` = 5, `lean/F1_pentagonal_descent_UNIFIED.lean` = 1, datos/salidas = 26) |
| **zip2** `F1_v168_scripts_faltantes` | 80 | 38 | 42 (`salidas/*.txt` 35, `datos/*.json` 2, `chi5_zeros_500.json`, `zeta_zeros_3000.npy`, `correr_todo.sh`, `LEEME.txt`, `LEDGER_ESTADO.md`) |
| **unión zip1 ∪ zip2** | — | **83** (solapamiento: `comun.py`) | — |
| **repo `hipotesis/pruebas/`** | 171 (incl. `__pycache__`) | **83** | — |

**Cobertura del `.py`: 83 de 83 = 100 %.** `repo_py − (zip1 ∪ zip2) = ∅` y `(zip1 ∪ zip2) − repo_py = ∅`.
Los 42 de la lista D7 (`scratch/f1_v168/d7_pending_scripts.txt`, balance 2026-11-24: *STILL PENDING (0)*)
están todos en el repo; el import fue `a475748` (56 ficheros: 40 scripts + `retro83/retro86/lp/opcert/verify_cert` + datos + salidas de certificados).

### A2. Tabla por script (83 filas)

| # | script | entregado en | portado en `hipotesis/pruebas/` | referenciado en el manuscrito (capítulo) | salida comprometida |
|--:|---|---|---|---|---|
| 1 | `W3_orbita_lado_primos.py` | zip1 | sí | 04 | — |
| 2 | `amplitud_clausula_ii.py` | zip2 | sí | 04 | salidas/amplitud_clausula_ii.txt |
| 3 | `arch_window.py` | zip2 | sí | 04, app | salidas/arch_window.txt |
| 4 | `balance.py` | zip2 | sí | 04, app | salidas/balance.txt |
| 5 | `blocks.py` | zip2 | sí | 04, 05, app | salidas/blocks.txt |
| 6 | `bridge.py` | zip2 | sí | 01, 02, 03, 04, 05, app | salidas/bridge.txt |
| 7 | `castelnuovo.py` | zip2 | sí | 04, app | salidas/castelnuovo.txt |
| 8 | `ceros_chi5_500.py` | zip2 | sí | — | — |
| 9 | `cert.py` | zip1 | sí | 04, app | weil_certificates/cert_L0.95.json · cert_L1.0.json |
| 10 | `chi5_zeros.py` | zip1 | sí | 04, app | chi5_zeros.json · chi5_zeros_T80.txt |
| 11 | `circle_and_detect.py` | zip2 | sí | 04, app | salidas/circle_and_detect.txt |
| 12 | `classes_test.py` | zip2 | sí | 04, app | salidas/classes_test.txt |
| 13 | `comun.py` | zip1+zip2 | sí | — | — |
| 14 | `comun_pruebas.py` | zip2 | sí | — | — |
| 15 | `corrected_operator.py` | zip2 | sí | 04, app | salidas/corrected_operator.txt |
| 16 | `cuintica.py` | zip2 | sí | — | — |
| 17 | `dedekind.py` | zip2 | sí | 01, 03, 04, 05, app | salidas/dedekind.txt |
| 18 | `dh.py` | zip2 | sí | 04, app | salidas/dh.txt |
| 19 | `dh_logderiv.py` | zip1 | sí | 04, app | — |
| 20 | `dh_zeros.py` | zip1 | sí | app | dh_zeros.json |
| 21 | `envelope.py` | zip1 | sí | 01, 03, 04, 05, 06, app | — |
| 22 | `escala_ceros_bajos.py` | zip2 | sí | 04 | salidas/escala_ceros_bajos.txt |
| 23 | `euler_link.py` | zip2 | sí | 04, app | salidas/euler_link.txt |
| 24 | `fejer_check.py` | zip2 | sí | 04, app | salidas/fejer_check.txt |
| 25 | `fermat_quintic_points.py` | zip2 | sí | app | salidas/fermat_quintic_points.txt |
| 26 | `fibres.py` | zip2 | sí | 01, 03, 04, 05, app | salidas/fibres.txt |
| 27 | `field_signature.py` | zip2 | sí | 04, app | salidas/field_signature.txt |
| 28 | `gram.py` | zip2 | sí | 04, app | salidas/gram.txt |
| 29 | `kisin.py` | zip2 | sí | 03 | salidas/kisin.txt |
| 30 | `law_resolution.py` | zip2 | sí | 04, app | salidas/law_resolution.txt |
| 31 | `lp.py` | zip1 | sí | 04 | — |
| 32 | `mertens341.py` | zip2 | sí | 04, app | salidas/mertens341.txt |
| 33 | `mobius.py` | zip2 | sí | 04, app | salidas/mobius.txt |
| 34 | `offline.py` | zip2 | sí | 04, app | salidas/offline.txt |
| 35 | `op_rig_validated.py` | zip1 | sí | 04, app | weil_certificates/op_rig_validated_output.json |
| 36 | `opcert.py` | zip1 | sí | — | — |
| 37 | `opcert_rig.py` | zip1 | sí | app | — |
| 38 | `orbita_cert.py` | zip2 | sí | 04, app | salidas/orbita_cert.txt |
| 39 | `oz_carried.py` | zip1 | sí | 03, app | — |
| 40 | `retro101.py` | zip1 | sí | 04, app | — |
| 41 | `retro102.py` | zip1 | sí | 04, app | — |
| 42 | `retro104.py` | zip1 | sí | 03, app | — |
| 43 | `retro105.py` | zip1 | sí | 03, 04, app | — |
| 44 | `retro109.py` | zip1 | sí | 03 | — |
| 45 | `retro119.py` | zip1 | sí | 03, app | — |
| 46 | `retro66.py` | zip1 | sí | 04, app | — |
| 47 | `retro67.py` | zip1 | sí | 04, app | — |
| 48 | `retro69.py` | zip1 | sí | 03 | — |
| 49 | `retro78.py` | zip1 | sí | 03, app | — |
| 50 | `retro81.py` | zip1 | sí | 04 | — |
| 51 | `retro83.py` | zip1 | sí | — | — |
| 52 | `retro86.py` | zip1 | sí | — | — |
| 53 | `retro87.py` | zip1 | sí | 04 | — |
| 54 | `retro88.py` | zip1 | sí | 04 | — |
| 55 | `retro89.py` | zip1 | sí | 04 | — |
| 56 | `retro93.py` | zip1 | sí | 04, app | — |
| 57 | `retro94.py` | zip1 | sí | 03, app | — |
| 58 | `retro99.py` | zip1 | sí | 04, app | — |
| 59 | `rho_interval.py` | zip2 | sí | 04, app | salidas/rho_interval.txt |
| 60 | `rigW.py` | zip1 | sí | 04, app | — |
| 61 | `rigorous_chain.py` | zip2 | sí | 04, app | salidas/rigorous_chain.txt |
| 62 | `sweep.py` | zip2 | sí | 04, app | salidas/sweep.txt |
| 63 | `t1_index.py` | zip2 | sí | 04, app | salidas/t1_index.txt |
| 64 | `t2_loo.py` | zip2 | sí | 04, app | salidas/t2_loo.txt |
| 65 | `teich.py` | zip2 | sí | app | salidas/teich.txt |
| 66 | `testB1b.py` | zip2 | sí | 04, app | salidas/testB1b.txt |
| 67 | `testGeom.py` | zip2 | sí | 04, app | salidas/testGeom.txt |
| 68 | `tstar.py` | zip1 | sí | 03, app | — |
| 69 | `v12_pitagoras_raiz_X.py` | zip1 | sí | 04 | — |
| 70 | `v27_reloj_ciclotomico.py` | zip1 | sí | 03 | — |
| 71 | `v28_hiperbola_reloj_tamano.py` | zip1 | sí | 03 | — |
| 72 | `v30_vertice_al_azar.py` | zip1 | sí | 04 | — |
| 73 | `v33_capas_1e9.py` | zip1 | sí | 04 | — |
| 74 | `verify_cert.py` | zip1 | sí | — | — |
| 75 | `verify_iv.py` | zip1 | sí | 04, app | weil_certificates/verify_iv_L1.0_output.txt |
| 76 | `verify_rig.py` | zip1 | sí | 04 | — |
| 77 | `verify_weil_chi5.py` | zip1 | sí | 04, app | — |
| 78 | `w4exact.py` | zip2 | sí | app | salidas/w4exact.txt |
| 79 | `weil_window_chi5.py` | zip1 | sí | 04, app | — |
| 80 | `weil_window_rigorous_check.py` | zip1 | sí | 04, app | — |
| 81 | `x_sweep.py` | zip1 | sí | 04, app | — |
| 82 | `zeroside.py` | zip2 | sí | 04, app | salidas/zeroside.txt |
| 83 | `zeroside_check.py` | zip1 | sí | 04, app | — |

Leyenda de la columna *entregado en*: `zip1` = `F1_v168_completo`, `zip2` = `F1_v168_scripts_faltantes`,
`zip1+zip2` = en ambos (solo `comun.py`).

### A3. Artefactos no-`.py` de zip1 (32) — estado

| estado | n | detalle |
|---|---:|---|
| no aplica (artículo/meta) | 5 | `F1_v168.tex`, `.pdf`, `.bbl`, `references_v168.bib`, `MANIFEST.md` |
| portado | 1 | `lean/F1_pentagonal_descent_UNIFIED.lean` → `lean/` (compilado en el build) |
| portado (datos) | 14 | `chi5_zeros.json`, `chi5_zeros_T80.txt`, `dh_zeros.json`, `zeta_zeros_3000.npy`, `datos/{capas,familias}_hasta_1e9.json`, `datos/ceros_nivel{80,135}.json`, `datos/ordenes_1000000.pkl`, `datos/torcidos135.json`, `weil_certificates/{cert_L0.95,cert_L1.0}.json`, `weil_certificates/op_rig_validated_output.json`, `weil_certificates/verify_iv_L1.0_output.txt` |
| **no portado — citado** | **2** | `datos/CW_EQUIVALENCIAS.md` (`appendix.tex:461`, `% pending(D7)`), `datos/fqn_map.json` (`appendix.tex:730`, `% pending(D7)`) |
| no portado — dependencia no citada | 10 | `datos/{ceros_zeta,ordenes_600000,ordenes_1400000}.json/.pkl`, `datos/registro_{unificado,unificado_historicos,verificar_todo}.txt`, `datos/v{17,18,19,32}.log` |

Los 10 de la última fila **no los lee ningún `.py` del repo** (`grep -F` sobre `hipotesis/pruebas/*.py`: 0 hits)
son dependencias declaradas en el MANIFEST de fichas muertas para el estado actual: su omisión no rompe nada,
pero el MANIFEST del zip ya no describe el repo.

zip2: los 38 `.py` y los 35 `salidas/*.txt` están **íntegros** en el repo (mismos nombres; `salidas/_registro.txt`
incluido, es el índice del conjunto, no la salida de un script).

### A4. Cruce final (las cuatro columnas pedidas)

| clase | n | quién |
|---|---:|---|
| entregado + portado + referenciado + con salida | 39 | ver columna *salida* ≠ `—` |
| entregado + portado + referenciado + **sin salida** | 36 | todos los `retro*`, `v*_*`, `weil_*`, `cert/verify_*`, `envelope/tstar/x_sweep/oz_carried/…` |
| entregado + portado + **sin referencia** (huérfanos) | 8 | ver abajo |
| **referenciado + sin portar** | **3** (0 si nos limitamos a `.py`) | ver abajo |

**Referenciados-sin-portar — verificación del "D7 = 0":**

* Sobre `.py`: **0**. Los 75 `.py` citados en el manuscrito están todos en el repo.
* Sobre cualquier nombre de archivo: **3**, y coinciden exactamente con los 3 marcadores
  `pending(D7)` que mide `docs/witness-inventory.md:45` (gate: **3**):

  1. `CW_EQUIVALENCIAS.md` — `src/chapters/appendix.tex:461` — entregado en zip1 (`datos/`), **no portado**;
  2. `fqn_map.json` — `src/chapters/appendix.tex:730` — entregado en zip1 (`datos/`), **no portado**;
  3. `unfold_by_conductor.txt` — `src/chapters/04-bridges.tex:107` — **nunca entregado** en ninguno de los dos zips
     (tampoco figura en la lista "citados y no disponibles" del MANIFEST: ahí hay 36 entradas y esta no es una).

  Además, `tests/verify_odd_zeta_pcf_unified.py` (fila del censo F9) ya **no se cita** en el manuscrito:
  F10 lo sustituyó por la suite `pytest` — no es hueco.

**Huérfanos (portados, sin referencia en el manuscrito) — 8:**

* dependencias declaradas en el MANIFEST "no citadas por nombre" (5): `comun.py`, `opcert.py`, `retro83.py`,
  `retro86.py`, `verify_cert.py` → **no son hueco**, son el andamiajo de los demás;
* **huérfanos de verdad (3)**: `ceros_chi5_500.py`, `comun_pruebas.py`, `cuintica.py` — los tres vienen de zip2
  (el pase F12 del autor), los tres con salida propia ausente y ninguno citado en ninguna parte del `.tex`.
  Opción de cierre: citarlos donde se usan o retirarlos; hoy pesan en el inventario sin aportar al texto.

**Notas pedidas:**

* **`retro65.py` — ausente en todas partes.** `hipotesis/pruebas/retro66.py:99-101` hace
  `exec(compile(open(__file__.replace("retro66.py","retro65.py")).read(), …))`; `retro65.py` no está en zip1,
  ni en zip2, ni en el repo, ni en la lista "no disponibles" del MANIFEST. **`retro66.py` no es ejecutable tal
  como está.** Hay que pedir el fichero al autor o declararlo no disponible en el texto.
* **`zeros.txt` vs `chi5_zeros_T80.txt` — no es un typo, es un nombre que no coincide con quien lo lee.**
  `envelope.py:3` y `weil_certificates/zeroside_check.py:5` abren `'zeros.txt'`; ese fichero no existe en el repo
  ni en ningún zip. El MANIFEST lo dice explícitamente (*"`envelope.py` lee `zeros.txt`; los ceros de $L(s,\chi_5)$
  hasta $T=80$ están en `chi5_zeros_T80.txt"`*): hay que renombrar/linkear, no hay conflicto de contenido.
  Ningún `.py` del repo referencia `chi5_zeros_T80.txt` por nombre.
* **`fqn_map.json` vs `fnq_map.json` — no hay typo.** `fnq_map` no aparece en ningún sitio del repo
  (0 hits); `fqn_map` aparece 2 veces: `appendix.tex:730` y `docs/reports/20261122_F9-001…md`. La grafía del
  MANIFEST del zip (`datos/fqn_map.json`) y la del manuscrito coinciden. Lo que falta es el **fichero**, no el nombre.
* `hipotesis/pruebas/` y `weil_certificates/` son directorios, no ficheros: F9-001 los marcaba como
  "2 nombres no resolubles"; hoy sí resuelven en el árbol.


## (b) ¿Está vigente la sección de scripts numéricos del apéndice?

**Localización.** `src/chapters/appendix.tex:567-581`, `\subsection{Numerical scripts}`, dentro de
`\section{Lean formalization audit}\label{app:lean}` (línea 407). Es un único párrafo, sin frase introductoria
que declare su alcance, y se apoya en `\cref{sec:results-verdict}` (existe: 2 hits del label).

**Texto (líneas 567-581, abreviado):**

```latex
\subsection{Numerical scripts}
\code{verify\_weil\_chi5.py} (explicit formula, $10^{-18}$),
\code{weil\_window\_chi5.py} (semilocal eigenvalues),
\code{weil\_window\_rigorous\_check.py} (constants of \cref{thm:first-window}),
\texttt{weil\_certificates/} (certificates of \cref{thm:second-window,thm:third-window}:
\code{cert.py}, \code{rigW.py}, \code{opcert\_rig.py}; the rigorous replays \code{verify\_iv.py}, …
\code{op\_rig\_validated.py}, …), \code{zeroside\_check.py} …, \code{envelope.py} and \code{tstar.py}
(\cref{prop:envelope-exact}); and, in \texttt{hipotesis/pruebas/}, the scripts of
\cref{sec:results-verdict}: \code{testGeom.py}, \code{testB1b.py}, … \code{retro105.py} and \code{retro119.py}.
```

**Veredicto: vigente en lo que afirma, incompleta en lo que sugiere.**

Lo que está correcto (medido, no supuesto):

* **51 scripts** listados con `\code{…}`; **51 de 51 existen en el repo** → ningún nombre colgante;
* **51 de 51 siguen citados en el cuerpo** → nada listado quedó huérfano tras los puertos F12/D7;
* los directorios que nombra (`weil_certificates/`, `hipotesis/pruebas/`) existen;
* es coherente con `appendix.tex:524` (*"The numerical tests are the scripts of `hipotesis/pruebas/`"*).

Lo que está desactualizado o ausente:

1. **No es un censo y lee como si lo fuera.** Hay **24 `.py` citados en el manuscrito que la sección no lista**:
   `W3_orbita_lado_primos.py`, `amplitud_clausula_ii.py`, `blocks.py`, `dedekind.py`, `escala_ceros_bajos.py`,
   `fermat_quintic_points.py`, `kisin.py`, `lp.py`, `orbita_cert.py`, `retro66/67/69/78/81/87/88/89.py`,
   `retro109.py`, `v12_pitagoras_raiz_X.py`, `v27_reloj_ciclotomico.py`, `v28_hiperbola_reloj_tamano.py`,
   `v30_vertice_al_azar.py`, `v33_capas_1e9.py`, `verify_rig.py`.
   De ellos, **16 forman parte de la lista D7 de 42** (los `retro*` y `v*_*` diferidos que D7 cerró el 2026-11-24).
   Un lector de la sección conclude que el aparato numérico son 51 scripts; el repo tiene **83**.
2. **No menciona la capa de salidas.** `hipotesis/pruebas/salidas/` (35 ficheros, entregados por zip2) no aparece
   en ningún sitio del `.tex` (2 únicos hits de `salidas`/`hipotesis/pruebas/` en `src/`: `appendix.tex:524` y
   `:575`, ninguno habla de salidas). Tampoco los módulos comunes `comun.py` / `comun_pruebas.py` ni los datos
   (`zeta_zeros_3000.npy`, `chi5_zeros_500.json`, `datos/`).
3. **No refleja el estado D7.** La sección sigue presentando la lista como "the scripts of `\cref{sec:results-verdict}`"
   sin decir que el corpus llegó en dos paquetes (zip1 2026-11-21 / zip2 2026-11-22) ni que el diferido está cerrado
   (42/42 portados, `a475748`, `pending(D7)` residual = **3**, todos no-`.py`). Los 3 marcadores vivos
   (`04-bridges.tex:107`, `appendix.tex:461`, `appendix.tex:730`) **no son scripts**, así que la sección de scripts
   está literalmente al día y lo que queda pendiente es de datos.
4. **No distingue qué es una salida y qué es un dato de entrada** — la misma ambigüedad que se trata en (c).

**Propuesta (no ejecutada):** mantener el párrafo como *lista de respaldo de las afirmaciones* (así está redactado
de hecho) y añadirle una frase de alcance, p. ej.
*"This subsection lists the scripts that back a statement of the text; the repository carries 83 scripts in
`hipotesis/pruebas/` with their outputs in `hipotesis/pruebas/salidas/`."*
— eso cierra el malentendido sin reescribir la lista de 51.

## (c) Columna `declarations` del apéndice: propuesta de tipo (`Kind`)

**Qué es cada columna hoy.** La sección `\section{Status ledger}\label{app:ledger}` (`appendix.tex:5`) contiene
**cuatro segmentos** (segmentación por propósito, ya aplicada — §6.13 del contrato), cada uno su propio `longtable`
con la misma forma de 3 columnas:

| segmento (subsección) | líneas | cabecera | columna 1 | columna 2 (`Declaration`) | columna 3 |
|---|---|---|---|---|---|
| `Proved claims registry` | 20-283 | `Claim & Declaration & Note` | el enunciado en el texto | **mezcla** nombres Lean (`\texttt{…}`), scripts (`\code{….py}`), aperturas `(open)` y artefactos de datos | nota |
| `Open problems` | 285-327 | `Statement & Declaration & Note` | enunciado abierto | `def … : Prop` del fichero unificado con `(Block • línea)` | nota |
| `Classical inputs` | 329-359 | `Claim & Declaration & Source` | input clásico | igual: `def … : Prop` con `(Block • línea)`; una fila ya es `theorem` | fuente |
| `Ledger rows whose class is not settled` | 361-374 | `Claim & Declaration & Note` | fila sin clase | `---` o un `\cref` (¡una referencia, no una declaración!) | nota |

El problema que describe el usuario es real y está en la **columna 2**: en un mismo sitio conviven
`\texttt{S1Closure.chi5\_fib\_all\_primes}` (prueba de Lean), `\code{weil\_certificates/verify\_iv.py}` (test numérico
con salida), `\texttt{KroneckerTwoPrimes} (Torus • 70025)` (input clásico) y `---` (ninguna). La cabecera dice
`Declaration` y no dice de qué tipo.

**Verificado sobre el fichero Lean** (`lean/F1_pentagonal_descent_UNIFIED.lean`):

* `pisano_five_is_twenty` → `theorem` (prueba);
* `ExactClosureAssembledLim` (72396) → `def … : Prop` (abierto);
* `KroneckerTwoPrimes` (70025), `WeylLaw` (70033), `GoldenArchimedeanWindow` (70871) → `def … : Prop` (clásico);
* `F1PaperTorus.lowFrequencyFraction_nonneg` (fila de `Classical inputs`) → **`theorem`**, ya probado
  (la prosa del propio segmento dice que tres de los 21 están ya probados).

Es decir: **abierto y clásico son la misma forma en la celda** (`def … : Prop` + `Block • línea`); la distinción
hoy la da el segmento, no la celda. Eso condiciona la propuesta.

### Propuesta: columna `Kind` (naturaleza de la fuente, no estatus)

**Valores fijos (alfabeto cerrado, 4):**

| `Kind` | significa | cómo se deriva de la celda |
|---|---|---|
| `Lean` | la celda nombra una declaración **con prueba** en el corpus compilado | `theorem`/`lemma` en el `.lean` |
| `Num` | la celda nombra una **prueba numérica con salida comprometida** (`hipotesis/pruebas/salidas/<x>.txt` o el artefacto de salida del zip) | termina en `.py` / es un directorio de scripts |
| `Stmt` | la celda nombra un **`def … : Prop` sin prueba** (lo que el segmento clasifica como abierto o como clásico) | `def` + `(Block • línea)` |
| `—` | la fila **no lleva declaración** | `---` o un `\cref` en la celda |

Se admite unión fija cuando la celda mezcla: `Lean; Stmt` (p. ej. `appendix.tex:34` lleva
`\texttt{W4Isometria.symEnergy\_le}` **y** `\texttt{PythagorasLaw} (open)`).

**Por qué `Kind` no es una columna de estatus (y por eso no choca con WD-03):**

1. sus valores son **clases de artefacto** (¿qué abro para comprobar esta fila?: un `.olean`, un `.py`+salida,
   un `def … : Prop`, nada), no un grado, una categoría ni una puerta;
2. es **invariante ante la reclasificación de estatus**: si mañana `GoldenArchimedeanWindow` se prueba, su fila
   pasa de `Stmt` a `Lean` *porque cambió el artefacto*, no porque cambie una etiqueta de calidad;
3. no codifica `*`, `P`/`N`, `Tier` ni ninguna letra del alfabeto de evidencia (WD-07: el alfabeto sigue congelado);
4. **la segmentación por propósito de §6.13 se conserva intacta** — `Kind` se añade *dentro* de cada segmento y no
   sustituye a ninguno; los cuatro `longtable` siguen separados por uso.

**Descarto el valor `Open`** (y por extensión `Classical` como valor): en la celda, un abierto y un clásico son
indistinguibles (`def … : Prop` + `Block • línea` en ambos), así que `Open` no se derivaría de la celda sino del
segmento — sería repetir el estatus dentro de la tabla, que es exactamente lo que WD-03 prohíbe
(*"no `Tier` column and no tier label in a table"*). El abierto/clásico ya viaja en el título del segmento
(§6.13) y en las marcas `[O→N]`/`[N→O]` de las propias filas. Si el autor quiere esa palabra a la vista, que
vaya en la celda `Note`, no en una columna nueva.

**Implementación (dos variantes, ninguna ejecutada):**

* **A — columna estrecha (recomendada).** Los cuatro `longtable` comparten la misma forma, así que es un único
  cambio mecánico. Nueva cabecera (para `Claim & Declaration & Note`):

  ```latex
  {\scriptsize\setlength{\tabcolsep}{3pt}
  \begin{longtable}{>{\raggedright\arraybackslash}p{0.18\textwidth}>{\raggedright\arraybackslash}p{0.06\textwidth}>{\raggedright\arraybackslash}p{0.44\textwidth}>{\raggedright\arraybackslash}p{0.29\textwidth}}
  \toprule Claim & Kind & Declaration & Note\\\midrule\endhead
  ```
  (0.18 + 0.06 + 0.44 + 0.29 = 0.97 < 1, dentro de lo que ya se gastaba; en los segmentos 2 y 4 cambiar
  `Claim`→`Statement` y en el 3 `Note`→`Source`, como hoy.)
* **B — prefijo en la celda** (cero cambios de ancho): `\textbf{Num}~\code{weil\_certificates/verify\_iv.py}`.
  Más barato, pero mezcla la etiqueta con el contenido y hace imposible filtrar/medir la columna.
* En ambos casos, una **nota al pie del primer segmento** con el alfabeto: *"`Kind` records what the cell points
  at — a proved declaration (`Lean`), a numerical test with its committed output (`Num`), a statement without a
  proof (`Stmt`), or no declaration (`—`); it is not a status, which the segmentation carries."*

### Tres filas reales, antes / después (variante A)

**Fila 1 — `appendix.tex:25` (segmento `Proved claims registry`), prueba de Lean**

*Antes:*
```latex
$\chi_5(p)\equiv F_p\pmod p$, all $p\ne5$ & \texttt{S1Closure.chi5\_fib\_all\_primes}; \texttt{lambda\_structure\_gives\_chi5}; \texttt{FrobeniusUnico.fib\_eq\_sign} & Supersedes the tabulation over six primes (\texttt{fib\_split\_criterion}).\\
```
*Después:*
```latex
$\chi_5(p)\equiv F_p\pmod p$, all $p\ne5$ & Lean & \texttt{S1Closure.chi5\_fib\_all\_primes}; \texttt{lambda\_structure\_gives\_chi5}; \texttt{FrobeniusUnico.fib\_eq\_sign} & Supersedes the tabulation over six primes (\texttt{fib\_split\_criterion}).\\
```

**Fila 2 — `appendix.tex:39` (mismo segmento), test numérico — la fila que motiva la confusión**

*Antes:*
```latex
Window $L\le1$, $Q\ge0.0445\|f\|^2$ & \code{weil\_certificates/verify\_iv.py} & Interval arithmetic; supersedes the double-precision $0.0431$.\\
```
*Después:*
```latex
Window $L\le1$, $Q\ge0.0445\|f\|^2$ & Num & \code{weil\_certificates/verify\_iv.py} & Interval arithmetic; supersedes the double-precision $0.0431$.\\
```
(`Num` está justificado: la salida existe y está comprometida — `hipotesis/pruebas/weil_certificates/verify_iv_L1.0_output.txt`.)

**Fila 3 — `appendix.tex:339` (segmento `Classical inputs`), input clásico**

*Antes:*
```latex
$log p/log q$ irrational $\Rightarrow$ ${a·log p/log q+b}$ dense in $\mathbb{R}$ & \texttt{KroneckerTwoPrimes} (Torus $\bullet$ 70025) & \\
```
*Después:*
```latex
$log p/log q$ irrational $\Rightarrow$ ${a·log p/log q+b}$ dense in $\mathbb{R}$ & Stmt & \texttt{KroneckerTwoPrimes} (Torus $\bullet$ 70025) & \\
```
(`Stmt`, no `Lean`: en `lean/F1_pentagonal_descent_UNIFIED.lean:70025` es `def KroneckerTwoPrimes … : Prop :=`,
sin prueba — que es justo lo que el segmento afirma de los inputs clásicos.)

**Filas de control** (muestran que el alfabeto cubre las cuatro formas): `appendix.tex:34` → `Lean; Stmt`
(celda mixta), `appendix.tex:370` → `—` (la celda es `---`), `appendix.tex:338` → `Lean` (ya es `theorem`,
la que la prosa del segmento dice que está probada).

## (d) Fila de cierre de "mathlib names at risk"

**Localización.** No hay fila WD para esto hoy (`docs/witness-decisions.md`: 0 hits de `mathlib`/`at risk`).
Sí está en dos informes:

* `docs/reports/20261122_F9-001_provenance_inventory.md:96-103` — *"## Mathlib names at risk → artefactos del proceso"*:
  los 71 tokens `\texttt{…}` de `appendix.tex:467-492` se reclasifican como **process artifacts**;
  *"with no case as permanent content once the build compiles against the pinned Mathlib `a8754b18`. The final
  presentation of the subsection is an F7 decision; nothing is changed now."*
* `docs/reports/20261123_MRG-001_f1_v168_merge_closure.md:113-114` (§5 item 4) — *"Names at risk … classified as
  process artifacts of the composition layers; no content action."* — es un ítem **abierto**, no una decisión.
* La subsection sigue viva en `src/chapters/appendix.tex:540-565` (`\subsection{Mathlib names at risk}`).

**Evidencia de compilación (medida, sin ejecutar nada en esta sesión):**

| hecho | fuente |
|---|---|
| `Build completed successfully (18248 jobs).` | `scratch/w2_val_02-odd-zeta.log` (2026-11-24, `pnpm run validate`, exit 0) — también `f11b_validate_final.log`, `mrg001_validate.log`, `f9_validate3.log`, `fti_validate_final2.log` |
| `counts:check ✓ … lean.theorems=5712, lean.axioms=0, lean.sorry=0` | mismo log; y `docs/counts.md:12-14` (regenerado desde el árbol: `lean.theorems 5712`, `lean.axioms 0`, `lean.sorry 0`) |
| `95 passed` (suite `pytest -m 'not slow'`) — hoy `docs/counts.md` mide **113** | `scratch/w2_val_02-odd-zeta.log` / `docs/counts.md:10-11` |
| Mathlib pineado `a8754b18`, toolchain 4.36.0-rc2 | MRG-001 §2 fila F3 |
| los nombres marcados existen en el build verde | `main.tex:360` (comentario: *"all 194 names it marked exist in the green build (18248 jobs, sorry = 0)"*) |

**Fila propuesta (texto exacto para `docs/witness-decisions.md`, sección `## Ruled and derived`, id siguiente `WD-34`; NO ejecutada):**

```markdown
| WD-34 | Is the "Mathlib names at risk" list of the appendix still owed a check? | **Ruled:** no per-name audit is owed — the list is a pre-compile checklist of the composition layers, reclassified as process artifacts, and every name it marks exists in the green build (`lake build` **18 248 jobs, success**, `lean.sorry` **0**, `lean.axioms` **0**, `lean.theorems` **5712**, measured 2026-11-24); the subsection's final presentation stays an F7 decision and the list is not content | 2026-11-26 · 02-odd-zeta/docs/reports/20261122_F9-001_provenance_inventory.md §"Mathlib names at risk → artefactos del proceso" · 02-odd-zeta/docs/reports/20261123_MRG-001_f1_v168_merge_closure.md §5 item 4 · 02-odd-zeta/docs/counts.md |
```

Notas de forma: respeta el encabezado del ledger (*"one row per question; a count is never a row"* — la pregunta es
"¿se debe una comprobación por nombre?", no "¿cuántos nombres hay?"); `ref` nombra el documento y la sección que
lleva la evidencia y la figura medida va fechada, como exige la cabecera del fichero.

## (e) Lagunas

1. **3 nombres citados siguen sin portar** (idénticos a los 3 marcadores `pending(D7)` residuales):
   `CW_EQUIVALENCIAS.md`, `fqn_map.json` (entregados en zip1, no importados) y `unfold_by_conductor.txt`
   (nunca entregado ni declarado no-disponible). **"referenciados-sin-portar = 0" es cierto solo para `.py`.**
2. **`retro65.py` no existe en ninguna entrega** y `retro66.py:99-101` lo `exec` → `retro66.py` no ejecuta.
3. **`zeros.txt` no existe**; `envelope.py` y `weil_certificates/zeroside_check.py` lo abren por nombre.
   Renombrar/linkear `chi5_zeros_T80.txt` (decisión del autor, no mía).
4. **3 huérfanos de verdad**: `ceros_chi5_500.py`, `comun_pruebas.py`, `cuintica.py` (zip2, nunca citados).
5. **36 scripts referenciados sin salida comprometida** — la afirmación numérica que sustentan está en el texto,
   pero el repo no guarda su fichero de salida (los `retro*`, `v*_*`, `weil_*`, `envelope`, `tstar`, `x_sweep`,
   `oz_carried`, …). Si la trazabilidad exige salida, es trabajo nuevo; si no, conviene decirlo en la sección.
6. **La sección `Numerical scripts` no es un censo**: 24 citados fuera de ella (16 de ellos del lote D7).
7. **Los 10 datos de zip1 no portados** no los lee ningún script del repo (0 hits), pero el MANIFEST del zip
   los sigue listando como dependencias — el MANIFEST ya no describe este árbol.
8. **No se ejecutó ningún build ni ningún script** (mandato de solo lectura): los conteos de compilación son
   los de los logs y `docs/counts.md` existentes, no una medición nueva de hoy.
9. El censo F9-001 está **desfasado en líneas** respecto al apéndice actual (sus `appendix.tex:386/657` hoy son
   `:461/:730`): la segmentación Opción C movió el texto y ningún informe lo renumeró.

**Dato de cierre sobre la lista "citados y no disponibles" del zip1 (36 entradas):** 34 de los 35 `.py` que el
autor declaró *no disponibles* fueron entregados después por **zip2** (el pase F12) y ya están en el repo;
`LEDGER_ESTADO.md` también viene en zip2. El único que sigue sin existir es `verify_odd_zeta_pcf_unified.py`,
que **ya no se cita en el manuscrito** (F10 lo sustituyó por la suite `pytest`): no queda ningún `.py`
declarado no-disponible que siga citado.
