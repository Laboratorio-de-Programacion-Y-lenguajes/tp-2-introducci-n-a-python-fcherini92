# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: Gemini 3

**Prompt usado**:
> 
Actuá como tutor de Python 3.13. Dame una receta paso a paso para:

1-realizar la suma de dos enteros, "a" y "b"

2-devolver el resultado de la suma

No uses librerías externas. Mostrá una función suma_enteros(a: int, b: int) -> int con docstring.

**Resultado obtenido**:
La Receta: Suma de Enteros
Paso 1: Definir la estructura de la función
Usamos la palabra clave def seguida del nombre de la función. Especificamos que los parámetros a y b deben ser de tipo int y que la función devolverá (->) un int.

Paso 2: Redactar el Docstring
Siguiendo el estándar PEP 257, el docstring explica qué hace la función, qué recibe y qué entrega. Esto es vital para el mantenimiento del código.

Paso 3: Realizar la operación y retornar
Simplemente usamos el operador +. Al ser una función pura, usamos return para que el resultado pueda ser guardado en una variable o usado en otra operación.

Código Completo
Aquí tenés el código listo para ser integrado en tus proyectos:

Python
def suma_enteros(a: int, b: int) -> int:
    """
    Suma dos números enteros y devuelve el resultado.

    Args:
        a (int): El primer número entero.
        b (int): El segundo número entero.

    Returns:
        int: La suma resultante de a + b.
    """
    return a + b

def main():
    # Ejemplo de uso:
    try:
        # 1. Pedir los datos y convertirlos a entero (int)
        num1 = int(input("Ingresá el primer número entero: "))
        num2 = int(input("Ingresá el segundo número entero: "))
        
        # 2. Llamar a la función y obtener el resultado
        resultado = suma_enteros(num1, num2)
        
        print(f"El resultado de la suma es: {resultado}")
        
    except ValueError:
        print("Error: Por favor, ingresá únicamente números enteros.")

if __name__ == "__main__":
    main()
Consideraciones técnicas
Manejo de Tipos: Aunque definimos : int en la función, Python no bloquea la ejecución si pasas un decimal (float) a menos que uses un verificador estático (como mypy). Por eso, en el main() usamos int(input()) para forzar la conversión.

Rendimiento: En Python 3.13, las operaciones aritméticas simples están sumamente optimizadas, manejando automáticamente enteros de precisión arbitraria (puedes sumar números increíblemente grandes sin que el sistema se desborde, limitado solo por tu memoria RAM).


**¿Lo usaste tal cual o lo modificaste?**
Lo modifique solicitando que forzara la conversion a INT dentro de la funcion suma_enteros

---

### 2 - condicionales.py

**Herramienta**: Gemini 3

**Prompt usado**:
> 
Quiero implementar una función mayor_de_tres(a: int, b: int, c: int) -> int en Python.

Antes de escribir el código, haceme 3 preguntas para confirmar:

1 - Qué mensajes exactos debo devolver para cada caso.

2 - Cómo tratar el número 0.

3 - Cual es el resultado que se espera de esta funcion.

Después de mis respuestas, recién ahí proponé el código, sin librerias externas y realizando el docstring

**Resultado obtenido**:
Para la función mayor_de_tres(a, b, c), necesito que me aclares estos puntos:

Mensajes de retorno: Dado que la firma de la función indica que devuelve un entero (-> int), ¿realmente debe devolver un mensaje (string) en algún caso, o te referís a qué valor debe retornar si, por ejemplo, hay números iguales?

Tratamiento del 0: ¿El cero tiene alguna relevancia especial o se compara como cualquier otro número entero dentro de la lógica de "mayor que"?

Resultado esperado: En caso de que haya un empate (por ejemplo, a y b son iguales y son los mayores), ¿qué debe devolver la función? ¿El valor de cualquiera de ellos o hay alguna prioridad?

Quedo a la espera de tus definiciones para escribir el código con su docstring.

**2do Prompt usado**:
> 
1 - debe retornar un int con el mayor de los valores suministrados
2 - el cero no tiene logica especial, tratalo como un entero más
3 - en caso de empate, informar el primero de los mayores que se haya ingresado. por ejemplo si b y c son iguales, informar b.

**Resultado obtenido**:
Perfecto, Franco. Con estas definiciones, la lógica es clara: vamos a priorizar el orden de entrada en las comparaciones para cumplir con tu criterio de desempate, aunque el valor final sea el mismo.

Aquí tenés la implementación:

Implementación en Python
Python
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

Detalles de la solución:
Lógica de Desempate: Al usar los operadores >= en el orden de evaluación, garantizamos que si a es igual al máximo, se devuelva a. Si no, pasamos a evaluar si b cumple la condición respecto a los restantes.

Tratamiento del Cero: Se comporta como cualquier otro entero dentro de las comparaciones lógicas, sin excepciones.

Eficiencia: La función resuelve el problema en un máximo de dos evaluaciones lógicas, manteniendo el código limpio y fácil de leer.

**¿Lo usaste tal cual o lo modificaste?**
lo use tal cual, me parecio una solucion sencilla y suficiente.

---

### 3 - listas.py

**Herramienta**: Gemini 3

**Prompt usado**:
> 
Estoy resolviendo un ejercicio de listas en Python 3.13 con estas reglas:

1 - generar una nueva lista sin elementos duplicados
2 - manteniendo el orden de primera aparicion

¿Podés revisar mi lógica como verificador cognitivo?

Enumerá casos borde que debería testear (ej: listas con un solo elemento, listas con negativos).
Decime errores típicos que podría cometer un principiante (ej: división por cero).
Proponé 3 tests con entradas y salidas esperadas (sin escribir el código final todavía)."

**Resultado obtenido**:
Como verificador cognitivo, confirmo que tu enfoque debe basarse en la pertenencia: "¿Ya vi este elemento antes? Si no, lo guardo".

1. Casos Borde (Edge Cases)
Para que tu función sea "indestructible", testeala con:

Lista Vacía ([]): Debe devolver [].

Todos los elementos iguales ([7, 7, 7, 7]): Debe devolver una lista con un solo elemento: [7].

Sin duplicados ([1, 2, 3]): La salida debe ser una copia idéntica de la entrada.

Duplicados no consecutivos ([1, 2, 1, 3, 2]): Aquí es donde se verifica si el orden de primera aparición se respeta (debería dar [1, 2, 3]).

Tipos mixtos ([1, "1", 1.0]): Python los trata como elementos distintos (en la mayoría de los casos), así que deben permanecer si su valor o tipo difiere según la lógica de comparación.

2. Errores típicos de principiante
¡Cuidado con caer en estas trampas!

El "Atajo del Set" (set(lista)): Convertir la lista a un conjunto (set) elimina los duplicados de un plumazo, pero destruye el orden original. Es el error número uno.

Búsqueda ineficiente (O(n 
2
 )): Si usás una lista nueva para guardar los elementos y hacés if elemento not in lista_nueva, Python tiene que recorrer toda la lista nueva en cada paso. Para listas gigantes, esto es lentísimo.

Modificar la lista original: Intentar borrar elementos de la lista mientras la estás recorriendo con un for. Esto causa que el iterador se pierda y saltee elementos.

No distinguir entre 0, False y None: En algunos contextos de Python, estos pueden comportarse de forma similar si no se comparan correctamente.

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual.

---

### 4 - diccionarios.py

**Herramienta**: Gemini3

**Prompt usado**:
> 
Generá 8 ejemplos distintos de diccionarios Python que retornen un nuevo diccionario con claves y valores intercambiados.
    Ejemplo: invertir_diccionario({"a": 1}) -> {1: "a"}
Luego, explicame la regla general para extraer estos valores y escribí la función invertir_diccionario(d: dict) -> dict: con docstring y no uses librerias externas 

**Resultado obtenido**:
Aquí tenés los 8 ejemplos, la lógica detrás del "truco" y el código.

Ejemplos de Inversión de Diccionarios
En estos ejemplos, transformamos cada {clave: valor} en {valor: clave}.

#	Entrada (Original)	Resultado (Invertido)
1	{"a": 1, "b": 2}	{1: "a", 2: "b"}
2	{"rojo": "#FF0000", "azul": "#0000FF"}	{"#FF0000": "rojo", "#0000FF": "azul"}
3	{"id": 101, "status": 200}	{101: "id", 200: "status"}
4	{"Python": "Lenguaje", "VS Code": "Editor"}	{"Lenguaje": "Python", "Editor": "VS Code"}
5	{"Enero": 1, "Febrero": 2, "Marzo": 3}	{1: "Enero", 2: "Febrero", 3: "Marzo"}
6	{"nombre": "Gemini", "rol": "AI"}	{"Gemini": "nombre", "AI": "rol"}
7	{10: "diez", 20: "veinte"}	{"diez": 10, "veinte": 20}
8	{"cat": "gato", "dog": "perro"}	{"gato": "cat", "perro": "dog"}
La Regla General: ¿Cómo se hace el intercambio?
Para invertir un diccionario, la lógica fundamental se basa en la iteración de pares.

Recorrido: Debemos acceder a cada par del diccionario original. En Python, esto se hace eficientemente con el método .items(), que nos entrega la clave y el valor al mismo tiempo.

Nueva Asignación: Creamos un nuevo diccionario donde el valor del original se convierte en la nueva clave, y la clave original se convierte en el nuevo valor.

Restricción Crítica: Recordá que en Python las claves deben ser únicas. Si el diccionario original tiene dos claves con el mismo valor (ej. {"a": 1, "b": 1}), al invertirlo, la última clave procesada sobrescribirá a las anteriores para ese valor.

La Función: invertir_diccionario
Aquí tenés la implementación utilizando una técnica llamada diccionario por comprensión (dictionary comprehension), que es la forma más elegante y "pythónica" de hacerlo:

Python
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

# Ejemplo de prueba
mi_dict = {"Manzana": "Roja", "Banana": "Amarilla"}
print(invertir_diccionario(mi_dict))
# Salida: {'Roja': 'Manzana', 'Amarilla': 'Banana'}

**¿Lo usaste tal cual o lo modificaste?**
lo use tal cual

---

### 5 - loops.py

**Herramienta**: Gemini 3

**Prompt usado**:
> 
P1: ¿Cómo agrego elementos a una lista a partir de 1 a un numero n en Python 3.13?
P2: ¿Cuál es la forma más simple si N debe ser como minimo 1?
P3: ¿Qué debería hacer si N es negativo? ¿Conviene lanzar un error o devolver una lista vacía para un TP universitario?
P4: Mostrame una implementación de la función contar_hasta(n: int) -> list sin usar librerias externas y con docstring

**Resultado obtenido**:
Para trabajar con secuencias numéricas en Python 3.13 (y versiones anteriores, ya que es una funcionalidad núcleo que no ha cambiado), la herramienta estrella es la función range.

Aquí tenés los detalles para tu TP:

P1 y P2: La forma más simple y eficiente
La manera más directa de crear una lista con números del 1 al n es convertir un objeto range en una list.

La técnica: list(range(1, n + 1))

Por qué n+1: Porque en Python, el límite superior de un rango es exclusivo (no se incluye). Si querés que el n aparezca, tenés que pedirle a Python que llegue hasta uno más.

Si n es al menos 1, esta función generará exactamente lo que buscás (ej: si n=3, genera [1, 2, 3]).

P3: ¿Qué hacer si N es negativo? (Criterio Académico)
Si hacés list(range(1, -5)), Python te devolverá una lista vacía [] sin quejarse.

¿Qué conviene para un TP universitario?

Devolver [] (Recomendado): Es lo más robusto. En programación, muchas veces es mejor que una función devuelva un "resultado nulo" (una lista vacía) a que rompa la ejecución de todo el programa con un error. Indica que "no hay elementos para contar en esa dirección".

Lanzar un ValueError: Solo hacelo si el enunciado del TP dice explícitamente: "La función debe validar que la entrada sea un entero positivo".

Mi consejo: Si no lo aclara, devolvé la lista vacía. Es el comportamiento estándar de Python y demuestra que entendés cómo funciona range.

P4: Implementación de contar_hasta
Aquí tenés el código listo para usar, siguiendo las buenas prácticas de documentación:

Python
def contar_hasta(n: int) -> list[int]:
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


**¿Lo usaste tal cual o lo modificaste?**
si

---

### 6 - funciones.py

**Herramienta**: Gemini 3

**Prompt usado**:
> 
Necesito una función memoizar(func) en Python 3.13.
Quiero comparar enfoques y elegir uno simple y performante para un TP:

1 - Retorna una versión de func que cachea sus resultados.
2 - Si se llama con los mismos argumentos, retorna el resultado cacheado.


Analizá pros/contras (performance + simplicidad + edge cases).
Luego recomendá UNO y escribí el código con docstring, dejando claro qué casos NO cubre.

**Resultado obtenido**:
La memoización es una técnica de optimización que consiste en guardar los resultados de funciones costosas en un "cache" para no tener que recalcularlos. En Python, esto se suele implementar mediante un decorador.

Análisis Comparativo
Método	Simplicidad	Performance	Notas
Diccionario en Closure	⭐⭐⭐⭐⭐	Muy Alta	Es la forma más pura y educativa. No requiere imports.
functools.lru_cache	⭐⭐⭐⭐	Máxima	Es la versión profesional (escrita en C), pero requiere un import.
Atributo de función	⭐⭐	Alta	Poco común, ensucia el objeto función con datos.
Evaluación de los Enfoques
Diccionario manual (Recomendado para el TP): Utiliza un diccionario donde las claves son los argumentos y el valor es el resultado. Es ideal para entender el concepto de clausura (closure) en programación.

lru_cache (Least Recently Used): Es parte de la librería estándar. La gran ventaja es que permite poner un límite de memoria (ej: guardar solo los últimos 128 resultados), evitando que el programa consuma toda la RAM en procesos largos.

Performance: El acceso a un diccionario en Python es O(1) (tiempo constante), lo que hace que la recuperación del cache sea casi instantánea comparada con cualquier cálculo matemático o procesamiento de texto.

Recomendación: Diccionario en Closure (Sin Librerías)
Es la mejor opción para un trabajo práctico porque demuestra que entendés cómo funcionan los ámbitos (scopes) en Python y el manejo de estructuras de datos básicas.

Código Sugerido (Python 3.13)
Python
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

# Ejemplo de uso (Fibonacci es el caso clásico):
# @memoizar
# def fibonacci(n):
#     if n < 2: return n
#     return fibonacci(n-1) + fibonacci(n-2)
⚠️ Lo que este código NO cubre (Edge Cases)
Al ser una implementación simplificada para un TP, tenés estos "puntos ciegos":

Argumentos Mutables: Este es el "limitante" más importante. Si intentás memoizar una función que recibe una lista ([1, 2]), el código fallará con un TypeError: unhashable type: 'list'. Las claves de un diccionario deben ser inmutables (tuplas, strings, números).

Consumo de Memoria: Este cache crece indefinidamente. Si llamás a la función con un millón de argumentos distintos, el diccionario ocupará cada vez más RAM hasta que cierres el programa.

Argumentos por Nombre (kwargs): Esta versión simple solo maneja argumentos posicionales (*args). Si llamás a la función como func(valor=10), no lo guardará correctamente a menos que se use una lógica más compleja para normalizar los argumentos.

**¿Lo usaste tal cual o lo modificaste?**
copiado y pegado

---

### 7 - operaciones.py

**Herramienta**: Gemini 3

**Prompt usado**:
> 
Tengo que implementar una función en python 3.13 es_palindromo(texto: str) -> bool: para un tp de la universidad, debo retornar TRUE si el texto es palíndromo (ignorando espacios y mayúsculas). Compara 3 enfoques para manejar la comprobación.
Elegí el enfoque más adecuado para un nivel inicial que debe pasar tests con pytest, justificá la elección y escribí el código final con la función y su docstring

**Resultado obtenido**:
 Para un TP de la universidad, lo más importante es que tu código sea legible, eficiente y fácil de probar.Aquí tenés la comparativa de los tres enfoques para determinar si una palabra o frase es un palíndromo:Comparativa de Enfoques:

 Enfoque Descripción Pros Contras
 A) Slicing ([::-1])Se limpia el texto y se compara directamente con su versión invertida usando texto == texto[::-1].Es la forma más "Pythonic". Es extremadamente concisa y fácil de leer.Crea una copia completa del string en memoria (aunque para strings cortos es despreciable).
 B) Bucle for / whileSe recorre el string con dos índices (uno al principio y otro al final) comparando caracteres.Es muy eficiente en memoria porque no copia el string. Es el enfoque clásico en lenguajes como C o Java.El código es más largo, propenso a errores de "off-by-one" (índices fuera de rango) y menos legible.
 C) reversed() y join()Se usa la función integrada reversed() para invertir y luego se une con "".join().Es explícito en su intención (invertir el objeto).Es más lento que el slicing y la sintaxis resulta un poco más cargada para un principiante.

 El enfoque ganador: Enfoque A (Slicing)Para un nivel inicial y para pasar tests con pytest, el Enfoque A es el más adecuado.Justificación:Simplicidad: En Python, "simple es mejor que complejo". El slicing ([::-1]) es una herramienta nativa muy potente que reduce la lógica a una sola línea de comparación.Mantenibilidad: Si los tests de pytest fallan, es mucho más fácil ver dónde está el error en una línea de comparación que revisar la lógica de punteros de un bucle.Limpieza previa: Este enfoque te obliga a normalizar el texto (quitar espacios y pasar a minúsculas) antes de comparar, lo cual es una excelente práctica de programación.Código Final ImplementadoHe incluido la normalización necesaria para que la función sea robusta frente a espacios y diferencias de mayúsculas/minúsculas.Pythondef es_palindromo(texto: str) -> bool:
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

**¿Lo usaste tal cual o lo modificaste?**
tal cual, la solucion con bucle for/while la implemente en java anteriormente 

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
    El contexto, la informacion especifica y los requerimientos claros contribuyen a una respuesta mucho mejor articulada, disminuyendo la posibilidades de errores no deseados o de tener que invertir más tiempo para corregir cosas que no fueron claras desde un principio. Al estar jugando con todas estas estrategias pude identificar con las que me sentia más comodo trabajando y se me hacian más naturales a la hora de escribirlas. voy a empezar a utilizarlas para otras cosas, ya que estos patrones no se limitan a la programacion.
- ¿En qué casos la IA fue útil y en cuáles no?
    La principal utilidad es la capacidad de "elegir las herramients" y poder explicarlas de manera clara, ya que python es un lenguaje con el que estoy empezando y no estoy familiarizado con la semantica ni las herramientas disponibles dentro  de este. 
- ¿Qué harías diferente la próxima vez?
    Probaria otros patrones de prompting para tal vez encontrar alguno que me sea más util.
