from modules.central_tendencies import is_collection, mean
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