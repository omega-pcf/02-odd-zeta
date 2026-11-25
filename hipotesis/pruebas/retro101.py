"""retro101.py — Sprint 101. La linea del indice (sprints 93n-96n) sobre una orbita libre REAL:
los ceros de Davenport-Heilbronn (dh_zeros.json: 71 en la recta, 2 orbitas libres, T<130; conteo 75 ~ 75.3).
Forma del lado de los ceros, truncada: W(f) = sum_{|gamma|<T} fhat(gamma) fhat(-gamma), f escalonada en [-L/2, L/2].
Uso: python3 -I retro101.py"""
import json, math, numpy as np
Zs = json.load(open(__file__.replace("retro101.py", "dh_zeros.json")))
line = np.array(Zs["line"]); off = Zs["off"]
ok = 0
def check(c, m):
    global ok
    assert c, m; ok += 1
check(abs(len(line) + 2 * len(off) - 130 / (2 * math.pi) * math.log(5 * 130 / (2 * math.pi * math.e))) < 1.5, "conteo de ceros")
def fr(x, D, r): return np.exp(1j * r * x) * (2 * np.sin(r * D / 2) / r)
def form(L, N, orbits, T=130.0):
    D = L / N; x = -L / 2 + (np.arange(N) + 0.5) * D
    M = np.zeros((N, N))
    for g in line[line < T]:
        v = fr(x, D, g); M += 2 * np.real(np.outer(v, np.conj(v)))
    for (b, g) in orbits:
        d = b - 0.5
        for r in (g + 1j * d, g - 1j * d, -g + 1j * d, -g - 1j * d):
            M += np.real(np.outer(fr(x, D, r), fr(x, D, -r)))
    return (M + M.T) / 2, D
def idx(M, D):
    N = len(M); J = np.eye(N)[::-1]
    Ue = (np.eye(N) + J)[:, : N // 2] / math.sqrt(2); Uo = (np.eye(N) - J)[:, : N // 2] / math.sqrt(2)
    tol = 1e-9 * np.abs(M).max()
    return int((np.linalg.eigvalsh(Ue.T @ M @ Ue) < -tol).sum()), int((np.linalg.eigvalsh(Uo.T @ M @ Uo) < -tol).sum())
print("A. una orbita libre real (g = 85.70, delta = 0.3085), ceros con T < 100")
o1 = [tuple(off[0])]; g1 = off[0][1]; rowsA = []
for L in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0):
    N = 2 * int(math.ceil(L * g1 / 0.35 / 2)); M, D = form(L, N, o1, T=100.0); e, o = idx(M, D); rowsA.append((L, e, o))
    print(f"   L = {L:4.1f}  N = {N:5d}  negativas: par {e}, impar {o}")
check(all(e <= 1 and o <= 1 for _, e, o in rowsA), "cota: a lo mas una por paridad")
check(any(e == 1 and o == 1 for _, e, o in rowsA), "la cota 2 se alcanza")
first = next(L for L, e, o in rowsA if e + o > 0); print(f"   primera deteccion en L = {first}; 1/delta = {1/(off[0][0]-0.5):.2f}")
both = [L for L, e, o in rowsA if e == 1 and o == 1]
check(all(e == 1 and o == 1 for L, e, o in rowsA if L >= both[0]), "una vez juntas, no desaparecen")
print("B. medio periodo: W(f) < 0  =>  W(tau_{pi/g} f - f) < 0   (una orbita)")
m = 10; D = math.pi / (g1 * m); nB = 0
for L0 in (1.0, 2.0, 3.0):
    N0 = 2 * int(round(L0 / D / 2)); K = m
    Ma, _ = form(N0 * D, N0, o1, T=100.0); Mb, _ = form((N0 + 2 * K) * D, N0 + 2 * K, o1, T=100.0); J0 = np.eye(N0)[::-1]
    for par in (+1, -1):
        P = (np.eye(N0) + par * J0) / 2
        ev, V = np.linalg.eigh(P @ Ma @ P + 1e3 * np.abs(Ma).max() * (np.eye(N0) - P))
        if ev[0] >= -1e-9 * np.abs(Ma).max(): continue
        f = V[:, 0]; emb = lambda s: np.concatenate([np.zeros(K + s), f, np.zeros(K - s)])
        v = emb(m) - emb(0); Vu = v @ Mb @ v; nB += 1
        check(Vu < 0, "medio periodo"); print(f"   L0 = {L0}  paridad {par:+d}: W(f) = {f @ Ma @ f:+.2e}, W(tau f - f) = {Vu:+.2e}")
check(nB >= 2, "casos de medio periodo")
print("C. las dos orbitas libres (T < 130): indice <= 2 por paridad")
o2 = [tuple(z) for z in off]; rowsC = []
for L in (1.0, 2.0, 4.0, 6.0, 8.0):
    N = 2 * int(math.ceil(L * off[1][1] / 0.35 / 2)); M, D = form(L, N, o2); e, o = idx(M, D); rowsC.append((L, e, o))
    print(f"   L = {L:4.1f}  negativas: par {e}, impar {o}")
check(all(e <= 2 and o <= 2 for _, e, o in rowsC), "cota con dos orbitas")
print("D. control: los mismos ceros de la recta, sin orbitas: indice 0")
for L in (2.0, 6.0):
    N = 2 * int(math.ceil(L * g1 / 0.35 / 2)); M, D = form(L, N, []); check(idx(M, D) == (0, 0), "control")
print(f"{ok} aserciones, 0 fallas")
