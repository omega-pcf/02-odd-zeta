#!/usr/bin/env python3
"""oz_carried.py -- numerical checks for the results carried from the predecessor version (F1 v157).

1. Generalised Bernoulli numbers B_{n,chi5}, n = 2, 4, 6, 8, in exact rational arithmetic, and the
   formula L(2k, chi5) = (-1)^{k+1} sqrt5 (2 pi)^{2k} B_{2k,chi5} / (2 (2k)! 5^{2k}) against the Hurwitz sums.
2. The polylogarithmic form of L(s, chi5) at s = 1, 3, 5 against the Hurwitz sums.
3. The Gauss--Lerch and digamma values of L(1, chi5).
4. The characters of Z/20 through G (the remark on T_K): L(1, chi4 chi5) = pi/sqrt5, T_K = 2 pi log phi
   = 5 L(1, chi5) L(1, chi4 chi5), L(3, chi4) = pi^3/32 and L(3, chi4 chi5) = 3 pi^3/(40 sqrt5).
5. The example from the pentagon to zeta(3): zeta_K(3) = 1.027548..., L(3, chi5) = 0.85482..., and their
   ratio zeta(3).
Precision: 40 digits.
"""
import sympy as sp
from mpmath import mp, mpf, sqrt, log, pi, factorial, zeta, digamma, polylog, exp, sin, re

mp.dps = 40
phi = (1 + sqrt(5)) / 2
chi = {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}
TOL = mpf(10) ** -35
ok = True


def check(name, err):
    global ok
    good = abs(err) < TOL
    ok &= good
    print(f"{name:45s} {mp.nstr(abs(err), 3):>10s}  {'ok' if good else 'FAIL'}")


def hurwitz_L(s):
    return sum(chi[a] * zeta(s, mpf(a) / 5) for a in range(1, 5)) / mpf(5) ** s


expected = {2: sp.Rational(4, 5), 4: sp.Integer(-8), 6: sp.Rational(804, 5), 8: sp.Integer(-5776)}
for n in (2, 4, 6, 8):
    B = 5 ** (n - 1) * sum(chi[a] * sp.bernoulli(n, sp.Rational(a, 5)) for a in range(1, 5))
    B = sp.nsimplify(B)
    assert B == expected[n], (n, B)
    k = n // 2
    Bf = mpf(B.p) / mpf(B.q)
    L = (-1) ** (k + 1) * sqrt(5) * (2 * pi) ** n * Bf / (2 * factorial(n) * mpf(5) ** n)
    check(f"B_{n},chi5 = {B}; L({n}) formula vs Hurwitz", L - hurwitz_L(n))

z = exp(2j * pi / 5)
L1 = 2 * log(phi) / sqrt(5)
check("polylog form, s = 1", sum(chi[a] * (-mp.log(1 - z ** a)) for a in range(1, 5)) / sqrt(5) - L1)
for s in (3, 5):
    P = sum(chi[a] * polylog(s, z ** a) for a in range(1, 5)) / sqrt(5)
    R2 = 2 / sqrt(5) * (re(polylog(s, z)) - re(polylog(s, z ** 2)))
    check(f"polylog form, s = {s}", P - hurwitz_L(s))
    check(f"real-part form, s = {s}", R2 - hurwitz_L(s))
check("Gauss--Lerch", -(sqrt(5) / 5) * sum(chi[a] * log(2 * sin(pi * a / 5)) for a in range(1, 5)) - L1)
check("digamma sum = -2 sqrt5 log phi", sum(chi[a] * digamma(mpf(a) / 5) for a in range(1, 5)) + 2 * sqrt(5) * log(phi))

# 4. characters of Z/20 through G
def chi4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def L20(s, c):
    if s == 1:
        return -sum(c(a) * digamma(mpf(a) / 20) for a in range(1, 21)) / 20
    return sum(c(a) * zeta(s, mpf(a) / 20) for a in range(1, 21)) / mpf(20) ** s


c45 = lambda n: chi4(n) * chi[n % 5]
c5 = lambda n: chi[n % 5]
check("L(1, chi4 chi5) = pi/sqrt5", L20(1, c45) - pi / sqrt(5))
check("T_K = 5 L(1, chi5) L(1, chi4 chi5)", 2 * pi * log(phi) - 5 * L20(1, c5) * L20(1, c45))
check("L(3, chi4) = pi^3/32", L20(3, chi4) - pi ** 3 / 32)
check("L(3, chi4 chi5) = 3 pi^3/(40 sqrt5)", L20(3, c45) - 3 * pi ** 3 / (40 * sqrt(5)))

# 5. the example from the pentagon to zeta(3)
L3 = hurwitz_L(3)
zK3 = zeta(3) * L3
trunc = lambda x, d: mpf(int(x * 10 ** d)) / 10 ** d
check("zeta_K(3) = 1.027548...", trunc(zK3, 6) - mpf("1.027548"))
check("L(3, chi5) = 0.85482...", trunc(L3, 5) - mpf("0.85482"))
check("zeta_K(3) / L(3, chi5) = zeta(3)", zK3 / L3 - zeta(3))
print("ALL OK" if ok else "FAILURES")
