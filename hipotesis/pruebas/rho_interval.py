"""rho_interval.py — W3, ssec:golden-field: la cota inferior rho <= lambda_{N+1} de la forma de Weil de Q(sqrt5).
Una funcion soportada en un intervalo de longitud S = 2L, ortogonal a los polinomios de grado < N, tiene a lo mas
la fraccion eps(R) = (2/pi)(RL)^{2N+1}/((2N+1)^2 (N!)^2) de su energia bajo la frecuencia R
(F1PaperTorus.lowFrequencyFraction_nonneg).  El simbolo m_K(r) = W_K(r) - 2 sum c_n cos(r log n) es >= W_K(R) - 2 sum c_n
en |r| >= R (W_K creciente) y >= W_K(0) - 2 sum c_n en todo r; el polo 2 a(g)b(g) se acota por debajo por 0 en ese
subespacio.  Luego, por min-max, para todo R:
   lambda_{N+1} >= rho(R) = W_K(R) - 2 sum c_n - eps(R) (W_K(R) - W_K(0)),
y rho = max_R rho(R).  Se encierra rho(R*) en aritmetica de intervalos (mpmath.iv) en el R* del maximo; W_K(R*) a
50 digitos con un margen de 1e-45.
El articulo (tabla): rho = 3.4808, 3.0425, 1.7039, 1.9369, 1.4234 para (S, N) = (log4, 28), (1.5, 50), (1.7, 60),
(2.0, 80), (2.3, 150).
Uso: python3 -I rho_interval.py"""
import mpmath as mp, math
mp.mp.dps = 50
iv = mp.iv; iv.dps = 50
W = lambda R: mp.log(5/mp.pi**2) + 2*mp.re(mp.digamma(mp.mpf(1)/4 + 0.5j*R))
def sum_c(S):
    tot = mp.mpf(0)
    for n in range(2, int(math.exp(S)) + 2):
        if mp.log(n) >= S: continue
        for p in range(2, n + 1):
            if n % p == 0:
                m = n
                while m % p == 0: m //= p
                if m == 1: tot += mp.log(p)*(1 + [0, 1, -1, -1, 1][n % 5])/mp.sqrt(n)
                break
    return tot
def rho_de(S, N, R):
    L = mp.mpf(S)/2; sc = sum_c(S)
    eps = (2/mp.pi)*(R*L)**(2*N + 1)/((2*N + 1)**2*mp.factorial(N)**2)
    return W(R) - 2*sc - eps*(W(R) - W(0)), eps
def encierro(S, N, R):
    Li = iv.mpf(mp.mpf(S))/2; Ri = iv.mpf(R); sc = iv.mpf(sum_c(S))
    eps = (2/iv.pi)*(Ri*Li)**(2*N + 1)/((2*N + 1)**2*iv.factorial(N)**2)
    WR = iv.mpf([W(R) - mp.mpf('1e-45'), W(R) + mp.mpf('1e-45')]); W0 = iv.mpf([W(0) - mp.mpf('1e-45'), W(0) + mp.mpf('1e-45')])
    return WR - 2*sc - eps*(WR - W0)
filas = [(mp.log(4), 28, 3.4808), (mp.mpf('1.5'), 50, 3.0425), (mp.mpf('1.7'), 60, 1.7039), (mp.mpf(2), 80, 1.9369), (mp.mpf('2.3'), 150, 1.4234)]
print("  S      N    R*        eps(R*)     rho (encierro, extremo inferior)    articulo")
for S, N, tab in filas:
    f = lambda R: rho_de(S, N, R)[0]
    R0 = max([mp.mpf(k)/4 for k in range(4, 4*120)], key=f)
    R = mp.findroot(lambda R: mp.diff(f, R), R0)
    e = encierro(S, N, R)
    print(f"  {float(S):.3f}  {N:3d}  {float(R):8.4f}  {float(rho_de(S, N, R)[1]):.3e}    [{mp.nstr(mp.mpf(e.a.a), 8)}, {mp.nstr(mp.mpf(e.b.b), 8)}]      {tab}")
# la condicion de Lehmann para lambda_1: m = numero de valores de Ritz bajo rho (rigorous_chain.py: 7, 7, 3, 4, 4)
print("rho con N = m (cota de lambda_(m+1), la que pide Lehmann para lambda_1):")
for (S, N, tab), m in zip(filas, (7, 7, 3, 4, 4)):
    f = lambda R: rho_de(S, m, R)[0]
    print(f"  S = {float(S):.3f}: m = {m}, rho = {float(max(f(mp.mpf(k)/8) for k in range(8, 8*80))):+.4f}")
print("Los valores del articulo estan en la misma curva rho(R), un poco por debajo de su maximo (rho(R) es cota")
print("valida para todo R); rigorous_chain.py usa los del articulo.")
