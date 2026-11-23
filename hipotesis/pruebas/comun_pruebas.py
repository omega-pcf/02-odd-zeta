"""comun_pruebas.py — utilidades comunes de hipotesis/pruebas/: criba, potencias de primo con Lambda,
caracteres modulo 20 (chi_4, chi_5, chi_20 = chi_4 chi_5) y las fibras de G : (Z/20)^* -> Z2 x Z2."""
import numpy as np
def criba(N):
    s = np.ones(N + 1, dtype=bool); s[:2] = False
    for i in range(2, int(N**.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
def potencias(N, primos=None):
    """(n, p, k) para cada potencia de primo n = p^k <= N, ordenadas por n."""
    P = criba(N) if primos is None else primos
    ns = [P.astype(np.int64)]; ps = [P.astype(np.int64)]; ks = [np.ones(len(P), np.int64)]
    k = 2
    while True:
        Q = P[P.astype(float)**k <= N].astype(np.int64)
        if len(Q) == 0: break
        ns.append(Q**k); ps.append(Q); ks.append(np.full(len(Q), k)); k += 1
    n = np.concatenate(ns); p = np.concatenate(ps); kk = np.concatenate(ks)
    o = np.argsort(n, kind='stable')
    return n[o], p[o], kk[o]
CHI4 = lambda n: np.where(n % 2 == 0, 0, np.where(n % 4 == 1, 1, -1))
CHI5 = lambda n: np.array([0, 1, -1, -1, 1])[n % 5]
CHI20 = lambda n: CHI4(n) * CHI5(n)
FIBRAS = {(0, 0): (1, 9), (0, 1): (13, 17), (1, 0): (11, 19), (1, 1): (3, 7)}
def G(a):
    """G(a) = (fibra en chi_4, fibra en chi_5): 0 si el caracter vale +1, 1 si vale -1."""
    return (0 if CHI4(np.array([a]))[0] == 1 else 1, 0 if CHI5(np.array([a]))[0] == 1 else 1)

# ---- la forma de Fejer (ssec:field-positivity) ----
import math
EG = 0.5772156649015329
def arch_fejer(L, q=5, par=0):
    """Termino arquimediano de la formula explicita (Iwaniec–Kowalski 5.12) para la ventana de Fejer
    g_L(u) = (1-|u|/2L)^+:  (1/2pi) int h_L(r)[log(q/pi) + Re psi(c + ir/2)] dr, c = 1/4 (par), 3/4 (impar),
    escrito en la variable u con la integral de Gauss para psi:
      g(0)(log(q/pi) - gamma_E) + 2 int_0^inf [e^{-2u} g(0) - e^{-u/2} g(u)]/(1-e^{-2u}) du   (par)
      g(0)(log(q/pi) - gamma_E) + 2 int_0^inf [e^{-2u} g(0) - e^{-3u/2} g(u)]/(1-e^{-2u}) du  (impar).
    Contrastado con la forma en r (digamma) a 1e-9."""
    import mpmath as mp
    b = mp.mpf(1)/2 if par == 0 else mp.mpf(3)/2
    g = lambda u: max(0.0, 1 - abs(float(u))/(2*L))
    I = mp.quad(lambda u: (mp.e**(-2*u) - mp.e**(-b*u)*g(u))/(1 - mp.e**(-2*u)), [0, 2*L, mp.inf])
    return float(math.log(q/math.pi) - EG + 2*I)
_PP = {}
def potencias_hasta(N):
    if N not in _PP: _PP[N] = potencias(N)
    return _PP[N]
def lado_primos(L, chi, N=None):
    """-2 sum Lambda(n) chi(n) n^{-1/2} g_L(log n), separado en: primos partidos (chi(p)=+1), inertes
    (chi(p)=-1) y potencias k >= 2.  Devuelve un dict."""
    N = int(math.exp(2*L)) + 1 if N is None else N
    n, p, k = potencias_hasta(N)
    m = np.log(n.astype(float)) < 2*L
    n, p, k = n[m], p[m], k[m]
    c = chi(n).astype(float)
    t = -2*np.log(p.astype(float))*c/np.sqrt(n.astype(float))*(1 - np.log(n.astype(float))/(2*L))
    cp = chi(p)
    return {'partidos': t[(k == 1) & (cp == 1)].sum(), 'inertes': t[(k == 1) & (cp == -1)].sum(),
            'potencias': t[k >= 2].sum(), 'cuadrados': t[k == 2].sum(), 'altas': t[k >= 3].sum(),
            'total': t.sum()}

def ceros_chi5():
    import json, os
    return np.array(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chi5_zeros_500.json'))))
def fejer_ceros(L, g, T=500.0, q=5, cola=True):
    """sum_rho h_L(gamma_rho) sobre los ceros +-gamma (L(s,chi) real), con los ceros 0<gamma<T de la lista g;
    con cola=True se suma la cola gamma > T con la densidad log(q t/2pi)/2pi y <sin^2> = 1/2."""
    h = 2*L*(np.sin(L*g)/(L*g))**2
    s = 2*h.sum()
    if cola:
        s += (2/L)*(math.log(q*T/(2*math.pi)) + 1)/(2*math.pi*T)
    return s

def polo_fejer(L):
    """h_L(i/2) + h_L(-i/2) = int g_L(u) 2 cosh(u/2) du: el termino del polo de zeta."""
    import mpmath as mp
    a = 2*L
    return float(4*mp.quad(lambda u: (1 - u/a)*mp.cosh(u/2), [0, a]))
def fejer_por_caracter(L):
    """Las cuatro sumas de Fejer de Q(i,sqrt5) desde los primos: zeta, chi_4, chi_5, chi_20 (primitivas)."""
    N = int(math.exp(2*L)) + 1
    n, p, k = potencias_hasta(N)
    m = np.log(n.astype(float)) < 2*L; n, p, k = n[m], p[m], k[m]
    w = np.log(p.astype(float))/np.sqrt(n.astype(float))*(1 - np.log(n.astype(float))/(2*L))
    out = {'zeta': polo_fejer(L) + arch_fejer(L, 1, 0) - 2*np.sum(w)}
    for nm, chi, q, par in (('chi_4', CHI4, 4, 1), ('chi_5', CHI5, 5, 0), ('chi_20', CHI20, 20, 1)):
        out[nm] = arch_fejer(L, q, par) - 2*np.sum(w*chi(n))
    return out

# ---- la orbita de Frobenius (ssec:weil-closure) ----
def A_tri(v, a):
    """autocorrelacion, en forma cerrada, del triangulo (1-|x|/a)^+ de semiancho a: soporte |v| <= 2a."""
    v = np.abs(np.asarray(v, float))/a
    return a*np.where(v <= 1, 2/3 - v**2 + v**3/2, np.where(v <= 2, (2 - v)**3/6, 0.0))
def arch_desplazada(a, s, q, par):
    """termino arquimediano de h(u) = A_tri(u - s), simetrizado, en la variable u (sin interpolacion)."""
    import mpmath as mp
    b = mp.mpf(1)/2 if par == 0 else mp.mpf(3)/2
    hs = lambda u: (float(A_tri(float(u) - s, a)) + float(A_tri(-float(u) - s, a)))/2
    h0 = float(A_tri(-s, a))
    kn = sorted(set([0.0] + [x for x in (s - 2*a, s - a, s, s + a, s + 2*a) if x > 0]))
    I = mp.quad(lambda u: (mp.e**(-2*u)*h0 - mp.e**(-b*u)*hs(u))/(1 - mp.e**(-2*u)), [mp.mpf(x) for x in kn] + [mp.inf])
    return h0*(math.log(q/math.pi) - EG) + 2*float(I)

# los ocho caracteres chi_4^a psi_5^b de (Z/20)^*, primitivos: (nombre, funcion en n, conductor, paridad)
def _psi5(n):
    t = {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}
    return np.array([t[int(x) % 5] for x in np.atleast_1d(n)], dtype=complex)
def ocho_caracteres():
    c4 = lambda n: CHI4(np.atleast_1d(n)).astype(complex)
    out = []
    for a in (0, 1):
        for b in (0, 1, 2, 3):
            if a == 0 and b == 0: nm, f, q = 'zeta', (lambda n: np.ones(len(np.atleast_1d(n)), complex)), 1
            elif b == 0: nm, f, q = 'chi_4', c4, 4
            elif a == 0: nm, f, q = {1: 'psi_5', 2: 'chi_5', 3: 'psi_5^3'}[b], (lambda n, b=b: _psi5(n)**b), 5
            else: nm, f, q = {1: 'chi_4 psi_5', 2: 'chi_20', 3: 'chi_4 psi_5^3'}[b], (lambda n, b=b: c4(n)*_psi5(n)**b), 20
            par = 0 if (f(np.array([19]))[0]*1).real > 0 else 1        # chi(-1) = chi(19)
            out.append((nm, f, q, par))
    return out
def orbita(a, s, chi, q, par, pp):
    """t(s) = W(g_a, tau_s g_a) para el caracter primitivo chi (zeta con su polo si q = 1); pp = (n, w, ln)."""
    import mpmath as mp
    n, w, ln = pp
    c = chi(n)
    m = (np.abs(ln - s) < 2*a) | (ln + s < 2*a)
    t = arch_desplazada(a, s, q, par) - np.sum(w[m]*(c[m]*A_tri(ln[m] - s, a) + np.conj(c[m])*A_tri(ln[m] + s, a)))
    if q == 1:
        t += 2*float(mp.quad(lambda u: float(A_tri(float(u) - s, a))*mp.cosh(u/2), [s - 2*a, s - a, s, s + a, s + 2*a]))
    return complex(t)

# ---- el operador y la correccion (ssec:weil-closure; x_sweep.py) ----
def zeta_ceros():
    import os
    return np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zeta_zeros_3000.npy'))
theta_rs = lambda t: t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t) + 7/(5760*t**3)
dtheta = lambda t: 0.5*np.log(t/(2*np.pi))
def Einv(y, t0):
    """inversa exacta de la envolvente E(t) = theta(t)/pi + 1 (Newton desde t0)."""
    t = np.array(t0, float).copy()
    for _ in range(30): t = t - (theta_rs(t)/np.pi + 1 - y)/(dtheta(t)/np.pi)
    return t
def tabla_primos_S(X):
    """potencias de primo n <= X con (n, p, k)"""
    return potencias(int(X))
def S_primos(t, X, n, p, k, peso='fejer', logs=None):
    """correccion S(t) = -(1/pi) sum_(n<=X) w(log n/log X) sin(t log n)/(k sqrt n) (Lambda(n)/log n = 1/k)."""
    m = n <= X
    ln = np.log(n[m].astype(float)) if logs is None else logs[m]
    u = np.log(n[m].astype(float))/math.log(X)
    W = {'sharp': np.ones_like(u), 'fejer': 1 - u}[peso]
    a = W/(k[m]*np.sqrt(n[m].astype(float)))
    return -(np.sin(np.outer(t, ln)) @ a)/np.pi
def operador_corregido(n_idx, X, n, p, k, peso='fejer', logs=None, iters=6):
    """t_n = E^{-1}(n - 1/2 - S(t_n)), por iteracion de punto fijo desde E^{-1}(n - 1/2)."""
    t = Einv(n_idx - 0.5, 2*np.pi*n_idx/np.log(np.maximum(n_idx, 2)))
    for _ in range(iters): t = Einv(n_idx - 0.5 - S_primos(t, X, n, p, k, peso, logs), t)
    return t
