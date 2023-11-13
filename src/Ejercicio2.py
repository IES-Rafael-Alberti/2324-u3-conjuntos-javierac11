#Ejercicio 3.3.2¶
#Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela,
#finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria,
#finalizando al introducir “x”.
"""
    Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
    Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
    Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
    Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""

def leerNombre(mensaje: str) -> str:
    """Lee un nombre

    Args:
        mensaje (str): El mensaje que quieras que este en el input

    Returns:
        str: El nombre introducido en el input
    """
    nombre = input(mensaje)
    return nombre

def leerNombres():
    """Lee nombres hasta que el usuario introduzca x

    Returns:
        set: Todos los nombres introducidos
    """
    nombres = set()
    nombre = leerNombre("Introduce un nombre o x para salir: ")
    while nombre != "x":
        nombres.add(nombre)
        nombre = leerNombre("Introduce un nombre o x para salir: ")
    return nombres

def todosNombresSinDuplicados(nombres1: set, nombres2: set) -> set:
    """Elimina los duplicados entre los 2 conjuntos

    Args:
        nombres1 (set): Un conjunto de nombres
        nombres2 (set): Otro conjunto de nombres

    Returns:
        set: Todos los nombres sin repetidos
    """
    nombres_sin_repetir = nombres1 | nombres2
    return nombres_sin_repetir

def nombresRepetidos(nombres1: set, nombres2: set) -> set:
    """Comprueba los nombres que esten repetidos

    Args:
        nombres1 (set): Un conjunto de nombres
        nombres2 (set): Otro conjunto de nombres

    Returns:
        set: Los nombres repetidos
    """
    nombres_repetidos = nombres1 & nombres2
    return nombres_repetidos

def nombres1NoRepetidosEnNombre2(nombres1: set, nombres2: set) -> set:
    """Comprueba los nombre de nombres1 que no se repitan en nombres2

    Args:
        nombres1 (set): Un conjunto de nombres
        nombres2 (set): Otro conjunto de nombres

    Returns:
        set: Los nombres de nombres1 no repetidos en nombres2
    """
    nombres_no_repetidos = nombres1 - nombres2
    return nombres_no_repetidos

def comprobarIncuido(nombres1: set, nombres2: set) -> bool:
    """Comprueba si el primer conjunto esta dentro del segundo

    Args:
        nombres1 (set): Un conjunto de nombres
        nombres2 (set): Otro conjunto de nombres

    Returns:
        bool: True si el primer conjunto esta en el primero, False si no
    """
    comprobacion = nombres1 <= nombres2
    return comprobacion

if __name__ == '__main__':
    nombres_primaria = leerNombres()
    nombres_secundaria = leerNombres()
    nombres_sin_duplicados = todosNombresSinDuplicados(nombres_primaria, nombres_secundaria)
    nombres_repetidos = nombresRepetidos(nombres_primaria, nombres_secundaria)
    nombres_primaria_no_repetidos_en_secundaria = nombres1NoRepetidosEnNombre2(nombres_primaria, nombres_secundaria)
    comprobacion_si_todos_los_nombres_primaria_estan_secundaria = comprobarIncuido(nombres_primaria, nombres_secundaria)
    
    print(f"Nombres sin duplicados: {nombres_sin_duplicados}")
    print(f"Nombres repetidos: {nombres_repetidos}")
    print(f"Nombres de primaria sin repetir en secundaria: {nombres_primaria_no_repetidos_en_secundaria}")
    print(f"Todos los nombres de primaria estan en secundaria: {comprobacion_si_todos_los_nombres_primaria_estan_secundaria}")