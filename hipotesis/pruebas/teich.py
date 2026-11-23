"""teich.py — ssec:delta-polar: la p-derivacion de Z[phi], la forma polar de phi en 2 y 3 y el grupo de color.
(El articulo lista teich.py entre los scripts sin atarlo a un numero; este reune las comprobaciones [N] de
prop:delta-ring, prop:polar y el parrafo entre ellas.)  Aritmetica exacta en Z[phi]/(p^N): x + y phi, phi^2 = phi + 1.
1. prop:delta-ring: delta_p(phi) = (Frob_p(phi) - phi^p)/p con phi^p = F_p phi + F_{p-1}; delta_11, delta_13; el cociente
   |delta_p(phi)|/(phi^p/p) en la inmersion real phi = 1.618...
2. prop:polar: el levantamiento de Teichmuller [phi] = lim phi^(q^n) (q = 4 en 2, q = 9 en 3; ambos primos inertes),
   a precision 2^8 y 3^5: en 2, [phi] es raiz cubica primitiva de la unidad y -15 = 1 mod 16 (Q2(sqrt5) = Q2(sqrt-3));
   en 3, [phi] tiene orden 8 y su cuadrado es +-i; la parte radial <phi> = phi [phi]^-1 = 1 mod p.
3. el grupo de color <phi_p> en F_(p^2)^* (p inerte): orden par, nunca 2, 4, 6; 16 (no 48) en 7, 28 (no 168) en 13.
El articulo: delta_11 = -5-8phi, delta_13 = -11-18phi; cocientes 1.236, 1.146, 0.992, ..., 0.999999 en p = 2, 3, 11, ..., 31.
Uso: python3 -I teich.py"""
import math
def mul(a, b, m):
    x1, y1 = a; x2, y2 = b
    return ((x1*x2 + y1*y2) % m, (x1*y2 + x2*y1 + y1*y2) % m)
def pw(a, n, m):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, m)
        a = mul(a, a, m); n >>= 1
    return r
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
chi5 = lambda p: [0, 1, -1, -1, 1][p % 5]
phi_r = (1 + 5**.5)/2
print("1. delta_p(phi):")
for p in (2, 3, 7, 11, 13, 17, 19, 23, 29, 31):
    Fp, Fp1 = fib(p), fib(p - 1)
    # Frob_p(phi) = phi (partido) o phi_bar = 1 - phi (inerte)
    if chi5(p) == 1: num = (-Fp1, 1 - Fp)
    else: num = (1 - Fp1, -1 - Fp)
    assert num[0] % p == 0 and num[1] % p == 0
    d = (num[0]//p, num[1]//p)
    val = d[0] + d[1]*phi_r
    print(f"   p = {p:2d} ({'partido' if chi5(p) == 1 else 'inerte'}): delta = {d[0]} + {d[1]} phi;  |delta|/(phi^p/p) = {abs(val)/(phi_r**p/p):.6f}")
print("2. Teichmuller:")
for p, N, q in ((2, 8, 4), (3, 5, 9)):
    m = p**N
    w = (0, 1)
    for _ in range(N + 2): w = pw(w, q, m)            # phi^(q^(N+2)) = [phi] mod p^N
    orden = next(d for d in range(1, q) if pw(w, d, m) == (1, 0))
    winv = pw(w, orden - 1, m); rad = mul((0, 1), winv, m)
    print(f"   p = {p}, precision {p}^{N}: [phi] = {w[0]} + {w[1]} phi;  orden {orden};  <phi> = phi [phi]^-1 = {rad} "
          f"(= 1 mod {p}: {rad[0] % p == 1 and rad[1] % p == 0})")
    if p == 3:
        w2 = mul(w, w, m); print(f"      ([phi]^2)^2 = {mul(w2, w2, m)}  (= -1 mod 3^5: {mul(w2, w2, m) == (m - 1, 0)})")
print(f"   -15 mod 16 = {(-15) % 16}: -15 es cuadrado 2-adico, Q2(sqrt5) = Q2(sqrt-3)")
print("3. grupo de color en F_(p^2)^* (p inerte):")
for p in (3, 7, 13, 17, 23, 37, 43, 47):
    e = next(d for d in range(1, p*p) if pw((0, 1), d, p) == (1, 0))
    print(f"   p = {p:2d}: orden de phi = {e} (de {p*p - 1});  phi^(p+1) = {pw((0, 1), p + 1, p)} (= -1)")
print("articulo: delta_11 = -5-8phi, delta_13 = -11-18phi; 1.236, 1.146, 0.992, ..., 0.999999; 16 en 7, 28 en 13")
