def LookSay():
    s = [1]
    while True:
        s2 = []
        cnt = 0
        prev = 0
        for el in s:
            yield el
            if not prev:
                prev = el
                cnt = 1
            elif prev == el:
                cnt += 1
            else:
                s2.append(cnt)
                s2.append(prev)
                prev = el
                cnt = 1
        s2.append(cnt)
        s2.append(prev)
        s = s2
