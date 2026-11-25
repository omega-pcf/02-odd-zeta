# x_sweep.py -- cited in F1_v156, ssec:weil-closure. Needs zeta_zeros_3000.npy (zeros.py).
"""As x_sweep.py, with the prime sum smoothed: weight w(log n/log X) on each prime power n,
w = 1 (sharp), 1-u (Fejer), or the Selberg-type weight of S(t) used in practice."""
import numpy as np, sys
from sympy import primerange
tz=np.load('zeta_zeros_3000.npy'); N=np.arange(1,len(tz)+1)
theta=lambda t: t/2*np.log(t/(2*np.pi))-t/2-np.pi/8+1/(48*t)+7/(5760*t**3)
dth=lambda t: 0.5*np.log(t/(2*np.pi))
def Einv(y,t0):
    t=t0.copy()
    for _ in range(30): t=t-(theta(t)/np.pi+1-y)/(dth(t)/np.pi)
    return t
sel=(N>=100)&(N<=3000); n=N[sel].astype(float); tn=tz[sel]
sp=2*np.pi/np.log(tn/(2*np.pi)); base=Einv(n-0.5,tn)
P=np.array(list(primerange(2,2000000)))
pp=[];kk=[]
for p in P:
    k=1;q=float(p)
    while q<=2e6: pp.append(q);kk.append((p,k));q*=p;k+=1
pp=np.array(pp); lp=np.array([np.log(p) for p,k in kk]); kv=np.array([k for p,k in kk])
o=np.argsort(pp); pp,lp,kv=pp[o],lp[o],kv[o]
def S(t,X,w):
    m=pp<=X; u=np.log(pp[m])/np.log(X); W={'sharp':np.ones_like(u),'fejer':1-u,'cos':np.cos(np.pi*u/2)**2}[w]
    a=W/(kv[m]*np.sqrt(pp[m])); f=kv[m]*lp[m]
    return -(np.sin(np.outer(t,f))@a)/np.pi
for w in ['sharp','fejer']:
    for X in [20,50,100,200,300,500,1000,2000,5000,1e4,3e4,1e5,3e5,1e6]:
        r=Einv(n-0.5-S(base,X,w),base); e=np.mean(np.abs(r-tn)/sp)
        print(w,int(X),round(e,4)); sys.stdout.flush()
