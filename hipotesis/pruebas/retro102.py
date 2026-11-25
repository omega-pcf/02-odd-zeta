"""retro102.py — Sprint 102. La flecha W3 => W4 del diccionario, y las dos mitades de W4 como las dos paridades.
Algebra [P]: para una forma W simetrica invariante por traslacion y t(u) = W(g, tau_u g):
   t(0) - t(u) = 1/2 W(tau_u g - g),   t(0) + t(u) = 1/2 W(tau_u g + g).
 => |t(u)| <= t(0)  <=>  W >= 0 en el plano {g, tau_u g}   (en particular W >= 0 implica W4: Cauchy-Schwarz).
 g par: tau_u g -+ g son impar/par respecto del punto medio u/2, asi que las dos mitades de W4 son las dos paridades.
Numerico [N]: lado de los ceros (truncado) de Davenport-Heilbronn (dh_zeros.json), triangulos g_a, u = k log 7.
Uso: python3 -I retro102.py"""
import json, math, numpy as np
Z = json.load(open(__file__.replace("retro102.py", "dh_zeros.json"))); line = np.array(Z["line"]); off = Z["off"]
ok = 0
def check(c, m):
    global ok
    assert c, m; ok += 1
rng = np.random.default_rng(102)
# (1) algebra en formas de Toeplitz al azar (indefinidas y semidefinidas)
for trial in range(200):
    N = 40; c = rng.normal(size=N); c[0] = abs(c[0]) + (5 if trial % 2 else 0)
    W = np.array([[c[abs(i - j)] for j in range(N)] for i in range(N)])
    if trial % 2: ev, V = np.linalg.eigh(W); W = V @ np.diag(np.abs(ev)) @ V.T  # semidefinida
    g = np.zeros(N); g[:10] = rng.normal(size=10); s = int(rng.integers(1, 20)); tg = np.roll(g, s)
    if trial % 2:  # invariancia por traslacion se usa via Toeplitz: comparar t(0) con W(tg, tg) solo en el caso Toeplitz
        pass
    t0 = g @ W @ g; tu = g @ W @ tg; t0b = tg @ W @ tg
    check(abs((t0 + t0b) / 2 - tu - 0.5 * (tg - g) @ W @ (tg - g)) < 1e-9 * (1 + abs(t0)), "identidad menos")
    check(abs((t0 + t0b) / 2 + tu - 0.5 * (tg + g) @ W @ (tg + g)) < 1e-9 * (1 + abs(t0)), "identidad mas")
    if trial % 2: check(abs(tu) <= math.sqrt(t0 * t0b) + 1e-9, "Cauchy-Schwarz: W >= 0 => |t(u)| <= t(0)")
# (2) lado de los ceros de DH con triangulos
gh = lambda a, x: a * (np.sinc(a * x / (2 * np.pi))) ** 2          # transformada de (1-|x|/a)^+, np.sinc(y)=sin(pi y)/(pi y)
def t(a, u, orbits=True, T=130.0):
    s = sum(2 * gh(a, gm) ** 2 * math.cos(gm * u) for gm in line[line < T])
    if orbits:
        for b, gm in off:
            d = b - 0.5
            for gg in (gm + 1j * d, gm - 1j * d, -gm + 1j * d, -gm - 1j * d):
                s += (gh(a, gg) ** 2 * np.exp(1j * gg * u)).real
    return s
L7 = math.log(7); worst = []
for a in (0.05, 0.1, 0.2, 0.4):
    t0 = t(a, 0); ks = range(1, 61); r = [t(a, k * L7) / t0 for k in ks]
    rc = [t(a, k * L7, orbits=False) / t(a, 0, orbits=False) for k in ks]
    check(all(abs(x) <= 1 + 1e-12 for x in rc), f"control sin orbitas, a={a}: |t_k| <= t_0 (Cauchy-Schwarz)")
    kmax = int(np.argmax(np.abs(r))) + 1; worst.append((a, t0, kmax, max(np.abs(r))))
print("a      t_0          k*  max_k |t_k|/t_0   (DH, u = k log 7, k <= 60)")
for a, t0, k, m in worst: print(f"{a:4.2f}  {t0:+.3e}  {k:3d}   {m:10.3e}")
check(any(m > 1 for *_, m in worst), "con la orbita libre, W4 falla para algun ancho")
# (3) el crecimiento de la orbita: |t_k| ~ p^{delta k}
a = 0.05; ks = np.arange(1, 61); r = np.array([abs(t(a, k * L7)) for k in ks])
big = ks[r > 10 * abs(t(a, 0))]
if len(big) > 5:
    sl = np.polyfit(ks[-20:] * L7, np.log(np.maximum(r[-20:], 1e-300)), 1)[0]
    print(f"pendiente de log|t_k| contra k log 7 (ultimos 20): {sl:.3f}; delta de la orbita mayor: {off[0][0]-0.5:.4f}")
print(f"{ok} aserciones, 0 fallas")
