import itertools

def solution(n):
    print(n, end=" ")
    for i in range(1, n):
        print(i, end=" ")
    print()


# Read in test cases
num_cases = int(input(""))
results = []
for i in range(num_cases):
    solution(int(input()))
 
# # Print resutls
# for r in results:
#     print(r)