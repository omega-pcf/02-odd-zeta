"""retro93.py — Sprint 93: una orbita libre de Klein y el indice de inercia de la forma de Weil.
Lado de los ceros: W(f) = sum_rho fhat(gamma_rho) fhat(-gamma_rho), gamma = (rho - 1/2)/i.
Teorema [P] (algebra lineal): para f real, el cuadruple {rho, rho_bar, 1-rho, 1-rho_bar} aporta
  q(f) = 4 Re(A B),  A = fhat(gamma), B = fhat(-gamma),
de signatura <= (2,2); en funciones pares q = 4 Re(A^2) (signatura <= (1,1)), en impares q = -4 Re(A^2) (<= (1,1)).
Un cero sobre la recta aporta 2|fhat(gamma)|^2 >= 0. Como W conmuta con la paridad (tau), el indice de W es
indice_par + indice_impar, y cada uno es <= numero de orbitas libres.  Aqui: comprobacion numerica del teorema
y medida de cuando la cota se alcanza en el mundo contrafactual de los sprints 76-77."""
import math, warnings; warnings.filterwarnings("ignore")
import numpy as np
_src = open(__file__.replace("retro93.py", "retro67.py")).read()
_src = _src[:_src.index("X = 1000; L = math.log(X)")]
_g = {"__file__": __file__, "__name__": "r67"}; exec(compile(_src, "retro67", "exec"), _g)
build, ideals_upto = _g["build"], _g["ideals_upto"]
LEDGER = []
def check(b, c, name, cond):
    assert cond, name; LEDGER.append((b, c, name))
rng = np.random.default_rng(93)
# ---- (1) el teorema, en una base generica
def fhat_rows(x, D, r): return np.exp(1j * r * x) * (2 * np.sin(r * D / 2) / r)
for trial in range(30):
    N = int(rng.integers(8, 40)); L = float(rng.uniform(2, 12)); D = L / N; x = -L / 2 + (np.arange(N) + 0.5) * D
    g = float(rng.uniform(3, 40)); d = float(rng.uniform(0.01, 0.49))
    rs = [g + 1j * d, -g - 1j * d, g - 1j * d, -g + 1j * d]          # rho, 1-rho, rho_bar, 1-rho_bar  ->  gamma
    M = sum(np.outer(fhat_rows(x, D, r), fhat_rows(x, D, -r)) for r in rs); M = np.real(M + M.T) / 2
    f = rng.normal(size=N); A = fhat_rows(x, D, rs[0]) @ f; Bv = fhat_rows(x, D, -rs[0]) @ f
    J = np.eye(N)[::-1]; Pe = (np.eye(N) + J) / 2; Po = (np.eye(N) - J) / 2
    def sig(Mx): ev = np.linalg.eigvalsh(Mx); s = np.abs(ev).max() * 1e-9; return int((ev > s).sum()), int((ev < -s).sum())
    Ue = np.linalg.svd(Pe)[0][:, : N - N // 2]; Uo = np.linalg.svd(Po)[0][:, : N // 2]
    check("P", "P", f"t{trial}: la forma del cuadruple es 4 Re(A B)", abs(f @ M @ f - 4 * np.real(A * Bv)) < 1e-8 * (1 + abs(f @ M @ f)))
    check("P", "P", f"t{trial}: signatura (2,2)", sig(M) == (2, 2))
    check("P", "P", f"t{trial}: conmuta con la paridad tau", np.allclose(J @ M @ J, M))
    check("P", "P", f"t{trial}: (1,1) en pares y (1,1) en impares", sig(Ue.T @ M @ Ue) == (1, 1) and sig(Uo.T @ M @ Uo) == (1, 1))
    gr = float(rng.uniform(3, 40)); Mr = sum(np.outer(fhat_rows(x, D, r), fhat_rows(x, D, -r)) for r in (gr, -gr)); Mr = np.real(Mr + Mr.T) / 2
    check("P", "P", f"t{trial}: un cero sobre la recta aporta una forma semidefinida", np.linalg.eigvalsh(Mr)[0] > -1e-9 * np.abs(Mr).max())
# ---- (2) el mundo contrafactual: W verdadera, se quitan dos ceros y se pone un cuadruple
N = 64
g1, g2 = 6.648453344727715, 9.83144443288667
ALL = ideals_upto(10 ** 6)
rows = []
for L in (3.0, 5.0, 8.0, 10.0, 12.0, math.log(10 ** 6)):
    B = build(L, N); x = B["x"]; D = B["D"]
    W = B["Pole"] + (math.log(5) - 2 * math.log(math.pi)) * B["G0"] + 2 * B["Psi1"] - B["Pform"]([n for n, _ in ALL if n <= math.exp(L) + 1e-9])
    def zer(rs): M = sum(np.outer(fhat_rows(x, D, r), fhat_rows(x, D, -r)) for r in rs); return np.real(M + M.T) / 2
    J = np.eye(N)[::-1]; Ue = (np.eye(N) + J)[:, : N // 2] / math.sqrt(2); Uo = (np.eye(N) - J)[:, : N // 2] / math.sqrt(2)
    check("Z", "T", f"L={L:.1f}: la base de celdas es simetrica, W conmuta con tau", np.allclose(J @ W @ J, W, atol=1e-9 * np.abs(W).max()))
    for d in (0.45, 0.2, 0.1):
        gq = (g1 + g2) / 2
        Wp = W - zer([g1, -g1]) - zer([g2, -g2]) + zer([gq + 1j * d, -gq - 1j * d, gq - 1j * d, -gq + 1j * d])
        tol = 1e-6 * D
        ne = int((np.linalg.eigvalsh(Ue.T @ Wp @ Ue) < -tol).sum()); no = int((np.linalg.eigvalsh(Uo.T @ Wp @ Uo) < -tol).sum())
        rows.append((L, d, ne, no))
check("Z", "P", "cota: en cada ventana el indice de W' es <= 2, y <= 1 en pares y <= 1 en impares", all(r[2] <= 1 and r[3] <= 1 for r in rows))
check("Z", "T", "cuando se detecta, la direccion negativa aparece en alguna paridad", any(r[2] + r[3] >= 1 for r in rows))
check("Z", "T", "el indice de W' es 0 o 2, nunca 1: la paridad par y la impar se encienden juntas", all(r[2] == r[3] for r in rows))
both = [r for r in rows if r[2] == 1 and r[3] == 1]
if __name__ == "__main__":
    print("  L     delta | neg par  neg impar")
    for r in rows: print(f"{r[0]:6.2f} {r[1]:5.2f} |   {r[2]}       {r[3]}")
    print("se alcanza la cota 2 (una par y una impar) en:", [(round(r[0], 2), r[1]) for r in both])
    print(f"{len(LEDGER)} aserciones, 0 fallas")
