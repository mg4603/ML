from modules.matrices import Matrix
from pytest import raises

def test_Matrix():
    mat = Matrix([[1, 2, 3, 4], [2, 4, 6, 8]])
    mat2 = Matrix()
    assert mat.Matrix[0][0] == 1
    assert len(mat2.Matrix) == 0
    assert type(mat2.Matrix) is type([])

def test_shape():
    mat = Matrix([[1, 2, 3, 4], [2, 4, 6, 8]])
    assert mat.shape() == (2, 4)
    mat = Matrix()
    assert mat.shape() == (0, 0)

def test_get_row():
    mat = Matrix([[1, 2, 3, 4], [2, 4, 6, 8]])
    assert mat.get_row(1) == [1, 2, 3, 4]
    assert mat.get_row(2) == [2, 4, 6, 8]

    with raises(IndexError):
        mat.get_row(0)
        
    with raises(IndexError):
        mat.get_row(5)


def test_get_column():
    mat = Matrix([[1, 2, 3, 4], [2, 4, 6, 8]])
    assert mat.get_column(1) == [1, 2]
    
    with raises(IndexError):
        mat.get_column(0)
    
    with raises(IndexError):
        mat.get_column(5)