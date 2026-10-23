"""Problema 3 — Dos subespacios con intersección trivial cuya suma no es directa."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 3
ETIQUETA = "Suma e intersección"
TITULO = "Dos subespacios con intersección trivial cuya suma no es directa"
CONCEPTO = "suma e intersección de subespacios"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
Sean los subespacios de $\mathbb R^3$

$$
U=\operatorname{span}\{(1,0,0),(0,1,0)\}
$$

y

$$
V=\operatorname{span}\{(1,0,0),(0,0,1)\}.
$$

Un estudiante debe calcular $U\cap V$, $U+V$ y decidir si la suma es directa.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Ambos subespacios son planos distintos de $\mathbb R^3$. Por ello, su intersección solo puede ser el vector nulo: $U\cap V=\{0\}$.",
    r"La suma tiene dimensión $\dim(U+V)=\dim(U)+\dim(V)=2+2=4$.",
    r"Como la intersección es trivial, la suma es directa: $U+V=U\oplus V$.",
]
PASO_ERRONEO = 1

EXPLICACION = r"""
El primer paso es incorrecto. Dos planos distintos que pasan por el origen pueden compartir una recta.

En este caso, ambos contienen el eje $x$, así que

$$
U\cap V=\operatorname{span}\{(1,0,0)\}.
$$

La fórmula correcta es

$$
\dim(U+V)=\dim(U)+\dim(V)-\dim(U\cap V)=2+2-1=3.
$$

Por consiguiente, 

$$
U+V=\mathbb R^3.
$$

La suma no es directa, porque $U\cap V\neq\{0\}$.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="θ (Rotación del plano V, en grados)",
                      minimo=0.0, maximo=180.0, valor=90.0, paso=1.0)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    fig = escena_base(rango=3)
    
    rad = np.radians(t)
    coinciden = (abs(t) < 1e-9) or (abs(t - 180.0) < 1e-9)
    
    # El plano U es el plano xy (z=0)
    agregar_plano(fig, normal=(0, 0, 1), d=0, nombre="Plano U",
                  color=COLORES["azul"], opacidad=0.3)
    
    # El plano V rotado (cuando t=90, es el plano xz, normal en y)
    normal_v = (0, -np.sin(rad), np.cos(rad))
    agregar_plano(fig, normal=normal_v, d=0, nombre="Plano V",
                  color=COLORES["rojo"], opacidad=0.3)
    
    # Eje x (intersección)
    agregar_segmento(fig, (-3, 0, 0), (3, 0, 0), color=COLORES["ambar"], dash="solid", nombre="Intersección (eje x)")
    
    # Vectores base del eje x (compartido)
    agregar_vector(fig, (1, 0, 0), "e1", COLORES["ambar"])
    
    if coinciden:
        mensaje = (f"**θ = {t:.0f}°:** Los planos coinciden. "
                   f"$\\dim(U\\cap V)=2$ y $\\dim(U+V)=2$. La suma no es directa.")
    else:
        mensaje = (f"**θ = {t:.0f}°:** Los planos son distintos. "
                   f"Comparten la recta del eje $x$ ($\\dim(U\\cap V)=1$). "
                   f"La suma tiene dimensión $\\dim(U+V) = 2+2-1 = 3$. "
                   f"Como la intersección no es $\\{{0\\}}$, la suma no es directa.")
                   
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
