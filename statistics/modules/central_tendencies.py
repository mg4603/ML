def is_collection(collection):
    try:
        len(collection)
        return True
    except TypeError:
        return False
        