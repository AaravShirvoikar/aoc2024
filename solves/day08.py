from collections import defaultdict

def solve1():
    with open("./inputs/input08", "r") as file:
       lines = file.readlines()

    mat = [list(line.strip()) for line in lines]

    antennas = defaultdict(list)
    for i, line in enumerate(mat):
        for j, ch in enumerate(line):
            if ch != '.':
                antennas[ch].append((i,j))

    antinodes = set()
    for coords in antennas.values():
       for i in range(len(coords)):
           for j in range(i + 1, len(coords)):
               diff = (coords[j][0] - coords[i][0], coords[j][1] - coords[i][1])
               for idx, dir in [(i, -1), (j, 1)]:
                   pos = (coords[idx][0] + diff[0] * dir, coords[idx][1] + diff[1] * dir)
                   if pos[0] >= 0 and pos[0] < len(mat) and pos[1] >= 0 and pos[1] < len(mat[0]):
                       antinodes.add(pos)
   
    res = len(antinodes)
    print(res)

def solve2():
    with open("./inputs/input08", "r") as file:
        lines = file.readlines()
    
    mat = [list(line.strip()) for line in lines]

    antennas = defaultdict(list)
    for i, line in enumerate(mat):
        for j, ch in enumerate(line):
            if ch != '.':
                antennas[ch].append((i,j))
    
    antinodes = set()
    for coords in antennas.values():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff = (coords[j][0] - coords[i][0], coords[j][1] - coords[i][1])
                for idx, dir in [(i, -1), (j, 1)]:
                    pos = coords[idx]
                    while pos[0] >= 0 and pos[0] < len(mat) and pos[1] >= 0 and pos[1] < len(mat[0]):
                        antinodes.add(pos)
                        pos = (pos[0] + diff[0] * dir, pos[1] + diff[1] * dir)
    
    res = len(antinodes)
    print(res)

