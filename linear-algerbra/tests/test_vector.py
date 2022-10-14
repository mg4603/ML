from modules.vector import Vector

def test_isNum():
    a = Vector()
    assert a.isNum(5)
    assert a.isNum(7.5)
    assert not a.isNum('a')
    assert not a.isNum('asdf')
    assert not a.isNum('')

def test_append():
    a = Vector()
    assert a.len() is 0
    a.append(1)
    assert a.len() is 1