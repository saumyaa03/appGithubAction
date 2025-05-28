from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-3,3) == 0

def test_sub():
    assert sub(4,3) == 1
    assert sub(-3,3) == -6
    assert sub(3,3) == 0