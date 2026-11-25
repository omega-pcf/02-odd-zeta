import mpmath as mp
mp.mp.dps=20
a0=mp.mpf(59)/40; b0=mp.mpf(1)/8; mu=mp.mpf(1)/2; sg=mp.mpf(3)/2
c=lambda n: 2+a0/(1+b0*mp.log(n))
Tstar=lambda n: c(n)*mp.pi*n/mp.log(mu*n+sg)
theta=lambda t: mp.im(mp.loggamma(mp.mpf(1)/4+0.5j*t))-t*mp.log(mp.pi)/2
Nsm=lambda t: theta(t)/mp.pi+1                       # smooth counting for zeta
Tsm=lambda n: mp.findroot(lambda t: Nsm(t)-n, max(14.0,float(Tstar(n))))
dens=lambda t: mp.log(t/(2*mp.pi))/(2*mp.pi)
print(" n     gamma_n      T*(n)     Tsmooth(n)   g-T*    g-Tsm    S(g)/dens")
for n in [1,2,5,10,20,50,100,200,500]:
    g=mp.zetazero(n).imag; ts=Tstar(n); tsm=Tsm(n)
    S=n-Nsm(g)                                        # S(gamma_n) with N(gamma_n)=n (upper limit)
    print(f"{n:4d} {float(g):11.5f} {float(ts):11.5f} {float(tsm):11.5f} {float(g-ts):8.4f} {float(g-tsm):8.4f} {float(S/dens(g)):9.4f}")
