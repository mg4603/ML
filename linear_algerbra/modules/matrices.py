class Matrix:
    def __init__(self, *Matrix):
        if Matrix:
            self.num_rows = len(Matrix[0])
            self.num_cols = len(Matrix[0][0]) if Matrix[0] else 0
            data_type = type(Matrix[0][self.num_rows-1][self.num_cols-1])
            self.Matrix = [[aij  for aij in ai if type(aij) is data_type] for ai in Matrix[0] ]
        else:
            self.Matrix = []
            self.num_rows = 0
            self.num_cols = 0

    def shape(self):
        return self.num_rows, self.num_cols

    def get_row(self, row_num):
        if row_num < 1 or row_num > self.num_rows:
            raise IndexError
        return self.Matrix[row_num-1]

    def get_column(self, col_num):
        if col_num < 1 or col_num > self.num_cols:
            raise IndexError
        return [Mat_i[col_num-1] for Mat_i in self.Matrix]
    
    def make_matrix(self, num_rows, num_cols, entry_fn):
        """
        create a num_rows x num_cols matrix 
        whose (i, j)th entry is entry_fn(i,j)
        """
        self.Matrix = [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]
        self.num_cols, self.num_cols = num_rows, num_cols
        return self.Matrix

def is_diagonal(i, j):
    return 1 if i == j else 0