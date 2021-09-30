import pytest
from solutions.task_6 import MyPy


def test_MyPy():
    @MyPy((int, str, int), int)
    def valid(a, b, c=0):
        return len(b * (a + 1)) + c

    valid(3, "--", 10) == 18
    with pytest.raises(TypeError, match=r"Type of argument 2 is not <class 'str'>"):
        valid(3, 7, 10)

    @MyPy((int, str, int), int)
    def valid(a, b, c=0):
        return len(b * (a + 1)) + c

    @MyPy([int, int], int)
    def semivalid(a, b):
        return a / b if a % 2 else a * b

    @MyPy((int for i in range(4)), int)
    def variable(*args, **kwargs):
        return len(args) + len(kwargs)

    for fn, positional, named, res, err in [
        (valid, (3, "--", 10), {}, 18, None),
        (valid, (3, 7, 10), {}, None, "Type of argument 2 is not <class 'str'>"),
        (valid, (3, "--", "*"), {}, None, "Type of argument 3 is not <class 'int'>"),
        (
            valid,
            (3, "--"),
            {"c": 1.23},
            None,
            "Type of argument 'c' is not <class 'int'>",
        ),
        (semivalid, (2, 2), {}, 4, None),
        (semivalid, (2, 2, 3), {}, None, "Function semivalid must have 2 arguments"),
        (semivalid, (1, 2), {}, None, "Type of result is not <class 'int'>"),
        (semivalid, (), {}, None, "Function semivalid must have 2 arguments"),
        (
            semivalid,
            (),
            {"A": 1, "B": 2},
            None,
            r"semivalid\(\) got an unexpected keyword argument 'A'",
        ),
        (variable, (1, 2, 3, 4), {}, 4, None),
        (variable, (1, 2), {"a": 100, "b": 500}, 4, None),
        (
            variable,
            (1, 2),
            {"a": 100},
            None,
            "Function variable must have 4 arguments",
        ),
    ]:
        if res:
            assert fn(*positional, **named) == res
        else:
            with pytest.raises(TypeError, match=err):
                fn(*positional, **named)
