# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Genera una lista con números enteros desde 1 hasta n inclusive.
    
    Si n es menor a 1, retorna una lista vacía conforme al
    comportamiento estándar de los rangos en Python.
    
    Args:
        n (int): El número límite superior.
        
    Returns:
        list: Una lista de enteros del 1 al n.
    """
    # range(inicio, fin_exclusivo)
    # Si n < 1, range(1, n+1) genera una secuencia vacía automáticamente.
    return list(range(1, n + 1))
    pass


def tabla_multiplicar(n: int) -> list:
    """
    Calcula los primeros 10 múltiplos de un número entero n.
    
    Args:
        n (int): El número base para la tabla de multiplicar.
        
    Returns:
        list[int]: Una lista con los resultados de n * 1 hasta n * 10.
    """
    # Usamos una lista por comprensión para multiplicar n por cada 
    # número en el rango del 1 al 10 (el 11 es exclusivo).
    return [n * i for i in range(1, 11)]
    pass


def suma_digitos(n: int) -> int:
    """
    Calcula la suma de todos los dígitos de un número entero n.
    Toma el valor absoluto de n para manejar números negativos.
    
    Args:
        n (int): El número entero a procesar.
        
    Returns:
        int: La suma de sus dígitos individuales.
    """
    # Convertimos a positivo para no sumar el guion "-" si fuera negativo
    n_positivo = abs(n)
    
    # Explicación del truco:
    # 1. str(n_positivo) convierte el número a "123"
    # 2. for d in ... recorre cada carácter '1', '2', '3'
    # 3. int(d) los convierte de nuevo a enteros
    # 4. sum(...) suma todos esos enteros
    return sum(int(d) for d in str(n_positivo))
    pass


def es_primo(n: int) -> bool:
    """
    Determina si un número entero n es primo.
    
    Un número primo es un número natural mayor que 1 que tiene 
    únicamente dos divisores distintos: él mismo y el 1.
    
    Args:
        n (int): El número a verificar.
        
    Returns:
        bool: True si es primo, False en caso contrario.
    """
    # Los números menores o iguales a 1 no son primos
    if n <= 1:
        return False
    
    # El 2 es el único primo par
    if n == 2:
        return True
    
    # Si es par y mayor a 2, no es primo
    if n % 2 == 0:
        return False
    
    # Comprobamos divisores impares desde 3 hasta la raíz cuadrada de n
    # Usamos int(n**0.5) + 1 para que el rango sea inclusivo
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    return True
    pass


def fibonacci(n: int) -> list:
    """
    Genera una lista con los primeros n números de la secuencia de Fibonacci.
    
    La secuencia comienza con 0 y 1. Cada número subsiguiente es la suma 
    de los dos anteriores.
    
    Args:
        n (int): Cantidad de números de la secuencia a generar.
        
    Returns:
        list[int]: Lista conteniendo los n primeros números de Fibonacci.
    """
    if n <= 0:
        return []
    
    resultado = []
    a, b = 0, 1
    
    for _ in range(n):
        resultado.append(a)
        # Actualizamos: 'a' toma el valor de 'b', 
        # y 'b' toma la suma de los dos anteriores.
        a, b = b, a + b
        
    return resultado
    pass
