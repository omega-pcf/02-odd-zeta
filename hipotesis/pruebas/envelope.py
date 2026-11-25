import mpmath as mp
mp.mp.dps=25
zs=[mp.mpf(l) for l in open('zeros.txt').read().split()]
th5=lambda t: mp.im(mp.loggamma(mp.mpf(1)/4+0.5j*t))-(t/2)*mp.log(mp.pi/5)
Nsm=lambda t: th5(t)/mp.pi+mp.mpf(1)/2     # constant fixed below
# calibrate constant so that S has mean ~0
vals=[n+1-Nsm(g) for n,g in enumerate(zs)]
c=sum(vals)/len(vals)
S=[v-c for v in vals]
dens=lambda t: mp.log(5*t/(2*mp.pi))/(2*mp.pi)
print("constant offset:",mp.nstr(c,6))
print(" n   gamma_n     S(gamma_n)   S/dens    Tsm(n-S)-gamma_n")
Tsm=lambda x: mp.findroot(lambda t: Nsm(t)+c-x, 10.0 if x<3 else float(2*mp.pi*x/mp.log(5*x)))
for i in [0,1,4,9,19,29,39]:
    g=zs[i]; s=S[i]
    print(f"{i+1:3d} {float(g):10.5f} {float(s):11.5f} {float(s/dens(g)):9.4f} {float(Tsm(i+1-s)-g):.2e}")
print("mean |S| =",float(sum(abs(x) for x in S)/len(S)), "  max|S| =",float(max(abs(x) for x in S)))
