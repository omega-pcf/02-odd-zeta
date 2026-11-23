"""rigorous_chain.py — W3, ssec:golden-field: las primeras ventanas del campo dorado sobre todo el espacio.
Para g soportada en un intervalo de longitud S (por traslacion, I = [-L, L], L = S/2), la forma de Weil de
zeta_K, K = Q(sqrt5), es
  Q(g) = (1/2pi) int |ghat(r)|^2 m_K(r) dr + 2 ghat(i/2) ghat(-i/2),   m_K(r) = W_K(r) - 2 sum_n c_n cos(r log n),
  W_K(r) = log(5/pi^2) + 2 Re psi(1/4 + ir/2),  c_n = Lambda(n)(1 + chi_5(n)) n^{-1/2},
y en la variable x:  Q(g) = C_0 ||g||^2 + D(g) - 2 sum_n c_n h(log n) + 2 a(g) b(g),
con h(u) = int g(x) g(x+u) dx, D(g) = 4 int_0^inf w(u)(h(0)-h(u)) du, w(u) = e^{-u/2}/(1-e^{-2u}),
a(g) = int g e^{-x/2}, b(g) = int g e^{x/2}, C_0 = W_K(0) (arch_window.py).  El operador en L^2(I):
  A g = C_0 g + 2 int_0^inf w(u)[(g(x)-g~(x+u)) + (g(x)-g~(x-u))] du - sum_n c_n [g~(x+log n) + g~(x-log n)]
        + a(g) e^{x/2} + b(g) e^{-x/2}      (g~ la extension por cero).
1. Ritz: el menor autovalor de la matriz de Galerkin en los polinomios de grado < N (Legendre ortonormales).
2. Lehmann: con rho <= lambda_{N+1} (rho_interval.py), el problema (A1 - rho A0) x = mu (A2 - 2 rho A1 + rho^2 A0) x,
   A0 = <phi_i, phi_j>, A1 = <A phi_i, phi_j>, A2 = <A phi_i, A phi_j>, da lambda_1 >= rho + 1/mu_N (mu_N < 0 el
   mayor de los N valores mu, todos negativos), sin suponer nada de ningun autovalor.  A2 se calcula con el
   operador aplicado exactamente (cuadratura graduada hacia los extremos por la singularidad log de D en el borde).
El articulo (tabla de ssec:golden-field): S, lugares, N, rho, Ritz lambda_1, cota inferior de lambda_1:
  log4 - 28 3.4808 6.8081e-3 +6.8052e-3 | 1.5 4 50 3.0425 2.4904e-3 +2.4876e-3 | 1.7 4,5 60 1.7039 3.7152e-4 +3.7002e-4
  2.0 4,5 80 1.9369 1.2171e-5 +1.2108e-5 | 2.3 4,5,9 150 1.4234 1.8873e-7 +1.8771e-7
Uso: python3 -I rigorous_chain.py"""
import numpy as np, math, mpmath as mp
from numpy.polynomial.legendre import leggauss, legvander
mp.mp.dps = 30
C0 = float(mp.log(5) - 2*mp.log(mp.pi) - 2*mp.euler + 4*mp.quad(lambda u: (mp.e**(-2*u) - mp.e**(-u/2))/(1 - mp.e**(-2*u)), [0, 1, mp.inf]))
def cn(n):
    chi = [0, 1, -1, -1, 1][n % 5]
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0: m //= p
            return math.log(p)*(1 + chi)/math.sqrt(n) if m == 1 else 0.0
w = lambda u: np.exp(-u/2)/(-np.expm1(-2*u))
Wtail = lambda d: np.arctanh(np.exp(-d/2)) + np.arctan(np.exp(-d/2))      # int_d^inf w
def phi(N, L, x):
    return legvander(np.clip(x/L, -1, 1), N - 1)*np.sqrt((2*np.arange(N) + 1)/(2*L))*((np.abs(x) <= L)[:, None])
def cruz(N, L, u, Q):
    if u >= 2*L: return np.zeros((N, N))
    t, wt = leggauss(Q); a, b = -L, L - u
    x = (b - a)/2*t + (a + b)/2; ww = wt*(b - a)/2
    H = (phi(N, L, x)*ww[:, None]).T @ phi(N, L, x + u)
    return (H + H.T)/2
def lugares(S): return [(n, cn(n)) for n in range(2, int(math.exp(S)) + 2) if math.log(n) < S and cn(n) != 0]
def galerkin(S, N):
    L = S/2; Q = N + 20
    tu, wu = leggauss(N + 60); U = L*(tu + 1); WU = wu*L
    D = sum(4*ww*w(u)*(np.eye(N) - cruz(N, L, u, Q)) for u, ww in zip(U, WU)) + 4*Wtail(2*L)*np.eye(N)
    P = sum(-2*c*cruz(N, L, math.log(n), Q) for n, c in lugares(S)) if lugares(S) else 0
    t, wt = leggauss(Q); x = L*t; F = phi(N, L, x); ww = wt*L
    a = F.T @ (ww*np.exp(-x/2)); b = F.T @ (ww*np.exp(x/2))
    return C0*np.eye(N) + D + P + np.outer(a, b) + np.outer(b, a), a, b
def nodos_graduados(L, cortes=(), m=30, q=0.5, k=16):
    """composite Gauss-Legendre en [-L, L]: graduada geometricamente hacia los dos extremos (singularidad log
    de D en el borde) y hacia cada corte interior +-(L - log n) (saltos de las traslaciones por log n)"""
    pts = sorted(set([-L, L] + [c for c in cortes if -L < c < L]))
    xs, ws = [], []
    t, wt = leggauss(k)
    for lo, hi in zip(pts[:-1], pts[1:]):
        mid = (lo + hi)/2
        for a0, b0, s in ((lo, mid, -1), (mid, hi, 1)):
            # graduacion hacia el extremo del subintervalo (b0 si s = 1, a0 si s = -1)
            h = b0 - a0
            br = [h*(1 - q**j) for j in range(m)] + [h]
            for u0, u1 in zip(br[:-1], br[1:]):
                a, b = (a0 + u0, a0 + u1) if s == 1 else (b0 - u1, b0 - u0)
                xs.append((b - a)/2*t + (a + b)/2); ws.append(wt*(b - a)/2)
    return np.concatenate(xs), np.concatenate(ws)
def aplica(S, N, a, b):
    """A phi_j en los nodos x (matriz nodos x N) y los pesos"""
    L = S/2
    cortes = [s_*(L - math.log(n)) for n, c in lugares(S) for s_ in (1, -1)]
    x, wx = nodos_graduados(L, cortes, m=30, k=max(16, N//5))
    F = phi(N, L, x)
    AF = C0*F + np.outer(np.exp(x/2), a) + np.outer(np.exp(-x/2), b)
    tu, wu = leggauss(N + 40)
    for s in (1, -1):                     # 2 int_0^{d} w(u)(g(x) - g(x+su)) du + 2 g(x) int_d^inf w
        d = L - s*x
        for i in range(len(x)):
            if d[i] <= 0: continue
            u = d[i]/2*(tu + 1); wwu = wu*d[i]/2
            G = phi(N, L, x[i] + s*u)
            AF[i] += 2*((wwu*w(u)) @ (F[i][None, :] - G)) + 2*Wtail(d[i])*F[i]
    for n, c in lugares(S):
        l = math.log(n)
        AF -= c*(phi(N, L, x + l) + phi(N, L, x - l))
    return x, wx, F, AF
filas = [(math.log(4), 28, 3.4808), (1.5, 50, 3.0425), (1.7, 60, 1.7039), (2.0, 80, 1.9369), (2.3, 150, 1.4234)]
print(" S      lugares   N    rho      Ritz lambda_1   Rayleigh(op. exacto)   cota inferior lambda_1")
for S, N, rho in filas:
    M, a, b = galerkin(S, N)
    ev, V = np.linalg.eigh(M)
    x, wx, F, AF = aplica(S, N, a, b)
    A0 = (F*wx[:, None]).T @ F; A1 = (AF*wx[:, None]).T @ F; A1 = (A1 + A1.T)/2; A2 = (AF*wx[:, None]).T @ AF
    v = V[:, 0]; ray = (v @ A1 @ v)/(v @ A0 @ v)
    Bm = A2 - 2*rho*A1 + rho**2*A0
    from scipy.linalg import eigh
    mu = eigh(A1 - rho*A0, Bm, eigvals_only=True)
    neg = mu[mu < 0]
    cota = rho + 1/neg.max()
    pl = ",".join(str(n) for n, c in lugares(S)) or "-"
    print(f" {S:.3f}  {pl:8s} {N:4d}  {rho:.4f}   {ev[0]:.4e}      {ray:.4e}            {cota:+.4e}   ({len(neg)} de {N} mu < 0; Ritz bajo rho: {int(np.sum(ev < rho))})")
