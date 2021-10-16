def main():
    n, m = map(int, input().split(","))
    line_sep = "=" * m
    mid_sep = " | "
    sep_size = len(mid_sep)
    max_size = len("{} * {} = {}".format(n, n, n * n))
    el_size = len(str(n))
    res_size = len(str(n * n))

    k = (m + sep_size) // (max_size + sep_size)

    print(line_sep)
    for raw in range(n // k + (1 if n % k > 0 else 0)):
        for inside_raw in range(n):
            print(mid_sep.join(
                ["{i:>{sel}} * {j:<{sel}} = {res:<{sres}}".format(i=inside_col + 1,
                                                                  j=inside_raw + 1,
                                                                  sel=el_size,
                                                                  res=(inside_raw + 1) * (inside_col + 1),
                                                                  sres=res_size) for inside_col in
                 range(raw * k, (raw + 1) * k) if inside_col < n]
            ))
        print(line_sep)


if __name__ == "__main__":
    main()
