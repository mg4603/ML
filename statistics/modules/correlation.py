from modules.central_tendencies import is_collection
from modules.dispersion import de_mean, standard_deviation

def dot(x, y):
    if not is_collection(x) and not is_collection(y):
        raise Exception('Dot product doesn\'t make sense for the given input')
    else:
        n = len(x)
        if n != len(y):
            raise Exception('Input vectors must be of the same size')
        return sum([i * j for i, j in zip(x, y)])

def covariance(x, y):
    if not is_collection(x) and not is_collection(y):
        raise Exception("Input doesn't allow calculation of covariance")
    else:
        n = len (x)
        if len(y) != n:
            raise Exception('Input vectors must be of the same size')
        return dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    n = len(x)
    if len(y) != n:
        raise Exception('Input vectors must be of same size')
    
    st_dev_x = standard_deviation(x)
    st_dev_y = standard_deviation(y)
    if st_dev_x > 0 and st_dev_y > 0:
        return covariance(x, y) / st_dev_x / st_dev_y
    else:
        return 0