def process_list(commands: list) -> list:
    res = []
    for action in commands:
        if action[0] == "i":
            i, e = map(int, action.split()[1:])
            res.insert(i, e)
        elif action[:3] == "rem":
            res.remove(int(action.split()[1]))
        elif action[0] == "a":
            res.append(int(action.split()[1]))
        elif action[0] == "s":
            res.sort()
        elif action[0] == "p":
            res.pop()
        else:
            res.reverse()
    return res


assert process_list(["append 1", "append 2", "insert 1 3"]) == [1, 3, 2]  # should be true
assert process_list(["insert 0 5", "insert 1 10", "insert 0 6",
                     "remove 6", "append 9", "append 1", "sort", "pop", "reverse"]) == [9, 5, 1]
