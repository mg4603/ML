from functools import reduce
from math import sqrt

class Vector:
    def __init__(self, vals = []):
        self.vals = [val for val in vals]
    
    def __add__(self, val2):
        self.vals = [v + w  for v, w in zip(self.vals, val2.vals)]
        return self.vals
    
    def __sub__(self, other_vector):
        self.vals = [v - w for v, w in zip(self.vals, other_vector.vals)]
        return self.vals

    def __len__(self):
        return len(self.vals)

    def __mul__(self, scalar):
        return [scalar * val for val in self.vals]

    __rmul__ = __mul__

    def isNum(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def append(self, new_val):
        if new_val:
            self.vals.append(new_val)
    
    def pop(self, pop=-1):
        yield self.vals[-1]
        del self.vals[-1]
    
    def vector_sum(self, vectors):
        return reduce(self.__add__, vectors)

    def summation(self, vector):
        return sum(vector)

    def vector_mean(self):
        return self.summation(self.__mul__(1/ len(self.vals)))
    
    def dot(self, w):
        return sum([v * w for v, w in zip(self.vals, w.vals)])

    def sum_of_squares(self):
        return self.dot(self)
    
    def magnitude(self):
        return sqrt(self.sum_of_squares())

    def squared_distance(self, w):
        return Vector(self - w).sum_of_squares()
    
    def distance(self, w):
        return self.magnitude(self.squared_distance(w))

