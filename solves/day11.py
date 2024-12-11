def solve1():
    with open("./inputs/input11", "r") as file:
        stones = list(map(int, file.read().split()))

    blinks = 25
    for _ in range(blinks):
        temp = []
        for no in stones:
            if no == 0:
                temp.append(1)
            elif len(str(no)) % 2 == 0:
                n1, n2 = str(no)[:len(str(no)) // 2], str(no)[len(str(no)) // 2:]
                temp.append(int(n1))
                temp.append(int(n2))
            else:
                temp.append(no * 2024)

        stones = temp

    res = len(stones)
    print(res)

def solve2():
    with open("./inputs/input11", "r") as file:
        stones = list(map(int, file.read().split()))

    counts = {}
    for stone in stones:
        counts[stone] = counts.get(stone, 0) + 1
    
    evens = set()
    odds = set()
    for stone in stones:
        if stone == 0:
            continue
        if len(str(stone)) % 2 == 0:
            evens.add(stone)
        else:
            odds.add(stone)
    
    blinks = 75
    for _ in range(blinks):
        tcounts = {}
        tevens = set()
        todds = set()

        if 0 in counts:
            tcounts[1] = counts[0]
            todds.add(1)

        for even in evens:
            first = int(str(even)[:len(str(even)) // 2])
            second = int(str(even)[len(str(even)) // 2:])
            
            tcounts[first] = tcounts.get(first, 0) + counts.get(even, 0)
            tcounts[second] = tcounts.get(second, 0) + counts.get(even, 0)

            if len(str(first)) % 2 == 0:
                tevens.add(first)
            elif first != 0:
                todds.add(first)

            if len(str(second)) % 2 == 0:
                tevens.add(second)
            elif second != 0:
                todds.add(second)

        for odd in odds:
            val = odd * 2024
            tcounts[val] = tcounts.get(val, 0) + counts.get(odd, 0)

            if len(str(val)) % 2 == 0:
                tevens.add(val)
            else:
                todds.add(val)

        evens = tevens
        odds = todds
        counts = tcounts

    res = sum(counts.values())
    print(res)

