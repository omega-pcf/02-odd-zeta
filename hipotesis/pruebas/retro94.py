"""retro94.py — sprint 94: la masa del reloj separada por las fibras de G.

Para cada nivel n <= NMAX:
  Q_n = |N(Phi_n(phi))| (entero exacto, por Moebius sobre |N(phi^d - 1)| = |(-1)^d - L_d + 1|),
  se factoriza, y el peso v_p(Q_n) log p de cada primo se asigna a la fibra de G de p mod 20:
     K = {1,9} (nucleo), S = {11,19}, I1 = {13,17}, I3 = {3,7};
  'otros' = los primos 2, 5 y los que dividen a n (clausula (iv) de prop:clock-cyclotomic).
Uso: python3 -I retro94.py [NMAX]
"""
import sys, math, time
from collections import defaultdict
from flint import fmpz

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 240
LOGPHI = math.log((1 + 5 ** 0.5) / 2)
FIB = {1: "K", 9: "K", 11: "S", 19: "S", 13: "I1", 17: "I1", 3: "I3", 7: "I3"}
ok = fail = 0


def check(c, msg):
    global ok, fail
    if c:
        ok += 1
    else:
        fail += 1
        print("  FALLA:", msg)


def mobius(n):
    r, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            r = -r
        p += 1
    return -r if n > 1 else r


def totient(n):
    r, p, m = n, 2, n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


# Lucas
L = [2, 1]
for k in range(2, NMAX + 2):
    L.append(L[-1] + L[-2])
Npow = {d: abs((-1) ** d - L[d] + 1) for d in range(1, NMAX + 1)}   # |N(phi^d - 1)|


def Q(n):
    num = den = 1
    for d in range(1, n + 1):
        if n % d == 0:
            mu = mobius(n // d)
            if mu == 1:
                num *= Npow[d]
            elif mu == -1:
                den *= Npow[d]
    assert num % den == 0
    return num // den


def tipo(n):
    if n % 2 == 1:
        return "impar"
    if n % 4 == 2:
        return "2 mod 4"
    if n % 8 == 4:
        return "4 mod 8"
    return "0 mod 8"


permitidas = {"impar": {"K", "S"}, "2 mod 4": {"K", "S"}, "4 mod 8": {"K", "I1"}, "0 mod 8": {"K", "I3"}}
masa = defaultdict(lambda: defaultdict(float))      # masa[tipo][fibra]
total_tipo = defaultdict(float)
porN = {}
t0 = time.time()
acum = defaultdict(float)
for n in range(3, NMAX + 1):
    q = Q(n)
    tp = tipo(n)
    # 0) el tamano del nivel (prop:clock-cyclotomic (iii))
    check(abs(math.log(q) - totient(n) * LOGPHI) <= 4 * 2.6180339887, f"tamano del nivel {n}")
    # 1) en los niveles 4 | n, n >= 8, Q_n es un cuadrado salvo el primo ramificado
    base = q
    if n % 4 == 0:
        q5 = q
        while q5 % 5 == 0:
            q5 //= 5
        r = math.isqrt(q5)
        check(r * r == q5, f"Q_{n} no es cuadrado fuera de 5")
        fac = [(int(p), 2 * int(e)) for p, e in fmpz(r).factor()] if r > 1 else []
        v5 = 0
        while base % 5 == 0:
            base //= 5; v5 += 1
        if v5:
            fac.append((5, v5))
    else:
        fac = [(int(p), int(e)) for p, e in fmpz(q).factor()] if q > 1 else []
    s = 0.0
    for p, e in fac:
        w = e * math.log(p)
        s += w
        if p in (2, 5) or n % p == 0:
            f = "otros"
        else:
            f = FIB[p % 20]
            # 2) la ley exacta: la fibra que puede aparecer en cada tipo de nivel
            check(f in permitidas[tp], f"nivel {n} ({tp}): primo {p} en la fibra {f}")
            # 3) escindido: p = 1 mod n (n impar) o mod n/2 (n = 2 mod 4) o mod n (4 | n); inerte: n | 2(p+1), n no divide p+1
            if f in ("K", "S"):
                m = n if n % 4 != 2 else n // 2
                check(p % m == 1, f"nivel {n}: escindido {p} no es 1 mod {m}")
            else:
                check((2 * (p + 1)) % n == 0 and (p + 1) % n != 0, f"nivel {n}: inerte {p}")
            # 4) 5 | n: solo escindidos; 20 | n: solo la clase 1
            if n % 5 == 0:
                check(f in ("K", "S"), f"nivel {n}: inerte {p} con 5 | n")
            if n % 20 == 0:
                check(p % 20 == 1, f"nivel {n}: {p} no es 1 mod 20")
        masa[tp][f] += w
        acum[f] += w
    check(abs(s - math.log(q)) < 1e-6 * max(1, s), f"suma de pesos del nivel {n}")
    total_tipo[tp] += s
    # 5) niveles m y 2m (m impar): la misma norma
    if n % 2 == 1:
        check(Q(n) == Q(2 * n) if 2 * n <= NMAX else True, f"Q_{n} = Q_{2*n}")
    if n % 60 == 0:
        porN[n] = dict(acum)

print(f"NMAX = {NMAX}; {time.time()-t0:.1f}s")
T = sum(total_tipo.values())
print("\nA) Reparto de la masa por tipo de nivel (limite: 2/3, 1/6, 1/12, 1/12):")
for tp, lim in [("impar", 2 / 3), ("2 mod 4", 1 / 6), ("4 mod 8", 1 / 12), ("0 mod 8", 1 / 12)]:
    print(f"   {tp:8s}: {total_tipo[tp]/T:.4f}  (limite {lim:.4f})")
    check(abs(total_tipo[tp] / T - lim) < 0.02, f"reparto del tipo {tp}")

print("\nB) Dentro de cada tipo de nivel, fraccion de la masa en cada fibra:")
frac = {}
for tp in ["impar", "2 mod 4", "4 mod 8", "0 mod 8"]:
    tt = total_tipo[tp]
    frac[tp] = {f: masa[tp][f] / tt for f in masa[tp]}
    print(f"   {tp:8s}: " + ", ".join(f"{f}={frac[tp].get(f,0):.4f}" for f in ["K", "S", "I1", "I3", "otros"]))

print("\nC) Fraccion acumulada de la masa por fibra, niveles n <= N:")
for n, d in porN.items():
    t = sum(d.values())
    print(f"   N={n}: " + ", ".join(f"{f}={d.get(f,0)/t:.4f}" for f in ["K", "S", "I1", "I3", "otros"])
          + f";  escindidos={(d.get('K',0)+d.get('S',0))/t:.4f}, inertes={(d.get('I1',0)+d.get('I3',0))/t:.4f}")

print(f"\n{ok} aserciones, {fail} fallas")
