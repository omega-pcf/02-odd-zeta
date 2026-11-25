"""retro99.py — sprint 99: que selecciona el estabilizador {id, mate}. La funcion de Davenport-Heilbronn
como contraste: simetria de Klein completa, sin producto de Euler, hecha con los caracteres de cuarto de vuelta
omega, omega-barra modulo 5 (omega^2 = chi_5), y con ceros fuera de la recta.
Uso: python3 -I retro99.py
"""
import mpmath as mp
mp.mp.dps = 30
ok = fail = 0
def check(c, m):
    global ok, fail
    if c: ok += 1
    else: fail += 1; print("  FALLA:", m)

I = mp.mpc(0, 1)
om = {0: 0, 1: 1, 2: I, 4: -1, 3: -I}          # Teichmuller mod 5, omega(2) = i
omb = {k: mp.conj(v) for k, v in om.items()}
chi5 = {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}
check(all(om[k] ** 2 == chi5[k] for k in range(5)), "omega^2 != chi5")
kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
a = lambda n: mp.re((1 - I * kap) * om[n % 5])     # coeficientes de DH
for n in range(1, 50):
    check(abs(mp.im((1 - I*kap)/2*om[n % 5] + (1 + I*kap)/2*omb[n % 5])) < 1e-25, "coef no real")
check(abs(a(2) * a(3) - a(6)) > 0.5, "DH multiplicativa")
print(f"1. omega^2 = chi_5; kappa = {mp.nstr(kap, 10)}; a(2)a(3) = {mp.nstr(a(2)*a(3), 6)} != a(6) = {mp.nstr(a(6), 6)}: sin producto de Euler")

def L(s, c): return mp.dirichlet(s, [c[k] for k in range(5)])
def DH(s): return (1 - I*kap)/2 * L(s, om) + (1 + I*kap)/2 * L(s, omb)
# ecuacion funcional: Lambda(s) = (5/pi)^{s/2} Gamma((s+1)/2) f(s) cumple Lambda(s) = Lambda(1-s) (DH, caracter impar)
def Lam(s): return (5 / mp.pi) ** (s / 2) * mp.gamma((s + 1) / 2) * DH(s)
for s in (mp.mpc(0.3, 7), mp.mpc(0.8, 20.5), mp.mpc(-0.4, 3)):
    check(abs(Lam(s) - Lam(1 - s)) < 1e-15 * abs(Lam(s)), f"ecuacion funcional en {s}")
print("2. DH: coeficientes reales y ecuacion funcional s <-> 1-s: tiene la simetria de Klein completa")

rho = mp.findroot(DH, mp.mpc(0.808, 85.699))
check(abs(DH(rho)) < 1e-20 and rho.real > 0.8, f"cero fuera de la recta: {rho}")
orb = {"id": rho, "conj": mp.conj(rho), "mate": 1 - mp.conj(rho), "conj.mate": 1 - rho}
for k, z in orb.items():
    check(abs(DH(z)) < 1e-18, f"{k} no es cero")
stab = [k for k, z in orb.items() if abs(z - rho) < 1e-15]
check(stab == ["id"], "estabilizador")
print(f"3. cero de DH fuera de la recta: {mp.nstr(rho, 12)}; su orbita de Klein tiene 4 ceros; estabilizador = {stab}")
rho2 = mp.findroot(DH, mp.mpc(0.651, 114.163))
check(abs(DH(rho2)) < 1e-20 and rho2.real > 0.6, "segundo cero")
print(f"   otro: {mp.nstr(rho2, 12)}")

# 4. los factores, con producto de Euler, en la recta en esa altura: ceros de L(s, omega) cerca de t = 85.7
# L(s,omega) tiene coeficientes complejos: su simetria es s -> 1 - conj(s) junto con omega -> omega-barra
for t0 in (85.0, 86.0, 114.0):
    try:
        z = mp.findroot(lambda s: L(s, om), mp.mpc(0.5, t0))
        check(abs(z.real - 0.5) < 1e-12, f"cero de L(omega) fuera de la recta {z}")
        print(f"4. un cero de L(s, omega) cerca de t={t0}: {mp.nstr(z, 12)}")
    except Exception as e:
        print("   sin convergencia", t0)
print(f"\n{ok} aserciones, {fail} fallas")
