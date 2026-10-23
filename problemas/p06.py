"""Problema 6 — Un complemento ortogonal que contiene vectores que no son ortogonales."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 6
ETIQUETA = "Complemento ortogonal"
TITULO = "Un complemento ortogonal que contiene vectores que no son ortogonales"
CONCEPTO = "complemento ortogonal"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
En $\mathbb R^3$, sea

$$
U=\operatorname{span}\{(1,1,0)\}.
$$

Se pide determinar $U^\perp$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Un vector $w=(x,y,z)$ pertenece a $U^\perp$ si es perpendicular al generador de $U$.",
    r"Como el generador tiene tercera coordenada cero, la coordenada $z$ de $w$ no influye en la ortogonalidad. Por tanto, basta imponer $x=0$.",
    r"Así, $U^\perp=\{(0,y,z):y,z\in\mathbb R\}$.",
]
PASO_ERRONEO = 2

EXPLICACION = r"""
El paso 2 interpreta incorrectamente el producto interior. La condición de ortogonalidad es

$$
(x,y,z)\cdot(1,1,0)=x+y=0,
$$

no $x=0$.

Por tanto,

$$
U^\perp=\{(x,y,z):x+y=0\}
$$

y una base posible es

$$
\boxed{\{(1,-1,0),(0,0,1)\}}.
$$

El conjunto propuesto por el estudiante contiene, por ejemplo, $(0,1,0)$, cuyo producto interior con $(1,1,0)$ es 1. Ese vector no es ortogonal a $U$.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="a   (Segunda coordenada del vector u_a)",
                      minimo=-2.0, maximo=2.0, valor=1.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    ua = np.array([1.0, t, 0.0])
    
    fig = escena_base(rango=3)
    
    # Plano perpendicular al vector ua (complemento ortogonal)
    agregar_plano(fig, normal=ua, d=0, nombre="Plano U^⟂",
                  color=COLORES["azul"], opacidad=0.3)
    
    # Vector original ua
    agregar_vector(fig, ua, "u_a", COLORES["rojo"])
    
    # Dos vectores contenidos en el plano U^perp como referencia
    v1 = np.array([-t, 1.0, 0.0])
    v2 = np.array([0.0, 0.0, 1.5])
    
    agregar_vector(fig, v1, "v_1 (en U^⟂)", COLORES["verde"])
    agregar_vector(fig, v2, "v_2 (en U^⟂)", COLORES["verde"])
    
    mensaje = (f"**a = {t:.1f}:** Vector: $u_a=(1, {t:.1f}, 0)$.\n\n"
               f"Condición de ortogonalidad: $x + ({t:.1f})y = 0$.\n\n"
               f"El complemento ortogonal es el plano $x + ({t:.1f})y = 0$, "
               f"perpendicular a $u_a=(1, {t:.1f}, 0)$.")
                   
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
