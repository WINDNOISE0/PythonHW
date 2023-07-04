def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hashable(key):
            key = str(key)
        result[value] = key
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

result = create_dict(a=1, b='hello', c=tuple([1, 2, 3]))

print(result)