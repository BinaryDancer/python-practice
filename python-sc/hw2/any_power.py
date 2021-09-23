from collections import defaultdict


def main():
    x = int(input())
    d = defaultdict(int)
    cnt = 0
    for i in range(2, x + 1):
        while x % i == 0:
            d[i] += 1
            x //= i
        if d.get(i) and d[i] % 2:
            cnt += 1
    if len(d) == 1:
        for el in d.keys():
            if d[el] == 1:
                print("NO")
            else:
                print("YES")
    elif cnt == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
