"""Problema 2 — Un conjunto que contiene el origen y es cerrado bajo escalares, pero no es un subespacio."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 2
ETIQUETA = "Cierre bajo suma"
TITULO = "Un conjunto que contiene el origen y es cerrado bajo escalares, pero no es un subespacio"
CONCEPTO = "espacio y subespacio vectorial"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
Considera el conjunto

$$
W=\{(x,y,z)\in\mathbb R^3:xy=0\}.
$$

Geométricamente, $W$ es la unión de los planos coordenados $x=0$ e $y=0$.

Un estudiante debe determinar si $W$ es un subespacio vectorial de $\mathbb R^3$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"El vector nulo pertenece a $W$, porque $0\cdot 0=0$.",
    r"Si $u=(x_1,y_1,z_1)\in W$ y $\lambda\in\mathbb R$, entonces $(\lambda x_1)(\lambda y_1)=\lambda^2 x_1 y_1=0$. Por tanto, $\lambda u\in W$. El conjunto es cerrado bajo multiplicación por escalares.",
    r"Como contiene al vector nulo y es cerrado bajo multiplicación por escalares, concluyo que $W$ es un subespacio vectorial.",
]
PASO_ERRONEO = 3

EXPLICACION = r"""
El paso 3 omite una condición indispensable: el cierre bajo la suma de vectores.

Tomemos

$$
u=(1,0,0),\qquad v=(0,1,0).
$$

Ambos pertenecen a $W$, pero

$$
u+v=(1,1,0)\notin W,
$$

porque $1\cdot 1\neq 0$.

Por tanto, $W$ no es un subespacio vectorial.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="t   (Magnitud de los vectores)",
                      minimo=-2.0, maximo=2.0, valor=1.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    u, v, suma = (t, 0, 0), (0, t, 0), (t, t, 0)
    en_origen = abs(t) < 1e-9

    fig = escena_base(rango=3)
    
    # Plano x = 0
    agregar_plano(fig, normal=(1, 0, 0), d=0, nombre="plano x = 0",
                  color=COLORES["azul"], opacidad=0.2)
    # Plano y = 0
    agregar_plano(fig, normal=(0, 1, 0), d=0, nombre="plano y = 0",
                  color=COLORES["verde"], opacidad=0.2)
    
    if not en_origen:
        agregar_vector(fig, u, "u", COLORES["azul"])
        agregar_vector(fig, v, "v", COLORES["verde"])
        agregar_vector(fig, suma, "u+v", COLORES["rojo"])
        
        # Lineas punteadas para formar el paralelogramo
        agregar_segmento(fig, u, suma, color=COLORES["verde"])
        agregar_segmento(fig, v, suma, color=COLORES["azul"])

    if en_origen:
        mensaje = ("**t = 0:** Ambos vectores son nulos. El vector nulo pertenece a $W$.")
    else:
        mensaje = (f"**t = {t:.1f}:** $u=({t:.1f}, 0, 0)$ y $v=(0, {t:.1f}, 0)$ están en los planos que forman $W$. "
                   f"Su suma es $u+v=({t:.1f}, {t:.1f}, 0)$. Como $({t:.1f})({t:.1f}) = {t**2:.2f} \\neq 0$, "
                   "el vector **rojo sale de la unión de los planos** $W$.")
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
