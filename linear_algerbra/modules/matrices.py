class Matrix:
    def __init__(self, *matrix):
        if matrix:
            m = len(matrix)
            n = len(matrix[0]) if matrix[0] else 0
            data_type = type(matrix[m-1][n-1])
            self.matrix = [aij for ai in matrix for aij in ai if type(aij) is data_type]
        else:
            self.matrix = []
