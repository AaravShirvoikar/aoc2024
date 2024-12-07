def check1(r):
    inc = None
    for i in range(len(r) - 1):
        if abs(r[i + 1] - r[i]) > 3:
            return False
        if r[i + 1] > r[i]:
            if inc is False:
                return False
            inc = True
        elif r[i + 1] < r[i]:
            if inc is True:
                return False
            inc = False
        else:
            return False
    return True

def check2(r):
    inc = None
    tol = False
    for i in range(len(r) - 1):
        if abs(r[i + 1] - r[i]) > 3:
            if tol:
                return False
            tol = True
        if r[i + 1] > r[i]:
            if inc is False:
                if tol:
                    return False
                tol = True
            inc = True
        elif r[i + 1] < r[i]:
            if inc is True:
                if tol:
                    return False
                tol = True
            inc = False
        else:
            return False
    return True

def solve1():
    with open("./inputs/input02", "r") as file:
        lines = file.readlines()

    reports = [[int(num) for num in line.split()] for line in lines]

    res = sum(1 for r in reports if check1(r))

    print(res)

def solve2():
    with open("./inputs/input02", "r") as file:
        lines = file.readlines()

    reports = [[int(num) for num in line.split()] for line in lines]

    res = sum(1 for r in reports if check2(r))

    print(res)

