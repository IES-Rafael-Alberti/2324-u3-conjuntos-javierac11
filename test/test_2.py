from src.Ejercicio2 import nombres1NoRepetidosEnNombre2, nombresRepetidos, comprobarIncuido, todosNombresSinDuplicados

conjunto = {"Edu", "Luis"}
conjunto1 = {"Javier", "Edu", "Rafa", "Adri"}
conjunto2 = {"Edu", "Luis", "Alberto", "Adri"}

def test_nombresRepetidos():
    assert nombresRepetidos(conjunto1, conjunto2) == {"Edu", "Adri"}

def test_todosNombresSinDuplicados():
    assert todosNombresSinDuplicados(conjunto1, conjunto2) == {"Javier", "Rafa", "Edu", "Luis", "Alberto", "Adri"}    
    
def test_nombres1NoRepetidosEnNombre2():
    assert nombres1NoRepetidosEnNombre2(conjunto1, conjunto2) == {"Javier", "Rafa"}
    
def test_comprobarIncuido():
    assert comprobarIncuido(conjunto1, conjunto2) == False
    assert comprobarIncuido(conjunto, conjunto2) == True