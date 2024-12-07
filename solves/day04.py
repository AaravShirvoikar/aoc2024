def check1(mat, target, row, col, direction):
    for i, ch in enumerate(target):
        nr = row + i * direction[0]
        nc = col + i * direction[1]

        if not (0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and mat[nr][nc] == ch):
            return False

    return True

def solve1():
    with open("./inputs/input04", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]
    target = "XMAS"
    dirs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1) 
    ]

    res = 0
    for row, line in enumerate(mat):
        for col, ch in enumerate(line):
            if ch == target[0]:
                for direction in dirs:
                    if check1(mat, target, row, col, direction):
                        res += 1

    print(res)

def check2(mat, row, col):
    if row == 0 or row == len(mat) - 1 or col == 0 or col == len(mat[0]) - 1:
        return False

    c1 = (
        (mat[row - 1][col - 1] == 'S' and mat[row + 1][col + 1] == 'M') or
        (mat[row - 1][col - 1] == 'M' and mat[row + 1][col + 1] == 'S')
    )
    c2 = (
        (mat[row + 1][col - 1] == 'S' and mat[row - 1][col + 1] == 'M') or
        (mat[row + 1][col - 1] == 'M' and mat[row - 1][col + 1] == 'S')
    )

    return c1 and c2

def solve2():
    with open("./inputs/input04", "r") as file:
        lines = file.readlines()

    mat = [list(line.strip()) for line in lines]

    res = 0
    for row, line in enumerate(mat):
        for col, ch in enumerate(line):
            if ch == 'A':
                if check2(mat, row, col):
                    res += 1

    print(res)

