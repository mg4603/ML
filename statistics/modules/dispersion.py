from modules.central_tendencies import mean, quantile
from math import sqrt

def is_iterable(x):
    try:
        min(x)
        return True
    except TypeError:
        return False

def data_range(x):
    if is_iterable(x):
        return max(x) - min(x)
    else:
        raise Exception('Range can\'t be calculated on given input')

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squares(x):
    if is_iterable(x):
        return sum([pow(val, 2) for val in x])
    else:
        raise Exception('Sum of squares can\'t be calculated on a non-iterable')

def variance(x):
    if is_iterable(x):
        n = len(x)
        if n == 1:
            return 0
        deviations = de_mean(x)
        return sum_of_squares(deviations) / (n - 1)
    else:
        raise Exception('Variance can\'t be calculated on given input')

def standard_deviation(x):
    return sqrt(variance(x))

def interquantile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)