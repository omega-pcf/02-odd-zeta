"""
verify_weil_chi5.py  — [N] numerical checks for the Weil route (F1 manuscript).

1. Zeros of L(s,chi5) up to height T=80 from sign changes of the completed
   Lambda(1/2+it) = (5/pi)^{s/2} Gamma(s/2) L(s,chi5), which is real on the line.
   Result: 40 zeros; first gamma = 6.648453344727715 (matches NoLowZeros);
   count agrees with Riemann-von Mangoldt (5T/2pi e) ~ 40.2.
2. Explicit formula (Weil; Iwaniec-Kowalski Thm 5.12), even chi, conductor 5:
     sum_gamma h(gamma) = (1/2pi) int h(r)[log(5/pi) + Re psi(1/4+ir/2)] dr
                          - 2 sum_n Lambda(n) chi(n) n^{-1/2} g(log n),
   h(r)=int g(u)e^{iru}du.  Checked with Gaussian g for sigma=0.30,0.35,0.45:
   both sides agree to ~1e-18.  This fixes the normalisation used in the paper.
3. Scan of A - 2P (= zero side) with split/inert decomposition of P.
"""
import mpmath as mp
from sympy import factorint
mp.mp.dps = 25
CHI = [0, 1, -1, -1, 1]
chi = lambda n: CHI[n % 5]

def Lam_completed(t):
    s = mp.mpf(0.5) + 1j*t
    return (mp.mpf(5)/mp.pi)**(s/2) * mp.gamma(s/2) * mp.dirichlet(s, CHI)

def zeros(T=80, N=8000):
    ts = [T*i/N for i in range(1, N+1)]
    v = [mp.re(Lam_completed(t)) for t in ts]
    return [mp.findroot(lambda t: mp.re(Lam_completed(t)), (ts[i], ts[i+1]), solver='bisect')
            for i in range(N-1) if v[i]*v[i+1] < 0]

VM = {}
for n in range(2, 6000):
    f = factorint(n)
    if len(f) == 1:
        VM[n] = mp.log(list(f)[0])

def sides(zs, sig):
    g = lambda u: mp.e**(-u**2/(2*sig**2))
    h = lambda r: sig*mp.sqrt(2*mp.pi)*mp.e**(-sig**2*r**2/2)
    Z = 2*sum(h(z) for z in zs)
    A = mp.quad(lambda r: h(r)*(mp.log(5/mp.pi) + mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2))),
                [-mp.inf, 0, mp.inf])/(2*mp.pi)
    Ps = sum(l/mp.sqrt(n)*g(mp.log(n)) for n, l in VM.items() if chi(n) == 1)
    Pi = sum(l/mp.sqrt(n)*g(mp.log(n)) for n, l in VM.items() if chi(n) == -1)
    return Z, A, Ps - Pi, Ps, Pi

if __name__ == "__main__":
    zs = zeros()
    print("zeros:", len(zs), "first:", mp.nstr(zs[0], 16))
    for sig in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]:
        Z, A, P, Ps, Pi = sides(zs, sig)
        print(f"sigma={sig:4} Z={float(Z): .6e} A={float(A): .5f} 2P={float(2*P): .5f} "
              f"split={float(Ps):.5f} inert={float(Pi):.5f} |Z-(A-2P)|={float(abs(Z-(A-2*P))):.1e}")
