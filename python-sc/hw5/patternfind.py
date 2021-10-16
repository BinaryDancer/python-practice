import re
import string

def main():
    s = input()
    p = input()
    reg = p.split("@")
    idx = 0
    while True:
        last_idx = idx
        for i, el in enumerate(reg):
            tmp = s.find(el, last_idx)
            if tmp == -1:
                print(-1)
                return
            curr_idx = s.index(el, last_idx)
            if i == 0:
                idx = curr_idx
            elif last_idx != curr_idx:
                idx += 1
                break
            last_idx = curr_idx + len(el) + 1
            if i == len(reg) - 1:
                print(idx)
                return


if __name__ == "__main__":
    main()
