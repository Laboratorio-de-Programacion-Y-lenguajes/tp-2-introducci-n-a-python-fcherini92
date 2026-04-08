# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Cuenta la frecuencia de cada palabra en un texto dado.
    
    Convierte el texto a minúsculas y elimina signos de puntuación básicos
    para asegurar que la comparación sea justa.
    
    Args:
        texto (str): La cadena de texto a procesar.
        
    Returns:
        dict: Un diccionario donde las llaves son palabras y los valores 
              son la cantidad de apariciones.
    """
    # 1. Limpieza básica y conversión a minúsculas
    # Reemplazamos comas y puntos por nada para que "mundo," sea "mundo"
    caracteres_a_limpiar = ",.;:¡!¿?"
    texto_limpio = texto.lower()
    for caracter in caracteres_a_limpiar:
        texto_limpio = texto_limpio.replace(caracter, "")
        
    # 2. Dividir el texto en una lista de palabras
    palabras = texto_limpio.split()
    
    # 3. Crear el diccionario de frecuencias
    frecuencias = {}
    
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
            
    return frecuencias
    pass


def invertir_diccionario(d: dict) -> dict:
    """
    Intercambia las claves y los valores de un diccionario.
    
    Toma cada par clave-valor del diccionario de entrada y retorna
    un nuevo diccionario donde los valores son las claves y las 
    claves son los valores.
    
    Nota: Si hay valores duplicados en el original, solo se 
    mantendrá el último par procesado en el resultado final.
    
    Args:
        d (dict): El diccionario que se desea invertir.
        
    Returns:
        dict: Un nuevo diccionario con las posiciones intercambiadas.
    """
    # Usamos dict comprehension para una sintaxis limpia y eficiente
    return {valor: clave for clave, valor in d.items()}
    pass


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios en uno nuevo.
    
    Si ambos diccionarios comparten la misma clave, el valor del 
    segundo diccionario (d2) prevalecerá sobre el primero (d1).
    
    Args:
        d1 (dict): El primer diccionario (base).
        d2 (dict): El segundo diccionario (sobrescribe al primero).
        
    Returns:
        dict: Un nuevo diccionario que contiene la unión de ambos.
    """
    # Creamos una copia de d1 para no modificar el original (buena práctica)
    resultado = d1.copy()
    
    # El método update() añade los elementos de d2 a resultado.
    # Si una clave ya existe, la actualiza con el valor de d2.
    resultado.update(d2)
    
    return resultado
    pass


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Filtra un diccionario conservando solo los pares cuyos valores 
    sean mayores o iguales a un valor mínimo.
    
    Args:
        d (dict): El diccionario original con valores numéricos.
        minimo (int): El valor umbral para el filtrado.
        
    Returns:
        dict: Un nuevo diccionario que contiene únicamente los elementos 
              que cumplen la condición valor >= minimo.
    """
    # Utilizamos dict comprehension para iterar y filtrar en una sola línea
    return {clave: valor for clave, valor in d.items() if valor >= minimo}
    pass
