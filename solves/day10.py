def solve1():
    with open("./inputs/input10", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, visited, peaks):
        if mat[x][y] == '9':
            peaks.add((x, y))
            return

        visited.add((x, y))
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]

            if (0 <= nx < len(mat) and 
                0 <= ny < len(mat[0]) and 
                (nx, ny) not in visited):
                if mat[nx][ny] == str(int(mat[x][y]) + 1):
                    dfs(nx, ny, visited, peaks)

    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '0':
                peaks = set()
                visited = set()
                dfs(i, j, visited, peaks)
                res += len(peaks)

    print(res)

def solve2():
    with open("./inputs/input10", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, visited):
        if not mat[x][y].isdigit():
            return 0

        curr = int(mat[x][y])
        if curr == 9:
            return 1

        visited.add((x, y))
        total = 0
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]

            if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and (nx, ny) not in visited:
                if not mat[nx][ny].isdigit():
                    continue

                next = int(mat[nx][ny])
                if next == curr + 1:
                    total += dfs(nx, ny, visited.copy())

        return total

    res = 0
    for i, line in enumerate(mat):
        for j, no in enumerate(line):
            if no == '0':
                visited = set()
                res += dfs(i, j, visited)

    print(res)

