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

def crearConjuntoConLista(lista: list):
    conjunto = set(lista)
    return conjunto

def encontrarRepetidos(conjunto1: set, conjunto2: set):
    comunes = conjunto1 & conjunto2
    return comunes

def elementosConjunto1NoEstenConjunto2(conjunto1: set, conjunto2: set):
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