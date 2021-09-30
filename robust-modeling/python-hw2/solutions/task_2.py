from typing import Generator


def even_odd(*args) -> Generator[int, None, None]:
    odd = []
    even = []
    for v in args:
        for el in v:
            if el % 2:
                odd.append(el)
            else:
                even.append(el)
    res = even + odd
    print(len(res))
    for el in res:
        yield el
