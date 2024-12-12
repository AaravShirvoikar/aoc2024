def solve1():
    with open("./inputs/input12", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, visited):
        if (x, y) in visited:
            return 0, 0

        visited.add((x, y))
        a = 1
        p = 0
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                if mat[nx][ny] == mat[x][y]:
                    sa, sp = dfs(nx, ny, visited)
                    a += sa
                    p += sp
                else:
                    p += 1
            else:
                p += 1
        return a, p

    visited = set()
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i, j) not in visited:
                a, p = dfs(i, j, visited)
                res += a * p

    print(res)

