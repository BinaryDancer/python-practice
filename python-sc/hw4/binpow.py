from sys import stdin


def BinPow(x, n, op=int.__mul__):
    if n == 1:
        return x
    if n % 2 == 1:
        return op(x, BinPow(x, n - 1, op))
    a = BinPow(x, n / 2, op)
    return op(a, a)


def main():
    for line in stdin:
        exec(line)


if __name__ == "__main__":
    main()
