"""
EJERCICIO 3 — Eliminar Duplicados de una Lista
################################################

Escribí una función llamada `eliminar_duplicados(lista)` que reciba una lista
y devuelva una nueva lista con los mismos elementos pero sin repetidos.
El orden de aparición de los elementos debe mantenerse (se conserva la primera vez
que aparece cada elemento).

Importante: no uses `set()` para resolver esto.
Debés recorrer la lista con un bucle y verificar manualmente si el elemento ya fue agregado.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista1 = [1, 2, 3, 1, 2, 4]
    # Resultado esperado: [1, 2, 3, 4]

    lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
    # Resultado esperado: ["Pedro", "Florencia", "Ana"]

    lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
    # Resultado esperado: [1, 2, 3, 4, "Pedro", "Florencia", "Ana"]

"""


def eliminar_duplicados(lista):
    """
    Elimina los elementos duplicados de una lista, y deja el mismo orden.
    Recorre la lista elemento por elemento y agrega cada valor a una lista nueva solo si no se hizo antes.
    return: devuelve una lista nueva sin elementos repetidos
    """
    
    nueva_lista = []

    for l in lista:
        if l not in nueva_lista:
            nueva_lista.append(l)
    
    return nueva_lista


# Ejemplos:
lista1 = [1, 2, 3, 1, 2, 4]
print(eliminar_duplicados(lista1))


lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
print(eliminar_duplicados(lista2))


lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
print(eliminar_duplicados(lista3))

