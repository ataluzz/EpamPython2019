from functools import reduce

def is_armstrong(number):
    n = reduce(lambda x, y: x + y, map(lambda x: int(x)**len(str(number)), str(number)))
    return(number == n)

assert is_armstrong(153) == True
assert is_armstrong(10) == False

def collatz_steps(n):
    return((1 + collatz_steps(n*3 + 1) if n % 2 else (1 + collatz_steps(n / 2))) if n != 1 else 0)

collatz_steps(1000000)

def applydecorator(decor):
    def wrapper(func):
        def inner(*args, **kwargs):
            return decor(func, *args, **kwargs)
        return inner
    return wrapper
