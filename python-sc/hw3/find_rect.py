def get_v(x, y, mat):
    n = len(mat)
    m = len(mat[0])
    return max(0, mat[x - 1][y], mat[x + 1][y], mat[x][y - 1], mat[x][y + 1])


def main():
    s = input()
    s = input()
    mat = [[0] * len(s)]
    while s[0] != '-':
        mat.append([(-1 if x == '.' else 0) for x in s])
        s = input()
    mat.append([0] * len(s))
    cnt = 0
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0])):
            if mat[i][j] == 0:
                v = get_v(i, j, mat)
                if v == 0:
                    cnt += 1
                    v = cnt
                mat[i][j] = v
    print(cnt)


if __name__ == "__main__":
    main()
