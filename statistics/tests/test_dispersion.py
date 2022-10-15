from modules.dispersion import *
from pytest import raises

def test_is_iterable():
    assert is_iterable('a')
    assert is_iterable([1, 2, 3, 4])
    assert is_iterable('asdf')
    assert not is_iterable(1)