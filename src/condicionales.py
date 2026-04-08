# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Evalúa la polaridad de un número entero.

    Args:
        n (int): El número entero a clasificar.

    Returns:
        str: "Positivo" si el número es mayor a cero, 
             "Negativo" si es menor a cero, 
             o "Cero" si el valor es exactamente cero.
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"
    pass


def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Determina el mayor de tres números enteros.

    En caso de empate en el valor máximo, se retorna el primero de ellos 
    según el orden de los parámetros (a > b > c).

    Args:
        a (int): Primer número a comparar.
        b (int): Segundo número a comparar.
        c (int): Tercer número a comparar.

    Returns:
        int: El valor del número más grande entre los tres suministrados.
    """
    if a >= b and a >= c:
        return a
    elif b >= c:
        # Si llegamos acá, sabemos que b > a, por lo que comparamos b con c
        return b
    else:
        # Si no es a ni b, el mayor es c
        return c
    pass


def clasificar_nota(nota: float) -> str:
    """
    Clasifica una nota numérica en una categoría descriptiva.

    Args:
        nota (float): El valor numérico de la calificación.

    Returns:
        str: La categoría correspondiente ("Sobresaliente", "Bueno", 
             "Aprobado", "Desaprobado") o "Nota inválida" si es negativa.
    """
    # 1. Validación de rango (Regla 2)
    if nota < 0:
        return "Nota inválida"
    
    # 2. Clasificación por rangos (Regla 1 y 3)
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"
    pass


def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto según el calendario gregoriano.

    Un año es bisiesto si es divisible por 4, pero no por 100, 
    a menos que también sea divisible por 400.

    Args:
        anio (int): El año que se desea evaluar.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    pass
