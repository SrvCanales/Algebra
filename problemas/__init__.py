"""Carga p01.py ... p08.py en orden. No necesitas tocar este archivo."""
import importlib

TOTAL = 8


def cargar():
    return [importlib.import_module(f"problemas.p{i:02d}").PROBLEMA
            for i in range(1, TOTAL + 1)]
