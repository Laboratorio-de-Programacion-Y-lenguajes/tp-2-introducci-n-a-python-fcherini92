# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica una función a cada elemento de una lista y retorna una nueva lista.

    Args:
        lista: La lista original con los datos a procesar.
        func: La función (o lambda) que se aplicará a cada elemento.

    Returns:
        list: Una nueva lista con los resultados de aplicar la función.
    """
    # Creamos la nueva lista transformando cada elemento en una sola línea.
    return [func(elemento) for elemento in lista]
    pass


def componer(f, g):
    """
    Crea una nueva función que representa la composición f(g(x)).

    Args:
        f: Función externa que recibirá el resultado de g.
        g: Función interna que se aplicará primero al argumento.

    Returns:
        function: Una nueva función que aplica g y luego f.
    """
    def funcion_compuesta(x):
        # Primero se evalúa g(x), y ese resultado pasa a f()
        return f(g(x))
    
    return funcion_compuesta
    pass


def memoizar(func):
    """
    Retorna una versión de la función que almacena sus resultados en cache.
    
    Args:
        func: La función que queremos optimizar.
        
    Returns:
        function: Una envoltura que gestiona el acceso al cache.
    """
    cache = {}

    def envoltura(*args):
        # Usamos la tupla de argumentos como clave del diccionario
        if args not in cache:
            # Si no está en el cache, ejecutamos y guardamos
            cache[args] = func(*args)
        
        return cache[args]

    return envoltura
    pass


def reducir(lista: list, func, inicial):
    """
    Aplica una función acumulativa a los elementos de una lista, 
    de izquierda a derecha, comenzando con un valor inicial.

    Args:
        lista: La secuencia de elementos a procesar.
        func: Función que recibe (acumulador, elemento_actual) y retorna el nuevo acumulador.
        inicial: El valor de partida para la acumulación.

    Returns:
        El resultado final tras procesar toda la lista.
    """
    acumulador = inicial
    
    for elemento in lista:
        # El resultado de cada operación se convierte en el nuevo punto de partida
        acumulador = func(acumulador, elemento)
        
    return acumulador
    pass
