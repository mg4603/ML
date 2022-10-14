class Matrix:
    def __init__(self, *matrix):
        if matrix:
            self.num_rows = len(matrix[0])
            self.num_cols = len(matrix[0][0]) if matrix[0] else 0
            data_type = type(matrix[0][self.num_rows-1][self.num_cols-1])
            self.matrix = [[aij  for aij in ai if type(aij) is data_type] for ai in matrix[0] ]
        else:
            self.matrix = []

