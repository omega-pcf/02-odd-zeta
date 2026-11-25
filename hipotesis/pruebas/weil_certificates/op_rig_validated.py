"""Validated replay of the operator-form Weil window (Thm 23.8), in chunks with checkpoints.
Floating point everywhere, with every rounding error bounded explicitly (see the error budget at the end):
  * W from below by partial sums of a positive series (rigW.W_lower, safety 1e-9 per value),
    W increasing; P_L Lipschitz with M = sum|a_n| log n; N_k = (t - W(r_k) - P_L(r_k) + M h)_+ >= (t-Psi)_+ on the cell.
  * G and eta_J by the midpoint rule, with the analytic quadrature bounds of the paper.
  * lambda_max(G) bounded by a Cholesky factorisation of mu I - G (Higham, Thm 10.3/10.7):
    if it completes in floating point, lambda_max(G) <= mu + gamma_{n+1}(1+gamma_{n+1}) tr(mu I - G) + u max|mu - G_ii|."""
import numpy as np, sys, os, io, contextlib, json
import mpmath as mp
mp.mp.dps=40
_C0=float(mp.log(5/mp.pi)+(-mp.euler-mp.pi/2-3*mp.log(2)))
def W_lower(r, K=400):
    # lower bound: partial sum of the positive series + integral bound of its tail (terms decreasing)
    r=np.atleast_1d(np.asarray(r,float)); y=r/2; u=np.arange(K)+0.25
    s=_C0+np.sum((y[:,None]**2)/(u[None,:]*(u[None,:]**2+y[:,None]**2)),axis=1)
    return s+0.5*np.log1p(y*y/(K+0.25)**2)-1e-9
with contextlib.redirect_stdout(io.StringIO()):
    import lp
L=float(sys.argv[1]); t=float(sys.argv[2]); J=int(sys.argv[3]); h=float(sys.argv[4]); nchunks=int(sys.argv[5])
tag=f"L{L}_J{J}_h{h}"; ck=f"state_{tag}.npz"
act={n:a for n,a in lp.A.items() if np.log(n)<L}
S=sum(abs(a) for a in act.values()); M=sum(abs(a)*np.log(n) for n,a in act.items())
R=0.5
while W_lower(R)[0]<t+S: R*=1.05
def phihat(r):
    j=np.arange(1,J+1); k=j*np.pi/L; rr=r[:,None]; den=k[None,:]**2-rr**2
    den=np.where(np.abs(den)<1e-12,1e-12,den)
    return np.sqrt(2/L)*np.exp(-1j*rr*L/2)*k[None,:]*(1-((-1.0)**j)[None,:]*np.exp(1j*rr*L))/den
chunk=4000
if os.path.exists(ck):
    z=np.load(ck); G=z['G']; eta=float(z['eta']); intN=float(z['intN']); r0=float(z['r0']); ncell=int(z['ncell']); maxw=float(z['maxw'])
else:
    G=np.zeros((J,J)); eta=0.0; intN=0.0; r0=0.0; ncell=0; maxw=0.0
done=0
while r0<R and done<nchunks:
    rk=np.arange(r0,min(R,r0+chunk*h),h); rm=rk+h/2
    Wk=W_lower(rk)
    low=Wk+sum(a*np.cos(rk*np.log(n)) for n,a in act.items())-M*h-1e-9
    N=np.clip(t-low,0,None)
    if N.max()>0:
        idx=N>0; F=phihat(rm[idx]); w=N[idx]*h/np.pi
        G+=np.real((F.conj().T*w)@F)
        eta+=np.sum(w*np.clip(L-np.sum(np.abs(F)**2,1),0,None)); intN+=np.sum(w); ncell+=int(idx.sum()); maxw=max(maxw,w.max())
    r0=rk[-1]+h; done+=1
np.savez(ck,G=G,eta=eta,intN=intN,r0=r0,ncell=ncell,maxw=maxw)
if r0<R:
    print(json.dumps({'progress':r0,'R':R})); sys.exit()
# --- final: validated bound
u=2.0**-53; n=J; gam=lambda m:(m*u)/(1-m*u)
Gs=(G+G.T)/2
lam_t=np.linalg.eigvalsh(Gs)[-1]; mu=lam_t+1e-8
A=mu*np.eye(n)-Gs
np.linalg.cholesky(A)                     # raises if it does not complete
chol_bound=gam(n+1)*(1+gam(n+1))*np.trace(A)+u*np.max(np.abs(np.diag(A)))
lam_up=mu+chol_bound
e_entry=intN*h*h*L**3/24; e_G=J*e_entry                     # quadrature (paper's analytic bound)
e_eta=intN*h*h*(J*L**3)/24          # (|phihat_j|^2)'' <= L^3 each: |x-y|<=L, ||phi_j||_1^2<=L
e_acc=J*gam(ncell+2*J)*intN*L*1.01                           # accumulation of G (|phihat|<=sqrt L)
e_eval=J*2*1e-9*intN*L   # phihat: relative error <= 1e-9 (min distance of midpoints to k_j >= 2.8e-6, so cancellation <= 3e-11, den <= 4e-10)
e_sym=np.max(np.abs(G-G.T))*J
margin=t-(lam_up+e_G+e_acc+e_eval+e_sym)-(eta+e_eta+gam(ncell)*intN*L)
print(json.dumps({'L':L,'t':t,'J':J,'h':h,'R':R,'lambda_float':lam_t,'lambda_upper':lam_up,'chol_bound':chol_bound,
 'eta':eta,'e_G':e_G,'e_eta':e_eta,'e_acc':e_acc,'e_eval':e_eval,'e_sym':e_sym,'MARGIN':margin}))
