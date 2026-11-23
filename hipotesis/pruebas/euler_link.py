"""euler_link.py — W4–W5, prop:euler-tower: el producto de Euler, la torre de phi y las posiciones.
(ii) A s real el producto solo lleva magnitudes: prod_p (1-p^-2)^-1 = pi^2/6 (primos hasta 10^7), y sum_p 1/p diverge
     (crece como log log x + M).
(iii) La frecuencia de un primo es su coordenada en la torre de phi: log p = sigma_p log phi, sigma_n = log_phi n;
     sigma_2 = lambda_log = log 2/log phi, sigma_(2^e) = e lambda_log, y para los numeros de Mersenne
     sigma_(2^e - 1) = e lambda_log + log_phi(1 - 2^-e), forma cerrada en el ancla binaria y el exponente.
El articulo: el segundo termino vale -2.5e-4 en e = 13 y -9.7e-10 en e = 31.
Uso: python3 -I euler_link.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from comun_pruebas import criba
mp.mp.dps = 40
phi = (1 + mp.sqrt(5))/2; lam = mp.log(2)/mp.log(phi)
P = criba(10**7).astype(float)
print(f"(ii) prod_(p<1e7) (1-p^-2)^-1 = {float(np.exp(-np.sum(np.log1p(-P**-2)))):.10f};  pi^2/6 = {float(mp.pi**2/6):.10f}")
for x in (1e3, 1e5, 1e7):
    print(f"     sum_(p<={x:.0e}) 1/p = {np.sum(1/P[P <= x]):.4f}  (log log x + 0.2615 = {np.log(np.log(x)) + 0.2615:.4f})")
print(f"(iii) lambda_log = log 2/log phi = {mp.nstr(lam, 15)}")
for e in (2, 3, 5, 7, 13, 17, 19, 31):
    M = 2**e - 1
    sig = mp.log(M)/mp.log(phi); cerr = e*lam + mp.log(1 - mp.mpf(2)**-e)/mp.log(phi)
    print(f"     e = {e:2d}: sigma_(2^e-1) = {mp.nstr(sig, 14)};  e*lambda_log + log_phi(1-2^-e) = {mp.nstr(cerr, 14)};"
          f"  segundo termino {mp.nstr(mp.log(1 - mp.mpf(2)**-e)/mp.log(phi), 3)};  phi^sigma = {mp.nstr(phi**sig, 12)}")
print("articulo: -2.5e-4 (e = 13), -9.7e-10 (e = 31)")
