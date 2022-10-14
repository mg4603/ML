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

def median(x):
    if not is_collection(x):
        raise Exception("Mean doesn't make sense w.r.t input")

    try:
        if all(isinstance(float(val), float) for val in x):
            n = len(x)
            x = sorted(x)
            midpoint = n//2
            if n % 2 == 1:
                return x[midpoint]
            else:
                return (x[midpoint-1] + x[midpoint])/2
    except ValueError:
        raise Exception("Requires a homogenous collection of numbers") 

