import inspect


_mypy_cache = dict()


def MyPy(args_types, res_type):
    def inner(func):
        def newfunc(*args, **kwargs):
            if func.__name__ not in _mypy_cache.keys():
                _mypy_cache[func.__name__] = list(args_types)
            new_args = _mypy_cache[func.__name__]
            if len(args) + len(kwargs) != len(new_args):
                raise TypeError("Function {} must have {} arguments".format(func.__name__, len(new_args)))
            for i in range(len(args)):
                if not isinstance(args[i], new_args[i]):
                    raise TypeError("Type of argument {} is not {}".format(i + 1, new_args[i]))

            if len(args) < len(new_args):
                inspected = inspect.getfullargspec(func)
                named_args = list(inspected.args[len(args):])
                if not inspected.varkw:
                    for el in kwargs.keys():
                        if el not in named_args:
                            raise TypeError("{}() got an unexpected keyword argument '{}'".format(func.__name__, el))
                for i, el in enumerate(named_args):
                    tmp_type = new_args[i + len(args)]
                    if not isinstance(kwargs.get(el, None), tmp_type):
                        raise TypeError("Type of argument '{}' is not {}".format(el, new_args[i + len(args)]))
            res = func(*args, **kwargs)
            if isinstance(res, res_type):
                return res
            else:
                raise TypeError("Type of result is not {}".format(res_type))

        return newfunc

    return inner
