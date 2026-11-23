"""field_signature.py — W3, ssec:golden-field: la signatura del indice de Hodge del campo dorado.
zeta_K = zeta L(s,chi_5), K = Q(sqrt5).  Funciones de prueba pares en un soporte fijo: para J funciones,
triangulos de semiancho a = 8/J centrados en 0, +-a, ..., +-(J-1)a (J = 8 son las de gram.py); h_jk = g_j * g_k
tiene soporte en |u| <= 16 (primos bajo e^16.2).
  parte local (arquimediana menos lugares) M_jk = A_zeta(h) + A_5(h) - 2 sum_n Lambda(n)(1+chi_5(n)) n^{-1/2} h(log n),
  polo: 2 v v^T con v_j = ghat_j(i/2);  forma total = 2vv^T + M.
Indice de Hodge: M tiene exactamente un autovalor negativo, en la direccion del polo, y el total es >= 0.
Ademas, en la forma de chi_5, el termino principal de la suma de primos es el funcional del polo y cada tipo de
orbita (partidos chi_5(p) = +1, inertes -1) lleva la mitad: el cociente v^T P_partidos v / v^T P_(p no 5) v.
El articulo: un negativo en la direccion del polo y total >= 0 con 8, 12, 16, 20 y 24 funciones; cociente 0.4994.
Uso: python3 -I field_signature.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, mpmath as mp
from comun_pruebas import potencias, CHI5, EG
n, p, kk = potencias(int(math.exp(16.2)))
ln = np.log(n.astype(float)); w = np.log(p.astype(float))/np.sqrt(n.astype(float)); c = CHI5(n).astype(float)
def A2(v, a):                            # autocorrelacion del triangulo de semiancho a
    v = np.abs(v)/a
    return a*np.where(v <= 1, 2/3 - v**2 + v**3/2, np.where(v <= 2, (2 - v)**3/6, 0.0))
def familia(J):
    a = 8.0/J
    sh = [[0.0]] + [[j*a, -j*a] for j in range(1, J)]
    return a, sh
def h(j, k, u, a, sh): return sum(A2(u - x - y, a) for x in sh[j] for y in sh[k])
def arch_par(j, k, a, sh, q):
    hf = lambda u: float(h(j, k, np.array([float(u)]), a, sh)[0])
    h0 = hf(0)
    kn = sorted(set([0.0] + [abs(x + y) + d*a for x in sh[j] for y in sh[k] for d in (-2, -1, 0, 1, 2) if abs(x + y) + d*a > 1e-12]))
    I = mp.quad(lambda u: (mp.e**(-2*u)*h0 - mp.e**(-u/2)*hf(u))/(1 - mp.e**(-2*u)), [mp.mpf(x) for x in kn] + [mp.inf])
    return h0*(math.log(q/math.pi) - EG) + 2*float(I)
def That(z, a): return a*(mp.sin(a*z/2)/(a*z/2))**2       # FT del triangulo de semiancho a
for J in (8, 12, 16, 20, 24):
    a, sh = familia(J)
    M = np.zeros((J, J)); Ps = np.zeros((J, J)); Pc = np.zeros((J, J))
    pr = kk == 1; sp = pr & (c == 1); co = pr & (c != 0)
    for j in range(J):
        for k in range(j, J):
            hv = h(j, k, ln, a, sh)
            Aj = arch_par(j, k, a, sh, 1) + arch_par(j, k, a, sh, 5)
            M[j, k] = M[k, j] = Aj - 2*np.sum(w*(1 + c)*hv)
            Ps[j, k] = Ps[k, j] = np.sum((w*hv)[sp]); Pc[j, k] = Pc[k, j] = np.sum((w*hv)[co])
    Th = float(That(0.5j, a).real)
    v = np.array([Th if j == 0 else 2*math.cosh(sh[j][0]/2)*Th for j in range(J)])
    el, U = np.linalg.eigh(M)
    et = np.linalg.eigvalsh(2*np.outer(v, v) + M)
    cosang = abs(U[:, 0] @ v)/np.linalg.norm(v)
    rat = (v @ Ps @ v)/(v @ Pc @ v)
    print(f"J = {J:2d}: negativos de la parte local {int(np.sum(el < 0))} (el menor {el[0]:.4g}, coseno con el polo {cosang:.4f}); "
          f"segundo {el[1]:.2e}; total: menor autovalor {et[0]:+.2e}; cociente partidos/todos {rat:.4f}")
print("articulo: un negativo, en la direccion del polo, y total >= 0 con 8, 12, 16, 20, 24 funciones; cociente 0.4994")
