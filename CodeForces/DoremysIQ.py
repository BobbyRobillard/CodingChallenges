def solution(contests, iq, difficulties):
    result = ""
    difficulties.sort()
    for i in range(contests):
        if iq <= 0:
            result += "0"
        elif difficulties[i] > iq:
            iq -= 1
            result += "1"
        else:
            result += "1"
    return result 

# Read in test cases
num_cases = int(input(""))
results = []
for i in range(num_cases):
    line_1 = (list(map(int,input().split())))
    contests, iq = line_1[0], line_1[1]
    difficulties = (list(map(int,input().split())))
    
    results.append(solution(contests, iq, difficulties))
 
# Print resutls
for r in results:
    print(r)