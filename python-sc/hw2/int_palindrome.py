def main():
    x = int(input())
    x1 = x
    x2 = 0
    while x1 != 0:
        x2 = x2 * 10 + (x1 % 10)
        x1 //= 10
    if x2 == x:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
