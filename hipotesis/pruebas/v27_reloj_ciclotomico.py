"""§68: el reloj ciclotómico.  N(Φ_n(φ)) = Φ_n(φ)·Φ_n(ψ), exacto como entero por Möbius sobre
N(φ^d − 1) = (−1)^d + 1 − L_d (prod_Ncyc, Npow_eq_int).
  cara arquimediana: |log|N(Φ_n(φ))| − φ(n)·log φ| ≤ 4φ²  (log_Ncyc_bound)
  la torre por divisores: |Σ_{d∣n} log|N(Φ_d(φ))| − n·log φ| ≤ 4φ^{−n}  (sum_log_Ncyc + log_Npow_bound)
  cara p-ádica: para p ∤ n, p ∣ N(Φ_n(φ)) ⇔ el reloj de p es n  (clock_iff_cyclotomic_root)"""
from comun import *
from fractions import Fraction
import numpy as np
NMAX = 600
phi = (1 + 5 ** 0.5) / 2; lphi = math.log(phi)
L = [2, 1]
for _ in range(NMAX + 2): L.append(L[-1] + L[-2])
Npow = [None] + [(-1) ** d + 1 - L[d] for d in range(1, NMAX + 1)]
def mu(n):
    r = 1; p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            r = -r
        p += 1
    return -r if n > 1 else r
def totient(n):
    r = n; m = n; p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0: m //= p
            r -= r // p
        p += 1
    if m > 1: r -= r // m
    return r
Ncyc = [None]
for n in range(1, NMAX + 1):
    v = Fraction(1)
    for d in range(1, n + 1):
        if n % d == 0 and mu(n // d): v *= Fraction(Npow[d]) ** mu(n // d)
    Ncyc.append(v)
comprobar('N(Φ_n(φ)) es entero para n ≤ %d' % NMAX, all(v.denominator == 1 for v in Ncyc[1:]))
Ncyc = [None] + [int(v) for v in Ncyc[1:]]
# contraste numérico directo Φ_n(φ)Φ_n(ψ) para n ≤ 40 (coeficientes por división de x^n − 1)
def ciclo(n, memo={}):
    if n in memo: return memo[n]
    num = np.zeros(n + 1); num[0] = 1; num[-1] = -1   # x^n − 1 en orden descendente
    q = num
    for d in range(1, n):
        if n % d == 0: q = np.polydiv(q, ciclo(d))[0]
    memo[n] = np.round(q); return memo[n]
psi = (1 - 5 ** 0.5) / 2
ok = all(abs(np.polyval(ciclo(n), phi) * np.polyval(ciclo(n), psi) - Ncyc[n]) < 1e-6 * max(1, abs(Ncyc[n])) for n in range(1, 41))
comprobar('Φ_n(φ)·Φ_n(ψ) evaluado directamente coincide con el entero, n ≤ 40', ok)
for n in (3, 4, 8, 12, 20, 60, 100):
    print('   N(Φ_%d(φ)) = %d = %s' % (n, Ncyc[n], factores(abs(Ncyc[n])) if abs(Ncyc[n]) < 10 ** 12 else '…'))
comprobar('valores de prop:polar: 4, 5, 9, 4 y N(Φ₆₀(φ)) = 61²', [Ncyc[3], Ncyc[4], Ncyc[8], Ncyc[12], Ncyc[60]] == [4, 5, 9, 4, 61 ** 2])
def logabs(z): return math.log(abs(z)) if abs(z) < 10 ** 300 else len(str(abs(z))) * math.log(10) + math.log(float('0.' + str(abs(z))[:17]))
err = [abs(logabs(Ncyc[n]) - totient(n) * lphi) for n in range(1, NMAX + 1)]
print('   cara arquimediana: máx |log|N(Φ_n)| − φ(n)·log φ| = %.4f (n = %d); cota 4φ² = %.3f' % (max(err), 1 + int(np.argmax(err)), 4 * phi ** 2))
comprobar('log_Ncyc_bound en n ≤ %d' % NMAX, max(err) <= 4 * phi ** 2)
torre = [abs(sum(logabs(Ncyc[d]) for d in range(1, n + 1) if n % d == 0) - n * lphi) <= 4 * phi ** (-n) + 1e-9 for n in range(1, 200)]
comprobar('torre por divisores: |Σ_{d∣n} log|N(Φ_d)| − n log φ| ≤ 4φ^{−n}, n < 200', all(torre))
# el reloj es por primo de ℤ[φ] sobre p: si p se parte, φ ↦ r y φ ↦ 1 − r = −1/r tienen
# órdenes que pueden diferir (n impar y 2n); el piso de §42 es el mcm de los dos.
def ordmod(x, p):
    o = p - 1
    for q in factores(p - 1):
        while o % q == 0 and pow(x, o // q, p) == 1: o //= q
    return o
P = primos(20000, 3); P = [p for p in P if p != 5]; pares = 0; fallos = 0; dobles = 0
for p in P:
    if partido(p):
        r = raiz_phi(p); relojes = {ordmod(r, p), ordmod((1 - r) % p, p)}
    else:
        relojes = {orden(p)[1]}
    if len(relojes) == 2:
        dobles += 1; a, b = sorted(relojes)
        assert b == 2 * a and a % 2 == 1 and orden(p)[1] == b
    for n in range(1, NMAX + 1):
        if n % p == 0: continue
        pares += 1
        if (Ncyc[n] % p == 0) != (n in relojes): fallos += 1
print('   primos partidos con dos relojes distintos {n, 2n}, n impar: %d de %d' % (dobles, len(P)))
print('   cara p-ádica: %d pares (p, n), p ≤ 20 000, n ≤ %d, p ∤ n' % (pares, NMAX))
comprobar('p ∣ N(Φ_n(φ)) ⇔ n es el reloj de φ en algún primo sobre p, en todos los pares', fallos == 0, '(%d fallos)' % fallos)
def v(x, q):
    k = 0
    while x % q == 0: x //= q; k += 1
    return k
print('   torres p-ádicas: valuación de N(Φ_{n₀·p^k}(φ)):')
for q, n0 in ((2, 3), (3, 8), (5, 4), (7, 16), (11, 10)):
    ks = [n0 * q ** k for k in range(5) if n0 * q ** k <= NMAX]
    print('     p = %2d, reloj %2d: ' % (q, n0) + ', '.join('n=%d→%d' % (n, v(Ncyc[n], q)) for n in ks))
v5 = [v(Ncyc[n], 5) for n in (4, 20, 100, 500)]
comprobar('en 5: valuaciones 1, 2, 2, 2 en los niveles 4, 20, 100, 500', v5 == [1, 2, 2, 2])
# el reloj acumulado es Mertens (clock_sum_mertens): Σ_{n≤N} err_n = Σ_{d≤N} ε_d·M(N/d)
NM = 10 ** 6
d_ = np.arange(1, NM + 1, dtype=float)
eps = np.log1p(-phi ** (-d_)) + np.log(np.abs(1 - ((-1.0) ** np.arange(1, NM + 1)) * phi ** (-d_)))
mu_ = np.ones(NM + 1, dtype=np.int64); mu_[0] = 0
es = np.ones(NM + 1, bool); es[:2] = False
for p in range(2, NM + 1):
    if es[p]:
        es[2 * p::p] = False
        mu_[p::p] *= -1
        if p * p <= NM: mu_[p * p::p * p] = 0
err = np.zeros(NM + 1)
for d in range(1, 60):                    # ε_d < 10⁻¹² para d ≥ 60
    err[d::d] += eps[d - 1] * mu_[1:NM // d + 1]
M = np.cumsum(mu_).astype(float); A = np.cumsum(err)
ok = all(abs(err[n] - (logabs(Ncyc[n]) - totient(n) * lphi)) < 1e-9 for n in range(1, NMAX + 1))
comprobar('err_n por convolución de Möbius coincide con el entero exacto, n ≤ %d' % NMAX, ok)
Ns = np.unique(np.logspace(2, 6, 300).astype(int))
ident = max(abs(A[N] - sum(eps[d - 1] * M[N // d] for d in range(1, 60))) for N in Ns[::10])
comprobar('identidad Σ_{n≤N} err_n = Σ_d ε_d·M(N/d) (máx. diferencia < 10⁻⁸)', ident < 1e-8, '(%.1e)' % ident)
aprox = -lphi * (M[Ns] + 2 * M[Ns // 2])
cc = np.corrcoef(A[Ns], aprox)[0, 1]
print('   correlación del reloj acumulado con −log φ·(M(N) + 2M(N/2)), N ≤ 10⁶: %.4f' % cc)
print('   máx |Σ err|/√N = %.3f;  máx |M(N)|/√N = %.3f' % (np.max(np.abs(A[Ns]) / np.sqrt(Ns)), np.max(np.abs(M[Ns]) / np.sqrt(Ns))))
comprobar('el reloj acumulado sigue a Mertens (correlación > 0,9)', cc > 0.9)
salir()
