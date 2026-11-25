# Coeficientes de -L'/L para Davenport-Heilbronn vs L(s,chi5): soporte y tamano
from mpmath import mp, sqrt, log, mpf
mp.dps=30
k=(sqrt(10-2*sqrt(5))-2)/(sqrt(5)-1)
def a_dh(n): return [0,1,k,-k,-1][n%5]
def a_c5(n): return [0,1,-1,-1,1][n%5]
N=400
def logderiv(a):
    # b = -L'/L : sum_{d|n} b(d) a(n/d) = a(n) log n , a(1)=1
    b=[mpf(0)]*(N+1)
    for n in range(2,N+1):
        s=a(n)*log(n)
        for d in range(2,n):
            if n%d==0: s-=b[d]*a(n//d)
        b[n]=s
    return b
def ppow(n):
    for p in range(2,n+1):
        if n%p==0:
            while n%p==0: n//=p
            return n==1
for name,a in (("chi5",a_c5),("DH",a_dh)):
    b=logderiv(a)
    off=[n for n in range(2,N+1) if not ppow(n) and abs(b[n])>1e-20]
    mx=max(abs(b[n])/log(n) for n in range(2,N+1))
    print(name,"coef. fuera de potencias de primo:",len(off),"primeros:",off[:8])
    print(name,"max |b(n)|/log n, n<=%d:"%N, mp.nstr(mx,6), " b(6)=",mp.nstr(b[6],6)," b(2)=",mp.nstr(b[2],6))
