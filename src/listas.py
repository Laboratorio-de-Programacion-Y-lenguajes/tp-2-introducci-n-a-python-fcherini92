# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Calcula la suma total de los elementos de una lista.
    
    Args:
        numeros (list): Una lista de números (int o float).
        
    Returns:
        int | float: La suma de los elementos. Retorna 0 si la lista está vacía.
        
    Example:
        >>> suma_lista([1, 2, 3.5])
        6.5
        >>> suma_lista([])
        0
    """
    # 1. Inicialización del acumulador
    # Usamos 0 como elemento neutro de la suma
    total = 0
    
    # 2. Iteración sobre la lista
    for numero in numeros:
        total += numero
        
    # 3. Retorno del resultado final
    return total
    pass


def filtrar_pares(numeros: list) -> list:
    """
    Filtra una lista de números y devuelve una nueva lista solo con los pares.
    
    Un número se considera par si el resto de su división por 2 es 0. 
    Esto incluye al 0 y a los números negativos pares.
    
    Args:
        numeros (list): Una lista de números enteros (int).
        
    Returns:
        list: Una nueva lista que contiene solo los números pares encontrados.
              Si no hay pares o la lista está vacía, devuelve [].
              
    Example:
        >>> filtrar_pares([1, 2, 3, 4])
        [2, 4]
        >>> filtrar_pares([-2, 0, 7])
        [-2, 0]
    """
    # 1. Inicialización de la nueva lista (contenedor)
    solo_pares = []
    
    # 2. Recorrido de la lista original
    for numero in numeros:
        # 3. Verificación de la condición de paridad
        # Matemáticamente: numero % 2 == 0
        if numero % 2 == 0:
            solo_pares.append(numero)
            
    # 4. Retorno del resultado filtrado
    return solo_pares
    pass


def invertir_lista(lista: list) -> list:
    """
    Crea una nueva lista con los elementos de la lista original en orden inverso.
    
    Esta función utiliza 'slicing' con un paso de -1, lo que garantiza que 
    se devuelva un nuevo objeto sin modificar la entrada original.
    
    Args:
        lista (list): La lista de elementos a invertir.
        
    Returns:
        list: Una nueva lista con el orden de los elementos espejado.
              Retorna una lista vacía si la entrada es [].
              
    Example:
        >>> invertir_lista([1, 2, 3])
        [3, 2, 1]
    """
    # El slicing [start:stop:step] con step -1 recorre la lista 
    # de derecha a izquierda hasta el final.
    return lista[::-1]
    pass


def eliminar_duplicados(lista: list) -> list:
    """
    Genera una nueva lista eliminando los elementos duplicados de la original.
    
    Mantiene el orden de la primera aparición de cada elemento mediante el uso
    de un conjunto auxiliar para optimizar la búsqueda de pertenencia.
    
    Args:
        lista (list): La lista original que puede contener duplicados.
        
    Returns:
        list: Una nueva lista con elementos únicos en su orden de aparición.
              Si la entrada es [], retorna [].
              
    Example:
        >>> eliminar_duplicados([1, 2, 2, 3, 1])
        [1, 2, 3]
    """
    # 1. 'vistos' es un set para que la búsqueda sea O(1)
    vistos = set()
    # 2. 'resultado' mantendrá el orden de inserción
    resultado = []
    
    for elemento in lista:
        # 3. Solo agregamos si no lo hemos procesado antes
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)  # Marcamos como visto
            
    return resultado
    pass


def aplanar_lista(lista: list) -> list:
    """
    Transforma una lista de listas en una única lista plana.
    
    Recorre cada sublista y extrae sus elementos individuales para 
    agruparlos en una nueva estructura lineal.
    
    Args:
        lista_de_listas (list): Una lista que contiene otras listas.
        
    Returns:
        list: Una nueva lista con todos los elementos de las sublistas.
              Si la entrada es [] o [[]], devuelve [].
              
    Example:
        >>> aplanar_lista([[1, 2], [3, 4]])
        [1, 2, 3, 4]
    """
    # 1. Creamos el contenedor para la nueva lista plana
    lista_plana = []
    
    # 2. Primer nivel: Iteramos sobre la lista principal (obtenemos cada sublista)
    for sublista in lista:
        # 3. Segundo nivel: Iteramos sobre cada elemento dentro de la sublista
        for elemento in sublista:
            # 4. Agregamos el elemento individual al resultado final
            lista_plana.append(elemento)
            
    return lista_plana
    pass
