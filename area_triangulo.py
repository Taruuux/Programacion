import math

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dados base y altura.

    Parámetros:
        base (float): longitud de la base
        altura (float): longitud de la altura

    Retorna:
        float: área del triángulo

    Excepciones:
        TypeError: si base o altura no son numéricos
        ValueError: si base o altura no son <= 0 o no son finitos
    """
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Base y altura deben ser numéricos")

    if not math.isfinite(base) or not math.isfinite(altura):
        raise ValueError("Base y altura deben ser números finitos")

    if base <= 0 or altura <= 0:
        raise ValueError("Base y altura deben ser mayores que cero")

    return (base * altura) / 2
