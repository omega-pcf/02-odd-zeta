import numpy as np
from scipy.optimize import linprog
from scipy.special import digamma
from sympy import factorint
chi=lambda n:[0,1,-1,-1,1][n%5]
def W(r): return np.log(5/np.pi)+np.real(digamma(0.25+0.5j*r))
A={}
for n in range(2,400):
    f=factorint(n)
    if len(f)==1 and chi(n)!=0: A[n]=-2*np.log(list(f)[0])*chi(n)/np.sqrt(n)
def certify(L,lam_max=12.0,m=120,R=400.0,nr=6000,B=None):
    PL=lambda r: sum(a*np.cos(r*np.log(n)) for n,a in A.items() if np.log(n)<L)
    sumPL=sum(abs(a) for n,a in A.items() if np.log(n)<L)
    lams=np.linspace(L,lam_max,m)
    r=np.concatenate([np.linspace(0,40,nr),np.linspace(40,R,nr)])
    base=W(r)+PL(r)
    C=np.cos(np.outer(r,lams))
    # vars: b+ (m), b- (m), t ; maximize t
    nv=2*m+1
    c=np.zeros(nv); c[-1]=-1
    Aub=np.hstack([-C, C, np.ones((len(r),1))]); bub=base
    # large-r safety: sum|b| <= W(R)-sumPL
    Bmax=W(R)-sumPL
    Aub=np.vstack([Aub, np.concatenate([np.ones(2*m),[0]])]); bub=np.append(bub,Bmax)
    bounds=[(0,None)]*(2*m)+[(None,10)]
    res=linprog(c,A_ub=Aub,b_ub=bub,bounds=bounds,method='highs')
    return -res.fun if res.success else None, Bmax
for L in [0.5,0.6,0.7,0.745,0.8,0.9,1.0,1.1,1.2]:
    t,B=certify(L); print(f"L={L}: best min(W+P+E) on grid = {t:.4f}   (sum|b| cap {B:.2f})")
