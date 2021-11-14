class DivStr(str):
    def __add__(self, other):
        return DivStr(super(DivStr, self).__add__(other))

    def __mul__(self, other):
        return DivStr(super(DivStr, self).__mul__(other))

    def __getitem__(self, key):
        if isinstance(key, slice):
            return DivStr(self.__str__()[key.start: key.stop: key.step])
        elif isinstance(key, int):
            return DivStr(self.__str__()[key])

    def __rmul__(self, other):
        return self * other

    def __radd__(self, other):
        return other + self

    def __floordiv__(self, other):
        assert isinstance(other, int)
        step = len(self) // other
        return [self[i * step: (i + 1) * step] for i in range(other)]

    def __mod__(self, other):
        assert isinstance(other, int)
        return self[len(self) - len(self) % other:]

    def center(self, *args, **kwargs):
        return DivStr(self.__str__().center(*args, **kwargs))

    def ljust(self, *args, **kwargs):
        return DivStr(self.__str__().ljust(*args, **kwargs))

    def rjust(self, *args, **kwargs):
        return DivStr(self.__str__().rjust(*args, **kwargs))

    def count(self, *args, **kwargs):
        return self.__str__().count(*args, **kwargs)

    def lower(self):
        return DivStr(self.__str__().lower())

    def capitalize(self):
        return DivStr(self.__str__().capitalize())

    def casefold(self, *args, **kwargs):
        return DivStr(self.__str__().casefold( *args, **kwargs))

    def lower(self):
        return DivStr(self.__str__().lower())

    def lstrip(self, *args, **kwargs):
        return DivStr(self.__str__().lstrip(*args, **kwargs))

    def rstrip(self, *args, **kwargs):
        return DivStr(self.__str__().rstrip(*args, **kwargs))

    def strip(self, *args):
        return DivStr(self.__str__().strip(*args))

    def swapcase(self):
        return DivStr(self.__str__().swapcase())

    def title(self):
        return DivStr(self.__str__().title())

    def upper(self):
        return DivStr(self.__str__().upper())

    def removeprefix(self, *args, **kwargs):
        return DivStr(self.__str__().removeprefix(*args, **kwargs))

    def removesuffix(self, *args, **kwargs):
        return DivStr(self.__str__().removesuffix(*args, **kwargs))

    def join(self, iterable):
        res = DivStr()
        for i, el in enumerate(iterable):
            if i == 0:
                res = res + el
            else:
                res = res + self + el
        return res

    def replace(self, *args, **kwargs):
        return DivStr(self.__str__().replace(*args, **kwargs))
