from functools import wraps


def counter(f):
    cnt = 0

    def count():
        return cnt
    f.counter = count

    @wraps(f)
    def wr(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        return f(*args, **kwargs)

    return wr
