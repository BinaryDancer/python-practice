def squares(w, h, *args):
    res = [['.' for x in range(w)] for y in range(h)]
    for i in range(h):
        for j in range(w):
            for x, y, s, c in args:
                if y <= i < y + s and x <= j < x + s:
                    res[i][j] = c
    for line in res:
        print("".join(line))


# squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))
