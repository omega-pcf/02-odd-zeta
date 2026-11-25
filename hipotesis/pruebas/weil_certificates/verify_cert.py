import numpy as np, mpmath as mp, json, sys, io, contextlib
from scipy.special import digamma
with contextlib.redirect_stdout(io.StringIO()):
    import cert
from fractions import Fraction
L=float(sys.argv[1]) if len(sys.argv)>1 else 1.0
t,lams,b,act=cert.solve(L)
# rationalise certificate
lamsQ=[Fraction(x).limit_denominator(10**6) for x in lams]
bQ=[Fraction(x).limit_denominator(10**7) for x in b]
keep=[(l,c) for l,c in zip(lamsQ,bQ) if c!=0 and float(l)>=L]
lamv=np.array([float(l) for l,_ in keep]); bv=np.array([float(c) for _,c in keep])
an=np.array(list(act.values())); ln=np.log(np.array(list(act.keys()),float))
W=lambda r: np.log(5/np.pi)+np.real(digamma(0.25+0.5j*r))
T=lambda r: (an[None,:]*np.cos(np.outer(r,ln))).sum(1)+(bv[None,:]*np.cos(np.outer(r,lamv))).sum(1)
MT=np.sum(np.abs(an)*ln)+np.sum(np.abs(bv)*lamv)
R=600.0
h=0.2*t/MT
worst=np.inf; r0=0.0; chunk=200000
while r0<R:
    r=np.arange(r0,min(R,r0+chunk*h)+h,h)
    val=W(r[:-1])+T(r[:-1])-MT*h        # valid lower bound on [r_k, r_{k+1}] (W increasing)
    worst=min(worst,val.min()); r0=r[-1]
tail=float(mp.log(5/mp.pi)+mp.re(mp.digamma(mp.mpf(1)/4+0.5j*R)))-np.abs(an).sum()-np.abs(bv).sum()
print(f"L={L}: LP margin {t:.4f}; certified lower bound on [0,R]: {worst:.5f} (h={h:.2e}, M_T={MT:.1f}); tail bound r>=R: {tail:.4f}; terms={len(keep)}")
print("min frequency in certificate:", float(min(l for l,_ in keep)), ">= L:", float(min(l for l,_ in keep))>=L)
json.dump({"L":L,"lam":[str(l) for l,_ in keep],"b":[str(c) for _,c in keep],"primes":{int(k):float(v) for k,v in act.items()},"certified_min":worst,"tail":tail},open(f"cert_L{L}.json","w"),indent=1)
