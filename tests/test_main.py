import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import add
from src.main import subtract
from src.main import multiply
from src.main import divide

def test_add_function():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(5,5) == 10
def test_subtract_function():
    assert subtract(1,2) == -1
    assert subtract(5,1) == 4
    assert subtract(7,2) == 5
def test_multiply_function():
    assert multiply(1,2) == 2
    assert multiply(5,1) == 5
    assert multiply(7,2) == 14
def test_divide_function():
    assert divide(1,2) == 0.5
    assert divide(5,1) == 5
    assert divide(7,2) == 3.5