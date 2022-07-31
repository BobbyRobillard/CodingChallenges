def getMaxDistance(x, nums):
    distances = {}
    for v in nums:
        i = 0
        while i < len(nums) and abs(v - nums[i]) <= x:
            if v in distances:
                distances[v] += 1
            else:
                distances[v] = 11
            i += 1
    return [
        max(distances),
        max(distances, key=lambda key: distances[key])
    ]

def solve(n, x, nums):
    
    v, max_distance = getMaxDistance(x, nums)
    changes = 0
    while True:
        for i in range(max_distance):
            del nums[0]
        if len(nums) == 0:
            return changes
        if not all(abs(v - el) <= x for el in nums):
            max_distance = getMaxDistance(x, nums)
            changes += 1

num_cases = int(input(""))
results = []

for i in range(num_cases):
    n, x = (list(map(int,input().split())))
    nums = (list(map(int,input().split())))
    results.append(solve(n, x, nums))

for result in results:
    print(result)