from collections import Counter

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
        raise Exception("Median doesn't make sense w.r.t input")

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

def quantile(x, p):
    if not is_collection(x):
        raise Exception("Quantile can't be calculated w.r.t input")
    
    try:
        if all(isinstance(float(val), float) for val in x):
            p_index = int(len(x) * p)
            return sorted(x)[p_index]
    except ValueError:
        raise Exception('Requires a homogenous collection of numbers')

def mode(x):
    if not is_collection(x):
        raise Exception('Mode can\'t be calculated w.r.t input')

    counts = Counter(x)
    max_count = max(counts.values())
    return [val for val, count in counts.items() if count == max_count]