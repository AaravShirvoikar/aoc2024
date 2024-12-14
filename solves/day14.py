def solve1():
    with open("./inputs/input14", "r") as file:
        lines = file.readlines()

    w, h = 101, 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line in lines:
        vals = line.split()
        p = eval(vals[0].split('=')[1])
        v = eval(vals[1].split('=')[1])

        nx, ny = (p[0] + 100 * v[0]) % w, (p[1] + 100 * v[1]) % h

        if nx == w // 2 or ny == h // 2:
            continue

        if nx < w // 2 and ny < h // 2:
            q1 += 1
        elif nx > w // 2 and ny < h // 2:
            q2 += 1
        elif nx < w // 2 and ny > h // 2:
            q3 += 1
        elif nx > w // 2 and ny > h // 2:
            q4 += 1

    res = q1 * q2 * q3 * q4
    print(res)

def solve2():
    with open("./inputs/input14", "r") as file:
        lines = file.readlines()

    w, h = 101, 103
    robots = []
    for line in lines:
        vals = line.split()
        p = eval(vals[0].split('=')[1])
        v = eval(vals[1].split('=')[1])
        robots.append((p, v))

    res = 0
    for t in range(1, 10000):
        pos = set()
        v = True

        for p, v in robots:
            nx, ny = (p[0] + t * v[0]) % w, (p[1] + t * v[1]) % h
            if (nx, ny) in pos:
                v = False
                break
            pos.add((nx, ny))

        if v:
            res = t

    print(res)

