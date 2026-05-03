"""
EJERCICIO 2 — Combinar Dos Listas
##################################

Escribí una función llamada `combinar_listas(lista1, lista2)` que reciba dos listas
como parámetros y devuelva una nueva lista con todos los elementos de ambas,
primero los de `lista1` y luego los de `lista2`.

Importante: no uses el operador `+` entre listas ni el método `.extend()`.
Debés recorrer cada lista con un bucle y construir la nueva lista elemento por elemento.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    # Resultado esperado: [1, 2, 3, 4, 5, 6]

    lista_c = ["manzana", "pera"]
    lista_d = ["naranja", "uva", "durazno"]
    # Resultado esperado: ["manzana", "pera", "naranja", "uva", "durazno"]

"""


def combinar_listas(lista1, lista2):
    """
    Combina dos listas en una sola.

    Recorre ambas listas elemento por elemento y crea una nueva lista con todos los valores en el mismo orden.
    lista1: primera lista de elementos
    lista2: segunda lista de elementos
    return: va a devolver la lista con los elementos nuevos
    """
    
    nueva_lista = []

    for l in lista1:
        nueva_lista.append(l)
    
    for l in lista2:
        nueva_lista.append(l)
    
    return nueva_lista


# Ejemplos:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

resultado_uno = combinar_listas(lista_a, lista_b)
print(resultado_uno)


lista_c = ["manzana", "pera"]
lista_d = ["naranja", "uva", "durazno"]

resultado_dos = combinar_listas(lista_c, lista_d)
print(resultado_dos)

