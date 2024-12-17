def solve1():
    with open("./inputs/input17", "r") as file:
        data = file.read().split("\n\n")

    registers = data[0].split("\n")
    a = int(registers[0].split(": ")[1])
    b = int(registers[1].split(": ")[1])
    c = int(registers[2].split(": ")[1])

    instructions = list(map(int, data[1].split(": ")[1].split(",")))

    iptr = 0
    output = []
    while iptr < len(instructions):
        opcode = instructions[iptr]
        operand = instructions[iptr + 1] if iptr + 1 < len(instructions) else 0

        if opcode == 0:
            d = 2 ** (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c)
            a //= d
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            b = (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c) % 8
        elif opcode == 3:
            if a != 0:
                iptr = operand
                continue
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            output.append((operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c) % 8)
        elif opcode == 6:
            d = 2 ** (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c)
            b = a // d
        elif opcode == 7:
            d = 2 ** (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c)
            c = a // d

        iptr += 2

    res = ",".join(map(str, output))
    print(res)

def solve2():
    with open("./inputs/input17", "r") as file:
        data = file.read().split("\n\n")

    instructions = list(map(int, data[1].split(": ")[1].split(",")))

    ca = sum(7 * 8**i for i in range(len(instructions) - 1)) + 1
    while True:
        a, b, c = ca, 0, 0
        iptr = 0
        output = []
        while iptr < len(instructions):
            opcode = instructions[iptr]
            operand = instructions[iptr + 1] if iptr + 1 < len(instructions) else 0

            if opcode == 0:
                d = 2 ** (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c)
                a //= d
            elif opcode == 1:
                b ^= operand
            elif opcode == 2:
                b = (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c) % 8
            elif opcode == 3:
                if a != 0:
                    iptr = operand
                    continue
            elif opcode == 4:
                b ^= c
            elif opcode == 5:
                output.append((operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c) % 8)
            elif opcode == 6:
                d = 2 ** (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c)
                b = a // d
            elif opcode == 7:
                d = 2 ** (operand if operand <= 3 else a if operand == 4 else b if operand == 5 else c)
                c = a // d

            iptr += 2

        if len(output) == len(instructions) and output == instructions:
            res = ca
            break

        for i in range(len(output) - 1, -1, -1):
            if output[i] != instructions[i]:
                ca += 8**i
                break

    print(res)

