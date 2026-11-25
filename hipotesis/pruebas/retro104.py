"""retro104.py — Sprint 104. Lo que un operador del nivel no separa, y el par que si separa.
Modelo finito del indice conjunto J = niveles x Z/3 x Z/2 (granularity note, ssec:observables), con el paso de
cubierta D = generador de mu_6 ~ Z/3 x Z/2 actuando por (k, e) -> (k+1, e+1).
Comprueba: (1) toda funcion del operador de nivel H es funcion del nivel y no separa la fibra (multiplicidad 6);
(2) los operadores de color C = diag(zeta3^k)/2 y orientacion W = diag((-1)^e) conmutan entre si y con H,
    y con H separan J; (3) D no conmuta con C ni con W: D C D^-1 = zeta3^{-1} C, D W D^-1 = -W;
(4) D y C W generan el algebra de matrices completa de la fibra (par de Weyl de orden 6);
(5) C es normal y no autoadjunto. Uso: python3 -I retro104.py"""
import numpy as np, itertools
ok = 0
def check(c, m):
    global ok
    assert c, m; ok += 1
z3 = np.exp(2j * np.pi / 3)
fib = [(k, e) for k in range(3) for e in range(2)]                    # 6 puntos de la fibra
idx = {p: i for i, p in enumerate(fib)}
Dm = np.zeros((6, 6), complex)
for (k, e) in fib: Dm[idx[((k + 1) % 3, (e + 1) % 2)], idx[(k, e)]] = 1
check(np.allclose(np.linalg.matrix_power(Dm, 6), np.eye(6)) and not np.allclose(np.linalg.matrix_power(Dm, 3), np.eye(6))
      and not np.allclose(np.linalg.matrix_power(Dm, 2), np.eye(6)), "D tiene orden exactamente 6")
C = np.diag([z3 ** k / 2 for k, e in fib]); Wm = np.diag([(-1) ** e for k, e in fib]).astype(complex)
levels = 5; I_L = np.eye(levels); I_F = np.eye(6)
H = np.kron(np.diag(np.arange(1, levels + 1).astype(float)), I_F)    # operador de nivel (funcion del nivel)
D = np.kron(I_L, Dm); CC = np.kron(I_L, C); WW = np.kron(I_L, Wm)
# (1)
check(np.allclose(D @ H, H @ D), "D conmuta con H")
for f in (np.exp, np.sin, lambda x: x ** 3 - 2 * x, lambda x: 1 / (1 + x * x)):
    ev, V = np.linalg.eigh(H); fH = V @ np.diag(f(ev)) @ V.conj().T
    check(np.allclose(D @ fH, fH @ D), "D conmuta con f(H)")
    blocks = [fH[6 * i:6 * i + 6, 6 * i:6 * i + 6] for i in range(levels)]
    check(all(np.allclose(b, b[0, 0] * np.eye(6)) for b in blocks), "f(H) es constante en cada fibra")
w, _ = np.linalg.eigh(H); mult = [int(np.sum(np.isclose(w, x))) for x in np.unique(np.round(w, 9))]
check(all(m == 6 for m in mult), "cada autovalor de H tiene multiplicidad 6")
# (2)
for A, B in itertools.combinations((H, CC, WW), 2): check(np.allclose(A @ B, B @ A), "la terna conmuta")
joint = {(round(H[i, i].real, 9), round(CC[i, i].real, 9), round(CC[i, i].imag, 9), round(WW[i, i].real, 9)) for i in range(6 * levels)}
check(len(joint) == 6 * levels, "la terna (H, C, W) separa el indice conjunto")
# (3)
Di = np.linalg.inv(Dm)
check(np.allclose(Dm @ C @ Di, C * 1) is False, "D no conmuta con C")
check(np.allclose(Dm @ C @ Di, z3 ** -1 * C) or np.allclose(Dm @ C @ Di, z3 * C), "D C D^-1 = zeta3^{+-1} C")
check(np.allclose(Dm @ Wm @ Di, -Wm), "D W D^-1 = -W")
# (4) D y X = (2C) W, de orden 6, forman un par de Weyl y generan M_6(C)
X = (2 * C) @ Wm
z6 = np.exp(2j * np.pi / 6)
rel = [c for c in (z6 ** j for j in range(6)) if np.allclose(Dm @ X @ Di, c * X)]
check(len(rel) == 1 and not np.isclose(rel[0], 1), "D X D^-1 = q X con q raiz primitiva")
words = [np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Dm, b) for a in range(6) for b in range(6)]
check(np.linalg.matrix_rank(np.array([w_.ravel() for w_ in words])) == 36, "las palabras X^a D^b generan M_6(C)")
# (5)
check(np.allclose(C @ C.conj().T, C.conj().T @ C) and not np.allclose(C, C.conj().T), "C es normal y no autoadjunto")
print(f"q = {np.round(rel[0], 6)} (raiz sexta primitiva: {np.isclose(abs(np.angle(rel[0])), np.pi/3)})")
print(f"{ok} aserciones, 0 fallas")
