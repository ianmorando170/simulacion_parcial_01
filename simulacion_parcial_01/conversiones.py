
# CORRECCIÓN GENERAL DEL ARCHIVO:
# La consigna del Ejercicio 6 pide explícitamente:
#   "Cada función debe tener un docstring de una línea que explique qué hace.
#    Ver formato: https://peps.python.org/pep-0257/#one-line-docstrings"
# Acá las explicaciones están escritas como comentarios (con #), pero deberían
# ser docstrings, es decir strings entre triples comillas inmediatamente después
# del def. Ejemplo de formato correcto:
#
#     def km_a_millas(km):
#         """Convierte kilómetros a millas."""
#         return km * 0.621371


def km_a_millas(km):
    # Convierte kilómetros a millas
    return km * 0.621371


def kg_a_libras(kg):
    # Convierte kilogramos a libras
    return kg * 2.20462

