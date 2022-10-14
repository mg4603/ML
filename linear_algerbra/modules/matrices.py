class Matrix:
    def __init__(self, *matrix):
        if matrix:
            self.num_rows = len(matrix)
            self.num_cols = len(matrix[0]) if matrix[0] else 0
            data_type = type(matrix[self.num_rows-1][self.num_cols-1])
            self.matrix = [aij for ai in matrix for aij in ai if type(aij) is data_type]
        else:
            self.matrix = []

