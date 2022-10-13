class Vector:
    def __init__(self, vals):
        self.vals = [val for val in vals]

    def append(self, new_val):
        if new_val:
            self.vals.append(new_val)
    
    def pop(self, pop=-1):
        yield self.vals[-1]
        del self.vals[-1]
    
    def __add__(self, other_vector):
        self.vals = [v + w  for v, w in zip(self.vals, other_vector.vals)]
        return self.vals
