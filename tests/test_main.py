from src.main import add
from src.main import subtract

def test_add_function():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(5,5) == 10
def test_subtract_function():
    assert subtract(1,2) == -1
    assert subtract(5,1) == 4
    assert subtract(7,2) == 5