def solve(n):
    if n == 1: return 2
    return (n + 2) // 3
    
# Read in test cases
num_cases = int(input(""))
results = []
for i in range(num_cases):
    results.append(solve(int(input())))
 
# Print resutls
for r in results:
    print(r)