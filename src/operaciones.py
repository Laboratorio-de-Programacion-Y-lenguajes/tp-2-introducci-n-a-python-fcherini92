# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Verifica si un texto es un palíndromo, ignorando espacios y mayúsculas.

    Un palíndromo es una palabra o frase que se lee igual de izquierda 
    a derecha que de derecha a izquierda.

    Argumentos:
        texto (str): La cadena de caracteres a evaluar.

    Retorna:
        bool: True si es palíndromo, False en caso contrario.
    """
    # 1. Limpieza: Pasamos a minúsculas y eliminamos espacios en blanco
    texto_limpio = texto.lower().replace(" ", "")
    
    # 2. Comparación: Usamos slicing para invertir el string
    return texto_limpio == texto_limpio[::-1]
    pass


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra en una cadena de texto.

    La función maneja espacios múltiples y asegura que solo la primera 
    letra de cada palabra esté en mayúscula, manteniendo el resto en minúscula.

    Argumentos:
        texto (str): La cadena original a transformar.

    Retorna:
        str: Una nueva cadena con las palabras capitalizadas.
    """
    # 1. Dividimos el texto en una lista de palabras (maneja espacios extras)
    palabras = texto.split()
    
    # 2. Capitalizamos cada palabra y las guardamos en una nueva lista
    # Usamos capitalize() porque pone la primera en mayúscula y el resto en minúscula
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    
    # 3. Unimos las palabras con un espacio simple entre ellas
    return " ".join(palabras_capitalizadas)
    pass


def contar_vocales(texto: str) -> int:
    """
    Cuenta la cantidad de vocales (a, e, i, o, u) en una cadena de texto.

    La función no distingue entre mayúsculas y minúsculas y solo 
    contabiliza vocales sin tilde.

    Argumentos:
        texto (str): La cadena de caracteres a analizar.

    Retorna:
        int: El número total de vocales encontradas.
    """
    vocales = "aeiouáéíóú"
    contador = 0
    
    # Normalizamos a minúsculas una sola vez para optimizar
    texto_minusc = texto.lower()
    
    for caracter in texto_minusc:
        if caracter in vocales:
            contador += 1
            
    return contador
    pass


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César a un texto dado un desplazamiento entero.

    Solo se desplazan las letras del alfabeto (A-Z y a-z). Los números, 
    espacios y símbolos permanecen inalterados.

    Argumentos:
        texto (str): El mensaje original.
        desplazamiento (int): Cantidad de posiciones a desplazar.

    Retorna:
        str: El texto cifrado.
    """
    resultado = []

    for caracter in texto:
        # Verificamos si es una letra
        if caracter.isalpha():
            # Determinamos si es mayúscula o minúscula para el valor base ASCII
            # 'A' es 65, 'a' es 97
            base = ord('A') if caracter.isupper() else ord('a')
            
            # Aplicamos la fórmula:
            # 1. Restamos la base para que la letra esté en el rango 0-25
            # 2. Sumamos el desplazamiento
            # 3. Usamos módulo 26 para que "de la vuelta" al alfabeto
            # 4. Sumamos la base de nuevo para volver al código ASCII original
            nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado.append(chr(nuevo_codigo))
        else:
            # Si no es letra (espacio, punto, número), se queda igual
            resultado.append(caracter)

    return "".join(resultado)
    pass
