from modules.vector import Vector

def test_add():
    vec1 = Vector([1, 2, 3, 4])
    vec2 = Vector([1, 2, 3, 4])
    vec3 = Vector([1, 2, 3, 4 , 5])
    assert (vec1 + vec2)  == [2, 4, 6, 8]
    assert (vec1 + vec3) == [2, 4, 6, 8]
    
def test_isNum():
    a = Vector()
    assert a.isNum(5)
    assert a.isNum(7.5)
    assert not a.isNum('a')
    assert not a.isNum('asdf')
    assert not a.isNum('')

def test_append():
    a = Vector()
    assert len(a) == 0
    a.append(1)
    assert len(a) == 1

def test_pop():
    a = Vector([1, 2, 3, 4])
    assert a.pop() == 4
    assert len(a) == 3
    assert a.pop(1) == 2
    assert len(a) == 2