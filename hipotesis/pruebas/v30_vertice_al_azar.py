"""§71: la geometría del n-gono y el modelo de vértice al azar.
En el grupo cíclico de cada primo, los elementos de índice > j son Σ_{c∣N, j·c<N} φ(c) y su fracción es
≤ d(N)/j (card_large_index, card_large_index_le).  Modelo: φ cae en un vértice al azar de su polígono.
  partido (N = p − 1): φ ↦ r = g^k, el otro primo ve −1/r; índice = gcd(k, N/2), k uniforme
      ⇒ P(índice = i) = φ(N/(2i))/(N/2),  i ∣ N/2;
  inerte (N = 2(p+1)): φ = h^k con k impar en el grupo de orden 2(p+1); índice = gcd(k, p+1)
      ⇒ P(índice = i) = φ(2(p+1)/i)/(p+1),  i ∣ p+1, i impar.
Se compara G_modelo(j) = Σ_{p≤X} log p·P_p(índice > j) con la masa medida G_X(j)."""
from comun import *
import numpy as np
# comprobación directa de card_large_index en grupos (ℤ/p)* pequeños
def tot(n):
    r = n; m = n; q = 2
    while q * q <= m:
        if m % q == 0:
            while m % q == 0: m //= q
            r -= r // q
        q += 1
    if m > 1: r -= r // m
    return r
def divisores(n):
    d = [1]
    for q, e in factores_exp(n).items():
        d = [x * q ** k for x in d for k in range(e + 1)]
    return sorted(d)
def factores_exp(n):
    f = {}; q = 2
    while q * q <= n:
        while n % q == 0: f[q] = f.get(q, 0) + 1; n //= q
        q += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
ok = True
for p in primos(400, 3):
    N = p - 1
    ords = []
    for x in range(1, p):
        o = 1; y = x
        while y != 1: y = y * x % p; o += 1
        ords.append(o)
    for j in (1, 2, 3, 5, 8, 13):
        cnt = sum(1 for o in ords if j * o < N)
        ok &= cnt == sum(tot(c) for c in divisores(N) if j * c < N)
        ok &= j * cnt <= len(divisores(N)) * N
comprobar('card_large_index y card_large_index_le en (ℤ/p)* para p < 400 y j = 1 … 13', ok)
T = tabla_ordenes(10 ** 6)
p_ = np.array([t[0] for t in T]); Np = np.array([t[1] for t in T]); fl = np.array([t[2] for t in T])
ind = Np // fl; lp = np.log(p_)
js = np.unique(np.logspace(0, 4, 41).astype(int))
X = 10 ** 6
Gm = np.zeros(len(js)); P2 = 0.0; P3 = 0.0
for (p, N, f) in T:
    if partido(p):
        M = N // 2; ds = divisores(M); pr = np.array([tot(M // i) / M for i in ds])
    else:
        M = p + 1; ds = [i for i in divisores(M) if i % 2 == 1]; pr = np.array([tot(2 * M // i) / M for i in ds])
    ds = np.array(ds); tail = np.cumsum(pr[::-1])[::-1]
    pos = np.searchsorted(ds, js, side='right')
    Gm += math.log(p) * np.where(pos < len(ds), tail[np.minimum(pos, len(ds) - 1)], 0.0)
    P2 += math.log(p) * pr[ds % 2 == 0].sum(); P3 += math.log(p) * pr[ds % 3 == 0].sum()
g = np.bincount(ind, weights=lp); G = np.cumsum(g[::-1])[::-1]
Gr = np.array([G[j + 1] if j + 1 < len(G) else 0.0 for j in js])
print('§71  masa de índice > j en X = 10⁶: medida frente al modelo de vértice al azar')
for j, a, b in zip(js[::4], Gr[::4], Gm[::4]):
    print('     j = %5d: medida %10.1f   modelo %10.1f   cociente %.3f   (modelo·j/X = %.3f)' % (j, a, b, a / b if b else 0, b * j / X))
rat = Gr / Gm; sel = (js >= 3) & (js <= 1000)
print('   cociente medida/modelo para 3 ≤ j ≤ 1000: %.3f – %.3f (media %.3f)' % (rat[sel].min(), rat[sel].max(), rat[sel].mean()))
comprobar('el modelo de vértice al azar reproduce la ley de la cola (cociente 0,85–1,15 para 3 ≤ j ≤ 1000)', np.all((rat[sel] > 0.85) & (rat[sel] < 1.15)))
comprobar('para j ≫ √X la torre corta más que el modelo (cociente < 0,8 en j ≥ 1500): los relojes pequeños son finitos', np.all(rat[js >= 1500] < 0.8))
comprobar('el modelo también da la ley 1/j: máx_j G_modelo(j)·j/X < 0,8', np.max(Gm * js / X) < 0.8)
# las capas: 2 ∣ índice y 3 ∣ índice, medidas frente al modelo
th = lp.sum(); m2 = lp[ind % 2 == 0].sum(); m3 = lp[ind % 3 == 0].sum()
print('   capa 2: medida %.4f, modelo %.4f;  capa 3: medida %.4f, modelo %.4f  (fracción de la masa)' % (m2 / th, P2 / th, m3 / th, P3 / th))
comprobar('capas 2 y 3: el modelo acierta a menos de 0,02', abs(m2 - P2) / th < 0.02 and abs(m3 - P3) / th < 0.02)
salir()
