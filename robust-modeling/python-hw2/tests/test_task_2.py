import pytest
from solutions.task_2 import even_odd


@pytest.mark.timeout(1)
def test_even_odd():
    for *args, result in [
        (
            [1, 2, 3],
            [6, 5, 4],
            [2, 6, 4, 1, 3, 5],
        ),
        (
            [1],
            [2],
            [3],
            [4],
            [5],
            [6],
            [2, 4, 6, 1, 3, 5],
        ),
    ]:
        assert list(even_odd(*args)) == result

    from random import randrange, seed
    from itertools import islice, repeat

    seed(100500)

    I = (repeat(randrange(1, 5), randrange(5, 15)) for i in range(100000))
    P = 477700
    try:
        g = even_odd(*I)
    except TimeoutError:
        raise Exception
    assert list(islice(g, P, P + 100, 7)) == [
        2,
        4,
        4,
        4,
        4,
        4,
        2,
        1,
        1,
        1,
        1,
        3,
        3,
        3,
        3,
    ]
