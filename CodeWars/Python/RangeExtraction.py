def solution(lst):
    ranges = []
    i = 0
    while i < len(lst):
        cnt = 0
        curr = i
        while curr+1 < len(lst) and lst[curr] + 1 == lst[curr+1]:
            cnt += 1
            curr += 1
        if cnt >= 2:
            ranges.append(lst[i:i+cnt+1])
            i += cnt + 1
        elif cnt == 1:
            ranges.append([lst[i]])
            ranges.append([lst[i+1]])
            i += 2
        else:
            ranges.append([lst[i]])
            i += 1
    return ",".join("{1}-{0}".format(max(item), min(item)) if len(item) > 1 else str(item[0]) for item in ranges)

print("RE: {}".format(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])))
