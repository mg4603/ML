from modules.central_tendencies import mean

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
