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