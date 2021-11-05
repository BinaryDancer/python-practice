from fractions import Fraction
from itertools import cycle


class Sausage:
    default_size = 12

    def __init__(self, material="pork!", size=1):
        self.material: str = material
        self.size: Fraction = Fraction(size)

    def __add__(self, other):
        return Sausage(self.material, self.size + other.size)

    def __sub__(self, other):
        return Sausage(self.material, self.size - other.size)

    def __mul__(self, other):
        return Sausage(self.material, self.size * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return Sausage(self.material, self.size / other)

    def __str__(self):
        res = []

        full_size = int(self.size)
        one_full = [0, 0, 0]
        one_full[0] = ["/"] + ["-" for _ in range(Sausage.default_size)] + ["\\"]
        tmp_math = cycle(self.material)
        one_full[1] = ["|"] + [next(tmp_math) for _ in range(Sausage.default_size)] + ["|"]
        one_full[2] = ["\\"] + ["-" for _ in range(Sausage.default_size)] + ["/"]
        for i in range(full_size):
            res.append(one_full)

        cropped_size = int((self.size - full_size) * Sausage.default_size)
        if full_size == 0 or cropped_size > 0:
            cropped = [0, 0, 0]
            cropped[0] = ["/"] + ["-" for _ in range(cropped_size)] + ["|"]
            tmp_math = cycle(self.material)
            cropped[1] = ["|"] + [next(tmp_math) for _ in range(cropped_size)] + ["|"]
            cropped[2] = ["\\"] + ["-" for _ in range(cropped_size)] + ["|"]
            res.append(cropped)
        return "\n".join(
            ["".join(["".join(res[i][0]) for i in range(len(res))]),
             "".join(["".join(res[i][1]) for i in range(len(res))]),
             "".join(["".join(res[i][1]) for i in range(len(res))]),
             "".join(["".join(res[i][1]) for i in range(len(res))]),
             "".join(["".join(res[i][2]) for i in range(len(res))])
             ]
        )

    def __abs__(self):
        if self.size < 0:
            return 0
        return self.size

    def __bool__(self):
        return bool(abs(self))
