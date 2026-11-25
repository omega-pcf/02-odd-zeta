"""Rigorous lower bound for W(r)=log(5/pi)+Re psi(1/4+ir/2).
Re psi(x+iy) = psi(x) + sum_{k>=0} y^2/((k+x)((k+x)^2+y^2)),  all terms > 0,
so any partial sum is a LOWER bound.  psi(1/4) = -gamma - pi/2 - 3 log 2."""
import numpy as np, mpmath as mp
mp.mp.dps=40
C0=float(mp.log(5/mp.pi)+(-mp.euler-mp.pi/2-3*mp.log(2)))   # = W(0)
SAFE=1e-9                                                     # float safety, subtracted
def W_lower(r):
    r=np.atleast_1d(np.asarray(r,float)); y=r/2; out=np.empty_like(r)
    for i,yy in enumerate(y):
        K=int(4000+60*yy); k=np.arange(K)+0.25
        out[i]=C0+np.sum(yy*yy/(k*(k*k+yy*yy)))
    return out-SAFE
if __name__=="__main__":
    from scipy.special import digamma
    for r in [0,1,5,20,100,600]:
        ex=np.log(5/np.pi)+np.real(digamma(0.25+0.5j*r))
        print(r, W_lower(r)[0], ex, ex-W_lower(r)[0])
