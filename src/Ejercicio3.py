#Ejercicio 3.3.3¶
#El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.
#Por ejemplo, el conjunto potencia de {1,2,3} es:
#{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
#Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y 
#retorne su «lista potencia» (la lista de todos sus subconjuntos):

""">>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
"""

def conjuntoPotencial(conjunto: set) -> list:
    """Calcula el conjunto potencial

    Args:
        conjunto (set): Un conjunto

    Returns:
        list: Conjunto potencial
    """
    conjunto_potencial = [set([0])]
    for numero in conjunto:
        if set([numero]) not in conjunto_potencial:
            conjunto_potencial.append(set([numero]))
    
    for numero in conjunto:
        for numero2 in conjunto:
            if set([numero, numero2]) not in conjunto_potencial:
                conjunto_potencial.append(set([numero, numero2]))
                
    conjunto_potencial.append(conjunto)
    
    return conjunto_potencial
    
if __name__ == '__main__':
    print(conjuntoPotencial({6, 1, 4}))