"""escala_ceros_bajos.py — W4–W5, prop:sqrt-x: la escala 1/2 desde los ceros bajos de las formas de niveles 80 y 135.
Simbolos de las capas d = 2, 3 (prop:phi-layers): las formas de peso 1 de niveles 80 y 135 (a_p como en
v12_pitagoras_raiz_X.py, desde las formas cuadraticas de discriminante -80 y -135; comun.py).  Sigma(X) = sum_(p<=X) a_p log p.
Por la formula explicita, Sigma(X) = X^(1/2) R(X), R(X) = -sum_rho X^(i gamma)/rho - 1 (el -1 es el de los cuadrados,
sum_(p<=sqrt X) a(p^2) log p ~ sqrt X), con los ceros calculados (datos/ceros_nivel80.json: 66 hasta t = 60;
datos/ceros_nivel135.json: 56 hasta t = 50).
1. El exponente nu que mejor ajusta Sigma(X) ~ X^nu R(X) en 300 puntos X de 10^3 a 10^6 (minimos cuadrados).
2. El primer cero solo, con su termino multiplicado por X^delta: el delta del mejor ajuste.
3. La parte del primer cero en sum_rho 1/|rho|^2 (los ceros calculados mas la cola con la densidad (1/pi) log(sqrt(N) t/2pi)).
El articulo: nu = 0.500 y 0.5065, dentro de +-0.01; delta = 0.004 +- 0.03; el primer cero lleva 31% y 48%.
Uso: python3 -I escala_ceros_bajos.py"""
import os, sys; AQUI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, AQUI)
import json, math, numpy as np
from comun import primos, representados, leg
L = 10**6; P = primos(L, 2)
R1 = representados([(1, 0, 20)], L + 1, -80); R2 = representados([(4, 0, 5)], L + 1, -80)
Rg = representados([(1, 1, 34), (5, 5, 8)], L + 1, -135)
def af(p):
    if p == 2: return 0
    if p == 5: return -1
    return 2 if p in R1 else (-2 if p in R2 else 0)
def ag(p):
    if p == 3: return 0
    if p == 5: return 1
    if p == 2: return -1
    if leg(-15, p) != 1: return 0
    return 2 if p in Rg else -1
Pa = np.array(P, float); Xs = np.unique(np.logspace(3, 6, 300).astype(int))
for nm, a, N, T in (('nivel 80', af, 80, 60.0), ('nivel 135', ag, 135, 50.0)):
    g = np.array(json.load(open(os.path.join(AQUI, 'datos', 'ceros_nivel%d.json' % N))))
    av = np.array([a(p) for p in P], float)
    SX = np.cumsum(av*np.log(Pa))[np.searchsorted(Pa, Xs, side='right') - 1]
    rho = 0.5 + 1j*g; lX = np.log(Xs)
    term = -2*np.real(np.exp(1j*np.outer(lX, g))/rho)          # (X, cero): aporte de +-gamma
    R = term.sum(1) - 1
    nus = np.arange(0.40, 0.60, 0.0001)
    nu = nus[np.argmin([np.sum((SX - Xs**v*R)**2) for v in nus])]
    ds = np.arange(-0.2, 0.2, 0.0005)
    resto = term[:, 1:].sum(1) - 1
    dl = ds[np.argmin([np.sum((SX - np.sqrt(Xs)*(resto + Xs**d*term[:, 0]))**2) for d in ds])]
    tot = 2*np.sum(1/(0.25 + g**2)); cola = (2/math.pi)*(math.log(math.sqrt(N)*T/(2*math.pi)) + 1)/T
    parte = 2/(0.25 + g[0]**2)/(tot + cola)
    print(f"{nm}: nu = {nu:.4f};  delta del primer cero (gamma = {g[0]:.4f}) = {dl:+.4f};  su parte en sum 1/|rho|^2 = {100*parte:.0f}%"
          f"  (ceros {tot:.4f} + cola {cola:.4f})")
print("articulo: nu = 0.500 y 0.5065 (+-0.01); delta = 0.004 +- 0.03; 31% y 48%")
