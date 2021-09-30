from typing import Generator


def fib() -> Generator[int, None, None]:
    x = [0, 1]
    while True:
        yield x[0]
        x = [x[1], x[0] + x[1]]
