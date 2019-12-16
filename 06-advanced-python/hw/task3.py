""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""

class Suppressor:
    
    def __init__(self, error_name):
        self.error_name = error_name
        
    def __enter__(self):
        return self.error_name
        
    def __exit__(self, exp_type, exp_value, exp_traceback):
        if exp_traceback is self.error_name:
            return True
        return True
        
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
