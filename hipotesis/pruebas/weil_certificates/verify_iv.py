"""Rigorous replay in interval arithmetic (mpmath.iv, outward rounding) of a Weil-window certificate.

Phi(r) = W(r) + a_2 cos(r log 2) + sum_i b_i cos(lambda_i r),  W(r) = log(5/pi) + Re psi(1/4 + i r/2).
Bounds used, each rigorous:
  * W is even and increasing on [0,inf) (d/dy Re psi(x+iy) > 0), so W(r) >= W(r_k) on [r_k, r_{k+1}].
  * Re psi(x+iy) = psi(x) + sum_{j>=0} f(j),  f(t) = y^2/((t+x)((t+x)^2+y^2)) > 0 and decreasing in t,
    so W(r) >= C0 + sum_{j<K} f(j) + (1/2) log(1 + y^2/(K+x)^2)   (integral bound for the tail),
    with C0 = log(5/pi) + psi(1/4) and psi(1/4) = -gamma - pi/2 - 3 log 2 (Gauss).
  * |Phi''| <= M = MW + M2 on R:  T'' is bounded by M2 = a_2 log(2)^2 + sum |b_i| lambda_i^2, and
    W''(r) = (1/4) sum_j f_j''(y) with |f_j''| <= 2/u^3 (u = j + 1/4), so |W''| <= MW =
    (1/2)(64 + 1/1.25^3 + 1/(2*1.25^2)) (the sum for j >= 1 bounded by its first term plus an integral).
    Hence on [r_k, r_{k+1}] (step h), Phi(r) >= min(Phi(r_k), Phi(r_{k+1})) - M h^2 / 8.
  * For r >= R: W(r) >= W(R) and T(r) >= -(a_2 + sum |b_i|).
All quantities are intervals; the reported numbers are lower endpoints."""
import json, sys
from fractions import Fraction
from mpmath import iv, mpf
import mpmath
lo = lambda v: mpf(v._mpi_[0]); hi = lambda v: mpf(v._mpi_[1])
iv.dps = 30
cert = json.load(open(sys.argv[1])); start = int(sys.argv[2]); stop = int(sys.argv[3])
Q = lambda s: iv.mpf(Fraction(s).numerator) / Fraction(s).denominator
lam = [Q(x) for x in cert['lam']]; b = [Q(x) for x in cert['b']]
L = Q(str(cert['L'])) if not isinstance(cert['L'], str) else Q(cert['L'])
assert all(lo(l - L) >= 0 for l in lam)            # every lambda_i >= L
a2 = iv.sqrt(2) * iv.log(2)                       # -2 Lambda(2) chi5(2) 2^{-1/2}; log 3 > 1 >= L
import os
x = iv.mpf(1) / 4; K = int(os.environ.get("KTERMS", "60"))
C0 = iv.log(iv.mpf(5) / iv.pi) + (-iv.euler - iv.pi / 2 - 3 * iv.log(2))
h = iv.mpf(1) / 100
M2 = a2 * iv.log(2) ** 2 + sum(abs(bi) * li ** 2 for bi, li in zip(b, lam))
MW = (64 + 1 / iv.mpf(1.25) ** 3 + 1 / (2 * iv.mpf(1.25) ** 2)) / 2
M = MW + M2
def W_low(r):
    y = r / 2; s = C0
    for j in range(K):
        u = j + x; s += y * y / (u * (u * u + y * y))
    U = K + x
    return s + iv.log(1 + y * y / (U * U)) / 2
def T(r):
    return a2 * iv.cos(r * iv.log(2)) + sum(bi * iv.cos(li * r) for bi, li in zip(b, lam))
Phi = lambda r: lo(W_low(r) + T(r))
worst = None; Pprev = Phi(start * h)
loss = hi(M * h * h / 8)
for k in range(start, stop):
    Pnext = Phi((k + 1) * h)
    low = min(Pprev, Pnext) - loss
    worst = low if worst is None or low < worst else worst
    Pprev = Pnext
out = {'start': start, 'stop': stop, 'min_lower': mpmath.nstr(worst, 12), 'M': mpmath.nstr(hi(M), 8), 'loss': mpmath.nstr(loss, 6)}
if len(sys.argv) > 4:   # tail beyond R
    R = iv.mpf(sys.argv[4]); out['tail_lower'] = mpmath.nstr(lo(W_low(R) - a2 - sum(abs(bi) for bi in b)), 12)
print(json.dumps(out))
