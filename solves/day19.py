def solve1():
    with open("./inputs/input19", "r") as file:
        data = file.read().split("\n\n")

    available = set(data[0].split(", "))
    designs = data[1].strip().split("\n")
    
    res = 0
    for design in designs:
        stack = [0]
        possible = False
        
        while stack:
            i = stack.pop()
            if i == len(design):
                possible = True
                break
            for pattern in available:
                if design[i:i + len(pattern)] == pattern:
                    stack.append(i + len(pattern))
        
        if possible:
            res += 1

    print(res)

def solve2():
    with open("./inputs/input19", "r") as file:
        data = file.read().split("\n\n")

    available = set(data[0].split(", "))
    designs = data[1].strip().split("\n")
    
    res = 0
    for design in designs:
        dp = [0] * (len(design) + 1)
        dp[0] = 1
        
        for i in range(len(design)):
            if dp[i] > 0:
                for pattern in available:
                    if design[i:i + len(pattern)] == pattern:
                        dp[i + len(pattern)] += dp[i]
        
        res += dp[len(design)]
    
    print(res)

