from functools import wraps


def cast(out_type):
    def decorator(f):
        @wraps(f)
        def wr(*args, **kwargs):
            res = f(*args, **kwargs)
            return out_type(res)
        return wr
    return decorator
