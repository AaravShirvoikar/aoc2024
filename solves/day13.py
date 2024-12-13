import re

def solve1():
    with open("./inputs/input13", "r") as file:
        data = file.read()

    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, data)

    res = 0
    for _, match in enumerate(matches, start=1):
        a1, a2, b1, b2, a, b = map(int, match)

        det = a1 * b2 - a2 * b1
        if det == 0:
            continue

        x = (a * b2 - b * b1) / det
        y = (a1 * b - a2 * a) / det
        if not x.is_integer() or not y.is_integer():
            continue
    
        res += int(3 * x + y)

    print(res)

def solve2():
    with open("./inputs/input13", "r") as file:
        data = file.read()

    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    matches = re.findall(pattern, data)

    res = 0
    for _, match in enumerate(matches, start=1):
        a1, a2, b1, b2, a, b = map(int, match)
        a += 10000000000000
        b += 10000000000000

        det = a1 * b2 - a2 * b1
        if det == 0:
            continue

        x = (a * b2 - b * b1) / det
        y = (a1 * b - a2 * a) / det
        if not x.is_integer() or not y.is_integer():
            continue
    
        res += int(3 * x + y)

    print(res)

