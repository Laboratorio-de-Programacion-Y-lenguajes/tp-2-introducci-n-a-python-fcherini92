# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    """
    Genera un string de saludo personalizado.

        Args:
            nombre (str): El nombre de la persona a saludar.

        Returns:
            str: El saludo formateado con 'Hola, {nombre}!'.
    """
    return f"Hola, {nombre}!"
    pass


def suma_enteros(a: int, b: int) -> int:
    """
    Convierte los argumentos a enteros, los suma y devuelve el resultado.

    Args:
        a (int | str | float): El primer valor a convertir y sumar.
        b (int | str | float): El segundo valor a convertir y sumar.

    Returns:
        int: La suma de los valores transformados a entero.
    """
    # Forzamos la conversión interna
    num1 = int(a)
    num2 = int(b)
    
    return num1 + num2
    pass


def es_mayor_de_edad(edad: int) -> bool:
    """
    Verifica si una persona tiene 18 años o más.

    Args:
        edad (int): La edad a evaluar.

    Returns:
        bool: True si edad >= 18, False en caso contrario.
    """
    # Retornamos directamente el resultado de la evaluación lógica
    return edad >= 18
    pass


def tipo_de_dato(valor) -> str:
    """
    Identifica la clase del valor ingresado y devuelve su nombre como string.

    Args:
        valor (any): Cualquier objeto de Python (int, float, str, list, etc.).

    Returns:
        str: El nombre del tipo de dato.
    """
    # type(valor) obtiene la clase, .__name__ obtiene el nombre de esa clase
    return type(valor).__name__
    pass


def convertir_a_float(valor: str) -> float:
    """
    Limpia comas en un string y lo convierte a un número de punto flotante.

    Args:
        valor (str): El string numérico (puede contener ',' o '.').

    Returns:
        float: El valor convertido a float.
    """
    # 1. Reemplazamos la coma por el punto
    # Si el string no tiene comas, .replace() simplemente no hace nada.
    valor_preparado = valor.replace(",", ".")
    
    # 2. Convertimos el string resultante a float
    return float(valor_preparado)
    pass
