# Odd Zeta Values from the PCF Torus: φ and π as Arithmetic-Geometric Sources

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19492791.svg)](https://doi.org/10.5281/zenodo.19492791)
[![Project Page](https://img.shields.io/badge/Project%20Page-omega--pcf.com-blue)](https://omega-pcf.com/odd-zeta)

## Authors

**Jorge Armando González García**¹, **Víctor Manuel González García**¹, **Itzel Marion Dressler Pérez**², **Luz María García Ordóñez**¹

¹ *TTAMAYO PUNTO COM, S.A.P.I. de C.V., Research & Development Division, Mexico*
² *Independent Researcher*

---

## Abstract

We demonstrate that the odd values $\zeta(2k+1)$ of the Riemann zeta function are structurally determined by $\varphi=(1+\sqrt{5})/2$ and $\pi$. The Euler product of $\zeta$ is built from local factors $f_p(s)$, one for each prime. We prove that the Frobenius lift $\varphi^p = F_p\varphi + F_{p-1}$—where $F_n$ is the $n$-th Fibonacci number—determines the splitting type of every prime $p$ in $\mathbb{Z}[\varphi]$, and hence every $f_p(s)$. Through the Dedekind factorisation $\zeta(s) = \zeta_{\mathbb{Q}(\sqrt{5})}(s)/L(s,\chi_5)$, this determines $\zeta(s)$ completely: the isomorphism between the Frobenius structure and the Euler product is demonstrated at every level (primes, splitting types, local factors, $L$-function), anchored by the base case $L(1,\chi_5) = 2\log\varphi/\sqrt{5}$ (the class-number formula for $\mathbb{Q}(\sqrt{5})$), which expresses the $L$-function value entirely in terms of $\varphi$. This resolves the apparent freedom of $\zeta(2k+1)$ noted by Elvang, Herderschee and Morales in the $\mathcal{N}=4$ SYM S-matrix bootstrap: those values are free only relative to the EFT; the pentagonal arithmetic fixes them.

**Keywords:** Riemann zeta function, Odd zeta values, Apéry's constant, S-matrix bootstrap, Modular bootstrap, AdS/CFT correspondence.

## Citation

González García, J. A., González García, V. M., Dressler Pérez, I. M., & García Ordóñez, L. M. (2026). *Odd Zeta Values from the PCF Torus: φ and π as Arithmetic-Geometric Sources*. Preprint prepared for SIGMA (Symmetry, Integrability and Geometry: Methods and Applications). DOI: [10.5281/zenodo.19492791](https://doi.org/10.5281/zenodo.19492791).

```bibtex
@article{Gonzalez2026OddZeta,
  author  = {González García, J. A. and others},
  title   = {Odd Zeta Values from the PCF Torus: φ and π as Arithmetic-Geometric Sources},
  journal = {Preprint},
  year    = {2026},
  doi     = {10.5281/zenodo.19492791},
  url     = {https://doi.org/10.5281/zenodo.19492791},
  note    = {Preprint prepared for SIGMA (Symmetry, Integrability and Geometry: Methods and Applications)}
}
```

## Structure

- `/src`: LaTeX manuscript sources.
- `/lean`: Formal verification of the arithmetic structures.
- `/scripts`: Verification and figure generation tools.

## Verification

To verify the formal results:
```bash
pnpm run verify
```
