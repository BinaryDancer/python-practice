def joinseq(*args):
    my_args: list = [[next(seq), seq] for seq in [iter(el) for el in args]]

    while my_args:
        idx = 0
        min_v = my_args[0][0]
        for i, (v, seq) in enumerate(my_args):
            if v < min_v:
                min_v = v
                idx = i
        try:
            my_args[idx][0] = next(my_args[idx][1])
        except Exception as e:
            my_args.pop(idx)
        yield min_v
