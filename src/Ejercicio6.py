#Ejercicio 3.3.6¶
#Dado el conjunto de letras:
"""
vocales = {'a', 'e', 'i', 'o', 'u'}
"""
#    Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
#    Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto
#       vocales como en el conjunto consonantes.

def generaAlfabetoConDescartes(descartes: set) -> set:
    """Genera un alfabeto descartando las letras que quieras

    Args:
        descartes (set): Letras que quieras descartar

    Returns:
        set: El alfabeto con los descartes
    """
    alfabeto = set()
    for posicion_letra in range(97, 122):
        if chr(posicion_letra) not in descartes:
            alfabeto.add(chr(posicion_letra))
    return alfabeto

def repetidos(conjunto1: set, conjunto2: set) -> set:
    """Encuentra los repetidos de 2 conjuntos

    Args:
        conjunto1 (set): Un conjunto
        conjunto2 (set): Otro conjunto

    Returns:
        set: Los repetidos en los 2 conjuntos
    """
    set_repetidos = conjunto1 & conjunto2
    return set_repetidos

if __name__ == '__main__':
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = generaAlfabetoConDescartes(vocales)
    letras_comunes = repetidos(vocales, consonantes)
    print(letras_comunes)
    