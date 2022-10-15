from modules.correlation import *
from pytest import raises

def test_dot():
    with raises(Exception):
        dot(1, 2)
    with raises(Exception):
        dot([1, 2], 1)
    
    assert dot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 55