def check(k, p):
    if ((k * (10 ** p - k)) % (k * 10 - 1)) != 0:
        return -1
    else:
        v = (k * (10 ** p - k)) // (k * 10 - 1)
        return v


def main():
    k = int(input())
    p = 0
    v = check(k, p)
    while v == -1:
        p += 1
        v = check(k, p)
    print(v*10 + k)


if __name__ == "__main__":
    main()
