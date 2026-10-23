"""Problema 7 — Una base de un subespacio que deja de serlo al cambiar un parámetro."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 7
ETIQUETA = "Base y dimensión"
TITULO = "Una base de un subespacio que deja de serlo al cambiar un parámetro"
CONCEPTO = "base y dimensión"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
Sea

$$
U_a=\operatorname{span}\{(1,0,0),(1,a,0)\}.
$$

Un estudiante debe determinar para qué valores de $a$ los dos generadores forman una base de $U_a$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Los dos vectores son diferentes para todo $a$, pues el primero tiene segunda coordenada cero y el segundo se presenta como un vector distinto.",
    r"Al haber dos vectores distintos, el conjunto es linealmente independiente.",
    r"Por tanto, los dos vectores forman una base de $U_a$ para cualquier $a\in\mathbb R$.",
]
PASO_ERRONEO = 2

EXPLICACION = r"""
El paso 2 es falso: dos vectores distintos pueden ser linealmente dependientes si uno es múltiplo del otro.

Cuando $a=0$,

$$
(1,a,0)=(1,0,0),
$$

de modo que ambos vectores coinciden. Entonces

$$
U_0=\operatorname{span}\{(1,0,0)\},
$$

que tiene dimensión 1, y el conjunto de dos generadores no es una base.

En cambio, si $a\neq 0$, los vectores son linealmente independientes y generan el plano $z=0$. En ese caso sí forman una base de $U_a$.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="a   (Parámetro del segundo vector)",
                      minimo=-2.0, maximo=2.0, valor=1.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([1.0, t, 0.0])
    v_suma = v1 + v2
    
    area = abs(t)
    en_recta = area < 1e-9

    fig = escena_base(rango=3)
    
    # Plano xy (z=0)
    agregar_plano(fig, normal=(0, 0, 1), d=0, nombre="Plano xy",
                  color=COLORES["gris"], opacidad=0.2)
    
    # Vectores
    agregar_vector(fig, v1, "v₁", COLORES["azul"])
    
    # Si coinciden, movemos ligeramente la etiqueta o el color para que se note
    if en_recta:
        agregar_vector(fig, v2, "v₂ (coincide con v₁)", COLORES["ambar"])
    else:
        agregar_vector(fig, v2, "v₂", COLORES["verde"])
        # Dibujar paralelogramo
        agregar_segmento(fig, v1, v_suma, color=COLORES["gris"], dash="dash")
        agregar_segmento(fig, v2, v_suma, color=COLORES["gris"], dash="dash")

    if en_recta:
        mensaje = (f"**a = 0:** Área del paralelogramo: $|a| = 0$. "
                   "Los vectores coinciden ($v_1 = v_2 = (1,0,0)$) y son dependientes. "
                   "Generan una recta (dimensión 1), por lo que **no forman una base** del plano.")
    else:
        mensaje = (f"**a = {t:.1f}:** Área del paralelogramo: $|a| = {area:.1f}$. "
                   "Los vectores son linealmente independientes y generan el plano $xy$ "
                   "(dimensión 2). Forman una base de $U_a$.")
                   
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
