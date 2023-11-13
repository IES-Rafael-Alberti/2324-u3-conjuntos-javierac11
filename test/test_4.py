from src.Ejercicio4 import crearConjuntoConLista, encontrarRepetidos, elementosConjunto1NoEstenConjunto2

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

def test_crearConjuntoConLista():
    assert crearConjuntoConLista(frutas1) == {"manzana", "pera", "naranja", "plátano", "uva"}
    
def test_encontrarRepetidos():
    assert encontrarRepetidos(set_frutas1, set_frutas2) == {"manzana", "pera", "uva"}
    
def test_elementosConjunto1NoEstenConjunto2():
    assert elementosConjunto1NoEstenConjunto2(set_frutas1, set_frutas2) == {"naranja", "plátano"}