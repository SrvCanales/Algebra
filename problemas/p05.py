"""
PLANTILLA DE PROBLEMA
=====================
Para agregar un problema: abre pNN.py (ya existe, vacío) y completa las
5 secciones de arriba hacia abajo. No toques nada más.
Mientras ENUNCIADO esté vacío, la app muestra "pendiente".
Texto: Markdown con LaTeX ($...$ en línea, $$...$$ en bloque).
Usa r-strings (r'''...''') para que las barras invertidas de LaTeX no den problemas.
"""
import numpy as np
from core.modelo import Problema, Parametro
from core.escena3d import (escena_base, agregar_vector, agregar_plano,
                           agregar_punto, agregar_segmento, COLORES)

# ── 1. ENCABEZADO ─────────────────────────────────────────────
NUMERO = 5
ETIQUETA = ""      # nombre corto para la lista izquierda
TITULO = ""
CONCEPTO = ""

# ── 2. ENUNCIADO (vacío = problema pendiente) ─────────────────
ENUNCIADO = r"""
"""

# ── 3. DESARROLLO ERRADO ──────────────────────────────────────
PASOS = [
    r"Texto del paso 1.",
    r"Texto del paso 2.",
    r"Texto del paso 3.",
]
PASO_ERRONEO = 3   # número del paso errado (1 = primer paso)

EXPLICACION = r"""
Explica aquí dónde está el error y por qué.
"""

# ── 4. PARÁMETRO MANUAL (deslizador) ──────────────────────────
PARAMETRO = Parametro(etiqueta="t", minimo=-2.0, maximo=2.0, valor=0.0, paso=0.1)


# ── 5. FIGURA 3D ──────────────────────────────────────────────
# Recibe el valor t del deslizador. Devuelve (figura, mensaje).
# Funciones: agregar_vector, agregar_plano, agregar_punto, agregar_segmento.
def figura(t):
    fig = escena_base(rango=3)
    agregar_vector(fig, (1, 0, 1), "v₁", COLORES["azul"])
    agregar_vector(fig, (0, 1, t), "v₂", COLORES["verde"])
    mensaje = f"**t = {t:.1f}**"
    return fig, mensaje


# ── No tocar ──────────────────────────────────────────────────
PROBLEMA = Problema(NUMERO, ETIQUETA, TITULO, CONCEPTO, ENUNCIADO, PASOS,
                    PASO_ERRONEO, EXPLICACION, PARAMETRO, figura)
