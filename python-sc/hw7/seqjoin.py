from itertools import chain


def joinseq(*args):
    my_args = []
    for seq in [iter(el) for el in args]:
        new_it = chain.from_iterable([seq, ["abracadabra"]])
        my_args.append([next(new_it), new_it])

    while my_args:
        idx = 0
        min_v = my_args[0][0]
        for i, (v, seq) in enumerate(my_args):
            if v < min_v:
                min_v = v
                idx = i
        my_args[idx][0] = next(my_args[idx][1])
        if my_args[idx][0] == "abracadabra":
            my_args.pop(idx)
        yield min_v
