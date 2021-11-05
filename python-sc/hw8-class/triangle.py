class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.correct = all([a + b > c, a + c > b, b + c > a, a > 0, b > 0, c > 0])

    def __abs__(self):
        if not self.correct:
            return 0

        p = (self.a + self.b + self.c) * 1.0 / 2.0
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return other < self

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __str__(self):
        return "{:.1f}:{:.1f}:{:.1f}".format(self.a, self.b, self.c)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ge__(self, other):
        return other <= self

    def __bool__(self):
        return self.correct
