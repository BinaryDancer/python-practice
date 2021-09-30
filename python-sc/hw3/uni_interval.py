def main():
    v: list = eval("[" + input() + "]")
    v.sort(key=lambda x: x[0])
    curr = list(v[0])
    res_len = 0
    for el in v:
        if el[0] > curr[1]:
            res_len += curr[1] - curr[0]
            curr = list(el)
        else:
            curr[1] = max(curr[1], el[1])
    res_len += curr[1] - curr[0]
    print(res_len)


if __name__ == "__main__":
    main()
