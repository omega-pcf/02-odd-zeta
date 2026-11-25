"""§73: las 20 capas del vértice al azar con primos hasta 10⁹ (datos de v32_capas_hasta_1e9.py).
  D_i(X) = Σ_{p≤X} log p·([i ∣ índice] − P_p(i)),  X de 10⁴ a 10⁹ (5 décadas).
  (a) ¿término sistemático b_i·X?  (b) exponente θ de la fluctuación en 5 ventanas de una década.
  (c) Identidades exactas con las familias (§46, §54, level80_coeff): la suma de la forma base de cada
      familia es q veces la desviación de su capa:  nivel 80 = 4·D₂,  nivel 135 = 3·D₃,  F₂₀ = 5·D₅.
  (d) La energía de cada capa, E_i = media en log X de (D_i/√X − media)², con la de las familias."""
from comun import *
import json, numpy as np
c = json.load(open(os.path.join(AQUI, 'datos', 'capas_hasta_1000000000.json')))
f = json.load(open(os.path.join(AQUI, 'datos', 'familias_hasta_1000000000.json')))
Xs = np.array(c['Xs'], float)
comprobar('las dos tablas usan la misma rejilla de 400 valores de X', np.array_equal(Xs, np.array(f['Xs'], float)))
for fam, q, i in (('80', 4, 2), ('135', 3, 3), ('F20', 5, 5)):
    T = np.array(f['res'][fam]['1']['re']) * np.sqrt(Xs); D = q * np.array(c['D'][str(i)])
    err = np.max(np.abs(T - D) / np.maximum(1, np.abs(D)))
    comprobar('familia %s, forma base = %d·D_%d en los 400 valores de X (error relativo < 10⁻⁹)' % (fam, q, i), err < 1e-9, '(%.1e)' % err)
w = Xs >= 1e4
print('§73  capa   b_i         rms(D/√X) por década 10⁴…10⁹                 θ      energía')
bs = []; ths = []; en = {}
for i in map(int, c['D']):
    D = np.array(c['D'][str(i)])
    b = np.sum(D[w] * Xs[w]) / np.sum(Xs[w] ** 2); bs.append(b)
    rm = []; cen = []
    for k in range(4, 9):
        s = (Xs >= 10 ** k) & (Xs < 10 ** (k + 1)); rm.append(np.sqrt(np.mean(D[s] ** 2))); cen.append(10 ** (k + 0.5))
    th = np.polyfit(np.log(cen), np.log(rm), 1)[0]; ths.append(th)
    v = D[w] / np.sqrt(Xs[w]); en[i] = np.mean((v - v.mean()) ** 2)
    print('     %3d  %+.2e   ' % (i, b) + '  '.join('%.3f' % (r / math.sqrt(x)) for r, x in zip(rm, cen)) + '    %.2f    %.4f' % (th, en[i]))
bs = np.array(bs); ths = np.array(ths)
print('   máx |b_i| = %.1e;  θ: media %.3f, mediana %.3f, rango %.2f – %.2f' % (np.max(np.abs(bs)), ths.mean(), np.median(ths), ths.min(), ths.max()))
comprobar('sin término sistemático hasta 10⁹: |b_i| < 10⁻⁴ en las 20 capas', np.max(np.abs(bs)) < 1e-4)
comprobar('θ medio entre 0,4 y 0,6 (escala √X) en cinco décadas', 0.4 <= ths.mean() <= 0.6)
comprobar('ninguna capa crece más deprisa que X^0,7', np.all(ths < 0.7))
V = {2: 0.618 / 16, 3: json.load(open(os.path.join(AQUI, 'datos', 'torcidos135.json')))['1']['V'] / 9, 5: 2.307 / 25}
print('   energía de las capas 2, 3, 5 frente a V/q² de su forma base: ' +
      ', '.join('%d: %.4f / %.4f' % (i, en[i], V[i]) for i in (2, 3, 5)))
comprobar('energía de las capas 2, 3, 5 = V/q² de su familia (cociente 0,8–1,25)', all(0.8 < en[i] / V[i] < 1.25 for i in (2, 3, 5)))
# §74: la reducción, con los datos.  energy_scale / layer_energy_iff_family: energía(q·D) = q²·energía(D)
Tb = {fam: np.array(f['res'][fam]['1']['re'])[w] for fam in ('80', '135', 'F20')}
def ener(x): return np.mean((x - x.mean()) ** 2)
ok = True
for fam, q, i in (('80', 4, 2), ('135', 3, 3), ('F20', 5, 5)):
    d = np.array(c['D'][str(i)])[w] / np.sqrt(Xs[w]); ok &= abs(ener(Tb[fam]) - q * q * ener(d)) < 1e-9 * ener(Tb[fam])
comprobar('energía de la forma base = q²·energía de su capa (layer_energy_iff_family), las tres familias', ok)
# energy_of_combination: media(Σ c_k D_k)² ≤ n·Σ c_k²·media(D_k²), con combinaciones al azar de las 20 capas
rng = np.random.default_rng(5); ok = True; peor = 0
Dk = np.array([np.array(c['D'][k])[w] / np.sqrt(Xs[w]) for k in c['D']])
for _ in range(200):
    cc = rng.normal(size=len(Dk)); E = cc @ Dk
    lhs = np.mean(E ** 2); rhs = len(Dk) * np.sum(cc ** 2 * np.mean(Dk ** 2, axis=1))
    ok &= lhs <= rhs; peor = max(peor, lhs / rhs)
comprobar('energy_of_combination en 200 combinaciones al azar de las 20 capas', ok, '(peor cociente %.3f)' % peor)
salir()
