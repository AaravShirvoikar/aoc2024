import re

def solve1():
    with open("./inputs/input03", "r") as file:
        data = file.read()

    r = re.compile(r"mul\((\d+),(\d+)\)")
    res = sum(int(x) * int(y) for x, y in r.findall(data))

    print(res)

def solve2():
    with open("./inputs/input03", "r") as file:
        data = file.read()

    data = re.sub(r"don't\(\).*?do\(\)", "", data, flags=re.DOTALL)

    r = re.compile(r"mul\((\d+),(\d+)\)")
    res = sum(int(x) * int(y) for x, y in r.findall(data))

    print(res)

