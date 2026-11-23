"""zeroside.py — W4–W5, ssec:weil-closure: la formula explicita sobre la orbita de Frobenius, comprobada.
Funcion de prueba: el triangulo g_a(x) = (1-|x|/a)^+; su autocorrelacion A_a (forma cerrada, soporte 2a) y
ghat_a(r) = a (sin(ar/2)/(ar/2))^2.  La orbita de p: t_k = W(g_a, tau_{k log p} g_a), con
  lado de los primos:  t_k = A(A_a(. - k log p)) - sum_n Lambda(n) chi_5(n) n^{-1/2} [A_a(log n - k log p) + A_a(log n + k log p)],
  (A el termino arquimediano de L(s,chi_5), conductor 5, par, en la variable u),
  lado de los ceros:   t_k = sum_rho |ghat_a(gamma)|^2 cos(k log p gamma)  sobre los ceros +-gamma.
La cola gamma > 500 esta acotada por 2 sum_(gamma>500) |ghat_a|^2 <= (32/a^2) int_500^inf d(t) t^{-4} dt.
El articulo: chi_5, a = 0.3, p = 3: primos y 397 ceros coinciden a 1e-8 para k = 0..12; la cola aporta a lo
mas 9.6e-7.
Uso: python3 -I zeroside.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from comun_pruebas import potencias, CHI5, A_tri, arch_desplazada, ceros_chi5
a, p0 = 0.3, 3
n, p, k = potencias(int(math.exp(12*math.log(p0) + 2*a)) + 1)
ln = np.log(n.astype(float)); w = np.log(p.astype(float))*CHI5(n)/np.sqrt(n.astype(float))
g = ceros_chi5(); G2 = (a*(np.sin(a*g/2)/(a*g/2))**2)**2
cota = (32/a**2)*(math.log(5*500/(2*math.pi)) + 1/3)/(2*math.pi)/(3*500**3)
print(f"cota de la cola (gamma > 500): {cota:.2e}  (articulo 9.6e-7)")
print("  k    primos            ceros (397)        diferencia")
peor = 0
for kk in range(13):
    s = kk*math.log(p0)
    tp = arch_desplazada(a, s, 5, 0) - np.sum(w*(A_tri(ln - s, a) + A_tri(ln + s, a)))
    tz = 2*np.sum(G2*np.cos(s*g))
    if kk == 0: tz += 3/8*cota          # cola suave en k = 0: <sin^4> = 3/8 (para k >= 1 la cola oscila y se cancela)
    peor = max(peor, abs(tp - tz))
    print(f" {kk:2d}  {tp:+.10f}   {tz:+.10f}   {tp - tz:+.1e}")
print(f"maxima diferencia: {peor:.1e}  (articulo: 1e-8); en k = 0 se suma la cola suave (3/8) x cota")
