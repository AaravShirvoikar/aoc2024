def solve1():
    with open('./inputs/input05', 'r') as file:
        data = file.read().strip().split("\n\n")
    
    rules, updates = data[0], data[1]

    rule_map = {}
    for item in rules.split('\n'):
        a, b = map(int, item.split('|'))
        if a not in rule_map:
            rule_map[a] = set()
        rule_map[a].add(b)
    
    res = 0
    for line in updates.split('\n'):
        nums = [int(n) for n in line.split(',')]
        
        correct = True
        for i, curr in enumerate(nums):
            for next in nums[i+1:]:
                if next in rule_map and curr in rule_map[next]:
                    correct = False
                    break
            if not correct:
                break
        
        if correct:
            res += nums[len(nums)//2]
    
    print(res)

def solve2():
    with open('./inputs/input05', 'r') as file:
        data = file.read().strip().split("\n\n")
    
    rules, updates = data[0], data[1]
    
    rule_map = {}
    for item in rules.split('\n'):
        a, b = map(int, item.split('|'))
        if a not in rule_map:
            rule_map[a] = set()
        rule_map[a].add(b)

    res = 0
    for line in updates.split('\n'):
        nums = [int(n) for n in line.split(',')]
        
        correct = True
        for i, curr in enumerate(nums):
            for next in nums[i+1:]:
                if next in rule_map and curr in rule_map[next]:
                    correct = False
                    break
            if not correct:
                break
        
        if not correct:
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[j] in rule_map.get(nums[i], set()):
                        nums[i], nums[j] = nums[j], nums[i]

            res += nums[len(nums)//2]

    print(res)

