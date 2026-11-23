"""Utilidades comunes de las verificaciones (§33–§54 del Lean unificado).

Todo es aritmética exacta en enteros, salvo donde se dice.  ℤ[φ]/p se
representa como pares (x, y) = x + y·φ con φ² = φ + 1.
"""
import math, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, 'vendor'))

FALLOS = []
def comprobar(nombre, cond, detalle=''):
    estado = 'PASA' if cond else 'FALLA'
    print('  [%s] %s %s' % (estado, nombre, detalle))
    if not cond: FALLOS.append(nombre)
def salir():
    if FALLOS:
        print('FALLAN %d comprobaciones: %s' % (len(FALLOS), ', '.join(FALLOS)))
        sys.exit(1)
    print('Todas las comprobaciones pasan.')

def criba(L):
    sv = bytearray([1]) * (L + 1); sv[0] = sv[1] = 0
    for i in range(2, int(L ** .5) + 1):
        if sv[i]: sv[i*i::i] = bytearray(len(sv[i*i::i]))
    return sv
def primos(L, desde=7):
    sv = criba(L)
    return [p for p in range(desde, L + 1) if sv[p]]
def menor_factor(L):
    spf = list(range(L + 1))
    for i in range(2, int(L ** .5) + 1):
        if spf[i] == i:
            for j in range(i*i, L + 1, i):
                if spf[j] == j: spf[j] = i
    return spf
_SPF = {}
def factores(n):
    """Primos distintos de n (división por tentativa; n ≤ ~10^7)."""
    fs = []; q = 2
    while q * q <= n:
        if n % q == 0:
            fs.append(q)
            while n % q == 0: n //= q
        q += 1
    if n > 1: fs.append(n)
    return fs

# ---- ℤ[φ]/p ----
def mul(a, b, p):
    x1, y1 = a; x2, y2 = b
    return ((x1*x2 + y1*y2) % p, (x1*y2 + x2*y1 + y1*y2) % p)
def pw(a, n, p):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, p)
        a = mul(a, a, p); n >>= 1
    return r
def partido(p): return p % 5 in (1, 4)
def N_p(p):
    """Orden del grupo donde vive φ: p−1 (partido) o 2(p+1) (inerte)."""
    return p - 1 if partido(p) else 2 * (p + 1)
def orden(p):
    """Piso: orden de φ en (ℤ[φ]/p)*.  Devuelve (N_p, piso)."""
    N = N_p(p); o = N
    for q in factores(N):
        while o % q == 0 and pw((0, 1), o // q, p) == (1, 0): o //= q
    return N, o
def indice(p):
    N, o = orden(p); return N // o

def sqrtmod(a, p):
    a %= p
    if a == 0: return 0
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1: z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1: t2 = t2 * t2 % p; i += 1
        b = pow(c, 1 << (m - i - 1), p); m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r
def raiz_phi(p):
    """r ∈ 𝔽_p con r² = r + 1 (p partido)."""
    return (1 + sqrtmod(5, p)) * pow(2, p - 2, p) % p
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def val(x, q):
    c = 0
    while x % q == 0: x //= q; c += 1
    return c
def orden_mult(x, p, N):
    """Orden de x en 𝔽_p* (N = p − 1)."""
    o = N
    for q in factores(N):
        while o % q == 0 and pow(x, o // q, p) == 1: o //= q
    return o

def representados(formas, L, disc):
    """Enteros 0 < n < L representados por alguna forma (A,B,C) de discriminante disc < 0."""
    R = set(); D = -disc
    for (A, B, C) in formas:
        ymax = int(math.sqrt(4 * A * L / D)) + 2
        for y in range(0, ymax):
            xr = int(math.sqrt(L / A)) + abs(B * y) // (2 * A) + 2
            for x in range(-xr, xr + 1):
                n = A*x*x + B*x*y + C*y*y
                if 0 < n < L: R.add(n)
    return R

def tabla_ordenes(L=10**6):
    """Lista de (p, N_p, piso) para 7 ≤ p ≤ L; se guarda en datos/ para reutilizar."""
    import pickle
    f = os.path.join(AQUI, 'datos', 'ordenes_%d.pkl' % L)
    if os.path.exists(f):
        with open(f, 'rb') as h: return pickle.load(h)
    T = [(p,) + orden(p) for p in primos(L)]
    with open(f, 'wb') as h: pickle.dump(T, h)
    return T
