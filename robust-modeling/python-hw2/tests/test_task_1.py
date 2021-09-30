from solutions.task_1 import fib


def test_fib():
    f = fib()
    assert next(f) == 0
    assert next(f) == 1
    assert next(f) == 1
    assert next(f) == 2
    assert next(f) == 3
    assert next(f) == 5
    assert next(f) == 8
    assert next(f) == 13

    for _ in range(1000):
        next(f)

    assert (
        next(f)
        == 2042002971870066065922491212196382680607147253289366532826965484994220499915473279749837677306845163604089753144121280064929639593676573049781351354479810278536145564533047532284708282169650119738487320831448896
    )
