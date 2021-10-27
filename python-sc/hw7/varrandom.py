import random
import itertools


def randomes(args):
    my_args = []
    for i, ranges in enumerate(args):
        el = [x for x in ranges]
        my_args.append(el)
        yield random.randint(el[0], el[1])
    while True:
        for el in my_args:
            yield random.randint(el[0], el[1])
