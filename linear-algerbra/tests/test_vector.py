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
    assert len(a) is 0
    a.append(1)
    assert len(a) is 1

