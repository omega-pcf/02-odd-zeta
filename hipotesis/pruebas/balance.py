"""balance.py — W3, ssec:field-positivity: la positividad como balance entre los dos tipos de orbita de Klein.
Z(L) = A(L) - 2 sum_n Lambda(n) chi_5(n) n^{-1/2} g_L(log n), g_L(u) = (1-|u|/2L)^+, a 2L = 18
(primos bajo e^18), separado en: primos partidos (chi_5(p) = +1: orbitas degeneradas), inertes
(chi_5(p) = -1: la orbita libre), el termino arquimediano A(L) y las potencias k >= 2.
El articulo: partidos -1787.59, inertes +1796.72, arquimediano -3.29, potencias -5.83, Z = 0.0113;
las dos orbitas se cancelan al 0.5%; queda el conductor mas los cuadrados.
Uso: python3 -I balance.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun_pruebas import lado_primos, arch_fejer, CHI5
L = 9.0
d = lado_primos(L, CHI5); A = arch_fejer(L)
Z = A + d['total']
print(f"2L = {2*L:g} (primos bajo e^18 = {int(2.718281828459045**18)}):")
print(f"  primos partidos (orbitas degeneradas): {d['partidos']:10.2f}")
print(f"  primos inertes (orbita libre):         {d['inertes']:+10.2f}")
print(f"  termino arquimediano:                  {A:10.2f}")
print(f"  potencias k >= 2:                      {d['potencias']:10.2f}   (cuadrados {d['cuadrados']:.2f}, k >= 3 {d['altas']:+.2f})")
print(f"  Z = {Z:.4f}")
can = abs(d['partidos'] + d['inertes'])/abs(d['partidos'])
print(f"  las dos orbitas se cancelan al {100*can:.2f}%: queda {d['partidos'] + d['inertes']:.3f}")
print("articulo: -1787.59, +1796.72, -3.29, -5.83, Z = 0.0113; cancelacion al 0.5%")
