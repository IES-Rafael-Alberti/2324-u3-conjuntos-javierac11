from src.Ejercicio6 import generaAlfabetoConDescartes

def test_generaAlfabetoConDescartes():
    assert generaAlfabetoConDescartes({"a", "b", "c", "x", "y", "z"}) == {"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"}