def solution(n):
    results = [1]
    for i in range(1, n):
      results.append(4*(i) + results[i-1])
    return results[n-1]


tests = [2, 3, 4, 5, 6]

for t in tests:
    print("TESTING:", t, "\nRESULT:" , str(solution(t)))
