def solve1():
    with open("./inputs/input18", "r") as file:
        lines = file.readlines()

    size = 71
    mat = [["." for _ in range(size)] for _ in range(size)]

    bytes = 1024
    for i in range(bytes):
        x, y = map(int, lines[i].strip().split(","))
        mat[y][x] = '#'

    start = (0, 0)
    end = (size - 1, size - 1)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = [start]
    visited = set()
    visited.add(start)
    dist = {start: 0}
    while queue:
        curr = queue.pop(0)
        if curr == end:
            print(dist[curr])
            break

        for dx, dy in dirs:
            nx, ny = curr[0] + dx, curr[1] + dy
            if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and mat[ny][nx] != '#':
                visited.add((nx, ny))
                queue.append((nx, ny))
                dist[(nx, ny)] = dist[curr] + 1

def solve2():
    with open("./inputs/input18", "r") as file:
        lines = file.readlines()

    size = 71
    mat = [["." for _ in range(size)] for _ in range(size)]

    bytes = 1024
    for i in range(bytes):
        x, y = map(int, lines[i].strip().split(","))
        mat[y][x] = '#'

    start = (0, 0)
    end = (size - 1, size - 1)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(bytes, len(lines)):
        x, y = map(int, lines[i].strip().split(","))
        mat[y][x] = '#'
        queue = [start]
        visited = set()
        visited.add(start)
        dist = {start: 0}
        flag = False
        while queue:
            curr = queue.pop(0)
            if curr == end:
                flag = True
                break

            for dx, dy in dirs:
                nx, ny = curr[0] + dx, curr[1] + dy
                if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and mat[ny][nx] != '#':
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    dist[(nx, ny)] = dist[curr] + 1

        if not flag:
            print(lines[i].strip())
            return

