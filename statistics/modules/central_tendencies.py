def is_collection(collection):
    try:
        len(collection)
        return True
    except TypeError:
        return False
        
def mean(x):
    if not is_collection(x):
        raise Exception("Mean doesn't make sense w.r.t input")

    try:
        if all(isinstance(float(val), float) for val in x):
            return sum(x)/ len(x)
    except ValueError:
        raise Exception("Requires a homogenous collection of numbers") 
