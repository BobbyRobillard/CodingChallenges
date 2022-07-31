for i in range(int(input())):
    n, k = map(int, input().split())
    m = set(map(int, input().split()))
    for j in m:
        if j + k in m:
            print('YES')
            break
    else:
        print('NO')