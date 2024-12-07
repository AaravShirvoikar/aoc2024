def solve1():
    with open("./inputs/input06", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos = next(((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == '^'))

    curr = 0
    x, y = pos
    visited = set()
    visited.add((x, y))

    while True:
        dx, dy = dirs[curr]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(mat) or ny < 0 or ny >= len(mat[0]):
            break

        if  mat[nx][ny] == '#':
            curr = (curr + 1) % 4
        else:
            x, y = nx, ny
            visited.add((x, y))

    res = len(visited)
    print(res)

def solve2():
    with open("./inputs/input06", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    pos = next(((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == '^'))

    def check(mat, ipos=None, idir=None):
        if ipos is None:
            ipos = pos
        if idir is None:
            idir = 0

        visited = set()
        visited.add(ipos)
        visited_map = {}
        cpos = ipos
        cdir = idir

        while True:
            dx, dy = dirs[cdir]
            nx, ny = cpos[0] + dx, cpos[1] + dy

            if nx < 0 or nx >= len(mat) or ny < 0 or ny >= len(mat[0]):
                return False, visited, visited_map

            if mat[nx][ny] == '#':
                cdir = (cdir + 1) % 4
                continue

            visited.add((nx, ny))

            if (nx, ny) not in visited_map:
                visited_map[(nx, ny)] = (cpos, cdir)
            elif visited_map[(nx, ny)] == (cpos, cdir):
                return True, None, None

            cpos = (nx, ny)

    _, ivisited, ientry = check(mat)

    if not ivisited or not ientry:
        return

    ivisited.remove(pos)

    res = 0
    for x, y in ivisited:
        mat[x][y] = '#'
        ipos, idir = ientry[(x, y)]

        loop, _, _ = check(mat, ipos, idir)

        if loop:
            res += 1

        mat[x][y] = '.'

    print(res)

