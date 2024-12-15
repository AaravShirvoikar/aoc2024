def solve1():
    with open("./inputs/input15", "r") as file:
        data = file.read().split("\n\n")

    mat = [list(row.strip()) for row in data[0].split("\n")]
    moves = data[1].replace("\n", "").strip()
    dirs = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    pos = next(((i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == '@'))
    for move in moves:
        dx, dy = dirs[move]
        nx, ny = pos[0] + dx, pos[1] + dy

        if mat[nx][ny] == '#':
            continue
        elif mat[nx][ny] == '.':
            mat[pos[0]][pos[1]] = '.'
            mat[nx][ny] = '@'
            pos = (nx, ny)
        elif mat[nx][ny] == 'O':
            nnx, nny = nx + dx, ny + dy
            while mat[nnx][nny] == 'O':
                nnx, nny = nnx + dx, nny + dy
            if mat[nnx][nny] == '.':
                while (nnx, nny) != (nx, ny):
                    pnx, pny = nnx - dx, nny - dy
                    mat[nnx][nny] = 'O'
                    nnx, nny = pnx, pny
                mat[nx][ny] = '@'
                mat[pos[0]][pos[1]] = '.'
                pos = (nx, ny)

    boxes = [(i, j) for i, row in enumerate(mat) for j, char in enumerate(row) if char == 'O']
    res = 0
    for box in boxes:
        res += 100 * box[0] + box[1]

    print(res)

