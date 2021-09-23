def process_set(numbers: list, commands: list) -> int:
    s = set(numbers)
    for action in commands:
        if action[0] == 'p':
            s.pop()  # pops random value, if empty than KeyError
        elif action[0] == 'd':
            s.discard(int(action.split()[1]))  # remove value v from set
        else:
            s.remove(int(action.split()[1]))  # remove value v from set, if v is not in than KeyError
    return sum(s)


# should be true
assert process_set(
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [
        "pop",
        "remove 9",
        "discard 9",
        "discard 8",
        "remove 7",
        "pop",
        "discard 6",
        "remove 5",
        "pop",
        "discard 5",
    ],
) == 4

try:
    process_set(
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [
            "remove 9",
            "remove 9",
        ],
    )
except Exception as ex:
    assert isinstance(ex, KeyError)

try:
    process_set(
        [1],
        [
            "pop",
            "pop",
        ],
    )
except Exception as ex:
    assert isinstance(ex, KeyError)

assert process_set(
    [8, 9],
    [
        "discard 9",
        "discard 9",
    ],
) == 8
