"""bridge.py — W3, prop:bridge-boosts: rotaciones sobre la linea, boosts fuera de ella.
Con las ocho funciones de prueba de gram.py (ghat_0 = T^, ghat_j = 2cos(jr) T^, T^(r) = (sin(r/2)/(r/2))^2),
un cuadruple de ceros fuera de la linea, rho = 1/2 + delta + i gamma y sus companeros, tiene alturas
gamma_rho = +-gamma +- i delta y aporta a la forma de Weil la matriz C = sum ghat(gamma_rho) ghat(gamma_rho)^T
= 4 Re(w w^T) = 4(a a^T - b b^T), w = ghat(gamma + i delta) = a + i b: un plano hiperbolico, signatura (1,1)
(prop:bridge-boosts (ii)).  La traslacion por log p multiplica el modo de gamma_rho por e^{i log p gamma_rho},
de modulo p^{-+delta}: un boost de rapidez delta log p (prop:bridge-boosts (i)).
El articulo: con gamma = 20 y delta = 0.1, autovalores -1.4e-4 y +5.3e-4; la traslacion por log 7 escala
los dos miembros por 1.2148 y 0.8232, de producto 1.
Uso: python3 -I bridge.py"""
import numpy as np, math, cmath
J = 8; gam, d = 20.0, 0.1
def ghat(z):
    T = (cmath.sin(z/2)/(z/2))**2
    return np.array([T if j == 0 else 2*cmath.cos(j*z)*T for j in range(J)])
alturas = [complex(gam, -d), complex(-gam, -d), complex(-gam, d), complex(gam, d)]
C = sum(np.outer(ghat(z), ghat(z)) for z in alturas)
print(f"parte imaginaria de C: {np.max(np.abs(C.imag)):.1e} (C es real)")
ev = np.linalg.eigvalsh(C.real)
nz = ev[np.abs(ev) > 1e-12*np.max(np.abs(ev))]
print(f"autovalores no nulos de C: {', '.join(f'{x:+.2e}' for x in nz)}  (rango {len(nz)}, signatura (1,1))")
for p in (7,):
    f1 = abs(cmath.exp(1j*math.log(p)*complex(gam, -d))); f2 = abs(cmath.exp(1j*math.log(p)*complex(gam, d)))
    print(f"traslacion por log {p}: modulos {f1:.4f} y {f2:.4f}, producto {f1*f2:.6f}; rapidez delta log p = {d*math.log(p):.4f}")
print("articulo: -1.4e-4 y +5.3e-4; 1.2148 y 0.8232, producto 1")
