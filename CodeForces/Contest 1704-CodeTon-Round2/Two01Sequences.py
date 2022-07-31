def solve(a, b):
    a = list(map(int, a))
    b = list(map(int, b))
    while len(a) > len(b):
        # Do min/max
        if b[0] == 0:
            a[1] = min(a[0], a[1])
            a = a[1:]
        else:
            a[1] = max(a[0], a[1])
            a = a[1:]
    return ("YES" if all(a[i] == b[i] for i in range(len(a))) else "NO")



num_cases = int(input(""))
results = []

for i in range(num_cases):
    size_a, size_b = (list(map(int,input().split())))
    line_1 = input()
    line_2 = input()
    results.append(solve(line_1, line_2))

for result in results:
    print(result)

"""
YES
YES
NO
NO
YES
YES
YES
NO
NO
YES
"""