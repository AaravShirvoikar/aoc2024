def solve1():
    with open("./inputs/input09", "r") as file:
       data = file.read().strip()

    disk_struct = []
    id = 0
    for i, n in enumerate(data):
        if i % 2 == 0:
           for _ in range(int(n)):
               disk_struct.append(id)
           id += 1
        else:
           for _ in range(int(n)):
               disk_struct.append('.')

    l = 0
    r = len(disk_struct) - 1
    while l < r:
        while l < len(disk_struct) and disk_struct[l] != '.':
           l += 1
        while r >= 0 and disk_struct[r] == '.':
           r -= 1
        if l >= r:
           break
       
        disk_struct[l] = disk_struct[r]
        disk_struct[r] = '.'
        l += 1
        r -= 1

    res = sum(i * block for i, block in enumerate(disk_struct) if block != '.')
    print(res)

def solve2():
    with open("./inputs/input09", "r") as file:
        data = file.read().strip()

    disk_map = map(int, data)
    blocks = []
    id = 0
    count = 0
    idx = []
    for i, size in enumerate(disk_map):
        if i % 2 == 0:
            blocks.append([1, [id] * size, 0])
            id += 1
        else:
            if size > 0:
                blocks.append([0, [], size])
                idx.append(len(blocks) - 1)
                count += size

    curr_block = len(blocks) - 1
    while curr_block > 0:
        if blocks[curr_block][0] == 0:
            curr_block -= 1
            continue

        block_len = len(blocks[curr_block][1])
        for space_idx in idx:
            if space_idx >= curr_block:
                break

            if blocks[space_idx][2] >= block_len:
                blocks[space_idx][1].extend(blocks[curr_block][1])
                blocks[space_idx][2] -= block_len

                blocks[curr_block][0] = 0
                blocks[curr_block][2] = block_len
                blocks[curr_block][1] = []

                if blocks[space_idx][2] == 0:
                    idx.remove(space_idx)

                break

        curr_block -= 1

    res = 0
    pos = 0
    for block in blocks:
        for file in block[1]:
            res += pos * file
            pos += 1
        if block[0] == 0:
            pos += block[2]

    print(res)

