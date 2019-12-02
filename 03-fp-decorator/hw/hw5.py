import time
import functools

counter = 0

def decoratorFunctionWithArguments(arg: str):
    def wrap(f):
        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            global counter
            counter += 1
            t = time.clock()
            res = f(*args, **kwargs)
            t = time.clock() - t
            globals()[arg] = [counter, t]
            return arg
        return wrapped_f
    return wrap


@decoratorFunctionWithArguments('fibon1')
def fib1(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib1(i - 1, next, current + next)

@decoratorFunctionWithArguments('fibon2')
def fib2(n):
    return fib2(n-1) + fib2(n-2) if n > 0 else 1

M = {0: 0, 1: 1}

@decoratorFunctionWithArguments('fibon3')
def fib3(n):
    if n in M:
        return M[n]
    M[n] = fib3(n - 1) + fib3(n - 2)
    return M[n]

@decoratorFunctionWithArguments('fibon4')
def fib4(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
    
fib1(15)
fib2(15)
fib3(15)
fib4(15)
times = [fibon1[1], fibon2[1], fibon3[1], fibon4[1]]
minind = times.index(min(times)) + 1
print("optimal fibonacci algorithm is function number " + str(minind))
