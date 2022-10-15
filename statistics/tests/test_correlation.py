from modules.correlation import *
from pytest import raises
from math import sqrt 

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

def test_correlation():
    with raises(Exception):
        correlation(1, 2)
    with raises(Exception):
        correlation(1, [1, 2])
    with raises(Exception):
        correlation([1, 2], [3, 4, 5])
    
    assert correlation([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == (2.5 / sqrt(2.5) / sqrt(2.5))
    assert correlation([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]) == 0