"""offline.py — W3, ssec:field-positivity: un cero fuera de la linea vuelve negativa la suma de Fejer.
Z(L) = sum_rho h_L(gamma_rho), h_L(z) = 2L (sin Lz/Lz)^2, sobre los 397 ceros de L(s,chi_5) bajo 500
(+-gamma) mas la cola gamma > 500 (densidad log(5t/2pi)/2pi, <sin^2> = 1/2).  Un cuadruple fuera de la
linea, rho = 1/2 + delta + i gamma con sus companeros conj(rho), 1-rho, 1-conj(rho), entra con
4 Re h_L(gamma + i delta), de tamano ~ e^{2L delta}/(2L gamma^2) y signo oscilante.
El articulo: con el cuadruple en gamma = 100, Z < 0 en 2L ~ 63 (delta = 0.1) y en 2L ~ 127 (delta = 0.05);
sin el, el minimo sobre 2L en [2, 240] es +6.3e-4.
Uso: python3 -I offline.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math
from comun_pruebas import ceros_chi5
g = ceros_chi5(); T = 500.0
def Z(L, cola=True):
    s = 2*np.sum(2*L*(np.sin(L*g)/(L*g))**2)
    if cola: s += (2/L)*(math.log(5*T/(2*math.pi)) + 1)/(2*math.pi*T)
    return s
def cuadruple(L, gam, d):
    z = complex(gam, d)
    return 4*(2*L*(np.sin(L*z)/(L*z))**2).real
dosL = np.arange(2.0, 240.0 + 1e-9, 0.01)
base = np.array([Z(x/2) for x in dosL]); base0 = np.array([Z(x/2, cola=False) for x in dosL])
i = np.argmin(base)
print(f"sin cuadruple: min_(2L en [2,240]) Z = {base[i]:+.2e} en 2L = {dosL[i]:.2f}"
      f"  (sin la cola: {base0.min():+.2e});  articulo: +6.3e-4")
for d in (0.1, 0.05):
    for paso in (0.1, 0.001):
        xs = np.arange(2.0, 240.0 + 1e-9, paso)
        tot = np.array([Z(x/2) + cuadruple(x/2, 100.0, d) for x in xs])
        j = np.nonzero(tot < 0)[0]
        print(f"cuadruple en gamma = 100, delta = {d}, malla de 2L con paso {paso}: primer Z < 0 en 2L = {xs[j[0]]:.3f}")
print("articulo: 2L ~ 63 (delta = 0.1) y ~ 127 (delta = 0.05).  El termino del cuadruple oscila con periodo")
print("2 pi/gamma = 0.063 en 2L, asi que el primer cruce depende de la malla; log(gamma)/delta = 46 y 92.")
