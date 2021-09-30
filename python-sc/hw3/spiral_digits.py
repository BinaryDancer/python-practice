class Spiral:
    mat = []
    curr = (0, 0)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    curr_v = 0
    x = 0

    def __init__(self, n, m):
        self.mat = [[-1] * m for _ in range(n)]
        self.mat[0][0] = 0
        self.n = n
        self.m = m

    def check(self):
        next_pos = (self.curr[0] + self.moves[self.curr_v][0], self.curr[1] + self.moves[self.curr_v][1])
        if next_pos[0] < 0 or next_pos[0] >= self.n or next_pos[1] < 0 or next_pos[1] >= self.m:
            return None
        elif self.mat[next_pos[0]][next_pos[1]] != -1:
            return None
        return next_pos

    def move(self):
        times = 0
        while times < 2:
            mv = self.check()
            if mv:
                self.curr = mv
                self.x = (self.x + 1) % 10
                self.mat[self.curr[0]][self.curr[1]] = self.x
                return True
            self.curr_v = (self.curr_v + 1) % 4
            times += 1
        return False


def main():
    m, n = map(int, input().split(","))
    s = Spiral(n, m)
    while s.move():
        pass
    for line in s.mat:
        print(*line)


if __name__ == "__main__":
    main()
