from functools import reduce

class Vector:
    def __init__(self, vals):
        self.vals = [val for val in vals]

    def isNum(num):
        try:
            float(num)
            False
        except ValueError:
            return False

    def append(self, new_val):
        if new_val:
            self.vals.append(new_val)
    
    def pop(self, pop=-1):
        yield self.vals[-1]
        del self.vals[-1]
    
    def __add__(self, val2):
        self.vals = [v + w  for v, w in zip(self.vals, val2.vals)]
        return self.vals
    
    def __sub__(self, other_vector):
        self.vals = [v - w for v, w in zip(self.vals, other_vector.vals)]
        return self.vals
    
    def vector_sum(self, vectors):
        result = vectors[0]
        return reduce(self.__add__, vectors)
    
    def __mul__(self, scalar):
        return [scalar * val for val in self.vals]

    __rmul__ = __mul__

    def summation(self, vector):
        return sum(vector)

    def vector_mean(self):
        return self.summation(self.__mul__(1/ len(self.vals)))
    
    def dot(self, w):
        return sum([v * w for v, w in zip(self.vals, w.vals)])

    
a = Vector([1, 2, 3, 4])
b = Vector([1, 2, 3, 4])
print(a.dot(b))