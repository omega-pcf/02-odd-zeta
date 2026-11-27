# Numerical port — coverage tracker

| Field | Value |
|---|---|
| **id** | `NUMPORT-001` |
| **title** | Coverage tracker of the `hipotesis/pruebas/` → `tests/` port campaign |
| **status** | living tracker |
| **date** | 2026-11-26 |
| **version** | 1.0 |

**Scope.** This is the working base of the port campaign: one row per
numerical script of `hipotesis/pruebas/` (83 `.py`, measured today),
reconciled against the suite that already exists in `tests/` (202 tests,
`uv run pytest tests/`). Sources: `docs/reports/20261126_SCRIPTS-RECON-003_scripts_reconciliation.md`
(promoted from the scratch inventory), the manuscript
(`main.tex` + `src/chapters/*.tex`, line hits measured with `git grep`
normalising `\_` → `_`), and the suite itself. `hipotesis/pruebas/` and
`tests/` are read-only here: this document records state, it changes no
test. Line numbers are snapshots and move with the manuscript.

## Destination convention

* **pytest in `tests/`** — one entrypoint, `uv run pytest tests/`; no
  second folder, no second runner (`pnpm run verify:py` wraps the same
  command).
* **F10 pattern** — a golden test reads the committed output under
  `hipotesis/pruebas/salidas/` and pins its digits (tolerance `1e-12`,
  the four decimals the files print); a claim test recomputes the number
  and asserts it with the tolerance of the check it ports and the
  condition declared in the docstring. Test ids are snake_case.
* **One test per family** where the scripts share a claim (the `FAM`
  groups below), not one test per script.
* **Nothing self-baked** — each test owns the code that produces its
  numbers and asserts values, never printed stdout; the support code is
  the importable `tests/src/oddzeta` (`constants`, `harness`).

**Rules used to fill `destino` and `status`:**

| destino | meaning |
|---|---|
| `absorbed` | an existing test already covers the script (its committed output is pinned, or it is scaffolding whose corpus is pinned) — no new row is opened |
| `generator:<… kept as fixture>` | the script's product is a data/cache file consumed by other scripts, not a claim of its own |
| `orphan-no-cited` | never cited anywhere in the manuscript and no test — the author decides: cite it where it is used, or remove it |
| `blocked:<motivo>` | the port cannot start until a named external condition is resolved |
| `<test-name>` | owed: a new test in the family named |

| status | meaning |
|---|---|
| `pending` | destino assigned, work not started |
| `in-progress` | port under way (no row is in this state today) |
| `absorbed` | scaffolding with no claim of its own: it is executed by scripts whose own rows are now `ported`, so its corpus is covered by them |
| `ported:<test-name>` | the test exists and covers the claim by recomputation |
| `verified-against-corpus` | the test reads and pins the script's committed output |
| `ported:<test-name> · verified-against-corpus` | the test exists, covers the claim by recomputation, and its assert reproduces the figure the `.tex` statement prints for it (for `bridge.py` it also pins the committed `salidas/bridge.txt`) |

## Master table — the 83 scripts

Columns: `script` · `qué hace` (one line, from its docstring) ·
`statements que respalda` (its citations in the manuscript) ·
`test existente que ya lo cubre` (reconciled against the 132 tests) ·
`destino propuesto` · `status`.

| script | qué hace | statements que respalda | test existente | destino propuesto | status |
|---|---|---|---|---|---|
| `amplitud_clausula_ii.py` | amplitud_clausula_ii.py — W4–W5, prop:closure-amplitude: la amplitud de la clausula (ii). | `04-bridges:1553` | `test_residual_scales_are_pinned` | `absorbed` | `verified-against-corpus` |
| `arch_window.py` | arch_window.py — W3, ssec:golden-field: la forma arquimediana de zeta_K, K = Q(sqrt5), explicitamente. | `04-bridges:1166`, `appendix:584` | `test_arch_window_crossings_are_pinned` | `absorbed` | `verified-against-corpus` |
| `balance.py` | balance.py — W3, ssec:field-positivity: la positividad como balance entre los dos tipos de orbita de Klein. | `04-bridges:950`, `appendix:581` | `test_orbit_balance_is_pinned` | `absorbed` | `verified-against-corpus` |
| `blocks.py` | blocks.py — W3, ssec:field-positivity: los tres bloques del lado de los primos y el limite forzado. | `04-bridges:925` | `test_fejer_window_is_pinned` | `absorbed` | `verified-against-corpus` |
| `bridge.py` | bridge.py — W3, prop:bridge-boosts: rotaciones sobre la linea, boosts fuera de ella. | `04-bridges:1050`, `appendix:582` | `tests/test_bridge_boosts.py` (golden de `salidas/bridge.txt` + 2 tests de claim) | `test_bridge_boosts` | `ported:test_bridge_boosts · verified-against-corpus` |
| `castelnuovo.py` | castelnuovo.py — W3, ssec:product-surface: el analogo de los conteos de puntos de Weil. | `04-bridges:993`, `appendix:582` | `test_castelnuovo_golden_values`, `test_castelnuovo_matches_manuscript_claim`, `test_castelnuovo_window_maxima` | `absorbed` | `verified-against-corpus` |
| `ceros_chi5_500.py` | ceros_chi5_500.py — los ceros de L(s,chi_5) en 0 < t < 500 (dato común de hipotesis/pruebas/). | — | — · su salida `chi5_zeros_500.json` sí la leen `circle_and_detect.py` y `comun_pruebas.py` | `orphan-no-cited` | `pending` |
| `weil_certificates/cert.py` | Programa lineal que da el certificado de la ventana de Weil (cert_L*.json). | `04-bridges:573`, `04-bridges:577`, `appendix:577` | — | `test_weil_certificates.py` | `ported:test_weil_certificates · verified-against-corpus` |
| `chi5_zeros.py` | chi5_zeros.py — ceros de L(s, chi_5) en la recta, 0 < t < T, por cambios de signo de la funcion Z real. | `04-bridges:175`, `appendix:586` | — · dato de entrada, no un claim | `generator:<chi5_zeros.json + chi5_zeros_T80.txt kept as fixture>` | `pending` |
| `circle_and_detect.py` | circle_and_detect.py — W4–W5, ssec:weil-closure: la densidad de Fejer en el circulo de p = 3, y lo que el | `04-bridges:1862`, `04-bridges:1880`, `appendix:585` | `test_circle_and_detect_golden_values`, `test_circle_and_detect_matches_manuscript_claim` | `absorbed` | `verified-against-corpus` |
| `classes_test.py` | classes_test.py — W4–W5, ssec:weil-closure: las ocho clases modulo 20 hacen falta en la correccion. | `04-bridges:1641`, `appendix:586` | — | `test_closures_and_sweeps.py` | `pending` |
| `comun.py` | Utilidades comunes de las verificaciones (§33–§54 del Lean unificado). | — | — · andamiaje de 8 scripts; sus consumidores escala_ceros_bajos/t1_index/t2_loo están fijados en `test_golden_n_marks.py` | `absorbed` | `verified-against-corpus` |
| `comun_pruebas.py` | comun_pruebas.py — utilidades comunes de hipotesis/pruebas/: criba, potencias de primo con Lambda, | — | — · lo importan 22 scripts; sin claim propio ni salida | `orphan-no-cited` | `pending` |
| `corrected_operator.py` | corrected_operator.py — W4–W5, ssec:weil-closure y prop:positions: las posiciones, desde la estructura. | `04-bridges:1238`, `appendix:586` | `test_corrected_operator_golden_values`, `test_corrected_operator_matches_manuscript_claim` | `absorbed` | `verified-against-corpus` |
| `cuintica.py` | cuintica.py — la representacion de la capa quintica (prop:sqrt-x, prop:phi-layers): a(n) para la formula explicita. | — | — · lo importa `orbita_cert.py` (`from cuintica import a_pk`) | `orphan-no-cited` | `pending` |
| `dedekind.py` | dedekind.py — W3, ssec:field-positivity: la suma de Fejer de Q(i,sqrt5), el campo de las cuatro fibras de G. | `04-bridges:958` | `test_orbit_balance_is_pinned` | `absorbed` | `verified-against-corpus` |
| `dh.py` | dh.py — W1–W2, ssec:two-sides: las sumas parciales de la inversa de Davenport–Heilbronn y de mu·chi_5. | `04-bridges:893`, `appendix:583` | `test_additive_side_statistics_are_pinned` | `absorbed` | `verified-against-corpus` |
| `dh_logderiv.py` | Coeficientes de −L′/L de Davenport–Heilbronn frente a L(s,χ₅): soporte y tamaño. | `04-bridges:909`, `appendix:123`, `appendix:586` | — | `test_closures_and_sweeps.py` | `pending` |
| `dh_zeros.py` | dh_zeros.py — ceros de Davenport-Heilbronn hasta T=130 (para retro101.py). Uso: python3 -I dh_zeros.py | `appendix:586` | — · dato de entrada, no un claim | `generator:<dh_zeros.json kept as fixture>` | `pending` |
| `envelope.py` | Envoltura exacta de S(t) con los ceros de L(s,χ₅) (prop:envelope-exact); abre `zeros.txt`. | `appendix:96`, `appendix:579` | `tests/test_envelope_bounds.py` (2 tests, recomputan desde la caché commiteada) | `test_envelope_bounds` | `ported:test_envelope_bounds · verified-against-corpus` |
| `escala_ceros_bajos.py` | escala_ceros_bajos.py — W4–W5, prop:sqrt-x: la escala 1/2 desde los ceros bajos de las formas de niveles 80 y 135. | `04-bridges:1307` | `test_residual_scales_are_pinned` | `absorbed` | `verified-against-corpus` |
| `euler_link.py` | euler_link.py — W4–W5, prop:euler-tower: el producto de Euler, la torre de phi y las posiciones. | `04-bridges:1791`, `appendix:586` | `test_euler_link_second_term_is_pinned` | `absorbed` | `verified-against-corpus` |
| `fejer_check.py` | fejer_check.py — W3, ssec:field-positivity: la suma de Fejer de L(s,chi_5) desde los primos y desde los ceros. | `04-bridges:929`, `appendix:581` | `test_fejer_window_is_pinned` | `absorbed` | `verified-against-corpus` |
| `fermat_quintic_points.py` | fermat_quintic_points.py — rmk:fermat-model y su fila del Status ledger: la quintica de Fermat en p = 1 mod 5. | `appendix:46` | `test_fermat_quintic_point_counts_are_pinned` | `absorbed` | `verified-against-corpus` |
| `fibres.py` | fibres.py — W3, ssec:field-positivity y prop:four-fibres: la suma de Fejer de cada fibra de G. | `04-bridges:955`, `appendix:582` | `test_orbit_balance_is_pinned` | `absorbed` | `verified-against-corpus` |
| `field_signature.py` | field_signature.py — W3, ssec:golden-field: la signatura del indice de Hodge del campo dorado. | `04-bridges:1148`, `appendix:584` | `test_field_signature_is_pinned` | `absorbed` | `verified-against-corpus` |
| `gram.py` | gram.py — W3, prop:intersection-form: la forma de Weil en dimension ocho es una matriz de Gram. | `04-bridges:1015`, `appendix:582` | `test_intersection_form_signature_is_pinned` | `absorbed` | `verified-against-corpus` |
| `kisin.py` | kisin.py — rmk:prism-five (junto a thm:L1 y el regulador R_K = log phi): el prisma en 5 y el regulador 5-adico. | `03-mechanisms:2138` | `test_kisin_interpolation_is_pinned` | `absorbed` | `verified-against-corpus` |
| `law_resolution.py` | law_resolution.py — W4–W5, ssec:weil-closure: lo que la ley tiene que dar.  (version d) | `04-bridges:1634`, `appendix:586` | `test_law_resolution_golden_values`, `test_law_resolution_matches_manuscript_claim`, `test_zero_side_correction_matches_the_manuscript` | `absorbed` | `verified-against-corpus` |
| `weil_certificates/lp.py` | Funciones W(r) y A del programa lineal subyacente a los certificados. | — | — · andamiaje: lo importan cert/opcert/op_rig_validated/opcert_rig (0 citas en el manuscrito — medido hoy) | `absorbed` | `absorbed` |
| `mertens341.py` | mertens341.py — W1–W2, ssec:two-sides: hasta donde llega la desigualdad 3-4-1 de Mertens para L(s,chi_5). | `04-bridges:898`, `appendix:583` | `test_additive_side_statistics_are_pinned` | `absorbed` | `verified-against-corpus` |
| `mobius.py` | mobius.py — W1–W2, ssec:two-sides: la inversa de la estructura, sum_{n<=y} mu(n) chi_5(n). | `04-bridges:901`, `appendix:583` | `test_additive_side_statistics_are_pinned` | `absorbed` | `verified-against-corpus` |
| `offline.py` | offline.py — W3, ssec:field-positivity: un cero fuera de la linea vuelve negativa la suma de Fejer. | `04-bridges:964`, `appendix:582` | `test_offline_minimum_stays_positive` | `absorbed` | `verified-against-corpus` |
| `weil_certificates/op_rig_validated.py` | Validated replay of the operator-form Weil window (Thm 23.8), in chunks with checkpoints. | `04-bridges:523`, `04-bridges:555`, `appendix:42` (+1) | — | `test_weil_certificates.py` | `ported:test_weil_certificates · verified-against-corpus` |
| `weil_certificates/opcert.py` | Óptimo primal del programa lineal de la ventana (reutiliza lp.py). | — | — · andamiaje: lo importa `zeroside_check.py` (su `phihat`); el propio no se importa | `absorbed` | `absorbed` |
| `weil_certificates/opcert_rig.py` | Óptimo primal riguroso con W_lower (versión con intervalos). | `appendix:578` | — | `test_weil_certificates.py` | `ported:test_weil_certificates` |
| `orbita_cert.py` | orbita_cert.py — W4–W5, ssec:weil-closure: la orbita certificada, y la familia de la capa quintica. | `04-bridges:1868`, `appendix:728` | — | `test_closures_and_sweeps.py` | `pending` |
| `oz_carried.py` | oz_carried.py -- numerical checks for the results carried from the predecessor version (F1 v157). | `03-mechanisms:2208`, `03-mechanisms:2232`, `03-mechanisms:2265` (+6) | — | `test_closures_and_sweeps.py` | `pending` |
| `retro101.py` | retro101.py — Sprint 101. La linea del indice (sprints 93n-96n) sobre una orbita libre REAL: | `04-bridges:1079`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro102.py` | retro102.py — Sprint 102. La flecha W3 => W4 del diccionario, y las dos mitades de W4 como las dos paridades. | `04-bridges:1925`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro104.py` | retro104.py — Sprint 104. Lo que un operador del nivel no separa, y el par que si separa. | `03-mechanisms:3546`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro105.py` | retro105.py — Sprint 105. Lo que una estructura haria ver en GUE, y lo que vemos. | `03-mechanisms:3595`, `04-bridges:176`, `appendix:126` (+1) | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro109.py` | retro109.py — Sprint 109: las dos caras de la dinamica de Fibonacci (toro real / puntos de torsion). | `03-mechanisms:3491` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro119.py` | Sprint 119: el 3-del-reloj de e_p y la clase 9 sobre μ₅. | `03-mechanisms:1490`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro66.py` | retro66.py — Sprint 66: quitar la hipotesis H del sprint 65. | `04-bridges:1502`, `appendix:263` | — | `blocked:retro65-never-delivered` | `pending` |
| `retro67.py` | retro67.py — Sprint 67: la positividad de Weil nivel por nivel. | `04-bridges:1509`, `appendix:263` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro69.py` | retro69.py — Sprint 69: el puente entre el polo del reloj y el polo de zeta_K. | `03-mechanisms:1402` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro78.py` | retro78.py — Sprint 78: la rotacion (B) en las dos caras. | `03-mechanisms:1627`, `appendix:175` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro81.py` | retro81.py — Sprint 81: el gato cuantizado de M^2 = [[1,1],[1,2]] (M = [[0,1],[1,1]], det M = -1) en N = 5^k y otros N, | `04-bridges:1725` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro83.py` | retro83.py — Sprint 83: (A) la demostracion por la formula del caracter; (B) el caso 5^k con fase exacta. | — | — · andamiaje: lo `exec` retro87/88/89 | `absorbed` | `absorbed` |
| `retro86.py` | retro86.py — Sprint 86: las trazas en 5^k por suma de Gauss binaria, exacta (enteros y simbolos de Legendre). | — | — · andamiaje: lo `exec` retro87/88/89 | `absorbed` | `absorbed` |
| `retro87.py` | retro87.py — Sprint 87: la prueba uniforme en k de las trazas con 5 \| m. | `04-bridges:1725` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro88.py` | retro88.py — Sprint 88: la pieza (B) sobre el complemento del estado excepcional. | `04-bridges:1746` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro89.py` | retro89.py — Sprint 89: pegar los modelos locales. El gato cuantizado en N compuesto (N impar, libre de cuadrados o con 5^k): | `04-bridges:1751` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro93.py` | retro93.py — Sprint 93: una orbita libre de Klein y el indice de inercia de la forma de Weil. | `04-bridges:1079`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro94.py` | retro94.py — sprint 94: la masa del reloj separada por las fibras de G. | `03-mechanisms:1528`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `retro99.py` | retro99.py — sprint 99: que selecciona el estabilizador {id, mate}. La funcion de Davenport-Heilbronn | `04-bridges:907`, `appendix:123`, `appendix:586` | — | `test_retro_sprints.py` | `ported:test_retro_sprints · verified-against-corpus` |
| `rho_interval.py` | rho_interval.py — W3, ssec:golden-field: la cota inferior rho <= lambda_{N+1} de la forma de Weil de Q(sqrt5). | `04-bridges:1191`, `appendix:584` | — | `test_closures_and_sweeps.py` | `pending` |
| `rigorous_chain.py` | rigorous_chain.py — W3, ssec:golden-field: las primeras ventanas del campo dorado sobre todo el espacio. | `04-bridges:1191`, `appendix:583` | — | `test_closures_and_sweeps.py` | `pending` |
| `weil_certificates/rigW.py` | Rigorous lower bound for W(r)=log(5/pi)+Re psi(1/4+ir/2). | `04-bridges:552`, `appendix:577` | — | `test_weil_certificates.py` | `ported:test_weil_certificates · verified-against-corpus` |
| `sweep.py` | sweep.py — W4–W5, ssec:weil-closure y prop:eight-classes: la cota (W4) en las ocho clases, barrida. | `04-bridges:1860`, `appendix:585` | — | `test_closures_and_sweeps.py` | `pending` |
| `t1_index.py` | t1_index.py — W4–W5, prop:what-fluctuation-takes (iv): el orden angular de phi carga la posicion del primo. | `04-bridges:1677`, `appendix:586` | `test_angular_index_statistics_are_pinned` | `absorbed` | `verified-against-corpus` |
| `t2_loo.py` | t2_loo.py — W4–W5, prop:what-fluctuation-takes: dejar un primo fuera de la correccion. | `04-bridges:1677`, `appendix:586` | `test_angular_index_statistics_are_pinned` | `absorbed` | `verified-against-corpus` |
| `teich.py` | teich.py — ssec:delta-polar: la p-derivacion de Z[phi], la forma polar de phi en 2 y 3 y el grupo de color. | `appendix:586` | `test_delta_p_tower_ratios_are_pinned` | `absorbed` | `verified-against-corpus` |
| `testB1b.py` | testB1b.py — W1–W2, ssec:fluct-geometry: los valores individuales piden log p con precision ~1/T. | `04-bridges:856`, `appendix:581` | `test_fluctuation_law_is_the_same_everywhere` | `absorbed` | `verified-against-corpus` |
| `testGeom.py` | testGeom.py — W1–W2, ssec:fluct-geometry: la ley de la fluctuacion es geometrica. | `04-bridges:854`, `appendix:581` | `test_fluctuation_law_is_the_same_everywhere` | `absorbed` | `verified-against-corpus` |
| `tstar.py` | La constante T*(n)=c(n)·πn/log(μn+σ) y su envoltura (prop:envelope-exact). | `03-mechanisms:3385`, `appendix:96`, `appendix:579` | — · el módulo ya existe pero en la ola P1 cubre a envelope/zeroside, no a tstar | `test_envelope_bounds.py` | `pending` |
| `v12_pitagoras_raiz_X.py` | √X como Pitágoras: energía E(X) = Σ_{p≤X} \|a_p\|² log² p frente a \|S(X)\|², S(X) = Σ a_p log p, | `04-bridges:1303` | `tests/test_v_layer_claims.py` (14 tests de claim) | `test_v_layer_claims` | `ported:test_v_layer_claims · verified-against-corpus` |
| `v27_reloj_ciclotomico.py` | §68: el reloj ciclotómico.  N(Φ_n(φ)) = Φ_n(φ)·Φ_n(ψ), exacto como entero por Möbius sobre | `03-mechanisms:1400`, `03-mechanisms:1453` | `tests/test_v_layer_claims.py` (14 tests de claim) | `test_v_layer_claims` | `ported:test_v_layer_claims · verified-against-corpus` |
| `v28_hiperbola_reloj_tamano.py` | §69: del reloj al tamaño, la hipérbola c·i = N_p. | `03-mechanisms:1674` | `tests/test_v_layer_claims.py` (14 tests de claim) | `test_v_layer_claims` | `ported:test_v_layer_claims · verified-against-corpus` |
| `v30_vertice_al_azar.py` | §71: la geometría del n-gono y el modelo de vértice al azar. | `04-bridges:1323` | `tests/test_v_layer_claims.py` (14 tests de claim) | `test_v_layer_claims` | `ported:test_v_layer_claims · verified-against-corpus` |
| `v33_capas_1e9.py` | §73: las 20 capas del vértice al azar con primos hasta 10⁹ (datos de v32_capas_hasta_1e9.py). | `04-bridges:1324`, `04-bridges:1487` | `tests/test_v_layer_claims.py` (14 tests de claim) | `test_v_layer_claims` | `ported:test_v_layer_claims · verified-against-corpus` |
| `weil_certificates/verify_cert.py` | Verifica un certificado JSON contra la cota que declara. | — | — · 0 importadores y 0 citas; andamiaje declarado en el MANIFEST del zip1, sin claim propio (reclasificado en la ola P1) | `orphan-no-cited` | `pending` |
| `weil_certificates/verify_iv.py` | Rigorous replay in interval arithmetic (mpmath.iv, outward rounding) of a Weil-window certificate. | `04-bridges:493`, `04-bridges:555`, `appendix:41` (+1) | — | `test_weil_certificates.py` | `ported:test_weil_certificates · verified-against-corpus` |
| `weil_certificates/verify_rig.py` | Replay riguroso de un certificado en aritmética de fracciones. | `04-bridges:517` | — | `test_weil_certificates.py` | `ported:test_weil_certificates · verified-against-corpus` |
| `verify_weil_chi5.py` | verify_weil_chi5.py  — [N] numerical checks for the Weil route (F1 manuscript). | `04-bridges:381`, `appendix:573` | — | `test_weil_certificates.py` | `pending` |
| `W3_orbita_lado_primos.py` | Criba hasta e^14.5 y mide la órbita del lado de los primos (W3). | `04-bridges:1870` | — | `test_closures_and_sweeps.py` | `pending` |
| `w4exact.py` | w4exact.py — W4–W5, prop:W4-from-W3 (i): (W4) es (W3) en los planos de la orbita, exactamente. | `appendix:585` | — | `test_closures_and_sweeps.py` | `pending` |
| `weil_window_chi5.py` | Autovalores semilocales de la ventana de Weil para L(s,χ₅). | `04-bridges:425`, `04-bridges:431`, `04-bridges:601` (+3) | — | `test_weil_certificates.py` | `pending` |
| `weil_window_rigorous_check.py` | Constantes de thm:first-window (κ, W(0)) con aritmética rigurosa. | `04-bridges:453`, `appendix:575` | — | `test_weil_certificates.py` | `pending` |
| `x_sweep.py` | As x_sweep.py, with the prime sum smoothed: weight w(log n/log X) on each prime power n, | `04-bridges:1637`, `appendix:586` | — · el módulo ya existe pero en la ola P1 cubre a envelope/zeroside, no a x_sweep | `test_envelope_bounds.py` | `pending` |
| `zeroside.py` | zeroside.py — W4–W5, ssec:weil-closure: la formula explicita sobre la orbita de Frobenius, comprobada. | `04-bridges:1854`, `appendix:585` | `test_zeroside_orbit_agrees_with_the_zeros` | `absorbed` | `verified-against-corpus` |
| `weil_certificates/zeroside_check.py` | Suelo de la ventana por el lado de los ceros: Q(f)=Σ\|f̂(γ)\|²; abre `zeros.txt`. | `04-bridges:601`, `appendix:578` | `tests/test_envelope_bounds.py` (2 tests, recomputan desde la caché commiteada) | `test_envelope_bounds` | `ported:test_envelope_bounds · verified-against-corpus` |

**Counts by destino:** `<test-name>` **44** (30 `ported`, 14 still owed) ·
`absorbed` **32** · `generator` **2** ·
`orphan-no-cited` **4** · `blocked` **1** — total
**83**. **Counts by status:**
`ported:<test> · verified-against-corpus` **29** ·
`ported:<test>` **1** ·
`verified-against-corpus` **28** ·
`absorbed` **4** ·
`pending` **21** · `in-progress` **0**.

**Deletion pass (wave P1):** none of the 8 scripts this wave ports was
removed from `hipotesis/pruebas/`. Measured first: no `.py` of the
repository imports any of them (zero `import <name>` / `from <name>`
hits), so nothing would break — but the test does **not** replace them as
evidence either. The manuscript names each one (`\code{envelope.py}`,
`\code{zeroside_check.py}`, `\code{bridge.py}` and the five `v*.py`) and
`appendix:571` asserts the census "the full census lives in
`hipotesis/pruebas/` ($83$ scripts)", which deleting eight rows would
falsify — and the manuscript is out of scope for this campaign.
`bridge.py` additionally has a runner, `correr_todo.sh`, which
regenerates its committed `salidas/bridge.txt`: `dependency:correr_todo.sh`.
So all 8 stay; whether the folder goes is the last wave's call.

**Deletion pass (wave P2):** none of the 16 scripts this wave ports was
removed from `hipotesis/pruebas/`, and none of the two scaffolding rows
either. Measured first: `git grep -E 'import retro|from retro'` over the
repository is empty — four of the family `exec` another's source *by path*,
which is a dependency, not an import — so nothing outside them would break,
but the test does not replace them as evidence either. Every one of the 16 is
named by the manuscript (`\code{retro101.py}` … `\code{retro99.py}`, one or
two `git grep` hits each, `retro81`/`retro87` inside the range at
`04-bridges:1725`), so all 16 rows are `census-cited` and stay: deleting them
would falsify the census of `appendix:571` ("the full census lives in
`hipotesis/pruebas/` ($83$ scripts)"), and the manuscript is out of scope for
this campaign. `retro66.py` is `census-cited` as well (`04-bridges:1502`,
`appendix:263`) and additionally cannot run: `retro65.py` was never
delivered, which its row now records as `blocked:retro65-never-delivered`.
`retro83.py` and `retro86.py` are named by no statement, but
`retro87/88/89.py` `exec` them by path — deleting either would break three
delivered scripts — so both stay as the scaffolding the reconciliation
already records (status `absorbed`). No `retro` has a committed
`salidas/*.txt`, so no row of this family could be `absorbed-into:<test>`.

**Deletion pass (wave P3):** none of the 9 scripts this wave ports was
removed from `hipotesis/pruebas/`, nor the tenth of the family
(`weil_certificates/zeroside_check.py`, already ported in P1). Measured
first: six are `census-cited` — `cert.py` (`04-bridges:573`,
`04-bridges:577`, `appendix:577`), `op_rig_validated.py`
(`04-bridges:524`, `04-bridges:555`, `appendix:42`, `appendix:578`),
`verify_iv.py` (`04-bridges:493`, `04-bridges:555`, `appendix:41`,
`appendix:578`), `verify_rig.py` (`04-bridges:517`), `rigW.py`
(`04-bridges:552`, `appendix:577`) and `opcert_rig.py`
(`appendix:578`) — so all six stay. The two scaffolding rows are
imported inside the family (`lp.py` by `cert.py`, `opcert.py`,
`op_rig_validated.py`, `opcert_rig.py`; `opcert.py` by
`zeroside_check.py`), so deleting either would break delivered scripts —
they stay with status `absorbed`. `verify_cert.py` is the only row with
neither citation nor importer, but it is what writes `cert_L1.0.json`
and `cert_L0.95.json` — the certificate named at `04-bridges:493` and
read by `verify_iv.py` and `verify_rig.py` — and deleting any of the 83
would falsify the census of `appendix:571` ("the full census lives in
`hipotesis/pruebas/` ($83$ scripts)"), so it stays as the
`orphan-no-cited` P1 recorded. No member of the family appears in
`correr_todo.sh` (measured), and the manuscript is out of scope.

**Reconciliation against the suite (measured today, not assumed):**

* **62 of 83** scripts are covered — **32 rows `absorbed`**, of which
  **28** are `verified-against-corpus`: an existing test reads the
  script's committed output (**27** of them the `salidas/<name>.txt` of
  the sub-table below; `comun.py` through the pins its consumers have in
  `test_golden_n_marks.py`) — the other **4** are scaffolding absorbed
  into the corpus they feed (`retro83.py`, `retro86.py`,
  `weil_certificates/lp.py`, `weil_certificates/opcert.py`) — plus the
  **30 rows ported by waves P1–P3**: the 8 of `test_envelope_bounds`,
  `test_bridge_boosts` and `test_v_layer_claims`, the 16 of
  `test_retro_sprints`, and the 6 of `test_weil_certificates`, whose
  tests recompute the number from the committed inputs and assert the
  figure the `.tex` statement prints.
* The 202 tests live in 20 modules; the covering ones are
  `test_golden_observations.py` (4 observation outputs),
  `test_golden_n_marks.py` (23 outputs behind the bare `N` marks) and
  `test_arch_window.py`, plus the five modules waves P1–P3 added.
* **74 of 83** scripts are cited in the manuscript (line hits measured);
  **9 are not**: the 4 true orphans plus 5 scaffolding modules.
  `SCRIPTS-RECON-003.md` counted 75 cited / 8 uncited — the difference
  is `weil_certificates/lp.py`, which the recon marks as cited in 04 but
  which has **0 line hits** today; it is reclassified here as scaffolding
  without citation.

## Sub-table: `salidas/` (35)

What each committed output feeds. Six committed outputs still have
no test: the script's claim is in the text and its output is already in
the tree, so the port is a reader, not a rerun (`_registro.txt` is the
index of the set, not a script's output).

| salida | productor | alimenta | status |
|---|---|---|---|
| `_registro.txt` | — | índice del conjunto (no es salida de un script) | — |
| `amplitud_clausula_ii.txt` | `amplitud_clausula_ii.py` | `test_residual_scales_are_pinned` | `verified-against-corpus` |
| `arch_window.txt` | `arch_window.py` | `test_arch_window_crossings_are_pinned` | `verified-against-corpus` |
| `balance.txt` | `balance.py` | `test_orbit_balance_is_pinned` | `verified-against-corpus` |
| `blocks.txt` | `blocks.py` | `test_fejer_window_is_pinned` | `verified-against-corpus` |
| `bridge.txt` | `bridge.py` | `test_bridge_boosts_golden_values` | `verified-against-corpus` |
| `castelnuovo.txt` | `castelnuovo.py` | `test_castelnuovo_golden_values`, `test_castelnuovo_matches_manuscript_claim` | `verified-against-corpus` |
| `circle_and_detect.txt` | `circle_and_detect.py` | `test_circle_and_detect_golden_values`, `test_circle_and_detect_matches_manuscript_claim` | `verified-against-corpus` |
| `classes_test.txt` | `classes_test.py` | golden candidato de `test_closures_and_sweeps.py` | `pending` |
| `corrected_operator.txt` | `corrected_operator.py` | `test_corrected_operator_golden_values`, `test_corrected_operator_matches_manuscript_claim` | `verified-against-corpus` |
| `dedekind.txt` | `dedekind.py` | `test_orbit_balance_is_pinned` | `verified-against-corpus` |
| `dh.txt` | `dh.py` | `test_additive_side_statistics_are_pinned` | `verified-against-corpus` |
| `escala_ceros_bajos.txt` | `escala_ceros_bajos.py` | `test_residual_scales_are_pinned` | `verified-against-corpus` |
| `euler_link.txt` | `euler_link.py` | `test_euler_link_second_term_is_pinned` | `verified-against-corpus` |
| `fejer_check.txt` | `fejer_check.py` | `test_fejer_window_is_pinned` | `verified-against-corpus` |
| `fermat_quintic_points.txt` | `fermat_quintic_points.py` | `test_fermat_quintic_point_counts_are_pinned` | `verified-against-corpus` |
| `fibres.txt` | `fibres.py` | `test_orbit_balance_is_pinned` | `verified-against-corpus` |
| `field_signature.txt` | `field_signature.py` | `test_field_signature_is_pinned` | `verified-against-corpus` |
| `gram.txt` | `gram.py` | `test_intersection_form_signature_is_pinned` | `verified-against-corpus` |
| `kisin.txt` | `kisin.py` | `test_kisin_interpolation_is_pinned` | `verified-against-corpus` |
| `law_resolution.txt` | `law_resolution.py` | `test_law_resolution_golden_values`, `test_law_resolution_matches_manuscript_claim`, `test_zero_side_correction_matches_the_manuscript` | `verified-against-corpus` |
| `mertens341.txt` | `mertens341.py` | `test_additive_side_statistics_are_pinned` | `verified-against-corpus` |
| `mobius.txt` | `mobius.py` | `test_additive_side_statistics_are_pinned` | `verified-against-corpus` |
| `offline.txt` | `offline.py` | `test_offline_minimum_stays_positive` | `verified-against-corpus` |
| `orbita_cert.txt` | `orbita_cert.py` | golden candidato de `test_closures_and_sweeps.py` | `pending` |
| `rho_interval.txt` | `rho_interval.py` | golden candidato de `test_closures_and_sweeps.py` | `pending` |
| `rigorous_chain.txt` | `rigorous_chain.py` | golden candidato de `test_closures_and_sweeps.py` | `pending` |
| `sweep.txt` | `sweep.py` | golden candidato de `test_closures_and_sweeps.py` | `pending` |
| `t1_index.txt` | `t1_index.py` | `test_angular_index_statistics_are_pinned` | `verified-against-corpus` |
| `t2_loo.txt` | `t2_loo.py` | `test_angular_index_statistics_are_pinned` | `verified-against-corpus` |
| `teich.txt` | `teich.py` | `test_delta_p_tower_ratios_are_pinned` | `verified-against-corpus` |
| `testB1b.txt` | `testB1b.py` | `test_fluctuation_law_is_the_same_everywhere` | `verified-against-corpus` |
| `testGeom.txt` | `testGeom.py` | `test_fluctuation_law_is_the_same_everywhere` | `verified-against-corpus` |
| `w4exact.txt` | `w4exact.py` | golden candidato de `test_closures_and_sweeps.py` | `pending` |
| `zeroside.txt` | `zeroside.py` | `test_zeroside_orbit_agrees_with_the_zeros` | `verified-against-corpus` |

## Sub-table: `datos/` (12)

The 12 `datos/` rows of the zip1 delivery: 10 never delivered (0
readers in the repo — their omission breaks nothing, but the zip's
MANIFEST no longer describes this tree) plus the 2 deferred files that
are cited and are **already in the tree** (commit `1d7f376`,
`chore(scripts): port the two delivered deferred files`).

| archivo | qué es | estado | status |
|---|---|---|---|
| `datos/CW_EQUIVALENCIAS.md` | equivalencias CW citadas en `appendix.tex:461` | portado — commit `1d7f376` (el par diferido ya está en el árbol) | n/a (dato) |
| `datos/fqn_map.json` | mapa fqn citado en `appendix.tex:730` | portado — commit `1d7f376` (el par diferido ya está en el árbol) | n/a (dato) |
| `datos/ceros_zeta.json` | ceros de ζ declarados en el MANIFEST del zip1 | pendiente — nunca entregado (0 lectores en el repo) | `pending` |
| `datos/ordenes_600000.pkl` | órdenes hasta 6·10⁵ (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/ordenes_1400000.pkl` | órdenes hasta 1.4·10⁶ (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/registro_unificado.txt` | registro del run unificado (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/registro_unificado_historicos.txt` | registro histórico (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/registro_verificar_todo.txt` | registro de verificación total (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/v17.log` | log del run v17 (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/v18.log` | log del run v18 (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/v19.log` | log del run v19 (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |
| `datos/v32.log` | log del run v32 (MANIFEST zip1) | pendiente — nunca entregado (0 lectores) | `pending` |

Already in the tree and out of the 12: `datos/capas_hasta_1000000000.json`,
`datos/familias_hasta_1000000000.json`, `datos/ceros_nivel80.json`,
`datos/ceros_nivel135.json`, `datos/ordenes_1000000.pkl`,
`datos/torcidos135.json` (import `a475748`), plus the root data
`chi5_zeros.json`, `chi5_zeros_500.json`, `chi5_zeros_T80.txt`,
`dh_zeros.json`, `zeta_zeros_3000.npy` and the four
`weil_certificates/` artefacts (three now pinned by
`tests/test_weil_certificates.py`: `cert_L1.0.json`,
`op_rig_validated_output.json`, `verify_iv_L1.0_output.txt`;
`cert_L0.95.json` is uncited and unpinned).

## Sub-table: huérfanos (4) y andamiaje sin cita (5)

The 4 true orphans — delivered, never cited anywhere in the `.tex`, no
claim of their own:

| script | origen | papel real | destino |
|---|---|---|---|
| `ceros_chi5_500.py` | zip2 | genera `chi5_zeros_500.json`, que leen `circle_and_detect.py` y `comun_pruebas.py` | `orphan-no-cited` |
| `comun_pruebas.py` | zip2 | utilidades (criba, Λ, caracteres mod 20, fibras) importadas por 22 scripts | `orphan-no-cited` |
| `cuintica.py` | zip2 | la capa quintica `a(p^k)`; la importa `orbita_cert.py` | `orphan-no-cited` |
| `weil_certificates/verify_cert.py` | zip1 | verifica un certificado JSON contra la cota que declara; andamiaje declarado en el MANIFEST, 0 importadores y 0 citas; su artefacto `cert_L1.0.json` lo fija `test_certificate_json_declares_the_manuscript_pairs_and_lipschitz` | `orphan-no-cited` |

And the 5 modules with no citation either (scaffolding, not a gap —
they carry no claim of their own): `comun.py`, `retro83.py`,
`retro86.py`, `weil_certificates/lp.py`, `weil_certificates/opcert.py`.
`weil_certificates/verify_cert.py` left this list in wave P1: 0
importers, 0 citations and no claim of its own, so it is recorded as
`orphan-no-cited` in the table above — the author still decides whether
to cite it where it is used or drop it.

## Sub-table: `retro65.py` — never delivered

`retro66.py:99-101` does
`exec(compile(open(__file__.replace("retro66.py","retro65.py")).read(), …))`
and `retro65.py` is in no delivery: not zip1, not zip2, not the repo,
not the MANIFEST's "not available" list. **`retro66.py` does not run as
it stands**, and `retro66.py` is cited (`04-bridges:1502`,
`appendix:263`). Row status: `blocked:retro65-never-delivered` — ask the author for the file or declare it unavailable in the
text.

## Sub-table: `unfold_by_conductor.txt` — cited, never delivered

`src/chapters/04-bridges.tex:107` cites `unfold_by_conductor.txt`; it
came in neither zip and it is not even in the zip1 MANIFEST's
"citados y no disponibles" list (36 entries, this is not one of them).
It is the third of the three `pending(D7)` markers of
`docs/witness-inventory.md:45` — the only one still open after
`1d7f376` ported the other two. Status: `blocked:no entregado por el autor`.

## Sub-table: `zeros.txt` / `chi5_zeros_T80.txt` — settled: the copy is committed

`envelope.py:3` and `weil_certificates/zeroside_check.py:5` open
`'zeros.txt'`. The zip1 MANIFEST says it explicitly: *"`envelope.py`
reads `zeros.txt`; the zeros of $L(s,\chi_5)$ up to $T=80$ are in
`chi5_zeros_T80.txt`"*, and the copy is now in the tree: commit
`7b0c68f` added `hipotesis/pruebas/zeros.txt`, byte-identical to
`chi5_zeros_T80.txt` (both tracked). Both readers run `exit 0` —
`envelope.py` from `hipotesis/pruebas/`, `zeroside_check.py` from the
same directory with `weil_certificates/` on the path (it imports
`opcert`). The earlier `blocked:zeros.txt no existe` was recon data
predating `7b0c68f`; both rows now carry their test,
`tests/test_envelope_bounds.py`, which reads the committed copy. The
zeros stay input to the envelope and zero-side checks, not a claim of
the paper — recomputing them per test would only add runtime.

## Sub-table: `__pycache__/`

`hipotesis/pruebas/__pycache__/` (and `tests/__pycache__/`) are already
covered by `.gitignore` (`__pycache__/`, `*.py[cod]`) — nothing to port,
nothing to track; listed here so the inventory of
`hipotesis/pruebas/`'s 171 entries closes at 83 `.py` + 35 `salidas/` +
`datos/` + `weil_certificates/` + `correr_todo.sh` + `__pycache__/`.

---

## Related documents

- `docs/reports/20261123_F10-001_pytest_suite_port.md` — the pattern this campaign extends.
- `scratch` inventory reconciled here: promoted to `docs/reports/20261126_SCRIPTS-RECON-003_scripts_reconciliation.md`.
- `tests/README.md` — suite layout, tolerances and the golden artifacts.
