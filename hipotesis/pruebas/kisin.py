"""kisin.py — rmk:prism-five (junto a thm:L1 y el regulador R_K = log phi): el prisma en 5 y el regulador 5-adico.
K_5 = Q_5(sqrt5), O = Z_5[sqrt5], A = Z_5[[u]] con phi_A(u) = u^5 y E(u) = u^2 - 5.
(i)  phi_A(E) - E^5 = 5 D(u), D = 5u^8 - 50u^6 + 250u^4 - 625u^2 + 624, D = -1 mod 5 (E distinguido).
(ii) A/(5, E) = F_5[u]/(u^2).
(iii) phi_A(E)(sqrt5) = 5^5 - 5 = tau(chi_5)^2 * 624, tau(chi_5) = sqrt5.
(iv) v_5(phi^4 - 1) = 1/2  (phi^4 - 1 = sqrt5 (3 + sqrt5)/2).
(v)  el conucleo de g -> g^5 - u^2 g en F_5[[u]], calculado hasta grado 33: clases u y u^2; phi^4 = 1 + 4 sqrt5 + 5(1 - phi).
(vi) Leopoldt: L_5(1,chi_5) = 2 log_5(phi)/sqrt5.  Lado derecho: log_5 phi = (1/4) log(phi^4) por la serie (exacta en Q(sqrt5)).
     Lado izquierdo: Kubota–Leopoldt, L_5(1-n, chi_5) = -B_(n,chi_5)/n para 4 | n, y n = 4*5^k -> 0 en Z_5 da L_5(1).
El articulo: el conucleo de (v) hasta grado 33, y L_5(1,chi_5) y 2 log_5 phi/sqrt5 ambos = 557 (mod 5^4).
Uso: python3 -I kisin.py"""
import sympy as sp
from fractions import Fraction as Fr
u = sp.symbols('u')
E = u**2 - 5
D = sp.expand((E.subs(u, u**5) - E**5)/5)
print("(i)  D =", D, "; D mod 5 =", sp.Poly(D, u, modulus=5).as_expr(), "(-1: unidad)")
print("(ii) A/(5,E) = F_5[u]/(u^2):", sp.Poly(E, u, modulus=5).as_expr() == u**2)
print("(iii) phi_A(E)(sqrt5) =", 5**5 - 5, "= 5 *", (5**5 - 5)//5)
# (iv) en Q(sqrt5): pares (a, b) = a + b sqrt5
def m(x, y): return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
phi = (Fr(1, 2), Fr(1, 2)); p4 = m(m(phi, phi), m(phi, phi))
x = (p4[0] - 1, p4[1])
print("(iv) phi^4 - 1 =", x, "= sqrt5 (3 + sqrt5)/2:", m((0, 1), (Fr(3, 2), Fr(1, 2))) == x, "; v_5 = 1/2")
print("     phi^4 = 1 + 4 sqrt5 + 5(1 - phi):", p4 == (1 + 5 - 5*phi[0], 4 - 5*phi[1]))
# (v) conucleo de T(g) = g^5 - u^2 g sobre F_5, modulo u^34
Ng = 34
rows = []
for i in range(Ng):
    v = [0]*Ng
    if 5*i < Ng: v[5*i] = (v[5*i] + 1) % 5
    if i + 2 < Ng: v[i + 2] = (v[i + 2] - 1) % 5
    rows.append(v)
from sympy.polys.matrices import DomainMatrix
from sympy import GF
rg = lambda R: DomainMatrix.from_Matrix(sp.Matrix(R)).convert_to(GF(5)).rank()
img = rows[:Ng - 2]                            # u^i con i + 2 < Ng: imagen sin truncar (grados < 34)
r0 = rg(img)
e = lambda j: [1 if t == j else 0 for t in range(Ng)]
r1 = rg(img + [e(1), e(2)])
print(f"(v)  T(g) = g^5 - u^2 g en F_5[u]/(u^{Ng}), g de grado < {Ng - 2}: rango de la imagen {r0}; con u y u^2 agregados {r1}"
      f" = {Ng}: el conucleo es F_5 u + F_5 u^2 (T(1) = 1 - u^2: la clase de 1 es la de u^2)")
# (vi) lado derecho: log(phi^4) = sum (-1)^(n+1) x^n/n, exacto en Q(sqrt5), luego reducido modulo 5^4
s = (Fr(0), Fr(0)); xn = (Fr(1), Fr(0))
for n in range(1, 60):
    xn = m(xn, x); s = (s[0] + Fr((-1)**(n + 1), n)*xn[0], s[1] + Fr((-1)**(n + 1), n)*xn[1])
c = s[1]/4                                   # log phi = c sqrt5 (+ parte racional de valuacion alta)
def mod5k(q, k):
    num, den = q.numerator, q.denominator
    v = 0
    while den % 5 == 0: den //= 5; v -= 1
    while num % 5 == 0 and num: num //= 5; v += 1
    assert v >= 0, v
    return (num*5**v*pow(den, -1, 5**k)) % 5**k
rhs = mod5k(2*c, 4)
print(f"(vi) 2 log_5(phi)/sqrt5 = {rhs} (mod 5^4);  parte racional del log (debe tener valuacion alta): v_5 >= "
      f"{min(k for k in range(1, 12) if mod5k(s[0], k) != 0) - 1 if mod5k(s[0], 11) else 11}")
# lado izquierdo: Kubota–Leopoldt
chi = [0, 1, -1, -1, 1]
x_ = sp.symbols('x')
def Bchi(n):
    f = 5
    return sp.Rational(f)**(n - 1)*sum(chi[a % 5]*sp.bernoulli(n, sp.Rational(a, f)) for a in range(1, f + 1))
for k in (1, 2, 3):
    n = 4*5**k
    val = -Bchi(n)/n
    q = Fr(int(sp.numer(val)), int(sp.denom(val)))
    print(f"     L_5(1-n, chi_5) = -B_(n,chi_5)/n con n = 4*5^{k} = {n}: {mod5k(q, 4)} (mod 5^4)")
print("articulo: ambos = 557 (mod 5^4)")
