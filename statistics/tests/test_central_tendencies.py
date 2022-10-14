from modules.central_tendencies import is_collection

def test_is_collection():
    assert not is_collection(1)
    assert is_collection('a')
    assert is_collection('')
    assert not is_collection(True)
    assert is_collection([1, 2, 3, 4])