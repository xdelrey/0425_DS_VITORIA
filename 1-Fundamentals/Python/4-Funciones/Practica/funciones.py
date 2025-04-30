def dibujar_linea(ancho=10):
    return print('-'*ancho)

def numero_a_dia_semana(num):
    '''
    función que convierte números del 1 al 7 en nombres de los dias de la semana.
    La función consta de un único argumento numérico y una salida de tipo string.
    '''
    # relación de días de la semana
    dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

    # comprobar que el argumento es un número entre 1 y 7
    if int(num) >= 1 and int(num) <=7:
        return dias_semana[num-1]
    else:
        print("El número debe estar entre 1 y 7.")
def piramide(altura):
    '''
    como output dibuja una pirámide invertida de la altura especificada en el input
    '''
    while altura > 0:
        linea = list(range(altura, 0, -1))
        for i in linea:
            print(i, end=' ')
        print("\n")
        altura -= 1
def compara_numeros(num_1, num_2):
    '''
    función para conocer cuál es mayor de 2 números o si son iguales
    '''
    if num_1 == num_2:
        return print("son iguales")
    elif num_1 > num_2:
        return print(f"el primero es mayor ({num_1} > {num_2})")
    else:
        return print(f"el segundo es mayor ({num_2} > {num_1})")
def contar_letras(texto,letra):
    '''
    devuelve el número de veces que aparece una letra (minúsculas o mayúsculas) en un texto
    '''
    contador = 0
    for i in range(len(texto)):
        if texto[i].upper() == letra.upper():
            contador += 1
    return contador
def conteo_de_letras(texto):
    '''
    función que con un string de input, el output sea un diccionario con el conteo de las letras
    '''
    # recorrer cada caracter del texto y si es una letra guardarlo en un set
    caracteres = set()
    for i in texto:
        caracter = i
        if caracter.isalpha():
            caracteres.add(caracter.lower())

    # para cada caracter del set obtener cuántas veces aparece en el texto
    # y añadir cada letra y el nº de apariciones en un diccionario
    conteo = {}
    for i in caracteres:
        conteo[i] = contar_letras(texto,i)
    return conteo
def actualiza_lista(lista, comando, elemento=None):
    '''
    función que actualiza una lista añadiendo o eliminando elementos.
    '''
    lista_actualizada = lista
    if comando == "add":
        lista_actualizada.append(elemento)
    elif comando == 'remove':
        lista_actualizada.remove(elemento)
    return lista_actualizada
def construye_frase(palabras):
    '''
    Une las palabras del input y devuelve una frase
    '''
    frase = " ".join(palabras)
    return frase
def fibonacci (n):
    '''
    Devuelve el enésimo número de la serie de Fibonacci
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def area_cuadrado (lado):
    return lado ** 2
def area_triangulo (base, altura):
    return (base * altura) / 2
def area_circulo (radio):
    import math
    return (math.pi) * (radio ** 2)
