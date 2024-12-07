def solve1():
    with open("./inputs/input07", "r") as file:
        lines = file.readlines()

    possvals = []
    for line in lines:
        val, nos = line.split(":")
        val = int(val.strip())
        nos = [int(x) for x in nos.strip().split()]

        poss = [nos.pop(0)]
        while nos:
            curr = nos.pop(0)
            temp = []

            for p in poss:
                temp.append(p + curr)
                temp.append(p * curr)
            poss = temp

        if val in poss:
            possvals.append(val)

    res = sum(possvals)
    print(res)

def solve2():
    with open("./inputs/input07", "r") as file:
        lines = file.readlines()

    possvals = []
    for line in lines:
        val, nos = line.split(":")
        val = int(val.strip())
        nos = [int(x) for x in nos.strip().split()]

        poss = [nos.pop(0)]
        while nos:
            curr = nos.pop(0)
            temp = []

            for p in poss:
                temp.append(p + curr)
                temp.append(p * curr)
                temp.append(int(str(p) + str(curr)))
            poss = temp

        if val in poss:
            possvals.append(val)

    res = sum(possvals)
    print(res)
    
