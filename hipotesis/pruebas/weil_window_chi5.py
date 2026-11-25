import numpy as np
from sympy import factorint
EG=0.5772156649015329
chi=lambda n:[0,1,-1,-1,1][n%5]
cn={}
for n in range(2,200):
    f=factorint(n)
    if len(f)==1 and chi(n)!=0:
        cn[n]=np.log(list(f)[0])*chi(n)/np.sqrt(n)
def lam_min(L,J=24,M=3000,with_primes=True):
    x=np.linspace(-L/2,L/2,M); dx=x[1]-x[0]
    F=np.array([np.sin(j*np.pi*(x+L/2)/L) for j in range(1,J+1)])
    F/=np.sqrt((F**2).sum(1)*dx)[:,None]          # orthonormal
    K=M-1; u=np.arange(0,K+1)*dx                  # u in [0,L]
    Q=np.zeros((J,J))
    w=np.zeros_like(u); 
    # integrand weights for g(u) (u>0) and coefficient on g(0)
    uu=u[1:]
    wg = -2*np.exp(-uu/2)/(1-np.exp(-2*uu))      # multiplies g(u)
    w0_int = 2*np.exp(-2*uu)/(1-np.exp(-2*uu))   # multiplies g(0)
    for a in range(J):
        for b in range(a,J):
            full=np.correlate(F[a],F[b],'full')*dx
            gpos=full[M-1:]; gneg=full[:M][::-1]
            g=(gpos+gneg)/2                       # even part, g(u) u>=0
            g0=g[0]
            # integral with singular pieces combined: integrand (e^{-2u}g0 - e^{-u/2}g)*2/(1-e^{-2u})
            integ=np.empty_like(u); integ[0]=-0.75*g0*2/2*2/1 if False else -1.5*g0
            integ[1:]=w0_int*g0+wg*g[1:]
            I=np.trapezoid(integ,u) - np.log(1-np.exp(-2*L))*g0
            A=g0*(np.log(5/np.pi)-EG)+I
            P=0.0
            if with_primes:
                for n,c in cn.items():
                    ln=np.log(n)
                    if ln<L: P+=c*np.interp(ln,u,g)
            Q[a,b]=Q[b,a]=A-2*P
    return np.linalg.eigvalsh(Q)[0]

# ---------------------------------------------------------------------------
# [N] Semilocal Weil positivity for L(s,chi5).
# lam_min(L): smallest eigenvalue of the Weil quadratic form restricted to
# test functions f supported in [-L/2, L/2] (orthonormal sine basis, J modes),
#   Q(f) = A(g) - 2 sum_n Lambda(n) chi5(n) n^{-1/2} g(log n),  g = f * f~,
#   A(g) = g(0)(log(5/pi) - gamma) + 2 int_0^inf [e^{-2u} g(0) - e^{-u/2} g(u)]/(1-e^{-2u}) du.
# A(g) validated against the digamma form to 1e-15 (arch.py).
# Findings (J=24):
#   archimedean-only positivity is lost at L = 0.9251 (> log 2 = 0.6931);
#   with the primes, lam_min stays > 0 (0.097 at L=1, 0.0053 at L=1.4, ~1e-6 at L=2);
#   counterfactual chi(2)=+1 (2 split): lam_min < 0 from L ~ 0.9.
# The inert Frobenius at 2 (psi_2 = sigma) carries positivity past the
# archimedean threshold.
if __name__ == "__main__":
    for L in [0.6, 0.9, 1.0, 1.2, 1.4, 1.6, 2.0]:
        print(L, lam_min(L), lam_min(L, with_primes=False))
