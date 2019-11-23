counter_name = 0

def make_it_count(func, counter_name):
    def function():
        global counter_name
        counter_name += 1
        func()
    return function
