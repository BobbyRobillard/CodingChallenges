from collections import Counter

def solution(tasks):
    steps = 0
    print(Counter(tasks).values())
    for c in Counter(tasks).values():
        if c % 3 == 0:
            steps += c//3
        elif c % 2 == 0:
            steps += c//2
        elif c % 5 == 0:
            steps += (c//5)*2
        else:
            return -1
    return steps

tests = [
    [2,2,3,3,2,4,4,4,4,4],
    [2,3,3],
    [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69]
]

for t in tests:
    print(solution(t))
