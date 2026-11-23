"""gram.py — W3, prop:intersection-form: la forma de Weil en dimension ocho es una matriz de Gram.
Funciones de prueba pares: g_0 = T(u), g_j = T(u-j) + T(u+j) (j = 1..7), T(u) = (1-|u|)^+ (triangulos
centrados en 0, +-1, ..., +-7); h_jk = g_j * g_k tiene soporte en |u| <= j+k+2 <= 16.
Forma de Weil de L(s,chi_5):  M_jk = A(h_jk) - 2 sum_n Lambda(n) chi_5(n) n^{-1/2} h_jk(log n)  (primos bajo e^16.2),
con A el termino arquimediano (conductor 5, par).  Si las alturas son reales es la matriz de Gram
sum_rho ghat_j(gamma) ghat_k(gamma) (prop:intersection-form (i)), ghat_j(r) = 2cos(jr)(sin(r/2)/(r/2))^2.
Para zeta: la parte local (arquimediana menos lugares) y el polo, v v^T con v_j = sqrt2 ghat_j(i/2);
el indice de Hodge pide un solo autovalor negativo de la parte local, en la direccion del polo, y total >= 0
(prop:intersection-form (ii)).
El articulo: para chi_5 la forma desde los primos es la de Gram de los 397 ceros (entradas a 3.5e-6), ocho
autovalores positivos de 3e-5 a 0.048; para zeta un solo negativo, -3646, siete positivos, total >= 0.
Uso: python3 -I gram.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, mpmath as mp
from comun_pruebas import potencias, ceros_chi5, CHI5, EG
def A2(v):                              # T*T, autocorrelacion del triangulo de semiancho 1
    v = np.abs(v)
    return np.where(v <= 1, 2/3 - v**2 + v**3/2, np.where(v <= 2, (2 - v)**3/6, 0.0))
J = 8
def shifts(j): return [0] if j == 0 else [j, -j]
def h(j, k, u):
    return sum(A2(u - a - b) for a in shifts(j) for b in shifts(k))
def arch(j, k, q):
    hf = lambda u: float(h(j, k, np.array([float(u)]))[0])
    h0 = hf(0)
    knots = sorted(set([0.0] + [abs(a + b) + d for a in shifts(j) for b in shifts(k) for d in (-2, -1, 0, 1, 2)
                                if abs(a + b) + d > 0]))
    pts = [mp.mpf(x) for x in knots] + [mp.inf]
    I = mp.quad(lambda u: (mp.e**(-2*u)*h0 - mp.e**(-u/2)*hf(u))/(1 - mp.e**(-2*u)), pts)
    return h0*(math.log(q/math.pi) - EG) + 2*float(I)
n, p, kk = potencias(int(math.exp(16.2)))
ln = np.log(n.astype(float)); w = np.log(p.astype(float))/np.sqrt(n.astype(float))
c = CHI5(n).astype(float)
M5 = np.zeros((J, J)); Mz = np.zeros((J, J))
for j in range(J):
    for k in range(j, J):
        hv = h(j, k, ln)
        M5[j, k] = M5[k, j] = arch(j, k, 5) - 2*np.sum(w*c*hv)
        Mz[j, k] = Mz[k, j] = arch(j, k, 1) - 2*np.sum(w*hv)
# lado de los ceros: Gram de los 397 ceros de L(s,chi_5) (+-gamma)
g = ceros_chi5()
T = (np.sin(g/2)/(g/2))**2
Gv = np.array([T if j == 0 else 2*np.cos(j*g)*T for j in range(J)])
G5 = 2*Gv @ Gv.T
e5 = np.linalg.eigvalsh(M5)
print(f"chi_5: max |M - Gram de los ceros| = {np.max(np.abs(M5 - G5)):.1e};  autovalores de M: de {e5[0]:.1e} a {e5[-1]:.3f}"
      f"  ({'todos positivos' if e5[0] > 0 else 'NO todos positivos'})")
# zeta: polo como clase amplia
Th = (math.sinh(0.25)/0.25)**2
v = np.array([math.sqrt(2)*(Th if j == 0 else 2*math.cosh(j/2)*Th) for j in range(J)])
el, U = np.linalg.eigh(Mz)
et = np.linalg.eigvalsh(np.outer(v, v) + Mz)
cosang = abs(U[:, 0] @ v)/np.linalg.norm(v)
print(f"zeta, parte local: autovalores {', '.join(f'{x:.4g}' for x in el)}")
print(f"  negativos: {int(np.sum(el < 0))}; el negativo {el[0]:.0f}, coseno con la direccion del polo {cosang:.4f}")
print(f"  total (polo + local): menor autovalor {et[0]:.2e}  ({'>= 0' if et[0] > -1e-9 else '< 0'})")
print("articulo: chi_5 a 3.5e-6, autovalores de 3e-5 a 0.048; zeta: un negativo -3646, siete positivos, total >= 0")
