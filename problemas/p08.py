"""Problema 8 — Un conjunto cerrado bajo suma que no es un subespacio."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 8
ETIQUETA = "Rectas y subespacios"
TITULO = "Un conjunto cerrado bajo suma que no es un subespacio"
CONCEPTO = "cierre bajo suma y producto por escalares"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
Considera el conjunto

$$
S=\{(x,y)\in\mathbb R^2:x+y=1\}.
$$

Es una recta que no pasa por el origen. Un estudiante debe decidir si es un subespacio vectorial de $\mathbb R^2$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Si $(x_1,y_1)$ y $(x_2,y_2)$ pertenecen a $S$, entonces $x_1+y_1=1,\quad x_2+y_2=1$.",
    r"Al sumar los vectores, $(x_1+x_2)+(y_1+y_2)=2$. La suma conserva una relación lineal entre sus coordenadas, así que el conjunto es cerrado bajo suma.",
    r"Además, $S$ es una recta, por lo que es un subespacio de $\mathbb R^2$.",
]
PASO_ERRONEO = 2

EXPLICACION = r"""
El paso 2 confunde satisfacer alguna relación lineal con satisfacer la ecuación que define el conjunto. La suma de dos elementos de $S$ cumple $x+y=2$, no $x+y=1$, por lo que no pertenece a $S$.

También puede detectarse el error observando que

$$
(0,0)\notin S,
$$

porque $0+0\neq 1$.

En consecuencia, $S$ no es un subespacio vectorial.
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="c   (Desplazamiento de la recta x+y=c)",
                      minimo=-3.0, maximo=3.0, valor=1.0, paso=0.5)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    c = t
    # Elegimos dos puntos en la recta x + y = c para trazar los vectores
    # Usamos p = (c+1, -1) y q = (-1, c+1) para que sean distintos incluso si c=0
    p = np.array([c + 1.0, -1.0, 0.0])
    q = np.array([-1.0, c + 1.0, 0.0])
    suma = p + q

    en_origen = abs(c) < 1e-9

    fig = escena_base(rango=5)
    
    # Origen como referencia
    agregar_punto(fig, (0, 0, 0), "Origen", color=COLORES["ambar"], tamano=5)
    
    # Recta x + y = c en el plano z=0 (dibujada usando un segmento largo)
    agregar_segmento(fig, (-5.0, c + 5.0, 0.0), (5.0, c - 5.0, 0.0), 
                     color=COLORES["azul"], dash="solid", nombre=f"Recta x+y={c:.1f}")
                     
    # Vectores p y q (pertenecientes a la recta)
    agregar_vector(fig, p, "p", COLORES["verde"])
    agregar_vector(fig, q, "q", COLORES["verde"])
    
    # Vector suma
    agregar_vector(fig, suma, "p+q", COLORES["rojo"])
    
    # Paralelogramo de la suma
    agregar_segmento(fig, p, suma, color=COLORES["gris"], dash="dash")
    agregar_segmento(fig, q, suma, color=COLORES["gris"], dash="dash")
    
    if en_origen:
        mensaje = (f"**c = 0.0:** Ecuación de la recta: $x+y=0.0$.\n\n"
                   f"La suma de los puntos satisface $x+y = 0.0$. "
                   f"El conjunto contiene al origen, es cerrado bajo la suma y **sí es un subespacio**.")
    else:
        mensaje = (f"**c = {c:.1f}:** Ecuación de la recta: $x+y={c:.1f}$.\n\n"
                   f"Los vectores $p$ y $q$ terminan en la recta azul. Sin embargo, su suma $p+q$ "
                   f"cumple $x+y = {2*c:.1f}$, por lo que el vector rojo sale de la recta.\n\n"
                   f"**No es un subespacio**: no contiene al origen y no es cerrado bajo suma.")
                   
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
