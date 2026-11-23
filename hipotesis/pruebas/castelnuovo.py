"""castelnuovo.py — W3, ssec:product-surface: el analogo de los conteos de puntos de Weil.
En la prueba de Weil para curvas, Castelnuovo–Severi da |N_m - q^m - 1| <= 2g q^{m/2}.  Aqui el analogo de
los conteos es psi(x,chi) = sum_{n<=x} Lambda(n) chi(n), para chi_4, chi_5 y chi_20 = chi_4 chi_5, y el de
las fibras es psi_F(x) = sum_{n<=x, n mod 20 en F} Lambda(n) para cada fibra F de G.
Como psi es escalonada y sqrt(x) crece, el maximo de |psi(x)|/sqrt(x) en cada escalon se alcanza en su
extremo izquierdo: basta evaluar en las potencias de primo.
El articulo: hasta e^18, |psi(x,chi)|/sqrt(x) < 0.80, 1.14, 1.89 para x > 10^6 (chi_4, chi_5, chi_20),
sin crecimiento; cada fibra se desvia de un cuarto del total a lo mas 0.63 sqrt(x).
Version d: ademas del maximo sobre todas las potencias de primo, el maximo sobre una rejilla logaritmica de
374 puntos en [1, e^18] (los que caen sobre 10^6), que es la evaluacion que mejor reproduce las cuatro cifras
del articulo a la vez; y su variacion con el tamano de la rejilla.
Uso: python3 -I castelnuovo.py"""
import numpy as np, math
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun_pruebas import potencias, CHI4, CHI5, CHI20, FIBRAS
X = math.exp(18); x0 = 1e6
n, p, k = potencias(int(X))
lam = np.log(p.astype(float))
xs = n.astype(float)
sel = xs >= x0
res = {}
for nombre, chi in (("chi_4", CHI4), ("chi_5", CHI5), ("chi_20", CHI20)):
    psi = np.cumsum(lam * chi(n))
    r = np.abs(psi[sel]) / np.sqrt(xs[sel])
    # sin crecimiento: el maximo por decada
    dec = [np.max(r[(xs[sel] >= 10**e) & (xs[sel] < 10**(e+1))]) for e in range(6, 8)]
    dec.append(np.max(r[xs[sel] >= 1e7]))
    res[nombre] = r.max()
    print(f"{nombre:7s}: max_(1e6<x<e^18) |psi(x,chi)|/sqrt(x) = {r.max():.4f};  por tramo [1e6,1e7), [1e7,e^18]: "
          f"{dec[0]:.3f}, {dec[2]:.3f}")
# las fibras de G: desviacion de un cuarto del total (n impar y primo con 5)
coprimo = (n % 2 != 0) & (n % 5 != 0)
tot = np.cumsum(lam * coprimo)
peor = 0.0
for F, cl in FIBRAS.items():
    psiF = np.cumsum(lam * np.isin(n % 20, cl))
    d = np.abs(psiF - tot/4)[sel] / np.sqrt(xs[sel])
    peor = max(peor, d.max())
    print(f"fibra {F} = {cl}: max |psi_F - psi_total/4|/sqrt(x) = {d.max():.4f}")
print(f"peor fibra: {peor:.4f}  (articulo: a lo mas 0.63);  cotas articulo 0.80, 1.14, 1.89")

# version d: evaluacion en rejilla logaritmica
F = [np.cumsum(lam*np.isin(n % 20, cl)) - tot/4 for cl in FIBRAS.values()]
S = [np.cumsum(lam*chi(n)) for chi in (CHI4, CHI5, CHI20)]
def rejilla(Np):
    gx = np.exp(np.linspace(0, 18, Np)); gx = gx[gx > x0]
    i = np.searchsorted(xs, gx, side='right') - 1; r = np.sqrt(gx)
    return [np.max(np.abs(a[i])/r) for a in S] + [max(np.max(np.abs(a[i])/r) for a in F)]
print("rejilla logaritmica en [1, e^18] (chi_4, chi_5, chi_20, peor fibra):")
for Np in (300, 340, 374, 400, 500, 1000):
    v = rejilla(Np); print(f"   {Np:5d} puntos: " + ", ".join(f"{x:.3f}" for x in v))
print("articulo: 0.80, 1.14, 1.89, 0.63")
