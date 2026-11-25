"""√X como Pitágoras: energía E(X) = Σ_{p≤X} |a_p|² log² p frente a |S(X)|², S(X) = Σ a_p log p,
para los tres primeros símbolos del 60 (nivel 80, nivel 135, F₂₀)."""
from comun import *
L = 10**6
P = primos(L, 2)
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
def aF(p):   # traza de ρ (F₂₀) = raíces del quíntico − 1, desde el índice
    if p == 5: return 0
    if p % 5 != 1: return 0          # 1 raíz − 1
    if p < 7: return 0
    return 4 if indice(p) % 5 == 0 else -1
marcas = [10**k for k in (3, 4, 5)] + [2*10**5, 5*10**5, 10**6]
for nombre, a in (('nivel 80', af), ('nivel 135', ag), ('F20', aF)):
    S = E = E1 = 0.0; j = 0; filas = []
    for p in P:
        v = a(p); lp = math.log(p)
        S += v * lp; E += v * v * lp * lp; E1 += v * v * lp
        while j < len(marcas) and p >= marcas[j] - 1 and (j == len(marcas) - 1 or True):
            if p >= marcas[j] - 1: filas.append((marcas[j], S, E, E1)); j += 1
            else: break
    if len(filas) < len(marcas): filas.append((marcas[-1], S, E, E1))
    print('\n%s:   X        Σ|a_p|²·log p / X     |S|²/E      S/√X' % nombre)
    for X, S_, E_, E1_ in filas:
        print('        %8d        %.4f            %6.3f    %+.3f' % (X, E1_ / X, S_ * S_ / E_, S_ / math.sqrt(X)))
    comprobar('%s: energía Σ|a_p|²log p / X → 1 (ortogonalidad de Schur + Chebotarev)' % nombre,
              abs(filas[-1][3] / filas[-1][0] - 1) < 0.02, '%.4f' % (filas[-1][3] / filas[-1][0]))
    comprobar('%s: |S|²/E acotado (Pitágoras) en todas las escalas' % nombre, max(f[1]**2 / f[2] for f in filas) < 5)
salir()
