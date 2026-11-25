import math
EG=0.5772156649015329
LMAX=14.5
N=int(math.exp(LMAX))+1
s=bytearray([1])*(N+1); s[0]=s[1]=0
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
def chi5(n):
    r=n%5; return 0 if r==0 else (1 if r in (1,4) else -1)
# prime powers with Lambda, chi5, class mod 20
pp=[]
for p in range(2,N+1):
    if s[p]:
        lp=math.log(p); q=p
        while q<=N:
            c=chi5(q)
            if c: pp.append((math.log(q),lp*c/math.sqrt(q),q%20))
            q*=p
def T(a,v):
    v=abs(v)
    if v<=a: return a*(2/3 - v*v/a**2 + v**3/(2*a**3))
    if v<=2*a: return a*(2-v/a)**3/6
    return 0.0
def arch(a,sh):
    h=lambda u: T(a,u+sh)
    h0=h(0.0)
    tot=h0*(math.log(5/math.pi)-EG)
    U=sh+2*a+40; M=200000; du=U/M; acc=0.0
    for j in range(1,M+1):
        u=(j-0.5)*du
        num=math.exp(-2*u)*h0 - math.exp(-u/2)*(h(u)+h(-u))/2
        acc+=num/(1-math.exp(-2*u))*du
    return tot+2*acc
def primes_side(a,sh,byclass=False):
    tot=0.0; cl={}
    for lq,w,c in pp:
        v=w*(T(a,lq+sh)+T(a,sh-lq))
        if v: tot+=v; cl[c]=cl.get(c,0)+v
    return (tot,cl) if byclass else tot
for p in (2,3):
    for a in (0.5,1.0):
        t0=arch(a,0)-primes_side(a,0)
        ratios=[]
        for k in range(1,12):
            sh=k*math.log(p)
            if sh+2*a>LMAX: break
            tk=arch(a,sh)-primes_side(a,sh)
            ratios.append(tk/t0)
        print('p=%d a=%.1f t0=%.4f  t_k/t0:'%(p,a,t0),' '.join('%.3f'%r for r in ratios), ' W3 ok:',all(abs(r)<=1 for r in ratios))

print('--- ajuste de una frecuencia: t_k/t0 ~ A cos(gamma k log p)')
for p in (2,3):
    a=0.5
    t0=arch(a,0)-primes_side(a,0)
    ks=[k for k in range(1,12) if k*math.log(p)+2*a<=LMAX]
    r=[(arch(a,k*math.log(p))-primes_side(a,k*math.log(p)))/t0 for k in ks]
    best=None
    for j in range(0,4001):
        g=4+j*0.001
        c=[math.cos(g*k*math.log(p)) for k in ks]
        A=sum(x*y for x,y in zip(r,c))/sum(y*y for y in c)
        err=sum((x-A*y)**2 for x,y in zip(r,c))
        if best is None or err<best[0]: best=(err,g,A)
    print('p=%d: gamma=%.3f A=%.3f resid=%.4f'%(p,best[1],best[2],best[0]))
