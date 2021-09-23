def lists_intersections(listA: list, listB: list) -> list:
    res = []
    for el in listB:
        res.append([i + 1 for i, x in enumerate(listA) if x == el] or [-1])
    return res


# should be true
assert lists_intersections(["a", "b", "a"], ["a", "c", "d"]) == [
    [1, 3],
    [-1],
    [-1]
]
