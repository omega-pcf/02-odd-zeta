import numpy as np, mpmath as mp
from scipy.optimize import linprog
from scipy.special import digamma
import lp
W=lp.W; A=lp.A
def solve(L,lam_max=16.0,m=200,R=600.0,Afull=None):
    Afull=Afull or A
    act={n:a for n,a in Afull.items() if np.log(n)<L}
    PL=lambda r: sum(a*np.cos(r*np.log(n)) for n,a in act.items())
    sumPL=sum(abs(a) for a in act.values())
    lams=np.linspace(L,lam_max,m)
    r=np.concatenate([np.linspace(0,60,12000),np.linspace(60,R,6000)])
    C=np.cos(np.outer(r,lams)); nv=2*m+1
    c=np.zeros(nv); c[-1]=-1
    Aub=np.vstack([np.hstack([-C,C,np.ones((len(r),1))]), np.concatenate([np.ones(2*m),[0]])])
    Bmax=W(R)-sumPL-0.05
    bub=np.append(W(r)+PL(r),Bmax)
    res=linprog(c,A_ub=Aub,b_ub=bub,bounds=[(0,None)]*(2*m)+[(None,10)],method='highs')
    b=res.x[:m]-res.x[m:2*m]
    return -res.fun, lams, b, act
if __name__=="__main__":
    for L in [1.0,1.05,1.08]:
        t,_,_,_=solve(L); print("L",L,"margin",round(t,4))
    flip=dict(A); 
    for n in (2,8,32,128): flip[n]=-flip[n]
    t,_,_,_=solve(1.0,Afull=flip); print("L=1.0 with chi(2)=+1 (2 split):",round(t,4))
