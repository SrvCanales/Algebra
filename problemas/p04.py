"""Problema 4 — Una transformación que parece conservar las dimensiones."""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 4
ETIQUETA = "Dependencia y dimensión"
TITULO = "Una transformación que parece conservar las dimensiones"
CONCEPTO = "dimensión y dependencia lineal"

# ── 2. ENUNCIADO ──────────────────────────────────────────────
ENUNCIADO = r"""
Para $a\in\mathbb R$, considera los vectores

$$v_1=(1,0,1),\quad v_2=(0,1,1),\quad v_3=(1,1,a).$$

Sea

$$W_a=\operatorname{span}\{v_1,v_2,v_3\}.$$

El estudiante debe determinar la dimensión de $W_a$ según el valor de $a$.
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Los vectores $v_1$ y $v_2$ son linealmente independientes para cualquier $a$, ya que sus coordenadas iniciales son diferentes.",
    r"El tercer vector tiene dos coordenadas iguales a 1, por lo que no puede ser combinación lineal de los dos anteriores.",
    r"En consecuencia, $\dim W_a=3$ para todo $a\in\mathbb R$.",
]
PASO_ERRONEO = 2

EXPLICACION = r"""
El paso 2 confunde la apariencia de las coordenadas con la independencia lineal. Para comprobar si $v_3$ es combinación de los otros vectores, debemos plantear

$$\alpha v_1+\beta v_2=v_3.$$

Comparando coordenadas,

$$\alpha=1,\quad \beta=1,\quad \alpha+\beta=a.$$

Las dos primeras ecuaciones obligan a que $\alpha+\beta=2$. Por tanto, si $a=2$,

$$v_3=v_1+v_2,$$

y los tres vectores son linealmente dependientes.

En conclusión,

$$\dim W_a= \begin{cases} 2, & a=2,\\ 3, & a\ne2. \end{cases}$$
"""

# ── 4. PARÁMETRO ──────────────────────────────────────────────
PARAMETRO = Parametro(etiqueta="a   (Parámetro del vector v₃)",
                      minimo=0.0, maximo=4.0, valor=2.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
def figura(t):
    v1 = np.array([1, 0, 1])
    v2 = np.array([0, 1, 1])
    v3 = np.array([1, 1, t])
