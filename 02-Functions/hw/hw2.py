def atom(val = None):
    def get_value():
        return val
    
    def set_value(new_value):
        nonlocal val
        val = new_value
        return val
    
    def process_value(*functions):
        nonlocal val
        for f in functions:
            val = f(val)
        return val
    
    def delete_value():
        nonlocal val
        del val
        
    return (get_value, set_value, process_value, delete_value)
