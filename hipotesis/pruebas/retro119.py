# Sprint 119: the 3-part of the clock order e_p, and the class 9 on mu_5.
from sympy import primerange, factorint
def mulq(a,b,p):  # (a0+a1 w)(b0+b1 w), w^2=w+1, over Z/p
    a0,a1=a; b0,b1=b
    return ((a0*b0+a1*b1)%p, (a0*b1+a1*b0+a1*b1)%p)
def powq(a,n,p):
    r=(1,0)
    while n:
        if n&1: r=mulq(r,a,p)
        a=mulq(a,a,p); n>>=1
    return r
def order(p,N):
    # order of w in (Z[w]/p)^x, given w^N=1
    e=N
    for q in factorint(N):
        while e%q==0 and powq((0,1),e//q,p)==(1,0): e//=q
    return e
bad=0; occ={'split':[0,0],'inert':[0,0]}
for p in primerange(7,6000):
    split = p%5 in (1,4)
    N = p-1 if split else 2*(p+1)
    assert powq((0,1),N,p)==(1,0)
    e=order(p,N)
    k=0; m=N
    while m%3==0: m//=3; k+=1
    crit = powq((0,1),m,p)!=(1,0)        # 3 | e_p  iff  w^m != 1
    if crit != (e%3==0): bad+=1
    nec = (p%3==1) if split else (p%3==2)
    if e%3==0: assert nec
    if nec: occ['split' if split else 'inert'][int(e%3==0)]+=1
print("criterion failures:",bad)
print("necessary condition holds, and among those primes (no 3 | e_p, 3 | e_p):",occ)
print("class 9: mod 5 =",9%5,"(=-1), mod 4 =",9%4,", 9*9 mod 20 =",81%20)
