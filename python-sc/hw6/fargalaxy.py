def get_far(positions):
    def get_distance(point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2

    i1, i2 = 0, 0
    max_distance = 0.0
    idx1 = 0
    idx2 = 0

    for i, p1 in enumerate(positions):
        for j in range(i + 1, len(positions)):
            p2 = positions[j]
            curr_dist = get_distance(p1, p2)
            if curr_dist > max_distance:
                max_distance = curr_dist
                idx1 = i
                idx2 = j
    return idx1, idx2


def main():
    s = input()
    galaxies = []
    geoposition = []
    while s[0] != '.':
        x, y, z, name = s.split()
        x = float(x)
        y = float(y)
        z = float(z)
        galaxies.append(name)
        geoposition.append((x, y, z))
        s = input()

    i1, i2 = get_far(geoposition)
    if galaxies[i1] < galaxies[i2]:
        print(galaxies[i1], galaxies[i2])
    else:
        print(galaxies[i2], galaxies[i1])


if __name__ == "__main__":
    main()
