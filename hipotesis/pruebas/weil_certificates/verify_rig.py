import numpy as np, json, sys
from fractions import Fraction
from rigW import W_lower
cert=json.load(open(sys.argv[1])); L=cert['L']
lam=np.array([float(Fraction(x)) for x in cert['lam']]); b=np.array([float(Fraction(x)) for x in cert['b']])
pr={int(k):v for k,v in cert['primes'].items()}
an=np.array(list(pr.values())); ln=np.log(np.array(list(pr.keys()),float))
assert lam.min()>=L
R=600.0
coarse=np.unique(np.concatenate([np.arange(0,5,2e-4),np.arange(5,50,2e-3),np.arange(50,R+0.02,0.02)]))
Wc=np.concatenate([W_lower(coarse[i:i+2000]) for i in range(0,len(coarse),2000)])
MT=np.sum(np.abs(an)*ln)+np.sum(np.abs(b)*lam)
h=2e-4; worst=np.inf; SAFE_T=1e-9
r0=0.0
while r0<R:
    rk=np.arange(r0,min(R,r0+20000*h),h)
    T=(an[None,:]*np.cos(np.outer(rk,ln))).sum(1)+(b[None,:]*np.cos(np.outer(rk,lam))).sum(1)
    idx=np.searchsorted(coarse,rk,side='right')-1     # coarse point <= rk
    val=Wc[idx]+T-MT*h-SAFE_T
    worst=min(worst,val.min()); r0=rk[-1]+h
tail=W_lower(R)[0]-np.abs(an).sum()-np.abs(b).sum()
print(f"L={L}: rigorous min on [0,{R}] = {worst:.5f}; tail r>={R}: {tail:.4f}; M_T={MT:.2f}")
