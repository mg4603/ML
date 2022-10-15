from modules.dispersion import *
from pytest import raises

def test_is_iterable():
    assert is_iterable('a')
    assert is_iterable([1, 2, 3, 4])
    assert is_iterable('asdf')
    assert not is_iterable(1)

def test_data_range():
    assert data_range([1, 2, 3, 4, 5]) == 4
    with raises(Exception):
        data_range(1)

def test_de_mean():
    with raises(Exception):
        de_mean(1)
    
    assert de_mean([1, 2, 3, 4, 5]) == [-2, -1, 0, 1, 2]

def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3, 4, 5]) == 55
    with raises(Exception):
        sum_of_squares(1)

def test_variance():
    with raises(Exception):
        variance(1)
    assert variance([1, 2, 3, 4, 5]) == 2.5

def test_standard_deviation():
    with raises(Exception):
        standard_deviation(1)
    assert standard_deviation([1, 2, 3, 4, 5]) == sqrt(2.5)