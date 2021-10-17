import decimal
from decimal import Decimal


def memory_wrapper(f):
    cache = {}

    def fun(v, p):
        res = cache.get(str(v) + " " + str(p))
        if res is None:
            res = f(v, p)
            cache[str(v) + " " + str(p)] = res
        return res
    return fun


@memory_wrapper
def factorial(v, p):
    if v == 1 or v == 0:
        return 1
    return v * factorial(v-1, p)


@memory_wrapper
def bin_pow(v, p):
    if p == 0:
        return 1
    if p == 1:
        return v
    if p & 1:
        return v * bin_pow(v, p - 1)
    tmp = bin_pow(v, p // 2)
    return tmp * tmp


def get_pi():
    pi = Decimal(0)
    for k in range(150):
        pi += (Decimal(-1) ** (k & 1)) * Decimal(factorial(6 * k, 0)) \
              / bin_pow(factorial(k, 0), 3) / factorial(3 * k, 0) \
              * (13591409 + 545140134 * k) / (640320 ** (3 * k))

    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = 1 / pi
    return pi


def sin(x):
    res = Decimal(0)
    for k in range(1, 150):
        res += (Decimal(-1) ** ((k + 1) & 1) * Decimal(bin_pow(x, (2 * k - 1)))) / Decimal(factorial(2 * k - 1, 0))

    return res


def cos(x):
    res = Decimal(0)
    for k in range(150):
        res += ((Decimal(-1) ** (k & 1)) * Decimal(bin_pow(x, (2 * k)))) / Decimal(factorial(2 * k, 0))

    return res


def main():
    x = Decimal(input())
    precision = int(input())
    decimal.getcontext().prec = 1010
    new_x = x * (get_pi() / Decimal(200))
    res = sin(new_x) / cos(new_x)

    print(decimal.Context(prec=precision).create_decimal(res))


if __name__ == "__main__":
    main()
