import string

def letters_range(*args, **kwargs):
    alphabet = list(string.ascii_lowercase)
    if len(args) == 0 or len(args) > 3:
        raise Exception
    if kwargs:
        for key in kwargs:
            alphabet[alphabet.index(key)] = kwargs[key]
    if len(args) == 1:
        return alphabet[0:alphabet.index(args[0]):1]
    if len(args) == 2:
        return alphabet[alphabet.index(args[0]):alphabet.index(args[1]):1]
    if len(args) == 3:
        return alphabet[alphabet.index(args[0]):alphabet.index(args[1]):args[2]]
