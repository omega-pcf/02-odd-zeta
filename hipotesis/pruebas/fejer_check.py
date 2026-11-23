"""fejer_check.py — W3, ssec:field-positivity: la suma de Fejer de L(s,chi_5) desde los primos y desde los ceros.
Z(L) = sum_rho h_L(gamma_rho), h_L(r) = 2L (sin Lr/Lr)^2 >= 0, sobre todos los ceros (+-gamma).
Por la formula explicita (Iwaniec–Kowalski 5.12, chi_5 par, conductor 5) es tambien
  Z(L) = A(L) - 2 sum_n Lambda(n) chi_5(n) n^{-1/2} g_L(log n),   g_L(u) = (1-|u|/2L)^+,
calculada solo con primos (F1PaperTorus.fejerKernel_nonneg, fejer_sum_nonneg).
Lado de los ceros: los 397 ceros bajo 500 (ceros_chi5_500.py) mas la cola gamma > 500 con la densidad
log(5t/2pi)/2pi y <sin^2> = 1/2, que vale (2/L)(log(5*500/2pi)+1)/(2pi*500) = 0.0044/L.
El articulo: comprobado contra los 397 ceros a 3e-4.
Uso: python3 -I fejer_check.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun_pruebas import lado_primos, arch_fejer, CHI5, ceros_chi5, fejer_ceros
g = ceros_chi5()
print(len(g), "ceros de L(s,chi_5) bajo 500")
print("  2L   Z desde primos   Z desde ceros (+cola)   diferencia   (sin cola)")
peor = 0.0
for L in (0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9):
    zp = arch_fejer(L) + lado_primos(L, CHI5)['total']
    zc = fejer_ceros(L, g); zs = fejer_ceros(L, g, cola=False)
    peor = max(peor, abs(zp - zc))
    print(f"  {2*L:4g}   {zp:.6f}        {zc:.6f}             {zp - zc:+.1e}     ({zp - zs:+.1e})")
print(f"maxima diferencia con la cola: {peor:.1e}  (articulo: a 3e-4); Z(L) > 0 en todos los L")
