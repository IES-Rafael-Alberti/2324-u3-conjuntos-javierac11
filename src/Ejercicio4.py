#Ejercicio 3.3.4¶
#Dadas las siguientes listas:
"""
frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
"""
#    Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
#    Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
#    Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
#    Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

def crearConjuntoConLista(lista: list) -> set:
    """Convierte una lista en un conjunto

    Args:
        lista (list): Una lista

    Returns:
        set: la lista convertida en un conjunto
    """
    conjunto = set(lista)
    return conjunto

def encontrarRepetidos(conjunto1: set, conjunto2: set) -> set:
    """Encuentra los repetidos de 2 conjuntos

    Args:
        conjunto1 (set): Un conjunto
        conjunto2 (set): Otro conjunto

    Returns:
        set: Los repetidos en los 2 conjuntos
    """
    comunes = conjunto1 & conjunto2
    return comunes

def elementosConjunto1NoEstenConjunto2(conjunto1: set, conjunto2: set):
    """Busca los elementos del conjunto1 que no esten en el conjunto2

    Args:
        conjunto1 (set): Un conjunto
        conjunto2 (set): Otro conjunto

    Returns:
        set: Elementos del conjunto1 que no esten en el conjunto2
    """
    no_comunes = conjunto1 - conjunto2
    return no_comunes

if __name__ == '__main__':
    
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1 = crearConjuntoConLista(frutas1)
    set_frutas2 = crearConjuntoConLista(frutas2)
    frutas_comunes = encontrarRepetidos(set_frutas1, set_frutas2)
    frutas_solo_en_frutas1 = elementosConjunto1NoEstenConjunto2(set_frutas1, set_frutas2)
    frutas_solo_en_frutas2 = elementosConjunto1NoEstenConjunto2(set_frutas2, set_frutas1)

    print(f"{frutas_comunes}\n{frutas_solo_en_frutas1}\n{frutas_solo_en_frutas2}")