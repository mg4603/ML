from modules.correlation import *
from pytest import raises

def test_dot():
    with raises(Exception):
        dot(1, 2)
    with raises(Exception):
        dot([1, 2], 1)
    
    assert dot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 55

def test_covariance():
    with raises(Exception):
        covariance(1, 2)
    with raises(Exception):
        covariance(1, [1, 2])
    with raises(Exception):
        covariance([1, 2], [3, 4, 5])
    
    assert covariance([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 2.5