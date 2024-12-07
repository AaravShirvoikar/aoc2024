import heapq
from collections import Counter

def solve1():
    with open("./inputs/input01", "r") as file:
        lines = file.readlines()
    
    l1 = [-int(line.split()[0]) for line in lines]
    l2 = [-int(line.split()[1]) for line in lines]

    heapq.heapify(l1)
    heapq.heapify(l2)

    res = 0
    while l1:
        n1 = -heapq.heappop(l1)
        n2 = -heapq.heappop(l2)
        res += abs(n1 - n2)

    print(res)


def solve2():
    with open("./inputs/input01", "r") as file:
        lines = file.readlines()

    l1 = [int(line.split()[0]) for line in lines]
    l2 = [int(line.split()[1]) for line in lines]

    counts = Counter(l2)

    res = sum(n * counts.get(n, 0) for n in l1)
    print(res)

