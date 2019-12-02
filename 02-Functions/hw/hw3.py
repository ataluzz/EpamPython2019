def make_it_count(func, counter_name: str):
    def function():
        globals()[counter_name] += 1
        func()
    return function

def func1():
    print("Hello, it's me")

asd = 0
funct = make_it_count(func1, 'asd')
for i in range(10):
    funct()
    print(asd)
