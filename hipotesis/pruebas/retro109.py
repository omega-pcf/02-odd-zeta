"""retro109.py — Sprint 109: las dos caras de la dinamica de Fibonacci (toro real / puntos de torsion)."""
from math import gcd
from sympy import primerange, factorint, Poly, symbols, GF, sqrt_mod
ok=0
def chk(c,msg):
    global ok; assert c,msg; ok+=1
def mpow(n,mod=None):
    a,b,c,d=1,0,0,1; x=(0,1,1,1)
    for _ in range(n):
        a,b,c,d=(a*x[0]+b*x[2],a*x[1]+b*x[3],c*x[0]+d*x[2],c*x[1]+d*x[3])
        if mod: a,b,c,d=a%mod,b%mod,c%mod,d%mod
    return a,b,c,d
L=[2,1]
for i in range(900): L.append(L[-1]+L[-2])
# (i) puntos fijos de M^n en R^2/Z^2 = |det(M^n-1)| = |N(phi^n-1)| = |L_n-1-(-1)^n|
for n in range(1,9):
    a,b,c,d=mpow(n); det=abs((a-1)*(d-1)-b*c); chk(det==abs(L[n]-1-(-1)**n),"det")
    D=det; cnt=sum(1 for x in range(D) for y in range(D) if ((a-1)*x+b*y)%D==0 and (c*x+(d-1)*y)%D==0)
    chk(cnt==det,("fix",n,cnt,det))   # puntos (x/D,y/D) fijos: todos los fijos tienen denominador | det
# producto ciclotomico: |N(phi^n-1)| = prod_{d|n} |N(Phi_d(phi))|, con N(Phi_d) por Moebius, enteros positivos
from sympy import mobius, divisors, Rational
Nn=lambda n: abs(L[n]-1-(-1)**n)
for n in range(1,41):
    val=Rational(1)
    for d in divisors(n): val*=Rational(Nn(d))**mobius(n//d)
    chk(val.q==1 and val>0,("NPhi entero",n))
    pr=1
    for d in divisors(n):
        v=Rational(1)
        for e in divisors(d): v*=Rational(Nn(e))**mobius(d//e)
        pr*=v
    chk(pr==Nn(n),"prod")
# (ii) periodo de M en la p-torsion = mcm de los relojes de los primos sobre p (p != 5)
def order_M(p):
    n=1
    while mpow(n,p)!=(1,0,0,1): n+=1
    return n
def clocks(p):
    if p%5 in (1,4):   # escindido: dos raices de x^2-x-1 en F_p
        r=sqrt_mod(5,p); inv2=pow(2,-1,p); roots=[(1+r)*inv2%p,(1-r)*inv2%p]; out=[]
        for t in roots:
            k,x=1,t
            while x!=1: x=x*t%p; k+=1
            out.append(k)
        return out
    # inerte: orden de phi en F_{p^2}=F_p[t]/(t^2-t-1)
    k,x=1,(0,1)
    while x!=(1,0):
        u,v=x; x=(v%p,(u+v)%p) ; k+=1   # (u+v t)*t = v + (u+v) t
    return [k]
from math import lcm
for p in primerange(2,400):
    if p==5: continue
    cl=clocks(p); chk(order_M(p)==lcm(*cl) if len(cl)>1 else order_M(p)==cl[0],("orden",p))
    n=order_M(p); chk(Nn(n)%p==0,("p | N(phi^n-1)",p))
chk(order_M(5)==20,"pisano 5")
# (iii) caracteres: la orbita de m != 0 bajo M no vuelve; correlacion <e_m o M^k, e_n> = [M^k m = n] a lo mas para un k
for m in [(1,0),(0,1),(2,-3),(5,8),(-1,1)]:
    seen=set(); v=m
    for k in range(60):
        chk(v not in seen,"orbita"); seen.add(v); v=(v[1],v[0]+v[1])
print("retro109:",ok,"aserciones, 0 fallos")
