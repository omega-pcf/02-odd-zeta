"""orbita_cert.py — W4–W5, ssec:weil-closure: la orbita certificada, y la familia de la capa quintica.
1. chi_5, triangulo de semiancho a = 0.01, p = 2, k = 0..25: t_k = W(g_a, tau_{k log 2} g_a) (zeroside.py).
2. La representacion de grado 4 de la capa quintica (cuintica.py: conductor 5^7, factor gamma
   Gamma_R(s)^2 Gamma_R(s+1)^2, a(p^k) = #raices de x^5+5x^3+5x-1 en F_{p^k} - 1), a = 0.1, p = 2, k = 0..25:
   t_k = A_4(h_s) - sum_n Lambda(n) a(n) n^{-1/2} [A_a(log n - s) + A_a(log n + s)].
Se acotan |t_k|/t_0 (k = 1..25) y el menor autovalor de la matriz de Toeplitz (t_{|j-k|}) relativo a t_0.
Redondeo hacia afuera: las sumas de primos en doble precision llevan la cota de error
|error| <= (N+2) 2^-52 sum |termino| (mas 4 ulp por termino de log, sqrt y A); el termino arquimediano (mpmath, 30
digitos) lleva su estimacion de error; el autovalor, la cota de Weyl ||E||_F mas n ||T|| 2^-52.  Las cotas se
redondean hacia afuera.
El articulo: chi_5 (a = 0.01, p = 2): |t_k| <= 0.1122 t_0 para k <= 25 y menor autovalor >= 0.248 t_0;
capa quintica (a = 0.1): 0.158 t_0 y 0.506 t_0.
Uso: python3 -I orbita_cert.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, math, mpmath as mp
from comun_pruebas import potencias, CHI5, A_tri, EG
from cuintica import a_pk
mp.mp.dps = 30
EPS = 2.0**-52
def arch(a, s, par):
    """h0(-log pi - gamma) + 2 int [e^{-2u} h0 - e^{-(1/2+par)u} hs(u)]/(1-e^{-2u}) du, con estimacion de error."""
    b = mp.mpf(1)/2 + par
    hs = lambda u: (A_tri(float(u) - s, a) + A_tri(-float(u) - s, a))/2
    h0 = float(A_tri(-s, a))
    kn = sorted(set([0.0] + [x for x in (s - 2*a, s - a, s, s + a, s + 2*a) if x > 0]))
    I, err = mp.quad(lambda u: (mp.e**(-2*u)*h0 - mp.e**(-b*u)*float(hs(u)))/(1 - mp.e**(-2*u)),
                     [mp.mpf(x) for x in kn] + [mp.inf], error=True)
    return h0*(-math.log(math.pi) - EG) + 2*float(I), 2*float(err) + 1e-15
def orbita(a, K, coef, gamma_fac, logq, Nmax):
    n, p, k = potencias(Nmax)
    ln = np.log(n.astype(float)); w = np.log(p.astype(float))/np.sqrt(n.astype(float))
    c = coef(n, p, k)
    t, e = [], []
    for kk in range(K + 1):
        s = kk*math.log(2)
        A = sum(m*arch(a, s, par)[0] for par, m in gamma_fac); eA = sum(m*arch(a, s, par)[1] for par, m in gamma_fac)
        A += float(A_tri(-s, a))*logq
        sel = (np.abs(ln - s) < 2*a) | (ln + s < 2*a)
        term = w[sel]*c[sel]*(A_tri(ln[sel] - s, a) + A_tri(ln[sel] + s, a))
        t.append(A - term.sum())
        e.append(eA + (len(term) + 2 + 4)*EPS*np.abs(term).sum() + 4*EPS*abs(A))
    return np.array(t), np.array(e)
def certifica(nombre, t, e):
    K = len(t) - 1
    t0lo = t[0] - e[0]
    rmax = max((abs(t[kk]) + e[kk])/t0lo for kk in range(1, K + 1))
    T = np.array([[t[abs(i - j)] for j in range(K + 1)] for i in range(K + 1)])
    E = np.array([[e[abs(i - j)] for j in range(K + 1)] for i in range(K + 1)])
    lam = np.linalg.eigvalsh(T)[0] - np.linalg.norm(E) - (K + 1)*np.linalg.norm(T, 2)*EPS
    lamr = lam/(t[0] + e[0])
    # redondeo hacia afuera de las cotas impresas
    print(f"{nombre}: |t_k|/t_0 <= {math.ceil(rmax*1e4)/1e4:.4f} (k = 1..{K});  menor autovalor de Toeplitz >= "
          f"{math.floor(lamr*1e3)/1e3:.3f} t_0;  error maximo de las entradas {e.max():.1e}")
# 1. chi_5
c5 = lambda n, p, k: CHI5(n).astype(float)
t, e = orbita(0.01, 25, c5, [(0, 1)], math.log(5), int(math.exp(25*math.log(2) + 0.02)) + 1)
certifica("chi_5, a = 0.01, p = 2", t, e)
# 2. capa quintica
def cq(n, p, k):
    return np.array([a_pk(int(pp), int(kk)) for pp, kk in zip(p, k)], float)
t, e = orbita(0.1, 25, cq, [(0, 2), (1, 2)], 7*math.log(5), int(math.exp(25*math.log(2) + 0.2)) + 1)
certifica("capa quintica (conductor 5^7), a = 0.1, p = 2", t, e)
print("articulo: chi_5: 0.1122 t_0 y 0.248 t_0; capa quintica: 0.158 t_0 y 0.506 t_0")
