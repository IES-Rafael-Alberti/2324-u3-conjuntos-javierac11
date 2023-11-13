from src.Ejercicio3 import conjuntoPotencial

def test_conjuntoPotencial():
    assert conjuntoPotencial({1, 2, 3}) == [{0}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]