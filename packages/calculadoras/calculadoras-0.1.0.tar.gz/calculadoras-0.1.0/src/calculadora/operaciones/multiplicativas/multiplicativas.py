from calculadora.utils.fraccion import obtener_fracciones


def multiplica(a, b):
    """Multiplica dos fracciones."""
    multiplicando = obtener_fracciones(a)
    multiplicador = obtener_fracciones(b)
    return multiplicando * multiplicador


def division(a, b):
    """Divide dos fracciones."""
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"
