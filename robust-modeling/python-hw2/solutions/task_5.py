from collections import defaultdict


class StringMinus(str):
    def __sub__(self, other):
        if isinstance(other, str):
            other = StringMinus(other)
        elif not isinstance(other, StringMinus):
            raise Exception("Wrong type of argument: {}, Should be str or StringMinus".format(type(other)))
        d = defaultdict(int)
        for el in other:
            d[el] += 1

        elements = self.__iter__()
        res = []
        for el in elements:
            if d[el] > 0:
                d[el] -= 1
            else:
                res.append(el)
        return StringMinus("".join(res))

    def __add__(self, other):
        return StringMinus(super(StringMinus, self).__add__(other))

    def __mul__(self, other):
        return StringMinus(super(StringMinus, self).__mul__(other))

    def __getitem__(self, key):
        if isinstance(key, slice):
            return StringMinus(self.__str__()[key.start: key.stop: key.step])
        elif isinstance(key, int):
            return StringMinus(self.__str__()[key])

    def replace(self, *args):
        return StringMinus(super(StringMinus, self).replace(*args))

    def count(self, *args):
        return self.__str__().count(*args)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __radd__(self, other):
        return StringMinus(other.__add__(self.__str__()))

    def center(self, *args):
        return StringMinus(self.__str__().center(*args))

    def strip(self, *args):
        return StringMinus(self.__str__().strip(*args))
