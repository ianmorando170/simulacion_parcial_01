"""
EJERCICIO 4 — Contar Apariciones en una Lista
###############################################

Escribí una función llamada `contar_apariciones(lista, elemento)` que reciba
una lista y un elemento, y devuelva cuántas veces aparece ese elemento en la lista.

Importante: no uses el método `.count()` de las listas.
Debés recorrer la lista con un bucle y contar manualmente.

Luego escribí otra función llamada `contar_todos(lista)` que reciba una lista
y devuelva un resumen de cuántas veces aparece cada elemento único.
El resultado debe imprimirse de esta forma (un elemento por línea):

    "manzana" aparece 3 veces
    "pera" aparece 1 vez
    "naranja" aparece 2 veces

Probá las funciones con los siguientes ejemplos:

    frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]

    print(contar_apariciones(frutas, "manzana"))  # 3
    print(contar_apariciones(frutas, "pera"))     # 1
    print(contar_apariciones(frutas, "uva"))      # 0

    contar_todos(frutas)
    # manzana aparece 3 veces
    # pera aparece 1 vez
    # naranja aparece 2 veces

Nota: para `contar_todos` podés apoyarte en la función `eliminar_duplicados`
del ejercicio anterior, o resolverlo de otra manera.

"""


def contar_apariciones(lista, elemento):
    """
    Va a contar cuántas veces aparece un elemento dentro de una lista.
    Recorre la lista elemento por elemento y suma cuántas veces coincide con el elemento que buscamos.
    lista: Lista de elementos
    elemento: elemento a buscar dentro de la lista
    return: Cantidad de apariciones del elemento
    """

    contador = 0

    for l in lista:
        if l == elemento:
            contador += 1

    return contador


def contar_todos(lista):
    """
    Muestra cuántas veces aparece cada elemento único en la lista.
    Primero obtiene los elementos sin repetir y luego utiliza la función
    contar_apariciones para calcular cuántas veces aparece cada uno.
    lista: lista de elementos (puede tener repetidos)
    """

    elementos_unicos = []

    for l in lista:
        if l not in elementos_unicos:
            elementos_unicos.append(l)

    for l in elementos_unicos:
        cantidad = contar_apariciones(lista, l)
        print(f"{l} aparece {cantidad} veces.")


# Ejemplos:
frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]

print(contar_apariciones(frutas, "manzana"))
print(contar_apariciones(frutas, "pera"))
print(contar_apariciones(frutas, "uva"))

contar_todos(frutas)

