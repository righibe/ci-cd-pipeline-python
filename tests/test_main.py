from src.main import add

def test_add_function():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(5,5) == 10