import sys
from collections import defaultdict, deque


def get_text(all_gramm:set, steps, it, n, text=[]):
    if it == 0:
        if n <= 3:
            return True, all_gramm.pop()[:n]
        for three in all_gramm:
            text = list(three)
            is_ok, ans = get_text(all_gramm, steps, it+1, n, text)
            if is_ok:
                return is_ok, ans
        return False, []

    it_parameters = {0: [0, 3, text[:]]}
    idx = 0
    tt = text[:]
    while True:
        curr_idx, curr_len, tt = it_parameters.get(idx, [-1, 3 + idx, tt])
        if idx == -1:
            return False, []
        if curr_len == n:
            return True, tt[:]
        if curr_idx + 1 == len(steps[tuple(tt[-2:])]):
            idx -= 1
        else:
            it_parameters[idx + 1] = [-1, curr_len + 1, tt + [steps[tuple(tt[-2:])][curr_idx + 1]]]
            idx += 1


def main():
    n_words = int(input())
    # with open("anna.txt") as f:
    #     text = f.read().replace("\n    ", " @ ").split()
    text = sys.stdin.read().replace("\n    ", " @ ").split()
    three_gramm = set(tuple(text[i: i + 3]) for i in range(len(text) - 2))
    map_three = defaultdict(list)
    for i in range(len(text) - 3):
        map_three[tuple(text[i: i + 2])].append(text[i + 2])
    for k, v in map_three.items():
        map_three[k] = list(set(v))

    is_ok, res_text = get_text(three_gramm, map_three, 0, n_words)
    if is_ok:
        for i in range(len(res_text) - 1):
            if res_text[i] == "@":
                print("\n    ", end="")
            else:
                print(res_text[i], end="")
                if res_text[i + 1] != "@":
                    print(" ", end="")
        print(res_text[-1] if res_text[i] != "@" else "\n    ", end="")


if __name__ == "__main__":
    main()
