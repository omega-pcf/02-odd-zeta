import mpmath as mp
mp.mp.dps=30
kappa=mp.log(5)-mp.log(mp.pi)-mp.euler-mp.pi/2-3*mp.log(2)
print("kappa =",kappa, "  W(0)=log(5/pi)+psi(1/4) =", mp.log(5/mp.pi)+mp.digamma(0.25))
# check  2 int_0^inf (e^{-u/2}-e^{-2u})/(1-e^{-2u}) du = pi/2+3log2
print(mp.quad(lambda u: 2*(mp.e**(-u/2)-mp.e**(-2*u))/(1-mp.e**(-2*u)),[0,1,mp.inf]), mp.pi/2+3*mp.log(2))
K=lambda d: 2*(mp.atanh(mp.e**(-d/2))+mp.atan(mp.e**(-d/2)))
print("K check:", K(0.4), mp.quad(lambda t: 2*mp.e**(-t/2)/(1-mp.e**(-2*t)),[0.4,1,mp.inf]))
bound=lambda L: kappa+K(L/2)
print("bound at L=log2:", bound(mp.log(2)))
Ls=mp.findroot(bound,0.75); print("L* =",Ls)
