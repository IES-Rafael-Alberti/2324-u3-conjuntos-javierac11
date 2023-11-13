#Ejercicio 3.3.5¶
#Dado el conjunto de números enteros:
"""
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
"""
#    Crea un conjunto pares que contenga los números pares del conjunto numeros.
#    Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
#    Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto 
#     llamado pares_y_multiplos_de_tres.

def pares(numeros: set) -> set:
    """Busca los numeros pares de un conjunto

    Args:
        numeros (set): Numeros

    Returns:
        set: Numeros pares
    """
    numeros_pares = set()
    for numero in  numeros:
        if numero % 2 == 0:
            numeros_pares.add(numero)
    return numeros_pares

def multiplos3(numeros: set) -> set: 
    """Busca los multiplos de 3 en un conjunto

    Args:
        numeros (set): Numeros

    Returns:
        set: Numeros multiplos de 3
    """
    multiplos3 = set()
    for numero in numeros:
        if numero % 3 == 0:
            multiplos3.add(numero)
    return multiplos3

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
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    par = pares(numeros)
    multiplos_de_tres = multiplos3(numeros)
    pares_y_multiplos_de_tres = repetidos(par, multiplos_de_tres)
    print(f"{par}\n{multiplos_de_tres}\n{pares_y_multiplos_de_tres}")