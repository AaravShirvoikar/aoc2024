def solve1():
    with open("./inputs/input16", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    start = next((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'S')
    end = next((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'E')
    
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    paths = []
    visited = {}
    queue = [(start, [start], 0, 0)]
    while queue:
        (y, x), hist, cscore, cdir = queue.pop(0)
        if (y, x) == end:
            paths.append((hist, cscore))
            continue
        
        if ((y, x), cdir) in visited and visited[((y, x), cdir)] < cscore:
            continue
        
        visited[((y, x), cdir)] = cscore
        
        for i, (dy, dx) in enumerate(dirs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(mat) and 0 <= nx < len(mat[0]) and mat[ny][nx] != "#" and (ny, nx) not in hist:
                if i == cdir:
                    queue.append(((ny, nx), hist + [(ny, nx)], cscore + 1, i))
                else:
                    queue.append(((y, x), hist + [], cscore + 1000, i))
    
    min_score = min(p[1] for p in paths)
    print(min_score)

def solve2():
    with open("./inputs/input16", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    start = next((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'S')
    end = next((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'E')
    
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    paths = []
    visited = {}
    queue = [(start, [start], 0, 0)]
    while queue:
        (y, x), hist, cscore, cdir = queue.pop(0)
        if (y, x) == end:
            paths.append((hist, cscore))
            continue
        
        if ((y, x), cdir) in visited and visited[((y, x), cdir)] < cscore:
            continue
        
        visited[((y, x), cdir)] = cscore
        
        for i, (dy, dx) in enumerate(dirs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(mat) and 0 <= nx < len(mat[0]) and mat[ny][nx] != "#" and (ny, nx) not in hist:
                if i == cdir:
                    queue.append(((ny, nx), hist + [(ny, nx)], cscore + 1, i))
                else:
                    queue.append(((y, x), hist + [], cscore + 1000, i))
    
    min_score = min(p[1] for p in paths)
    best_paths = [p for p in paths if p[1] == min_score]
    tiles = {t for p in best_paths for t in p[0]}
    print(len(tiles))

