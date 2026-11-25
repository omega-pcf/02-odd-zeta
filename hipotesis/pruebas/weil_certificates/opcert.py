import numpy as np, sys, io, contextlib
from scipy.special import digamma
with contextlib.redirect_stdout(io.StringIO()):
    import lp
A=lp.A
W=lambda r: np.log(5/np.pi)+np.real(digamma(0.25+0.5j*r))
def phihat(r,L,J):
    j=np.arange(1,J+1); k=j*np.pi/L
    rr=r[:,None]; den=k[None,:]**2-rr**2
    den=np.where(np.abs(den)<1e-12,1e-12,den)
    I=k[None,:]*(1-((-1.0)**j)[None,:]*np.exp(1j*rr*L))/den
    return np.sqrt(2/L)*np.exp(-1j*rr*L/2)*I
def certify(L,t,J=300,h=1e-3,chunk=20000):
    act={n:a for n,a in A.items() if np.log(n)<L}
    S=sum(abs(a) for a in act.values()); Mlip=sum(abs(a)*np.log(n) for n,a in act.items())
    # R: beyond, W(r)>=t+S so Psi>=t (W increasing)
    R=0.5
    while W(R)<t+S: R*=1.05
    G=np.zeros((J,J),complex); eta=0.0; r0=0.0
    while r0<R:
        rk=np.arange(r0,min(R,r0+chunk*h),h); rm=rk+h/2
        low=W(rk)+sum(a*np.cos(rk*np.log(n)) for n,a in act.items())-Mlip*h
        N=np.clip(t-low,0,None)
        if N.max()>0:
            F=phihat(rm,L,J)                       # midpoint of each cell
            wN=N*h/np.pi
            G+=(F.conj().T*wN)@F                    # (1/pi) int_0^inf N phihat_j conj phihat_k  (take Re below)
            eps2=np.clip(L-np.sum(np.abs(F)**2,1),0,None)
            eta+=np.sum(wN*eps2)
        r0=rk[-1]+h
    lamJ=np.linalg.eigvalsh(np.real(G))[-1]
    return t-lamJ-eta, lamJ, eta, R
for L,t in [(1.1,2.0),(1.1,3.0),(1.2,3.0),(1.2,2.5)]:
    m,lj,et,R=certify(L,t)
    print(f"L={L} t={t}: margin={m:.4f}  lam_J={lj:.4f}  eta_J={et:.2e}  R={R:.0f}")
