"""§69: del reloj al tamaño, la hipérbola c·i = N_p.
Cada primo p (≠ 2, 3, 5) tiene reloj c (el piso de §42) e índice i con c·i = N_p ≤ 2(p + 1).
Ordenar por tamaño (p ≤ X) es cortar la tabla (c, i) por la hipérbola c·i ≲ 2X.
  tail_bound_phi: la masa Σ log p de los primos con reloj ≤ y + 1 está acotada por
    Σ_{m=1}^{y} ((m+1)·log φ + 4φ^{−(m+1)}) ≈ (log φ/2)·y²   (antes, §41: con log 2)
  large_index_clock: índice > j ⇒ reloj < 2(X+1)/j.  Por eso la cola de índice grande está acotada
    por la torre: con j = X^{3/4} es O(√X) sin hipótesis.  Lo que queda son las filas de índice
    ≤ X^{3/4}: las pequeñas son las familias de Kummer (niveles 80, 135, F₂₀) y el tramo medio es
    el de Hooley, que necesita la recta para cuerpos de Kummer de grado creciente."""
from comun import *
import numpy as np
T = tabla_ordenes(10 ** 6)
phi = (1 + 5 ** 0.5) / 2; lphi = math.log(phi)
p_ = np.array([t[0] for t in T]); Np = np.array([t[1] for t in T]); fl = np.array([t[2] for t in T])
ind = Np // fl; lp = np.log(p_)
comprobar('c·i = N_p ≤ 2(p+1) para los %d primos 7 ≤ p ≤ 10⁶' % len(T), np.all(ind * fl == Np) and np.all(Np <= 2 * (p_ + 1)))
def TB(y): return sum((m + 1) * lphi + 4 * phi ** (-(m + 1)) for m in range(1, y + 1))
# tail_bound_phi por niveles: primos ≤ 10⁶ con reloj ∣ m+1
ok = True; peor = 0
for c in range(2, 61):
    s = lp[(c % fl) == 0].sum(); b = c * lphi + 4 * phi ** (-c)
    ok &= s <= b; peor = max(peor, s / b)
comprobar('Σ_{p ≤ 10⁶, reloj ∣ c} log p ≤ c·log φ + 4φ^{−c} para c ≤ 60', ok, '(peor cociente %.3f)' % peor)
print('§69  masa Σ log p por tramos de índice (θ = total):')
print('       X       θ(X)     i=1     2–10   11–√X   √X–X^¾   >X^¾   |  cota de torre para >X^¾   para >√X')
res = {}
for X in (10 ** 4, 10 ** 5, 10 ** 6):
    s = p_ <= X; th = lp[s].sum(); r1, r2 = X ** 0.5, X ** 0.75
    tr = [lp[s & (ind == 1)].sum(), lp[s & (ind >= 2) & (ind <= 10)].sum(), lp[s & (ind > 10) & (ind <= r1)].sum(),
          lp[s & (ind > r1) & (ind <= r2)].sum(), lp[s & (ind > r2)].sum()]
    y34 = int(2 * (X + 1) / r2); y12 = int(2 * (X + 1) / r1)
    b34, b12 = TB(y34), TB(y12)
    t12 = lp[s & (ind > r1)].sum()
    print('   %7d  %9.1f  ' % (X, th) + '  '.join('%6.1f' % x for x in tr) + '   |   %8.1f (= %.2f√X)   %9.1f' % (b34, b34 / X ** 0.5, b12))
    res[X] = (tr[4], b34, t12, b12, th, tr[3])
comprobar('la masa de índice > X^¾ cumple la cota de la torre en X = 10⁴, 10⁵, 10⁶', all(v[0] <= v[1] for v in res.values()))
comprobar('la masa de índice > √X cumple la cota de la torre en X = 10⁴, 10⁵, 10⁶', all(v[2] <= v[3] for v in res.values()))
comprobar('la cota para índice > X^¾ es O(√X): cociente con √X entre 1 y 3 en las tres escalas',
          all(1 <= v[1] / X ** 0.5 <= 3 for X, v in res.items()))
# el corte por tamaño en la tabla (c, i): los primos ≤ X con reloj c e índice i están bajo c·i ≤ 2(X+1)
X = 10 ** 6; s = p_ <= X
comprobar('todo primo ≤ X cae bajo la hipérbola c·i ≤ 2(X+1)', np.all(fl[s] * ind[s] <= 2 * (X + 1)))
print('   tramo medio (√X, X^¾] dividido entre √X: ' + ', '.join('%.2f' % (v[5] / X_ ** 0.5) for X_, v in res.items()))
comprobar('la cota explícita y(y+3)/2·log φ + 4φ² domina a la suma (tail_bound_phi_explicit)',
          all(TB(y) <= y * (y + 3) / 2 * lphi + 4 * phi ** 2 for y in range(1, 3000)))
frac = lp[s & (ind <= 10)].sum() / lp[s].sum()
print('   en X = 10⁶ el %.2f %% de la masa está en índice ≤ 10, y el %.4f %% en índice > √X' % (100 * frac, 100 * res[X][2] / res[X][4]))
salir()
