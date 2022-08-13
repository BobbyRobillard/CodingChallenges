def solve(n, k, p):
    swaps = 0
    for i in range(k):
        sliced = p[k:]
        if sliced:
            curr_min = min(sliced)
            sliced_index = sliced.index(curr_min)
            min_index = (sliced_index + k)
            if curr_min < p[i]:
                p[i], p[min_index] = p[min_index], p[i]
                swaps += 1
    return swaps


# Read in test cases
num_cases = int(input(""))
results = []
for i in range(num_cases):
    n, k = list(map(int,input().split()))
    p = list(map(int,input().split()))
    results.append(solve(n,k,p))
 
# Print resutls
for r in results:
    print(r)