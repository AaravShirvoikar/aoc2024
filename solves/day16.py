def solve1():
    with open("./inputs/input16", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    start = next((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'S')
    end = next((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'E')
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = {}
    stack = [(start[0], start[1], 1, 0)]
    min_score = float('inf')
    while stack:
        r, c, dir, score = stack.pop()

        if not (0 <= r < len(mat) and 0 <= c < len(mat[0])) or mat[r][c] == '#':
            continue

        if (r, c) == end:
            min_score = min(min_score, score)
            continue

        if (r, c, dir) in visited and visited[(r, c, dir)] <= score:
            continue

        visited[(r, c, dir)] = score

        nr, nc = r + dirs[dir][0], c + dirs[dir][1]
        stack.append((nr, nc, dir, score + 1))

        for turn in [-1, 1]:
            new_dir = (dir + turn) % 4
            stack.append((r, c, new_dir, score + 1000))

    print(min_score)

