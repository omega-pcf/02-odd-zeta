import numpy as np, io, contextlib
from rigW import W_lower
with contextlib.redirect_stdout(io.StringIO()):
    import lp
A=lp.A
def phihat(r,L,J):
    j=np.arange(1,J+1); k=j*np.pi/L; rr=r[:,None]; den=k[None,:]**2-rr**2
    den=np.where(np.abs(den)<1e-12,1e-12,den)
    return np.sqrt(2/L)*np.exp(-1j*rr*L/2)*k[None,:]*(1-((-1.0)**j)[None,:]*np.exp(1j*rr*L))/den
def certify(L,t,J,h,chunk=8000):
    act={n:a for n,a in A.items() if np.log(n)<L}
    S=sum(abs(a) for a in act.values()); M=sum(abs(a)*np.log(n) for n,a in act.items())
    R=0.5
    while W_lower(R)[0]<t+S: R*=1.05
    coarse=np.unique(np.concatenate([np.arange(0,5,2e-4),np.arange(5,min(R,50),2e-3),np.arange(50,R+0.02,0.02) if R>50 else []]))
    Wc=np.concatenate([W_lower(coarse[i:i+2000]) for i in range(0,len(coarse),2000)])
    G=np.zeros((J,J),complex); eta=0.0; intN=0.0; r0=0.0
    while r0<R:
        rk=np.arange(r0,min(R,r0+chunk*h),h); rm=rk+h/2
        Wk=Wc[np.searchsorted(coarse,rk,side='right')-1]
        low=Wk+sum(a*np.cos(rk*np.log(n)) for n,a in act.items())-M*h-1e-9
        N=np.clip(t-low,0,None)
        if N.max()>0:
            F=phihat(rm,L,J); w=N*h/np.pi
            G+=(F.conj().T*w)@F
            eta+=np.sum(w*np.clip(L-np.sum(np.abs(F)**2,1),0,None))
            intN+=np.sum(w)
        r0=rk[-1]+h
    G=np.real(G)
    lamJ=np.linalg.eigvalsh(G)[-1]
    # quadrature error of midpoint rule on each cell: |f''|<= L^3 for phihat_j*conj(phihat_k) -> entry error <= intN*h^2*L^3/24
    e_entry=intN*h*h*L**3/24
    e_G=J*e_entry                                   # ||E||_2 <= J*max|E_ij|
    # eta integrand eps^2 = L - sum|phihat|^2 ; |(eps^2)''| <= 2*J*(L/2)^2*L  -> error <= intN*h^2*that/24
    e_eta=intN*h*h*(2*J*(L/2)**2*L)/24
    e_float=1e-9*J
    margin=t-(lamJ+e_G+e_float)-(eta+e_eta)
    return margin,lamJ,eta,e_G,e_eta,R
for L,t,J,h in [(1.1,2.0,400,5e-4),(1.2,2.0,400,5e-4)]:
    m,lj,et,eg,ee,R=certify(L,t,J,h)
    print(f"L={L} t={t} J={J}: RIGOROUS margin={m:.5f} (lamJ={lj:.5f}, eta={et:.2e}, quad errs {eg:.1e},{ee:.1e}, R={R:.0f})")
