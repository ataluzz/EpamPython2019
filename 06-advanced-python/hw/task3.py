""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""

class Suppressor:
    
    def __init__(self, *error_names):
        self.error_names = error_names
        
    def __enter__(self):
        pass
        
    def __exit__(self, exp_type, exp_value, exp_traceback):
        return issubclass(exp_type, self.error_names)
        
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
