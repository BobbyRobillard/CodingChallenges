import operator

def solve(h, m, alarms):
    for alarm in alarms:
        # h == alarm[0]
        if h == alarm[0]:
            if m >= alarm[1]:
                return [0, m - alarm[1]]
        # h > alarm[0]
        if alarm[0] > h:
            if alarm[1] < m:
                return [alarm[0]-h-1, m-alarm[1] if m>=alarm[1] else 60 - alarms[1]]
            else:
                return [alarm[0]-h, m-alarm[1] if m>=alarm[1] else 60 - alarms[1]]
    # h < alarm[0]
    hours = 24-h-alarms[0][1]
    minutes = m-alarms[0][1] if m>=alarms[0][1] else 60 - m - alarms[0][1]
    return [hours,minutes]

# Read in test cases
num_cases = int(input(""))
results = []
for i in range(num_cases):
    inp = list(map(int,input().split()))
    n, h, m = inp
    alarms = []
    for j in range(n):
        inp2 = list(map(int,input().split()))
        alarms.append(inp2)

    # Get ideal alarm
    alarms.sort(key=operator.itemgetter(0, 1))
    results.append(solve(h, m, alarms))
 
# Print resutls
for r in results:
    print(r)