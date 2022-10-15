def is_iterable(x):
    try:
        min(x)
        return True
    except TypeError:
        return False
