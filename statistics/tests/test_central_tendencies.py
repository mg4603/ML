from modules.central_tendencies import is_collection, mean, median, quantile
from pytest import raises

def test_is_collection():
    assert not is_collection(1)
    assert is_collection('a')
    assert is_collection('')
    assert not is_collection(True)
    assert is_collection([1, 2, 3, 4])

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3

    with raises(Exception):
        mean([1, 2, 3, 4, 'a'])
    
    with raises(Exception):
        mean('a')

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    with raises(Exception):
        median([1, 2, 3, 4, 'a'])
    
    with raises(Exception):
        median('a')

def test_quantile():
    assert quantile([1, 2, 3, 4, 5], 0.1) == 1
    assert quantile([1, 2, 3, 4, 5], 0.2) == 2
    with raises(Exception):
        quantile([1, 2, 3, 4, 'a'], 0.1)
    
    with raises(Exception):
        quantile('a', 0.1)