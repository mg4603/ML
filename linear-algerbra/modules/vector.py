class Vector:
    def __init__(self, vals):
        self.vals = [val for val in vals]

    def append(self, new_val):
        if new_val:
            self.vals.append(new_val)
    
    