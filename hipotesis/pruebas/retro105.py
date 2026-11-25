"""retro105.py — Sprint 105. Lo que una estructura haria ver en GUE, y lo que vemos.
A. Kramers (GSE): una simetria antiunitaria T = U K con T^2 = -1 que conmuta con H fuerza dobletes exactos.
B. Sectores: una simetria unitaria que conmuta con H parte el espectro en sectores independientes; entre sectores no hay
   repulsion (superposicion). Se compara GUE con GUE condicionado a conmutar con Z/2 (binario) y con mu_6 (la fibra).
C. El par de Weyl de la fibra (D, Y) es irreducible: su conmutante es de dimension 1, asi que no impone sectores.
D. Aritmetica: ceros de zeta y de L(s, chi_5) (chi5_zeros.json) hasta T: cada uno solo, y su union (zeta_K = zeta L):
   la simetria de Galois de orden 2 se ve como superposicion de dos sectores.
E. El binario de Lawvere (sin punto fijo) y el de la simetria (punto fijo 1/2).
Uso: python3 -I retro105.py"""
import json, math, numpy as np, mpmath as mp
rng = np.random.default_rng(105); ok = 0
def check(c, m):
    global ok
    assert c, m; ok += 1
def gue(n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); return (a + a.conj().T) / 2
def unfolded_small(ev, a=0.1, frac=(0.25, 0.75)):
    """fraccion de espaciamientos (desdoblados por la densidad local) menores que a, en el centro del espectro"""
    ev = np.sort(ev); n = len(ev); i0, i1 = int(frac[0] * n), int(frac[1] * n)
    s = np.diff(ev[i0:i1]); s = s / s.mean(); return float(np.mean(s < a)), float(s.min())
# A. Kramers
for trial in range(5):
    n = 40; A = gue(n); B = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); B = B - B.T     # B antisimetrica
    H = np.block([[A, B], [-B.conj(), A.conj()]])                                                     # cuaternionica autodual
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])                     # T = J K, T^2 = J conj(J) = -1
    check(np.allclose(J @ J.conj(), -np.eye(2 * n)), "T^2 = -1")
    check(np.allclose(J @ H.conj(), H @ J), "T conmuta con H")
    w = np.linalg.eigvalsh(H); check(np.allclose(w[0::2], w[1::2], atol=1e-8), "cada autovalor es un doblete (Kramers)")
    v = rng.normal(size=2 * n) + 1j * rng.normal(size=2 * n)
    check(abs(np.vdot(v, J @ v.conj())) < 1e-9 * np.linalg.norm(v) ** 2, "<v, T v> = 0")
print("A. GSE: con T^2 = -1 todo nivel es doblete exacto (espaciamiento 0 en la mitad de los casos)")
# B. sectores
N = 720; rows = []
for name, m in (("GUE", 1), ("simetria Z/2 (binario)", 2), ("simetria mu_6 (fibra)", 6)):
    fr = []; mins = []
    for trial in range(12):
        ev = np.concatenate([np.linalg.eigvalsh(gue(N // m)) for _ in range(m)])
        f, mn = unfolded_small(ev); fr.append(f); mins.append(mn)
    rows.append((name, m, float(np.mean(fr)), float(np.min(mins))))
for name, m, f, mn in rows: print(f"B. {name:24s} sectores {m}: fraccion de espaciamientos < 0.1 = {f:.4f}; minimo {mn:.4f}")
check(rows[0][2] < 0.005 and rows[1][2] > 0.02 and rows[2][2] > rows[1][2], "una simetria que conmuta se ve como perdida de repulsion")
# C. el par de Weyl
z3 = np.exp(2j * np.pi / 3); fib = [(k, e) for k in range(3) for e in range(2)]; idx = {p: i for i, p in enumerate(fib)}
D = np.zeros((6, 6), complex)
for (k, e) in fib: D[idx[((k + 1) % 3, (e + 1) % 2)], idx[(k, e)]] = 1
Y = np.diag([z3 ** k * (-1) ** e for k, e in fib])
def commutant_dim(gens):
    n = gens[0].shape[0]; rows_ = []
    for g in gens: rows_.append(np.kron(np.eye(n), g) - np.kron(g.T, np.eye(n)))
    M = np.vstack(rows_); return n * n - np.linalg.matrix_rank(M, tol=1e-9)
check(commutant_dim([D]) == 6, "el conmutante de D tiene dimension 6: seis sectores")
check(commutant_dim([D, Y]) == 1, "el conmutante del par de Weyl es C: no hay sectores")
print("C. conmutante de D: dim 6 (seis sectores); conmutante de {D, Y}: dim 1 (irreducible, ningun sector)")
# D. aritmetica
L = json.load(open(__file__.replace("retro105.py", "chi5_zeros.json"))); T = L[-1]
Z = []
n = 1
while True:
    g = float(mp.im(mp.zetazero(n)))
    if g > T: break
    Z.append(g); n += 1
NZ = lambda t: t / (2 * math.pi) * math.log(t / (2 * math.pi * math.e)) + 7 / 8
NL = lambda t: t / (2 * math.pi) * math.log(5 * t / (2 * math.pi * math.e))
def small(seq, N_, a=0.1, tmin=20.0):
    x = np.array([N_(t) for t in seq if t > tmin]); s = np.diff(x); return int(np.sum(s < a)), len(s), float(s.min())
cz = small(Z, NZ); cl = small(L, NL)
merged = sorted(Z + L); cm = small(merged, lambda t: NZ(t) + NL(t))
dmin = min(abs(a - b) for a in Z for b in L)
print(f"D. zeta: {len(Z)} ceros; espaciamientos < 0.1: {cz[0]} de {cz[1]} (min {cz[2]:.3f})")
print(f"   L(chi5): {len(L)} ceros; espaciamientos < 0.1: {cl[0]} de {cl[1]} (min {cl[2]:.3f})")
print(f"   zeta_K = zeta L(chi5): espaciamientos < 0.1: {cm[0]} de {cm[1]} (min {cm[2]:.4f}); distancia minima entre un cero de zeta y uno de L: {dmin:.4f}")
gue_exp = 32 / math.pi ** 2 * 0.1 ** 3 / 3                                       # Wigner beta=2, s pequeno
two_exp = rows[1][2]
print(f"   esperado por espaciamiento: GUE ~ {gue_exp:.5f}; dos sectores independientes ~ {two_exp:.4f}")
check(cz[0] + cl[0] <= 2, "cada funcion sola repele (como GUE)")
check(cm[0] >= 3, "la union muestra espaciamientos chicos: la simetria de Galois se ve como superposicion")
check(dmin > 1e-6, "zeta y L(chi5) no comparten ordenada en el rango: superposicion, no dobletes")
# E. Lawvere
check(all((1 - b) != b for b in (0, 1)) and abs((1 - 0.5) - 0.5) < 1e-15, "1-x: sin punto fijo en {0,1}; punto fijo 1/2 en R")
print(f"{ok} aserciones, 0 fallas")
