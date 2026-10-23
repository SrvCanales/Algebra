"""Problema 5 — Una proyección ortogonal que no es realmente una proyección."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 5
ETIQUETA = "Proyección y producto interior"
TITULO = "Una proyección ortogonal que no es realmente una proyección"
CONCEPTO = "producto interior y proyección ortogonal"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
En $\mathbb R^2$ con el producto interior usual, considera

$$
u=(1,1),\quad v=(1,0).
$$

Se quiere calcular la proyección ortogonal de $v$ sobre la recta generada por $u$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"La proyección debe ser paralela a $u$, así que tendrá la forma $p=cu$.",
    r"Como $v\cdot u=1$, el coeficiente de la proyección es $c=1$.",
    r"Por tanto, $\operatorname{proj}_u(v)=(1,1)$. El resultado es correcto porque el vector obtenido tiene la dirección de $u$.",
]
PASO_ERRONEO = 2

EXPLICACION = r"""
El paso 2 omite la normalización correspondiente al producto interior. El coeficiente no es simplemente $v\cdot u$, sino

$$
c=\frac{v\cdot u}{u\cdot u}.
$$

Como $v\cdot u=1$ y $u\cdot u=2$,

$$
\operatorname{proj}_u(v) =\frac12(1,1) =\left(\frac12,\frac12\right).
$$

Para verificarlo, el residuo debe ser ortogonal a $u$:

$$
v-p=\left(\frac12,-\frac12\right),
$$

y

$$
(v-p)\cdot u=\frac12-\frac12=0.
$$

El vector propuesto originalmente no cumple esa condición.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="t   (Segunda coordenada de v)",
                      minimo=-2.0, maximo=2.0, valor=0.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    u = np.array([1.0, 1.0, 0.0])
    v = np.array([1.0, t, 0.0])
    
    # Cálculos
    prod_punto = np.dot(v, u)
    norma_u_cuadrado = np.dot(u, u)
    c = prod_punto / norma_u_cuadrado
    p = c * u
    residuo = v - p
    
    fig = escena_base(rango=3)
    
    # Recta generada por u (span de u)
    agregar_segmento(fig, -3*u, 3*u, color=COLORES["gris"], dash="solid", nombre="Recta gen(u)")
    
    # Vectores principales (en el plano z=0 para emular R2)
    agregar_vector(fig, u, "u", COLORES["azul"])
    agregar_vector(fig, v, "v", COLORES["verde"])
    agregar_vector(fig, p, "proj_u(v)", COLORES["rojo"])
    
    # Segmento residual (perpendicular)
    agregar_segmento(fig, p, v, color=COLORES["ambar"], dash="dash", nombre="Residuo v - p")

    # Formateo de los vectores para el mensaje
    px, py = p[0], p[1]
    rx, ry = residuo[0], residuo[1]
    
    mensaje = (f"**t = {t:.1f}:** $v=(1, {t:.1f})$. Producto interior $v\\cdot u = {prod_punto:.1f}$.\n\n"
               f"Proyección: $p = ({px:.2f}, {py:.2f})$.\n\n"
               f"Vector residual: $v-p = ({rx:.2f}, {ry:.2f})$.\n\n"
               "La proyección roja es paralela a $u$ y el vector residual punteado amarillo es siempre perpendicular a $u$.")
                   
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
