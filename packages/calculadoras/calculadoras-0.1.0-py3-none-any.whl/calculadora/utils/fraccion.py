

def obtener_fracciones(frac_str):
    """Obtiene el valor de una fraccion."""
    if isinstance(frac_str, (int, float)):
        return frac_str

    if "/" in frac_str:
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    return float(frac_str)

def read_csv(path):
    """Lee un archivo csv."""
    print(path)
    return 0