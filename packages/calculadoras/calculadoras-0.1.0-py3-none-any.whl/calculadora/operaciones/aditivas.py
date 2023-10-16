"""Modulo de operaciones matematicas."""
from calculadora.utils.fraccion import obtener_fracciones

def suma(a, b):
    """Suma dos fracciones."""
    sumando_a = obtener_fracciones(a)
    sumando_b = obtener_fracciones(b)
    return sumando_a + sumando_b


def resta(a, b):
    """Resta dos fracciones."""
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo

