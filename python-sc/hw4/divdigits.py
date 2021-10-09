from collections import defaultdict


def divdigit(n):
    d = defaultdict(int)
    for el in str(n):
        d[int(el)] += 1

    res = 0
    for el, k in d.items():
        if el != 0 and n % el == 0:
            res += k
    return res


def main():
    eval(input())


if __name__ == "__main__":
    main()
