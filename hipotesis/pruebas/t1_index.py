"""t1_index.py — W4–W5, prop:what-fluctuation-takes (iv): el orden angular de phi carga la posicion del primo.
El indice de phi en p: i_p = N_p / e_p, con N_p = p-1 (p partido) o 2(p+1) (p inerte) el orden del grupo donde vive phi
en (Z[phi]/p)^* y e_p el orden de phi (comun.py: aritmetica exacta en Z[phi]/p).  e_p i_p = p - 1 o 2(p+1): el orden
angular fija la posicion de p salvo el indice.
El articulo: el indice es 1 para el 66.5% de los primos bajo 2*10^5 y a lo mas 6 para el 90.3%.
Uso: python3 -I t1_index.py"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comun import primos, indice
for desde in (7, 2):
    P = [p for p in primos(200000, desde) if p != 5]
    I = [indice(p) for p in P]
    print(f"primos {desde} <= p < 2e5, p != 5 ({len(P)}): indice 1: {100*sum(i == 1 for i in I)/len(P):.1f}%;"
          f"  indice <= 6: {100*sum(i <= 6 for i in I)/len(P):.1f}%")
print("articulo: 66.5% y 90.3%")
