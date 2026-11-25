"""dh_zeros.py — ceros de Davenport-Heilbronn hasta T=130 (para retro101.py). Uso: python3 -I dh_zeros.py"""
import mpmath as mp, json, time
mp.mp.dps = 15
I = mp.mpc(0,1)
om = [0,1,I,-I,-1]; omb=[0,1,-I,I,-1]
kap = (mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
def DH(s): return (1-I*kap)/2*mp.dirichlet(s,om)+(1+I*kap)/2*mp.dirichlet(s,omb)
def Z(t):  # real en la recta: Lambda(1/2+it) normalizada
    s = mp.mpc(0.5,t)
    th = mp.im(mp.loggamma((s+1)/2)) + t/2*mp.log(5/mp.pi)
    return mp.re(mp.exp(I*th)*DH(s))
T=130.0; h=0.04; t0=time.time()
ts=[0.1+h*k for k in range(int((T-0.1)/h)+1)]
vals=[Z(t) for t in ts]
line=[]
for a,b,va,vb in zip(ts,ts[1:],vals,vals[1:]):
    if va*vb<0: line.append(float(mp.findroot(Z,(a,b),solver='illinois')))
off=[]
for g in ((0.808,85.699),(0.651,114.163)):
    r=mp.findroot(DH,mp.mpc(*g)); off.append((float(r.real),float(r.imag)))
# conteo esperado de ceros con 0<Im<T: (T/2pi) log(5T/(2 pi e)) + O(1)
NT=T/(2*mp.pi)*mp.log(5*T/(2*mp.pi*mp.e))
print(len(line),"en la recta;",off,"fuera; total",len(line)+2*len(off),"; formula",float(NT),"; seg",round(time.time()-t0))
json.dump({"line":line,"off":off},open("dh_zeros.json","w"))
