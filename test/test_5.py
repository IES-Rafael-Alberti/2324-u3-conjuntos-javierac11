from src.Ejercicio5 import pares, multiplos3

def test_pares():
    assert pares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {2, 4, 6, 8, 10}
    
def test_multiplo3():
    assert multiplos3({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {3, 6, 9}