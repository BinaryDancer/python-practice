def chainslice(begin, end, *args):
    res = []
    idx = 0
    for seq in args:
        for el in seq:
            if begin <= idx < end:
                res.append(el)
            if idx >= end:
                break
            idx += 1

    return iter(res)
