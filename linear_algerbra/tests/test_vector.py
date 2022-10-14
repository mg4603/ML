from modules.vector import Vector

def test_add():
    vec1 = Vector([1, 2, 3, 4])
    vec2 = Vector([1, 2, 3, 4])
    vec3 = Vector([1, 2, 3, 4 , 5])
    assert (vec1 + vec2) == [2, 4, 6, 8]
    assert (vec1 + vec3) == [2, 4, 6, 8]

def test_len():
    vec1 = Vector([1, 2, 3, 4, 5]) 
    assert len(vec1) == 5
    vec1.pop()
    assert len(vec1) == 4

def test_mul():
    vec1 = Vector([1, 2, 3, 4, 5])
    assert vec1 * 3 == [3, 6, 9, 12, 15]
    assert 3 * vec1 == [3, 6, 9, 12, 15]

def test_sub():
    vec1 = Vector([1, 2, 3, 4])
    vec2 = Vector([1, 2, 3, 4])
    vec3 = Vector([1, 2, 3, 4 , 5])
    assert (vec1 - vec2) == [0, 0, 0, 0]
    assert (vec1 - vec3) == [0, 0, 0, 0]

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

def test_summation():
    a = Vector([1, 2, 3, 4, 5])
    assert a.summation() == 15

def test_vector_mean():
    a = Vector([1, 2, 3, 4, 5])
    assert a.vector_mean() == 3

def test_dot():
    vec1 = Vector([1, 2, 3, 4, 5])
    assert vec1.dot(vec1) == 55