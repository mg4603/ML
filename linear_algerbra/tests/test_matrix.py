from modules.matrices import Matrix

def test_Matrix():
    mat = Matrix([[1, 2, 3, 4], [2, 4, 6, 8]])
    mat2 = Matrix()
    assert mat.matrix[0][0] == 1
    assert len(mat2.matrix) == 0
    assert type(mat2.matrix) is type([])

def test_shape():
    mat = Matrix([[1, 2, 3, 4], [2, 4, 6, 8]])
    assert mat.shape() == (2, 4)