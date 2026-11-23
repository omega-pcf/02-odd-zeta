> Source: principal author's pass, 2026-11-22 — `Downloads/F1 v168 — cambios por hacer en el texto.md`; scripts origin `Downloads/F1_v168_scripts_faltantes.zip`, imported at `hipotesis/pruebas/`. Verbatim copy below.

# F1 v168 — cambios por hacer en el texto

Nov 22, 2026 · @Jorge Armando Gonzalez Garcia

## Qué es

Cuatro párrafos de la v168 cuyas cifras no salen al rehacer los scripts que citan. Para cada uno: el texto actual, el texto propuesto y por qué. Ningún teorema cambia: los cuatro son observaciones numéricas \[N\].

Las cifras nuevas salen de los scripts de `F1_v168_scripts_faltantes.zip` (carpeta `hipotesis/pruebas/`, con sus salidas en `salidas/`). Cada script imprime su cifra y la del artículo una junto a la otra.

| Párrafo | Script | Qué pasa |
| --- | --- | --- |
| ssec:product-surface, el análogo de los conteos | `castelnuovo.py` | Las cotas del artículo salen de evaluar ψ en una muestra de x; el máximo verdadero es mayor |
| ssec:weil-closure, las posiciones | `corrected_operator.py` | El 0.20 es la mediana; el texto dice media (0.21) |
| ssec:weil-closure, lo que la ley tiene que dar | `law_resolution.py` | Las dos cifras de referencia salen con la mediana, no con la media; cuatro de las cinco ventanas no salen |
| ssec:weil-closure, lo que los números pueden ver | `circle_and_detect.py` | Con la órbita del barrido, la detección es 0.10 y 0.38, no 0.001 y 0.057 |

## 1. El análogo de los conteos (ssec:product-surface, castelnuovo.py)

Texto actual:

```latex
Up to $e^{18}$,
$|\psi(x,\chi)|/\sqrt x$ stays below $0.80$, $1.14$ and $1.89$ for $x>10^6$ ($\chi_4$, $\chiv$,
$\chi_{20}$), with no growth, and each fibre of $G$ deviates from a quarter of the total by at
most $0.63\sqrt x$ (\texttt{castelnuovo.py} \tierN).
```

Texto propuesto:

```latex
Up to $e^{18}$,
$|\psi(x,\chi)|/\sqrt x$ stays below $1.27$, $1.28$ and $2.22$ for $x>10^6$ ($\chi_4$, $\chiv$,
$\chi_{20}$), with no growth --- its maximum over $[3\cdot10^7,e^{18}]$ is $1.13$, $1.07$ and $1.76$ ---,
and each fibre of $G$ deviates from a quarter of the total by at most $0.79\sqrt x$
(\texttt{castelnuovo.py} \tierN).
```

Por qué: «stays below» es una cota, y tiene que ser el máximo sobre todas las potencias de primo entre 10⁶ y e¹⁸. Ese máximo es 1.267, 1.278, 2.213 y 0.782 (fibras). Las cifras actuales salen de evaluar en unos pocos cientos de valores de x: con una rejilla logarítmica de 374 puntos dan 0.84, 1.15, 1.92 y 0.60, y con 340 o 400 puntos cambian hasta en 0.3. «No growth» sí se sostiene, y la frase nueva lo respalda con el máximo del último tramo.

## 2. Las posiciones (ssec:weil-closure, corrected\_operator.py)

Texto actual:

```latex
the mean error of $T^*(n)$ is about
$4.9$ mean spacings; with the exact envelope, which uses no prime and no zero, it is $0.20$
spacings,
```

Texto propuesto:

```latex
the mean error of $T^*(n)$ is about
$4.9$ mean spacings; with the exact envelope, which uses no prime and no zero, it is $0.21$
spacings ($n\le1000$; the median is $0.19$),
```

Por qué: el texto dice «mean». La media del error de la envolvente exacta es 0.212 (n ≤ 1000) y su mediana 0.186; el 0.20 del texto es la mediana en n = 100 a 3000 (0.195). El 4.9 de T\* sí es la media (4.96). Se deja la media, que es lo que el texto nombra, y la mediana entre paréntesis porque es la medida del cambio 3.

## 3. Lo que la ley tiene que dar (ssec:weil-closure, law\_resolution.py)

Texto actual:

```latex
Replacing each prime by the count of its window of width
$\delta$ in $\log p$ --- what a law that knows how many primes of each kind fall in each window,
but not the primes one by one, would give --- the mean error of the corrected operator
($n=100$ to $3000$) is $0.183$ at $\delta=10^{-2}$, $0.087$ at $3\cdot10^{-3}$, $0.053$ at $10^{-3}$,
$0.028$ at $3\cdot10^{-4}$ and $0.023$ at $10^{-4}$, against $0.20$ with no correction and
$0.020$ prime by prime (\texttt{law\_resolution.py} \tierN).  The improvement is gradual, and at
height $T$ the law has to resolve a scale of order $1/T$.
```

Texto propuesto:

```latex
Replacing each prime by the count of its window of width
$\delta$ in $\log p$ --- what a law that knows how many primes of each kind fall in each window,
but not the primes one by one, would give --- the median error of the corrected operator
($n=100$ to $3000$) is $0.194$ at $\delta=10^{-2}$, $0.170$ at $3\cdot10^{-3}$, $0.089$ at $10^{-3}$,
$0.041$ at $3\cdot10^{-4}$ and $0.025$ at $10^{-4}$, against $0.20$ with no correction and
$0.021$ prime by prime (\texttt{law\_resolution.py} \tierN).  The error falls between
$\delta=10^{-3}$ and $3\cdot10^{-4}$, the scale $1/T$ of the heights measured ($T\approx240$ to
$3700$): at height $T$ the law has to resolve a scale of order $1/T$.
```

Por qué:

- **Media o mediana.** Las dos cifras de referencia salen exactas con la mediana (0.195 sin corrección, 0.021 primo por primo). Con la media dan 0.225 y 0.038, y ningún corte X ni peso baja de 0.029.
- **La forma de la ventana.** Las cinco cifras nuevas son de la rejilla fija: cada primo cae en su ventana \[jδ, (j+1)δ) y entra con el promedio de la ventana. Es la que corresponde a «not the primes one by one». Una ventana centrada en cada primo da cifras más bajas (0.193, 0.143, 0.047, 0.023, 0.021), pero conserva la fase de cada primo, así que sí los conoce uno por uno.
- **«The improvement is gradual».** Con la rejilla fija la caída es más brusca. Se cambia por dónde cae el error, que es lo que sostiene la conclusión: la caída está en la escala 1/T de las alturas medidas.

## 4. Lo que los números pueden ver (ssec:weil-closure, circle\_and\_detect.py)

Texto actual:

```latex
A zero of $L(s,\chiv)$ at height $\gamma$ with
$\Re\rho=\tfrac12+\delta$ would have made some Toeplitz matrix of the sweep indefinite as soon as
$\delta\ge0.001$ at $\gamma=30$, $\delta\ge0.057$ at $\gamma=100$, $\delta\ge0.31$ at $\gamma=200$; above
$\gamma\approx300$ no admissible $\delta$ is detected, because $|\hat g_a(\gamma)|^2$ decays like
$\gamma^{-4}$.
```

Texto propuesto:

```latex
A zero of $L(s,\chiv)$ at height $\gamma$ with
$\Re\rho=\tfrac12+\delta$ would have made some Toeplitz matrix of the sweep indefinite as soon as
$\delta\ge0.10$ at $\gamma=30$ and $\delta\ge0.38$ at $\gamma=100$; above $\gamma\approx200$ no admissible
$\delta$ is detected, because $|\hat g_a(\gamma)|^2$ decays like $\gamma^{-4}$.  Longer orbits see
further: with $k\log p\le120$ in place of $14.2$ the thresholds fall to $0.001$, $0.009$, $0.022$
and $0.028$ at $\gamma=30$, $100$, $200$ and $300$ (\texttt{circle\_and\_detect.py} \tierN).
```

Por qué: el párrafo habla de «the sweep», y la órbita del barrido es k log p ≤ 14.2. Con ella el menor δ detectado es 0.10 en γ = 30 y 0.38 en γ = 100, y ninguno desde 200; lo mismo desde el lado de los primos que desde el de los 397 ceros, y con cinco formas distintas de poner el cero fuera de la recta. Lo único que baja el umbral es alargar la órbita:

| k log p ≤ | γ ≈ 30 | γ ≈ 100 | γ ≈ 200 | γ ≈ 300 |
| --- | --- | --- | --- | --- |
| 14.2 (barrido) | 0.103 | 0.385 | ninguno | ninguno |
| 25 | 0.049 | 0.112 | 0.316 | 0.376 |
| 60 | 0.006 | 0.028 | 0.085 | 0.118 |
| 120 | 0.001 | 0.009 | 0.022 | 0.028 |

La conclusión del párrafo queda más firme: el barrido deja de ver antes (γ ≈ 200, no 300), y la frase sobre órbitas largas respalda con números la oración siguiente del texto, `(W4) for every k and every width is as strong as the line`. El resto del párrafo no cambia.

## Lo que queda abierto

- **El 0.087 de la ley por ventanas** (δ = 3·10⁻³, cambio 3). No sale con la rejilla fija (0.170), ni con la ventana centrada (0.143), ni con la rejilla de la torre de una sesión anterior, que tampoco reprodujo las cifras de este párrafo. Si aparece el `law_resolution.py` original, el párrafo puede volver a sus cifras.
- **Las cifras originales de detección** (0.001, 0.057, 0.31). Ninguna longitud de órbita las da juntas con «ninguno sobre \~300». El texto propuesto usa las de la órbita del barrido, que es lo que el párrafo dice medir.
