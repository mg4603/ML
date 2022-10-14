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

def test_pop():
    a = Vector([1, 2, 3, 4])
    assert a.pop() is 4
    assert len(a) is 3
    assert a.pop(1) is 2
    assert len(a) is 2