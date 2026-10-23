"""Problema 1 — Un conjunto que no genera R^3 y no es base."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 1
ETIQUETA = "Generador vs. base"
TITULO = "Un conjunto que genera todo el espacio, pero no es una base"
CONCEPTO = "conjunto generador, base y dependencia lineal"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
Sea $V=\mathbb R^3$ y considera el conjunto $S=\{v_1,v_2,v_3,v_4\}$, donde

$$
v_1=(1,0,1),\quad v_2=(0,1,1),\quad v_3=(1,1,2),\quad v_4=(1,-1,0).
$$

Un estudiante debe determinar si $S$ es una base de $\mathbb R^3$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Los vectores $v_1$ y $v_2$ son linealmente independientes, pues ninguno es múltiplo del otro.",
    r"Además, $v_3=v_1+v_2$, por lo que el conjunto contiene vectores redundantes. Sin embargo, $v_4$ no es múltiplo de $v_1$ ni de $v_2$, así que introduce una nueva dirección.",
    r"Por tanto, el conjunto genera tres direcciones independientes. Como genera $\mathbb R^3$, concluyo que $S$ es una base de $\mathbb R^3$.",
]
PASO_ERRONEO = 3

EXPLICACION = r"""
El error está en el paso 3. Que un conjunto genere $\mathbb R^3$ no significa que sea linealmente independiente.

En efecto,

$$
v_3=v_1+v_2,\qquad v_4=v_1-v_2.
$$

Por tanto, los cuatro vectores pertenecen al subespacio generado por $v_1,v_2$, que tiene dimensión 2. El conjunto no genera $\mathbb R^3$, y mucho menos puede ser una base.

Una base posible del subespacio generado es $\{v_1,v_2\}$.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="t   (v₄ = (1, −1, t))",
                      minimo=-2.0, maximo=2.0, valor=0.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    v1, v2, v3, v4 = (1, 0, 1), (0, 1, 1), (1, 1, 2), (1, -1, t)
    en_plano = abs(t) < 1e-9

    fig = escena_base(rango=3)
    agregar_plano(fig, normal=(1, 1, -1), d=0, nombre="plano z = x + y",
                  color=COLORES["ambar"] if en_plano else COLORES["gris"],
                  opacidad=0.45 if en_plano else 0.18)
    agregar_vector(fig, v1, "v₁", COLORES["azul"])
    agregar_vector(fig, v2, "v₂", COLORES["verde"])
    agregar_vector(fig, v3, "v₃", COLORES["violeta"])
    agregar_vector(fig, v4, "v₄", COLORES["rojo"])
    if not en_plano:
        agregar_segmento(fig, v4, (1, -1, 0), color=COLORES["rojo"])

    rango = np.linalg.matrix_rank(np.array([v1, v2, v3, v4], float))
    if en_plano:
        mensaje = (f"**t = 0:** $v_4=(1,-1,0)$ está sobre el plano $z=x+y$. "
                   f"Los cuatro vectores generan sólo un plano (rango {rango}).")
    else:
        mensaje = (f"**t = {t:.1f}:** $v_4$ queda a {abs(t):.1f} unidades (en $z$) del plano. "
                   f"Ahora el conjunto genera $\\mathbb R^3$ (rango {rango}), "
                   f"pero con 4 vectores en $\\mathbb R^3$ sigue siendo dependiente.")
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
