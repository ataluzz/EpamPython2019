import inspect

def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_function(*args, **kwargs):
        '''A func implementation of {func_name}
        with pre-applied arguments being:
        {fixated_args}
        {fixated_kwargs}
        source_code:
        {source_code}'''
        
        new_function.__name__ = "func_" + func.__name__
        new_function.__doc__ = new_function.__doc__.replace('{func_name}', str(new_function.__name__))
        new_function.__doc__ = new_function.__doc__.replace('{fixated_args}', str(fixated_args))
        new_function.__doc__ = new_function.__doc__.replace('{fixated_kwargs}', str(fixated_kwargs))
        new_function.__doc__ = new_function.__doc__.replace('{source_code}', inspect.getsource(new_function))

        if args or kwargs:
            all_args = fixated_args + args
            all_kwargs = {**fixated_kwargs, **kwargs}
            res = func(all_args, all_kwargs)
            return res
        else:
            res = func(fixated_args, fixated_kwargs)
            return res
    return new_function
