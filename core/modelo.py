"""Estructuras de datos. No necesitas tocar este archivo."""
from dataclasses import dataclass
from typing import Callable


@dataclass
class Parametro:
    etiqueta: str      # texto junto al deslizador, p. ej. "t"
    minimo: float
    maximo: float
    valor: float       # valor inicial
    paso: float = 0.1


@dataclass
class Problema:
    numero: int
    etiqueta: str          # nombre corto para la lista de la izquierda
    titulo: str
    concepto: str
    enunciado: str         # Markdown + LaTeX ($...$ y $$...$$)
    pasos: list            # lista de textos (Markdown + LaTeX)
    paso_erroneo: int      # número del paso errado (empieza en 1)
    explicacion: str       # texto de "¿Dónde está el error?"
    parametro: Parametro
    figura: Callable       # figura(t) -> (plotly Figure, mensaje_markdown)

    @property
    def pendiente(self) -> bool:
        return not self.enunciado.strip()
