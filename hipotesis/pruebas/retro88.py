"""retro88.py — Sprint 88: la pieza (B) sobre el complemento del estado excepcional.
Escindido: conjugando M^2 a diag(a, 1/a), a = phi^2, el operador de Weil es (D f)(x) = (a/p) f(x/a) (o f(a x)):
escalamiento de F_p. delta_0 es el punto fijo (autovalor +1) y en las funciones sobre F_p^* la multiplicacion por un
caracter multiplicativo beta (un caracter de Dirichlet mod p) cumple  beta D beta^{-1} = beta(a)^{+-1} D : la beta de la Prop. 6.7.
Identidad virtual: Weil|_T = Reg(T) + chi5(p) sigma  (es la formula del caracter del sprint 83).
En 5^k: la traslacion de fases por 5^(v+1) preserva las fases ocupadas con v5(j) = v."""
import math
import numpy as np
from sympy import legendre_symbol, primitive_root
_g = {"__name__": "r83", "__file__": __file__.replace("retro88.py", "retro83.py")}
exec(compile(open(__file__.replace("retro88.py", "retro83.py")).read().split("rng = random.Random(83)")[0], "r83", "exec"), _g)
Wn, mm, order = _g["Wn"], _g["mm"], _g["order"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
B = ((1, 1), (1, 2))
for p in (11, 19, 29, 31, 41, 59, 61):
    r = next(x for x in range(p) if (x * x - x - 1) % p == 0); a = r * r % p; ai = pow(a, -1, p)
    # h con h B h^{-1} = diag(a, 1/a): filas = autovectores izquierdos; se normaliza a det 1
    def left(l): return (1, (l - 1) % p)                       # (1, l-1) B = l (1, l-1) si l^2 - 3l + 1 = 0
    v1, v2 = left(a), left(ai); det = (v1[0] * v2[1] - v1[1] * v2[0]) % p; s = pow(det, -1, p)
    h = ((v1[0] * s % p, v1[1] * s % p), (v2[0], v2[1])); hi = ((h[1][1], -h[0][1] % p), (-h[1][0] % p, h[0][0]))
    check("S", "T", f"p={p}: h B h^-1 = diag(a, 1/a)", mm(mm(h, B, p), hi, p) == ((a, 0), (0, ai)))
    assert h[0][1] % p and hi[0][1] % p
    H = Wn(h, p); D = H @ Wn(B, p) @ np.linalg.inv(H)
    eps = int(legendre_symbol(a, p)); x = np.arange(p)
    D1 = np.zeros((p, p)); D1[x, x * ai % p] = eps            # (D f)(x) = eps f(x/a)
    D2 = np.zeros((p, p)); D2[x, x * a % p] = eps             # (D f)(x) = eps f(a x)
    which = 1 if np.allclose(D, D1, atol=1e-7) else (2 if np.allclose(D, D2, atol=1e-7) else 0)
    check("S", "T", f"p={p}: en la base del toro, U(M^2) es el escalamiento de F_p por a = phi^2 (sin fase)", which in (1, 2))
    check("S", "T", f"p={p}: delta_0 es el estado excepcional: punto fijo del escalamiento, autovalor (a/p) = +1", abs(D[0, 0] - 1) < 1e-7 and np.allclose(D[0, 1:], 0, atol=1e-7) and np.allclose(D[1:, 0], 0, atol=1e-7))
    g0 = primitive_root(p); ind = {pow(g0, k, p): k for k in range(p - 1)}
    beta = np.array([0] + [np.exp(2j * np.pi * ind[y] / (p - 1)) for y in range(1, p)])
    Bt = np.diag(beta[1:]); Dc = D[1:, 1:]
    z = np.exp(2j * np.pi * ind[a] / (p - 1))
    ok = np.allclose(Bt @ Dc @ np.linalg.inv(Bt), z * Dc, atol=1e-7) or np.allclose(Bt @ Dc @ np.linalg.inv(Bt), np.conj(z) * Dc, atol=1e-7)
    e = order(B, p)
    check("B", "T", f"p={p}: sobre las funciones en F_p^*, beta U beta^-1 = zeta U con beta un caracter de Dirichlet mod p y zeta de orden e = {e}", ok and abs(z ** e - 1) < 1e-9 and all(abs(z ** k - 1) > 1e-9 for k in range(1, e)))
    ev = np.linalg.eigvals(Dc); k_ = np.round(np.angle(ev) / (2 * np.pi) * e).astype(int) % e
    check("B", "T", f"p={p}: quitado delta_0, las e fases tienen todas multiplicidad m = (p-1)/e: partes exactamente iguales, permutadas ciclicamente por beta", set(np.bincount(k_, minlength=e).tolist()) == {(p - 1) // e})
# 5^k: la regla de ocupacion y sus traslaciones
L5 = lambda x: int(legendre_symbol(x % 5, 5))
def occ(j, K):
    N = 5 ** K; j %= 2 * N
    if j % N == 0: return j == 0
    while j % 5 == 0: j //= 5
    return L5(j) == 1
for K in range(1, 7):
    N = 5 ** K; e = 2 * N
    for v in range(K):
        layer = [j for j in range(e) if j % 5 ** v == 0 and j % 5 ** (v + 1) != 0]
        sh = 5 ** (v + 1)
        check("5", "P", f"K={K} v={v}: la traslacion de fases por 5^{v+1} preserva la capa v5(j) = {v} y su ocupacion; orbitas de tamano 2*5^{K-v-1}", all(occ(j, K) == occ(j + sh, K) for j in layer))
        check("5", "P", f"K={K} v={v}: la capa tiene 4*5^{K-v-1} estados ocupados de 8*5^{K-v-1}", sum(occ(j, K) for j in layer) == 4 * 5 ** (K - v - 1) and len(layer) == 8 * 5 ** (K - v - 1))
    check("5", "P", f"K={K}: fuera de las capas queda j = 0 (ocupado) y j = 5^K (vacio): un estado", occ(0, K) and not occ(N, K) and sum(occ(j, K) for j in range(e)) == N)
if __name__ == "__main__":
    from collections import Counter
    print(dict(Counter(b for b, _, _ in LEDGER)))
    print(f"{len(LEDGER)} aserciones, 0 fallas")
