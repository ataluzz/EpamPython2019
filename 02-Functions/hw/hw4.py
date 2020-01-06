import inspect

def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_function(*args, **kwargs):
        new_function.__name__ = "func_" + func.__name__
        new_function.__doc__ = (f'A func implementation of {str(new_function.__name__)} ' 
                               f'with pre-applied arguments being: '
                               f'{str(fixated_args)} '
                               f'{str(fixated_kwargs)} '
                               f'source_code: '
                               f'{inspect.getsource(new_function)}')
        all_args = list(fixated_args + args)
        all_kwargs = {**fixated_kwargs, **kwargs}
        all_args = all_args + list(all_kwargs[key] for key in all_kwargs)
        res = func(all_args)
        return res
    return new_function
