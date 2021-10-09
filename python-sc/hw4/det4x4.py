def det(mat):
    res = 0
    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(4):
                for i4 in range(4):
                    mul = [i1, i2, i3, i4]
                    if len(set(mul)) == 4:
                        p = sum([1 for i in range(4) for j in range(i+1, 4) if mul[i] > mul[j]])
                        res += ((-1) ** p) * mat[0][i1] * mat[1][i2] * mat[2][i3] * mat[3][i4]

    return res


def main():
    mat = eval(input())
    print(det(mat))


if __name__ == "__main__":
    main()
