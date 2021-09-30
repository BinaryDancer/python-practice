import csv
from collections import Counter
from solutions.task_3 import counter


def test_counter():
    class C:
        x, y, z = 1, 3, 5

        def X(self):
            return self.x

        def Y(self):
            return self.y

        def __init__(self, dx, dy, dz):
            self.x = dx
            self.Y = dy
            self.Z = dz

    cm, cf, om, of = counter(C, 6, 7, 8)
    assert cm == ["X", "Y"]
    assert cf == ["x", "y", "z"]
    assert om == []
    assert of == ["Y", "Z"]

    cm, cf, om, of = counter(Counter, "qweqweqwe")
    assert cm == [
        "clear",
        "copy",
        "elements",
        "fromkeys",
        "get",
        "items",
        "keys",
        "most_common",
        "pop",
        "popitem",
        "setdefault",
        "subtract",
        "update",
        "values",
    ]
    assert cf == []
    assert om == []
    assert of == []

    cm, cf, om, of = counter(csv.DictReader, "")
    assert cm == []
    assert cf == ["fieldnames"]
    assert om == []
    assert of == ["dialect", "line_num", "reader", "restkey", "restval"]

    class Var:
        val, fun = 1, 2

        def stat(self):
            return 0

        def __init__(self):
            self.fun = lambda x: x * 2 + 1
            self.stat = -1

    cm, cf, om, of = counter(Var)
    assert cm == ["stat"]
    assert cf == ["fun", "val"]
    assert om == ["fun"]
    assert of == ["stat"]
