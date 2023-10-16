"""Calculadora de operaciones básicas."""
import pandas as pd
import calculadora.operaciones as op

from calculadora.utils.fraccion import *

def main():

    res_divide = op.division(10, 2)
    print(f"Resultado Division: {res_divide}")

    res_multiplica = op.multiplica(10, 2)
    print(f"Resultado Multiplicacion: {res_multiplica}")

    res_suma = op.suma(10, 2)
    print(f"Resultado Suma: {res_suma}")


if __name__ == "__main__":
    main()