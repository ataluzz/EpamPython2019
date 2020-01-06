def make_it_count(func, counter_name):
    def function(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)
    return function

def func1():
    print("Hello, it's me")

asd = 0
funct = make_it_count(func1, 'asd')
for i in range(10):
    funct()
    print(asd)
