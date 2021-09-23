def main():
    x, y, r = map(int, input().split(','))
    s = input()
    check = True
    x1, y1 = map(int, s.split(','))
    while x1 or y1:
        if ((x1 - x) ** 2) + ((y1 - y) ** 2) > r**2:
            check = False
            print("NO")
            break
        s = input()
        x1, y1 = map(int, s.split(','))
    if check:
        print("YES")


if __name__ == "__main__":
    main()
