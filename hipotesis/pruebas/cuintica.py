"""cuintica.py — la representacion de la capa quintica (prop:sqrt-x, prop:phi-layers): a(n) para la formula explicita.
f(x) = x^5 + 5x^3 + 5x - 1 (con x = y - 1/y es y^5 - y^{-5} = 1, es decir y^5 = phi): discriminante 5^7, un solo
cero real (f' > 0), grupo de Galois F20.  La representacion de grado 4 es la de permutacion de las raices menos la
trivial: a(p^k) = #(raices de f en F_{p^k}) - 1 para p != 5; a(5^k) = 0 (5 totalmente ramificado: sin invariantes de
inercia en la parte de grado 4).  Factor gamma Gamma_R(s)^2 Gamma_R(s+1)^2 (la conjugacion compleja fija una raiz),
conductor 5^7.
Regla por clase (contrastada con la factorizacion modulo p para p < 3000):
  p = 1 mod 5: a(p^k) = 4 si phi es potencia quinta modulo p, si no a(p^k) = 4 si 5 | k y -1 si no;
  p = 4 mod 5: Frobenius de orden 2:  a = 0 (k impar), 4 (k par);
  p = 2, 3 mod 5: Frobenius de orden 4: a = 4 si 4 | k, 0 si no."""
import numpy as np
def sqrtmod(a, p):
    a %= p
    if a == 0: return 0
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p - 1)//2, p) != p - 1: z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1)//2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1: t2 = t2*t2 % p; i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b*b % p, t*b*b % p, r*b % p
    return r
def phi_quinta(p):
    """phi = (1+sqrt5)/2 es potencia quinta modulo p (p = 1 mod 5)?"""
    r = sqrtmod(5, p); ph = (1 + r)*pow(2, -1, p) % p
    return pow(ph, (p - 1)//5, p) == 1
def a_pk(p, k):
    if p == 5: return 0
    r = p % 5
    if r == 1: return 4 if (phi_quinta(p) or k % 5 == 0) else -1
    if r == 4: return 0 if k % 2 else 4
    return 4 if k % 4 == 0 else 0
if __name__ == '__main__':
    import sympy as sp
    x = sp.symbols('x'); f = x**5 + 5*x**3 + 5*x - 1
    malos = 0
    for p in sp.primerange(2, 3000):
        if p == 5: continue
        degs = [fa.degree() for fa, e in sp.Poly(f, x, modulus=p).factor_list()[1] for _ in range(e)]
        for k in (1, 2, 3, 4, 5, 10):
            raices = sum(d for d in degs if k % d == 0)
            if raices - 1 != a_pk(p, k): malos += 1
    print("regla contra factorizacion (p < 3000, k = 1..5, 10): discrepancias", malos)
