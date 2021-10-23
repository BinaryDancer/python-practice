from math import sqrt


def to_max(x, v, st=0):
    for i in range(st, len(v)):
        if v[i] < x:
            yield i, v[i]
        else:
            return i, v[i]


def main():
    seq = set(eval(input()))
    all_sqr = set()
    mm = int(sqrt(max(seq))) + 1
    for i1 in range(1, mm):
        for i2 in range(i1, int(sqrt(mm * mm - i1 * i1)) + 1):
            sq = sqrt(mm * mm - i1 * i1 - i2 * i2)
            if sq > 0:
                for i3 in range(i2, int(sq + 1)):
                    all_sqr.add(i1 * i1 + i2 * i2 + i3 * i3)
    cnt = 0
    for el in seq:
        if el in all_sqr:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
