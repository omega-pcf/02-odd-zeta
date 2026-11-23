"""fermat_quintic_points.py — rmk:fermat-model y su fila del Status ledger: la quintica de Fermat en p = 1 mod 5.
C: x^5 + y^5 = z^5.  Para p = 1 mod 5 y chi un caracter de orden 5 de F_p^*, las sumas de Jacobi
J(chi^a, chi^b) = sum_x chi^a(x) chi^b(1-x) (a, b = 1..4, a + b != 0 mod 5: doce pares) son los valores propios de
Frobenius en H^1 (Weil); se comprueba que el numero de puntos proyectivos es exactamente p + 1 + sum J y que
|J| = sqrt(p) para los doce.
El articulo: para p = 11, 31, 41, 61, 71 el conteo es exactamente p + 1 + sum J, y las doce sumas tienen modulo sqrt(p).
Uso: python3 -I fermat_quintic_points.py"""
import cmath, math
def raiz_primitiva(p):
    fs = [q for q in range(2, p) if (p - 1) % q == 0 and all(q % r for r in range(2, int(q**.5) + 1))]
    return next(g for g in range(2, p) if all(pow(g, (p - 1)//q, p) != 1 for q in fs))
for p in (11, 31, 41, 61, 71):
    g = raiz_primitiva(p); ind = {pow(g, k, p): k for k in range(p - 1)}
    z = cmath.exp(2j*math.pi/5)
    ch = lambda x, a: 0 if x % p == 0 else z**((a*ind[x % p]) % 5)
    J = {(a, b): sum(ch(x, a)*ch(1 - x, b) for x in range(p)) for a in range(1, 5) for b in range(1, 5) if (a + b) % 5}
    # puntos proyectivos de x^5 + y^5 = z^5
    pot = [pow(t, 5, p) for t in range(p)]
    cnt = {}
    for t in range(p): cnt[pot[t]] = cnt.get(pot[t], 0) + 1
    afin = sum(cnt.get((pot[x] + pot[y]) % p, 0) for x in range(p) for y in range(p))   # (x, y, z) con z libre
    N = (afin - 1)//(p - 1)                                         # quita (0,0,0), cociente por escalares
    sJ = sum(J.values())
    print(f"p = {p}: N = {N};  p + 1 + sum J = {(p + 1 + sJ).real:.6f} (imag {abs(sJ.imag):.1e});  "
          f"|J| / sqrt p de {min(abs(v) for v in J.values())/math.sqrt(p):.12f} a {max(abs(v) for v in J.values())/math.sqrt(p):.12f}")
print("articulo: exactamente p + 1 + sum J; |J| = sqrt p")
