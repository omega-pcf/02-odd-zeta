# Equivalencias: el Lean de The Crystalline Worldsheet contra el corpus

El paper citaba 100 declaraciones del Lean de CW (`CW6_complete_v2.lean`). Resultado de la revisión, ecuación por ecuación:

- **24** ya estaban en el corpus: con el mismo nombre (5) o con otro nombre y el mismo enunciado o contenido.
- **20 grupos** no estaban en el corpus y ahora se prueban en `F1_cw_equivalents.lean` (namespace `F1CW`), solo con Mathlib.
- Las **4** que faltaban en la demostración (`euler_from_ideals_K`, `coeff_stabilises_K`, `colimit_exists_K`, `even_L_rationality`) se integraron desde el extracto de CW6 que proporcionó el autor, con sus definiciones y pruebas tal cual, en `F1_cw_equivalents.lean` (§4).
- **39** quedan como del Lean de CW, marcadas con † en el paper, **todas en la Discusión** (§27, física de CW). La cadena de demostración de las Partes I–V no cita ninguna.

Con esto el proyecto Lean ya no importa el archivo de CW: `F1_v2_formalizations` y el paper dependen del corpus y de `F1_cw_equivalents`.

## 1. Ya en el corpus

| Nombre en CW | Dónde en CW | Equivalente en el corpus | Archivo | Relación |
|---|---|---|---|---|
| `mersenne_bridge` | (1.14) | `mersenne_bridge` | F1_compilado_sin_axiomas | mismo nombre |
| `lambda_log` | (1.14) | `lambda_log` | F1_compilado_sin_axiomas | mismo nombre |
| `conductor_is_derived` | (2.61) | `conductor_is_derived` | F1_PCF_session_modules | mismo nombre |
| `extreme_case_is_binary` | Prop. 2.79 | `extreme_case_is_binary` | PCF_sesion_completa | mismo nombre |
| `E_iff_no_shared_ordinate` | Thm. 2.83 | `E_iff_no_shared_ordinate` | PCF_sesion_completa | mismo nombre |
| `binet_general` | (2.34) | `fib_pow_aux` | F1_spectra_anchor_G_standalone | mismo enunciado |
| `psi_functorial` | Prop. 2.44 | `psi_comp` | F1_compilado_sin_axiomas | mismo enunciado (en exponentes) |
| `psi_on_powers` | Def. 2.42 | `psi_add, psi` | F1_compilado_sin_axiomas | mismo objeto |
| `phi_root_unique` | Thm. 2.14 | `golden_fixed_point_unique` | F1_compilado_sin_axiomas | mismo enunciado |
| `galois_conj_is_one_sub` | §2.1 | `phi_bar_eq` | F1_compilado_sin_axiomas | mismo enunciado |
| `collapse_norm_product` | Thm. 2.32 | `norm_Omega_is_half` | F1_compilado_sin_axiomas | mismo enunciado |
| `omega_eigenvalues` | Prop. 2.19 | `eigenvalue_half, positive_spectral_half` | F1_compilado_sin_axiomas | mismo contenido |
| `anchor_is_exterior` | (1.14) | `lambda_is_not_an_integer, two_not_in_golden_lattice` | PCF_unificado | mismo enunciado |
| `L1_from_class_number_formula` | (2.55) | `anchor_is_a_crossed_identity` | PCF_sesion_completa | mismo contenido (CNF como entrada) |
| `entropy_bridge` | (2.55) | `branches_meet_at_log_two` | PCF_sesion_M12_unificado | mismo enunciado |
| `theta_fixed_point_unique` | (2.47) | `selfdual_fixed_point` | PCF_sesion_M12_unificado | mismo enunciado |
| `four_cocone` | §2.12 | `conductor_is_joint_period` | F1_PCF_session_modules | mismo contenido |
| `odd_zeta_ratio` | Thm. 2.62 | `zeta_odd_pentagonal_determination` | F1_compilado_sin_axiomas | más fuerte en el corpus |
| `regge_tower_is_euler_product` | Prop. 2.47 | `euler_product_identity (+ F1CW.dirichlet_is_euler)` | F1_compilado_sin_axiomas | mismo contenido |
| `towerHam` | §5 | `towerH` | PCF_sesion_M12_unificado | misma definición |
| `local_dedekind_*_K` | (2.44) | `local_factor_identity (+ F1CW.local_dedekind_*_K)` | F1_compilado_sin_axiomas | mismo contenido |
| `framework_colimit` | §3.5 | `apex_colimit_universal` | PCF_sesion_M12_unificado | mismo tipo de enunciado (solo Discusión) |
| `bulk_boundary_isometry` | (3.19) | `isometry_with_common_modulus₅` | PCF_sesion_2026_08_18_unificado | mismo contenido (solo Discusión) |
| `repulsion_excludes_the_extreme_case` | Prop. 2.82 | `repulsion_excludes_zero_spacing` | PCF_sesion_2026_08_18_unificado | contenido cercano (solo Discusión) |

## 2. Probadas ahora en `F1_cw_equivalents.lean`

| Nombre en CW | Enunciado |
|---|---|
| `pi_eq_five_arccos` | π = 5 arccos(φ/2) |
| `norm_cosine_phi` | |2cos(πa/5)| = φ^{χ₅(a)} |
| `psi_not_additive` | φ^{2p} ≠ φ^p + 1, p ≥ 2 |
| `even_zeta_bernoulli` | ζ(2k) por Bernoulli (Mathlib) |
| `degree_formula_K` | Σ eᵢfᵢ = 2 |
| `ideal_norm_values_K` | normas p, p² |
| `von_mangoldt_k_values` | log p, 2 log p |
| `period_eq_two_pi_regulator` | T = 2πR_K |
| `lambda_log_mul_regulator` | λ_log log φ = log 2 |
| `s_duality_fixes_i` | −1/i = i |
| `hinge_central_charge, brown_henneaux_c_eq_three` | 3/(2G) = 3 ⟺ G = ½ |
| `triad_trace_zero, triad_two_products` | traza 0, producto 2⁻⁵ |
| `sineKernel_at_nonzero_integer` | K(n) = 1 |
| `five_is_the_unique_prime_with_four_units` | p − 1 = 4 ⟹ p = 5 |
| `binary_period_lives_in_the_five_component` | 2⁴ ≡ 1, 2² ≡ −1 (mod 5) |
| `kappa_per_real_place, kappa_k_two_real_places, kappa_k_simple_pole` | κ_ℚ = u²/(u²−1), κ_K = 2κ_ℚ, polo simple |
| `tower_ham_is_hermitian` | diag(m₀φ^i) hermitiano |
| `minkowski_bound_lt_two, class_number_one_K` | √5/2 < 2; h_K = 1 dado Minkowski |
| `pentagon_log_signature` | sin(2π/5)/sin(π/5) = φ |
| `bernoulli_eval_rational` | B_n(a/5) ∈ ℚ |

## 3. Solo en el Lean de CW (marcadas † en el paper, todas en §27)

**Solo en la Discusión (§27, la física de CW):**

- `CWfig.binary_entropy_half`
- `CWfig.weinberg_angle_gut`
- `CurvatureCoeffs.G_AB_pcf`
- `CurvatureCoeffs.R_scalar_pcf`
- `CurvatureCoeffs.lambda5_pcf`
- `GravitySectorPCF.ds_first_law`
- `GravitySectorPCF.komar_first_law`
- `GravitySectorPCF.modular_generator_is_entropy`
- `GravitySectorPCF.modular_generator_is_tower`
- `PCF.CW5.regge_residue_degree`
- `PCF.CW5.regge_residue_ne_zero`
- `PCFEntropyDOF.a2_gram_det`
- `PCFEntropyDOF.a2_minimal_vectors_exactly_six`
- `PCFEntropyDOF.beta_is_mssm`
- `PCFEntropyDOF.binary_entropy_le_one`
- `PCFEntropyDOF.ladder_dim_eq_kissing_plus_rank`
- `PCFEntropyDOF.lattice_radius_conjugate`
- `PCFEntropyDOF.rho_is_state`
- `PCFEntropyDOF.tower_start`
- `PCFEntropyDOF.two_positivities_distinct`
- `PaperMobius.fibre_independent_of_base`
- `PaperMobius.fibre_monodromy`
- `PaperMobius.fibre_reflection_order_two`
- `PaperS2.certainty_principle`
- `PaperS2.faceLine_apex`
- `PaperS2.mu_diagram_commutes`
- `PaperS3a.S_tower_recurrence`
- `PaperS3a.bulk_boundary_intertwine`
- `PaperS3a.modular_bulk_ratio_level_independent`
- `PaperS3a.tower_e_eq_exp_regulator`
- `SitterPCF.ds_temperature_pos`
- `TwoTowersOneMicrostate.no_privileged_level`
- `V11fig.omega_flow_invariant`
- `four_faces_one_datum`
- `framework_partition_eq_completed_zeta`
- `places_assembly`
- `projector_frame_invariant`
- `selfdual_gaussian_unique`
- `tower_first_law`

## 4. κ_K

El corpus tenía dos funciones con ese nombre. La del paper es la de CW, κ_ℚ(u) = u²/(u²−1) por lugar real y κ_K = 2κ_ℚ, ahora en `F1CW.kappaK`. El `kappa_K` de `F1_compilado_sin_axiomas` es otra función, u²(log u + ½ log 5)/(u²−1), y el paper no la usa.

## 5. Nota sobre `local_factor_identity`

El extracto de CW6 dice que `local_factor_identity` "no está definido en el corpus actual;
sólo se lo cita". Sí está: `F1_compilado_sin_axiomas.lean`, línea 1148, con prueba
(f_ζ · f_L = f_K en cada primo p, los tres casos). Lo que no estaba en el folder del
proyecto al final era el archivo mismo, que ahora vive dentro de `F1Paper_unified`.
